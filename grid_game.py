import random as rdm

def randomizer(k):
  #Generate random numbers within range to be displayed in the cells
  num = rdm.randint(0,K-1) #will double-check with old notes about this
  return num

def set_up():
  #Get input from user: M, N, K
  M = int(input("Please enter no. of rows: "))
  N = int(input("Please enter no. of cols: "))
  K = int(input("Please enter boundary num: "))
  print("\n")

  #How can I generate the grid?
  dim = M*N   #number of cells
  grid_list = [] #unsure of whether I'll keep this but 

set_up()
