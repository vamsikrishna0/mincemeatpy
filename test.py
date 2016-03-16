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


'''if v%10000 != 0:
    x = v - 2999
  elif v in [4000000, 8000000 ,10000000]:
    x = v - 2999
  else:'''



m = i
    a = 0 
    while (m!=0):
        a = m % 10 + a * 10
        m = m / 10

    if (i == a):
