# CHALLENGES

# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  sum = 0
  for num in range(1, n+1):
    sum += num
  print (sum)

sum_to(6)

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(list):
  print (max(list))

largest([10, 4, 2, 231, 91, 54])

# 3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurences(str1, str2):
  print(str1.count(str2))

occurences('fleep floop', 'fe')

# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*nums):
  p = 1
  for num in nums:
    p = p * num
  print (p)

product(-1, 4)