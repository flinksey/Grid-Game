import random as rdm

def set_up():
  M = int(input("no. of rows: "))
  N = int(input("no. of cols: "))
  K = int(input("boundary no: "))

  nums = [rdm.randint(0,K-1) for i in range(M*N)] #nums displayed in each cell of the grid
  kys = [(a,b) for a in range(M) for b in range(N)] #tuples representing coords of each cell
  #print to double-check
  print(nums) 
  print(kys)

  #initially, used a list but wanted to see if using a dict would make it easier to select & manipulate a cell given the coords from User
  grid_vals = {kys[_]: nums[_] for _ in range(M*N)}
  print(grid_vals)
  #print(len(grid_vals))
  
  #works up to here---------------|
  #figuring out how to actually generate the grid

  for row in range(M):
      for col in range(N):
          print()
    
set_up()
