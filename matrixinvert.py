## template
## leegy

def invertmatrix(matrix, i, j):
  if matrix[i][j] == 1:
    matrix[i][j] = 0
  elif matrix[i][j] == 0:
    matrix[i][j] = 1
  return matrix


n = int(input())
matrix = [[0 for _ in range(10)] for _ in range(10)]

for i in range(n):
  for j in range(10):
    matrix = invertmatrix(matrix, i, j)
  for k in range(10):
    matrix = invertmatrix(matrix, k, i)
  matrix = invertmatrix(matrix, i, i)

  
for i in range(10):
  tempstr = ""
  for j in range(10):
    tempstr += str(matrix[i][j])
    tempstr += " "
  print(tempstr)
