#!/usr/local/bin/python3

def matr_mul(op1, op2):
  m = len(op1)
  n = len(op2[0])

  if (len(op1[0]) != len(op2)):
    raise Exception("Matrix format is invalid")
  result = []

  for i in range(m):
    result.append([0] * n)
    for j in range(n):
      for k in range(len(op2)):
        result[i][j] += op1[i][k] * op2[k][j]
  return result

def print_mart(matr):
  mark_up = {"v_c":"\u2551", "h_c":"=", "t_l": "\u2554", "t_r":"\u2510",
    "b_l":"\u255A" , "b_r":"\u255D", "m_l":"\u2560", "m_r":"\u2563"}


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

a = [
 [1,9,3],
 [2,7,8],
 [2,4,5],
 [3,5,6]
]

b = [ [1, -4, 5],[2, 78, 2],[3, 6, 8] ]

c = matr_mul(a, b)

print_mart(a);
print("TIMES")
print_mart(b);
print("EQUALS")
print_mart(c);
