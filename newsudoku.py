Equations = []

matrix = {}

for x in range(9):
 for y in range(9):
  matrix[x,y] = []

input = {}
input[0] = "706100240"
input[1] = "500000100" 
input[2] = "004020583"
input[3] = "000000000"
input[4] = "040900835"
input[5] = "000060974"
input[6] = "050017000"
input[7] = "000305706"
input[8] = "007040058"

#input[0] = "610050000"
#input[1] = "000000562" 
#input[2] = "000080007"
#input[3] = "005000000"
#input[4] = "000200400"
#input[5] = "060070980"
#input[6] = "000800090"
#input[7] = "002103000"
#input[8] = "400560100"


def sudoinput():
 matrix = {}
 for x in range(9):
  for y in range(9):
   matrix[x,y] = []
 for x in range(9):
  aux = raw_input("Enter row " + str(x) + " : ")
  input[x] = aux
 for x in range(9):
  for y in range(9):
   matrix[x,y].append(int(input[x][y]))
 for x in range(9):
  for y in range(9):
   if matrix[x,y] == [0]:
    matrix[x,y] = [1,2,3,4,5,6,7,8,9]


def fileinput():
 with open("sudoku.txt") as f:
    input = f.readlines()
 input = [x.strip() for x in input]
 print input 
 global matrix	
 matrix = {}
 for x in range(9):
  for y in range(9):
   matrix[x,y] = []
 for x in range(9):
  for y in range(9):
   matrix[x,y].append(int(input[x][y]))
 for x in range(9):
  for y in range(9):
   if matrix[x,y] == [0]:
    matrix[x,y] = [1,2,3,4,5,6,7,8,9]

for x in range(9):
 for y in range(9):
   matrix[x,y].append(int(input[x][y]))


for x in range(9):
 for y in range(9):
  if matrix[x,y] == [0]:
    matrix[x,y] = [1,2,3,4,5,6,7,8,9]


def single(x,y):
 if len(matrix[x,y]) == 1:
  return True
 else:
  return False

def get(x,y):
 return matrix[x,y][0]

def dorow(x,y):
 for n in range(9):
  if n!= y and single(x,n) and get(x,n) in matrix[x,y]:
    matrix[x,y].remove(get(x,n))

def docolumn(x,y):
 for n in range(9):
  if n!= x and single(n,y) and get(n,y) in matrix[x,y]:
    matrix[x,y].remove(get(n,y))

def row(n):
 r = []
 for x in range(9):
  r.append((n,x))
 return r

def column(n):
 r = []
 for x in range(9):
  r.append((x,n))
 return r

def square(n):
 square = {}
 if n == 0:
  for a in range(3):
   for b in range(3):
    square[a,b] =matrix[a,b]
 if n == 1:
  for a in range(3): 
   for b in range(3):
    square[a,b] =matrix[a,b+3]
 if n == 2:
  for a in range(3): 
   for b in range(3):
    square[a,b] =matrix[a,b+6]
 if n == 3:
  for a in range(3): 
   for b in range(3):
    square[a,b] =matrix[a+3,b]
 if n == 4:
  for a in range(3): 
   for b in range(3):
    square[a,b] =matrix[a+3,b+3]
 if n == 5:
  for a in range(3): 
   for b in range(3):
    square[a,b] =matrix[a+3,b+6]
 if n == 6:
  for a in range(3): 
   for b in range(3):
    square[a,b] =matrix[a+6,b]
 if n == 7:
  for a in range(3): 
   for b in range(3):
    square[a,b] =matrix[a+6,b+3]
 if n == 8:
  for a in range(3): 
   for b in range(3):
    square[a,b] =matrix[a+6,b+6]
 return square

def getsquare(x,y):
 if 0 <= x < 3 and 0 <= y < 3:
   return 0
 if 0 <= x < 3 and 3 <=y < 6:
   return 1
 if 0 <= x < 3 and 6 <= y < 9:
   return 2
 if 3 <= x < 6 and 0 <= y < 3:
   return 3
 if 3 <= x < 6 and 3 <= y < 6:
   return 4
 if 3 <= x < 6 and 6 <= y < 9:
   return 5
 if 6 <= x < 9 and 0 <= y < 3:
   return 6
 if 6 <= x < 9 and 3 <= y < 6:
   return 7
 if 6 <= x < 9 and 6 <= y < 9:
   return 8

def getrange(n):
 ran = []
 for x in range(9):
  for y in range(9):
   if getsquare(x,y)== n:
    ran.append((x,y))
 return ran

def dosquare(x,y):
 num = getsquare(x,y)
 for cor in getrange(num):
  if cor!=(x,y) and single(cor[0],cor[1]) and get(cor[0],cor[1]) in matrix[x,y]:
   matrix[x,y].remove(get(cor[0],cor[1]))

def deduce():
 for m in range(1,10):
  for n in range(9):
   list = [cor for cor in getrange(n) if m in matrix[cor]]
   if len(list) == 1:
    matrix[list[0]] = [m]

def rowdeduce():
 for m in range(1,10):
  for n in range(9):
   list = [cor for cor in row(n) if m in matrix[cor]]
   if len(list) == 1:
    matrix[list[0]] = [m]

def columndeduce():
 for m in range(1,10):
  for n in range(9):
   list = [cor for cor in column(n) if m in matrix[cor]]
   if len(list) == 1:
    matrix[list[0]] = [m]

def sudoprint():
 for y in range(9):
  for x in range(8):
   if single(y,x):
    print get(y,x),
   else:
    print 0,
  if single(y,8):
   print get(y,8)
  else:
   print 0
 
def solve():
 for x in range(9):
  for y in range(9):
   dorow(x,y)
   docolumn(x,y)
   dosquare(x,y)
   deduce()
   rowdeduce()
   columndeduce()

def absurd():
 for n in range(1,10):
  for count in range(9):
   aux = [cor for cor in row(count) if n in matrix[cor]]
   if aux == []:
    return True
   aux = [cor for cor in column(count) if n in matrix[cor]] 
   if aux == []: 
    return True 
   aux = [cor for cor in getrange(count) if n in matrix[cor]] 
   if aux == []: 
    return True 
 return False 


