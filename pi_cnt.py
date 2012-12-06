#!/usr/local/bin/python3

import random
import re
import sys
import threading
import time
import os

class PiCounter:
  def __init__(self):
    self.computed_pi = 0;
    self.pi_lock = threading.Lock()
    
  def compute(self, *args):
    contribution_to_pi = 0
    next_den = (-1 if args[0] % 2 == 0 else 1) * (2 * args[0] - 1)
    for i in range(args[0], args[1]):
      contribution_to_pi += 1 / next_den
      next_den = - (next_den + 2 * (-1 if next_den < 0 else 1))
      #for better visualization
      time.sleep(0.0001)

    self.add_to_pi(4 * contribution_to_pi)

  def get_pi_value(self):
    self.pi_lock.acquire(True)
    current_pi = self.computed_pi
    self.pi_lock.release()
    return current_pi

  def add_to_pi(self, delta):
    self.pi_lock.acquire(True)
    self.computed_pi += delta
    self.pi_lock.release()


CPU_GRAPH_SCALE = 10
def print_cpu_info(loading, cpu = 0, offset = 0):
  for i in range(0, CPU_GRAPH_SCALE):
    if (CPU_GRAPH_SCALE - i) / CPU_GRAPH_SCALE > loading: continue

    os.system("tput cup {0} {1}".format(offset + i, cpu * 5))
    print("\033[{0}m    \033[0m".format(41 if (CPU_GRAPH_SCALE-i) > 7 else 42))
  os.system("tput cup {0} {1}".format(offset + CPU_GRAPH_SCALE, cpu * 5))
  print(loading)

IDLE_IND = 3
CPU_RE = re.compile(r"^cpu[0-9]+.*")
def get_cpu_usage():  
  cpu_infos = []
  error_msg = ""
  try:
    with open("/proc/stat", "r") as f:
      
      cpu_cnt = 0
      for line in f:
        #line is not <cpu blahblah>, but <cpuN blah blah>
        if not CPU_RE.search(line): continue
         
        times = [int(i) for i in line.split()[1:8]]
        cpu_infos.append((cpu_cnt, int(100 * (1 - times[IDLE_IND] / sum(times))) / 100))
        cpu_cnt += 1
  except IOError:
    error_msg = "Proc stat is available only on Linux"
 
  return (error_msg, cpu_infos)

def visualizer(*args):
  while True:
    os.system("tput clear")
    
    # 2 = 1 (main thread) + 1 (viewer thread)
    print("Running worker threads # is {0}".format(threading.active_count() - 2));
    print("Approximated PI value is {0}".format(args[0].get_pi_value()))
    offset = 2

    err_msg, data = get_cpu_usage()
    if err_msg:
      print(err_msg)
    else:
      for cpu_num, usage in data:
        print_cpu_info(usage, cpu_num, offset)  
    time.sleep(0.5)

MAX_THREAD_COUNT = 10 + 2
BASE_CHUNCKS_COUNT = 3000

if __name__ == "__main__":
  counter = PiCounter()
  
  os.system("tput civis");
  spawn_interval = .5 if len(sys.argv) < 2 else sys.argv[1]
  threading.Thread(target=visualizer, args=(counter,)).start()
  
  last_outsourced_bound = 20
  base_cntr = threading.Thread(target=counter.compute, args=(1, last_outsourced_bound))
  base_cntr.start()
  base_cntr.join()
  
  while True:
    if random.uniform(1, MAX_THREAD_COUNT) > threading.active_count():
      start = last_outsourced_bound
      last_outsourced_bound += (MAX_THREAD_COUNT - threading.active_count()) * BASE_CHUNCKS_COUNT
      threading.Thread(target=counter.compute, args=(start, last_outsourced_bound,)).start()

    time.sleep(spawn_interval)
