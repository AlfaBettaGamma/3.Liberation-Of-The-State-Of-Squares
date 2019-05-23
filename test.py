
def ConquestCampaign(N, M, L, battalion):
  n = []
  m = []
  p = []
  newn = []
  newm = []
  lastn = []
  lastm = []
  p2 = 0
  d = 2
  if(L*2 == len(battalion)):
    for i in range(len(battalion)):
      if(i == 0):
        n.append(battalion[i])
      elif(i == 1):
        m.append(battalion[i])
      else:
        if(i%2 == 0):
          n.append(battalion[i]) 
        else:
          m.append(battalion[i])
    for i in range(len(n)):
      if n[i] > N or m[i] > M :
        return print('Введенные значения выходят за рамки матрицы')
    for i in range(L): #проверка на повторы
      p.clear()
      p.append(n[i])
      p.append(m[i])
      p2 = 0
      for j in range(len(n)):
        if p[0] == n[j] and p[1] == m[j]:
          p2 += 1
        if p2 > 1:
          n[j] = 0
          m[j] = 0
          p2 = 0
    for i in range(n.count(0)):
      n.remove(0)
      m.remove(0)
      L -= 1
    while N*M is not L:
        if(d <= 2 and L <= N*M):
            for i in range(L): #захват
              if(1 <= n[i] <= N and 1 <= m[i] - 1 <= M ):
                n.append(n[i])
                m.append(m[i]-1)
                newn.append(n[i])
                newm.append(m[i] -1)
                L += 1
              if(1 <= n[i] + 1 <= N and 1 <= m[i] <= M ):
                n.append(n[i]+1)
                m.append(m[i])
                newn.append(n[i]+1)
                newm.append(m[i])                
                L += 1
              if(1 <= n[i] <= N and 1 <= m[i] + 1 <= M ):
                n.append(n[i])
                m.append(m[i]+1)
                newn.append(n[i])
                newm.append(m[i]+1)
                L += 1
              if(1 <= n[i] - 1 <= N and 1 <= m[i] <= M ):
                n.append(n[i]-1)
                m.append(m[i])
                newn.append(n[i]-1)
                newm.append(m[i])
                L += 1
            for i in range(len(n)): #проверка на повторы
              p.clear()
              p.append(n[i])
              p.append(m[i])
              p2 = 0
              for j in range(len(n)):
                if p[0] == n[j] and p[1] == m[j]:
                  p2 += 1
                if p2 > 1:
                  n[j] = 0
                  m[j] = 0
                  p2 = 0
            for i in range(n.count(0)):
              n.remove(0)
              m.remove(0)
              L -= 1
            d += 1
            battalion.clear()
            for i in range(len(n)):
                battalion.append(n[i])
                battalion.append(m[i])
        elif(d%2 == 1 and L <= N*M):
            for i in range(len(newn)): #захват
              if(1 <= newn[i] <= N and 1 <= (newm[i] - 1) <= M ):
                n.append(newn[i])
                m.append(newm[i]-1)
                lastn.append(newn[i])
                lastm.append(newm[i] -1)
                L += 1
              if(1 <= (newn[i] + 1) <= N and 1 <= newm[i] <= M ):
                n.append(newn[i]+1)
                m.append(newm[i])
                lastn.append(newn[i]+1)
                lastm.append(newm[i])                
                L += 1
              if(1 <= newn[i] <= N and 1 <= (newm[i] + 1) <= M ):
                n.append(newn[i])
                m.append(newm[i]+1)
                lastn.append(newn[i])
                lastm.append(newm[i]+1)
                L += 1
              if(1 <= (newn[i] - 1) <= N and 1 <= newm[i] <= M ):
                n.append(newn[i]-1)
                m.append(newm[i])
                lastn.append(newn[i]-1)
                lastm.append(newm[i])
                L += 1
            for i in range(len(n)): #проверка на повторы
              p.clear()
              p.append(n[i])
              p.append(m[i])
              p2 = 0
              for j in range(len(n)):
                if p[0] == n[j] and p[1] == m[j]:
                  p2 += 1
                if p2 > 1:
                  n[j] = 0
                  m[j] = 0
                  p2 = 0
            for i in range(n.count(0)):
              n.remove(0)
              m.remove(0)
              L -= 1
            for i in range(len(lastn)): #проверка на повторы
              p.clear()
              p.append(lastn[i])
              p.append(lastm[i])
              p2 = 0
              for j in range(len(lastn)):
                if p[0] == lastn[j] and p[1] == lastm[j]:
                  p2 += 1
                if p2 > 1:
                  lastn[j] = 0
                  lastm[j] = 0
                  p2 = 0
            for i in range(lastn.count(0)):
              lastn.remove(0)
              lastm.remove(0)
            d += 1
            newn.clear()
            newm.clear()
            battalion.clear()
            for i in range(len(n)):
                battalion.append(n[i])
                battalion.append(m[i])
        elif(d%2 == 0 and L <= N*M):
            for i in range(len(lastn)): #захват
              if(1 <= lastn[i] <= N and 1 <= (lastm[i] - 1) <= M ):
                n.append(lastn[i])
                m.append(lastm[i]-1)
                newn.append(lastn[i])
                newm.append(lastm[i]-1)
                L += 1
              if(1 <= (lastn[i] + 1) <= N and 1 <= lastm[i] <= M ):
                n.append(lastn[i]+1)
                m.append(lastm[i])
                newn.append(lastn[i]+1)
                newm.append(lastm[i])                
                L += 1
              if(1 <= lastn[i] <= N and 1 <= (lastm[i] + 1) <= M ):
                n.append(lastn[i])
                m.append(lastm[i]+1)
                newn.append(lastn[i])
                newm.append(lastm[i]+1)
                L += 1
              if(1 <= (lastn[i] - 1) <= N and 1 <= lastm[i] <= M ):
                n.append(lastn[i]-1)
                m.append(lastm[i])
                newn.append(lastn[i]-1)
                newm.append(lastm[i])
                L += 1
            for i in range(len(n)): #проверка на повторы
              p.clear()
              p.append(n[i])
              p.append(m[i])
              p2 = 0
              for j in range(len(n)):
                if p[0] == n[j] and p[1] == m[j]:
                  p2 += 1
                if p2 > 1:
                  n[j] = 0
                  m[j] = 0
                  p2 = 0
            for i in range(n.count(0)):
              n.remove(0)
              m.remove(0)
              L -= 1
            for i in range(len(newn)): #проверка на повторы
              p.clear()
              p.append(newn[i])
              p.append(newm[i])
              p2 = 0
              for j in range(len(newn)):
                if p[0] == newn[j] and p[1] == newm[j]:
                  p2 += 1
                if p2 > 1:
                  newn[j] = 0
                  newm[j] = 0
                  p2 = 0
            for i in range(newn.count(0)):
              newn.remove(0)
              newm.remove(0)  
            d += 1
            lastn.clear()
            lastm.clear()           
            battalion.clear()
            for i in range(len(n)):
                battalion.append(n[i])
                battalion.append(m[i])
    d -= 1
    return d
  else:
    print('неверно введены данные!')

def test1():
  ConquestCampaign(5,6,3,[1,1,2,4,3,5])

def test2():
  ConquestCampaign(6,6,4,[1,1,2,4,3,5])

def test3():
  ConquestCampaign(5,6,4,[1,1,2,4,3,5,6])

def test4():
  ConquestCampaign(3,4,2,[2,2,3,5])