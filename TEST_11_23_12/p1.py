#!/usr/local/bin/python3

import random
import threading
import time

class PiCounter:

  def run_round(self):
    pass
  
  def get_curr_approx(self):
    pass

  def clone(self):
    pass

  def run_forewer(self, stop_evnt):
    while not stop_evnt.is_set():
      self.run_round()

  def nextApproximation(self):
    #clone to prevent state corruption
    ctr = self.clone()
    while True:
      ctr.run_round()
      yield ctr.get_curr_approx()

  def approximate(self, n):
    for i in range(n):
      self.run_round()
    return self.get_curr_approx()

  def approximateT(self, _time):
    ctr = self.clone()
    t_stop = threading.Event()
    t = threading.Thread(name='runner', target=lambda x: ctr.run_forewer(x), args=(t_stop,))
    t.start()
    time.sleep(_time / 1000)
    t_stop.set()
    return ctr.get_curr_approx()

class StaticPiCounter(PiCounter):
  def clone(self):
    return StaticPiCounter()
  def get_curr_approx(self):
    return 3.1415926535897932384626433832795;

class RandomPiCounter(PiCounter):
  def __init__(self, trials_per_round = 300):
    self.trials_per_round = trials_per_round
    self.total_rounds = 0
    self.in_place = 0
  def clone(self):
    return RandomPiCounter(self.trials_per_round)
  def run_round(self):
    for i in range(self.trials_per_round):
      x = random.uniform(0, 1)
      y = random.uniform(0, 1)
      if x**2+y**2 <= 1:
        self.in_place += 1
      self.total_rounds += 1

  def get_curr_approx(self):
    return 4 * self.in_place / self.total_rounds

class SeriesPiCounter(PiCounter):
  def __init__(self):
    self.sum = 0
    self.next = 1
  def clone(self):
    return SeriesPiCounter();
  def run_round(self):
    self.sum += 1 / self.next
    self.next = -(self.next + (2 if self.next > 0 else - 2))
  def get_curr_approx(self):
    return 4 * self.sum

def compare(n, ctr1, ctr2):
  return abs(ctr1.approximate(n) - ctr2.approximate(n))
def compareT(time, ctr1, ctr2):
  return abs(ctr1.approximateT(time) - ctr2.approximateT(time))
