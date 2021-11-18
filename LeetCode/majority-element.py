from itertools import groupby


def majority_element(nums):
  # First we sort it first
  nums.sort()
  major_ele = 0
  n = len(nums) 
  # after that we will group it and calcutelate its length and compare to the n\2
  
  a =  [list(j) for i,j in groupby(nums)]     

  for i in range(len(a)):
    if len(a[i]) >= n/2:
      return a[i][0]       

def main():
  test = [2,2,2,2,1,1,1,1,2,2]
  print(majority_element(test))


if __name__ == '__main__':
  main()
