#!/usr/local/bin/python3

def operation(func):
  
  def wrapper(*args):
    prefix, res = func(*args)

    #trim leading zeroes
    while len(res) > 1 and res[0] == 0: del res[0]
    if len(res) == 1 and res[0] == 0: prefix = ""
    return prefix, res

  return wrapper

def prepare_for_operation(num1, num2):
  num1.reverse()
  num2.reverse()

  if len(num1) == len(num2): return
  min_num, max_num = (num2, num1) if len(num1) > len(num2) else (num1, num2)
  pad = [0] * (len(max_num) - len(min_num))
  min_num.extend(pad)

def to_compelement(op):
  carry = 1
  for i in range(0, len(op)):
    op[i] = 9 - op[i] + carry
    carry = op[i] // 10
    op[i] %= 10
  return op

@operation
def add(op1, op2):
  num1, num2 = op1[1], op2[1]
  prepare_for_operation(num1, num2)
  
  if op1[0] == -1: num1 = to_compelement(num1)
  if op2[0] == -1: num2 = to_compelement(num2)

  res = [0] * (len(num1) +1)
  for ind in range(0, len(num1)):
    res[ind] += num1[ind] + num2[ind]
    res[ind + 1] += res[ind] // 10
    res[ind] %= 10

  prefix = ""
  sign_is_predefined = op1[0] == op2[0]
  result_is_negative = \
    (sign_is_predefined and op1[0] == -1) or (not sign_is_predefined and res[-1] == 0)
  if result_is_negative:
    res, prefix = to_compelement(res), "-"
  if not sign_is_predefined:
    #clear overflow
    res = res[:-1]

  res.reverse()
  return prefix, res

def sub(op1, op2):
  op2 = (-1*op2[0], op2[1])
  return add(op1, op2)

@operation
def mul(op1, op2):
  num1, num2 = op1[1], op2[1]
  prepare_for_operation(num1, num2)
  
  res = [0] * (len(num1) + len(num2))
  for i in range(0, len(num1)):
    for j in range(0, len(num1)):
      res[i+j] += num1[i] * num2[j]
      res[i+j+1] += res[i+j] // 10
      res[i+j] %= 10

  res.reverse()
  prefix = "" if op1[0] == op2[0] else "-"
  return prefix, res

def long_cmp(n1, n2):
  p, res = add((1, n1[:]), (-1, n2[:]))
  if res == 0: return 0
  if p == "-": return -1
  return 1

@operation
def div(op1, op2):
  num1, num2 = op1[1], op2[1]
  res = []
  
  shift = 0
  while long_cmp(num1, num2) != -1:
    tmp = num1[:len(num2)+ shift]
    mult = 9

    #'borrow' digits
    while True:
      if long_cmp(tmp, num2) == -1:
        if len(tmp) == len(num1): break
        tmp = num1[:len(tmp)+1]
        res.append(0)
      else: break

    while True:
      ##can be optimized with binary search
      pr, mul_res = mul((1, [mult]), (1, num2[:]))
      cmp_res = long_cmp(tmp, mul_res);
      if cmp_res >= 0: break
      else: mult -= 1
    
    res.append(mult)
    #mul_res last is used
    for i in range(len(num1) - len(tmp)): mul_res.append(0)
    pr, num1 = add((1, num1[:]), (-1, mul_res))
    shift = 1
  
  prefix = "" if op1[0] == op2[0] else "-"
  return prefix, res if res else [0]

def input_digit():
  while (True):
    digit = str(input("Enter digit (q - for exit):"))

    if digit and (digit.isdigit() or (digit[0] == "-" and digit[1:].isdigit())):
      sign, value = (-1, digit[1:]) if digit[0] == "-" else (1, digit)
      return (sign, [int(i) for i in value])
      
    if digit == "q": quit()
    print("Stuff you entered is not a digit, try again")

SUPPORTED_OPS = {"+":add, "-":sub, "*":mul, "/":div}

def  calc():
  op1 = input_digit()
  op2 = input_digit()
  operation = input("Enter operation:")
  if operation in SUPPORTED_OPS:
    prefix, res = SUPPORTED_OPS[operation](op1, op2)
    #StringIO can be used but the code will be a bit awkward
    print("Result: {0}".format(prefix + "".join(str(i) for i in res)))
  else:
    print("Operation {0} is not supported.".format(operation))

calc() 