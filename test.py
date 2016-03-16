def mapfn(k, v):
  print "hey"
  print v
  x = v - 99
  p = []
  for i in xrange(x, v):
    y = 2
    if i < 2:
       continue
    while i % y != 0:
      y = y+1
    if y == i:
      p.append(i)
  return p

y = mapfn(1, 100)

print y
