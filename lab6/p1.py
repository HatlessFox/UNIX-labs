#!/usr/local/bin/python3

import math
from multimethod import multimethod

class Matr3x3(object):
  def __init__(self, data):
    self.data, self.side = data, 3
  
  def __add__(self, val):
    result = []

    for i in range(self.side):
      result.append([0] * self.side)
      for j in range(self.side):
        result[i][j] = self.data[i][j] + val.data[j][j]
    return Matr3x3(result)

  def inv(self):
    det = self.data[0][0] * self.data[1][1] * self.data[2][2] + \
      self.data[0][1] * self.data[1][2] * self.data[2][0] + \
      self.data[1][0] * self.data[2][1] * self.data[0][2] - \
      self.data[0][2] * self.data[1][1] * self.data[2][0] - \
      self.data[1][0] * self.data[0][1] * self.data[2][2] - \
      self.data[2][1] * self.data[1][2] * self.data[0][0]
    if det == 0:
      print("Not invertable")
      return None

    transposed = [list(row) for row in self.data]
    for i in range(3):
      for j in range(3):
        transposed[j][i] = self.data[i][j]
    res_matr = Matr3x3(transposed)
    res_matr.mult_v(1 / abs(det))
    return res_matr
    
  def print(self):
    mark_up = {"v_c":"\u2551", "h_c":"=", "t_l": "\u2554", "t_r":"\u2510",
    "b_l":"\u255A" , "b_r":"\u255D", "m_l":"\u2560", "m_r":"\u2563"}

    matr = self.data
    max_len = 0
    for i in range(len(matr)):
      for j in range(len(matr[0])):
        max_len = max(max_len, len(str(matr[i][j])))
    format_string = "{0:" + str(max_len) + "}" + mark_up["v_c"]

    width = (len(matr[0]) * (max_len+1) + 1);

    print(mark_up["t_l"]+mark_up["h_c"]*(width-2)+mark_up["t_r"])
    for i in range(len(matr)):
      print(mark_up["v_c"], end="")
      for j in range(len(matr[0])):
        print(format_string.format(matr[i][j]), end="")
      print();
      if i+1 != len(matr):
        print(mark_up["m_l"]+mark_up["h_c"]*(width-2)+mark_up["m_r"])
      else:
        print(mark_up["b_l"]+mark_up["h_c"]*(width-2)+mark_up["b_r"])

class Vector(Matr3x3):
  def __init__(self, data):
    super(Vector, self).__init__([data]) 
  def __add__(self, val): pass
  def __int__(self, val): pass

class ZRol(Matr3x3):
  def __init__(self, angle):
    data = [
      [math.cos(angle), -math.sin(angle), 0],
      [math.sin(angle), math.cos(angle), 0],
      [0, 0, 1]
    ]
    super(ZRol, self).__init__(data) 

@multimethod(Matr3x3, int)
def mult(m, val):
  m.data = [[ val*m.data[i][j] for j in range(0, m.side)] for i in range(0, m.side)]
  return m

@multimethod(Matr3x3, Matr3x3)
def mult(self, val):
  result = []

  for i in range(self.side):
    result.append([0] * self.side)
    for j in range(self.side):
      for k in range(self.side):
        result[i][j] += self.data[i][k] * val.data[k][j]
  return Matr3x3(result)

@multimethod(Matr3x3, Vector)
def mult(self, val):
  result = [0] * self.side

  for i in range(self.side):
    for j in range(self.side):
      result[i] += self.data[i][j] * val.data[0][j]
  return Vector(result)


m = Matr3x3([[2,2,3],[4,5,6],[7,8,9]])
mult(m,Vector([1,2,3])).print()
