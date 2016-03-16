import mincemeat

data = {}
for i in range(1, 30):
  data[i-1] = i* 100000

print data

def mapfn(k, v):
  print "hey"
  print v
  x = v - 999999
  if x <2:
    x = 2
  for i in xrange(x, v):
    y = 2
    while i % y != 0:
      y = y+1
    if y == i:
      p = str(i)
      if p == p[::-1]:
        yield k, i


def reducefn(k, vs):
  x = []
  print k, vs
  for i in vs:
       x.append(i)
  return x

s = mincemeat.Server()
s.datasource = data
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

print results

