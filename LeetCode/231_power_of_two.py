import math


def is_power_of_two(n):
  if n == 0:
    return "false"
  print(math.log2(n))  
  if (math.log2(n)).is_integer():
    return "true"
  return "false"
   


def main():
  n = int(input("Enter n to check is power of two: "))
  print(is_power_of_two(n))


if __name__ == '__main__':
  main()  
