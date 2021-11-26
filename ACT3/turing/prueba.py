import sys

P = []
G = { "P": {}, "S": "" }
strings = []

# Aquí se leen las lineas
for line in sys.stdin:
  line = line.rstrip().split(' ')
  if len(line) > 1:
    P.append(line)
  else:
    strings.append(line[0])

# Se establece el inicial
G["S"] = P[0][0]

# Se añaden las producciones
for p in P:
    G["P"][p[0]] = p[1:]

def CYK(G, x):
  """
  Algoritmo CYK
  Regresa una matriz
  """

  n = len(x)
  T = [[[] for x in range(0, n)] for y in range(0, n)]

  for i in range(0, n):
    for key, values in G["P"].items():
      if x[i] in values:
        T[i][i].append(key)
  
  for l in range(1, n):
    for r in range(0, n-l):
      for t in range(0, l):
        for key, values in G["P"].items():
          for value in values:
            if len(value) == 2:
              if value[0] in T[r][r+t] and value[1] in T[r+t+1][r+l]:
                T[r][r+l].append(key)              
  return T

for string in strings:
  T = CYK(G, string)

  if G["S"] in T[0][-1]:
    print("Aceptado")
  else:
    print("Rechazado")