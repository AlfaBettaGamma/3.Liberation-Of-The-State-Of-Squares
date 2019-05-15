def odometer(oksana):
  t = []
  v = []
  V = 0
  T = 0
  res = 0
  for i in range(len(oksana)):
    if(i == 0):
      v.append(oksana[i])
    elif(i == 1):
      t.append(oksana[i])
    else:
      if(i%2 == 0):
        v.append(oksana[i]) 
      else:
        t.append(oksana[i])
  if(len(v) == len(t)):
    for i in range(len(v)):
      if(i == 0):
        V = v[i]
        T = t[i]
      else:
        V = v[i]
        T = t[i] - t[i-1]
        if(T < 0):
          T = 0
      res = (T*V)+res
  elif(len(v) > len(t)):
    for i in range(len(t)):
      if(i == 0):
        V = v[i]
        T = t[i]
      else:
        V = v[i]
        T = t[i] - t[i-1]
        if(T < 0):
          T = 0
      res = (T*V)+res
  return res