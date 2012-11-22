#!/usr/local/bin/python3
import sys

class Student:
  def __init__(self, name):
    self.name, self.points = name, []
  def __repr__(self):
    return self.name + ": " + " ".join(str(point_e) for point_e in self.points)
  def avg(self): return 0 if len(self.points) == 0 else sum(self.points) / len(self.points)
  def add_pts(self, *args): self.points.extend(args)

class FDB(object):
  def __init__(self, file_name):
    self.entries = {}
    with open (file_name) as fl:
      for line_num in range(int(fl.readline())):
        name, pts = fl.readline().split(": ");
        st = Student(name)
        st.add_pts(*(int(pt) for pt in pts.split(" ")))
        self.entries[name] = st
  def get_by_name(self, st_name): return self.entries[st_name]
  def add(self, st): self.entries[st.name] = st
  def rm(self, name): 
    if name in self.entries:
      del self.entries[name]
  def flush(self, fname):
    with open(fname, "w") as fl:
      fl.write(str(len(self.entries)) + "\n")
      for st in self.entries.values():print(st, file=fl)
  def find_max_gpa(self): return max(self.entries.values(), key = lambda x: x.avg())

db = FDB("db_cnt.txt")
db.add(Student("SDF"))
print(db.find_max_gpa())
