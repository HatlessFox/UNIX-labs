#!/usr/local/bin/python3

# water problem

def gcd(a,b):
  while b: a, b = b, a % b
  return a

a = int(input("Enter capacity of the first tank: "))
b = int(input("Enter capacity of the second tank: "))
b_val, sm_val, b_name, sm_name = (a, b, "A", "B") if a > b else (b, a, "B", "A")
c = int(input("Enter capacity we need to produce: "))

#some shortcuts
if  a < c and b < c:
  #required cpacity can't be held by any tank
  print("Impossible")
  quit()

if c % gcd(a, b) != 0:
  print("Impossible")
  quit()

sm_state, bigger_state = 0, 0

while True:
  #get extra little
  print(">"+sm_name)
  print(sm_name+">"+b_name)
  bigger_state += sm_val
  
  if bigger_state == c:
    print("Tank {0} has required amount of water".format(b_name))
    quit()

  if bigger_state > a:
    if bigger_state - b_val == c:
      print("Tank {0} has required amount of water".format(sm_name)) 
      quit()
    print(b_name+">")
    print(sm_name+">"+b_name)
    bigger_state = bigger_state - b_val

