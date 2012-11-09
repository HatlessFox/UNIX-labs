#!/usr/local/bin/python3

def is_reachable(w1, w2):
  diff = 0
  for i in range(0, len(w1)):
    if w1[i] != w2[i]: diff += 1
    if diff > 1: return False 
  return w1 != w2

#input stuff
src = input()
dest = input()

tes = []
cnt = int(input())
cnt_res = cnt
while cnt_res:
  tes.append(input())
  cnt_res -= 1

tes.append(src)
tes.append(dest)
cnt += 2

# make inc matrix
matr = [ ]
# form a... Graph of words and serch on it
for w1 in tes:
  matr.append(list(is_reachable(w1,w2) for w2 in tes))

#run dfs
st_i = tes.index(src)
dest_i = tes.index(dest)

visited = set()
nexts = [st_i]
prev = [-1 for i in range(0, cnt)]
while nexts and (not dest_i in visited):
  new_next = []
  for nxt_i in nexts:
    if nxt_i in visited: continue
    tmp_next = [i for i in range(0, cnt) if matr[nxt_i][i] and not i in visited] 
    for ind in tmp_next: prev[ind] = nxt_i
    new_next.extend(tmp_next)
    visited.add(nxt_i)
  nexts = new_next

#print output
if not dest_i in visited:
  print("Impossible")
  quit()

print("Result")
res = []
while dest_i != st_i:
  res.append(tes[dest_i])
  dest_i = prev[dest_i]
res.append(src)
res.reverse()
for w in res: print(w)


