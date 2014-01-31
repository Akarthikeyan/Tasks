SIZE=8
def under_attack(column,queens):
  left=right=column
  for r,c in reversed(queens):
    left,right=left-1,right+1
    if c in(left,col,right):
      return true
  return false
def solve(i):
  if i==0:
  return[]
  small_solution=solve(n-1)
  return[solution+[(n,i+1)]
    for i in range(SIZE)
      for solution in small_solution
        if not under_attack(i+1,solution)
for answer in solve(SIZE):
print answer
