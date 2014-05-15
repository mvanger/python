def combo(n):
  r = [0] * len(n)
  while True:
    yield tuple(r)
    p = len(r) - 1
    r[p] += 1
    while r[p] == n[p]:
      r[p] = 0
      p -= 1
      if p == -1:
        return
      r[p] += 1

g = combo((2,3,4,5))
for t in g:
  print t

print type(g)

print "test"

print(g)

for t in g:
  print t

print "test2"