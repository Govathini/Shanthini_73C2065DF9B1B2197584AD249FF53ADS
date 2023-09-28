# 1.1 implement a recursive function to calculate the factorial of a given number.

"""
1! = 1 X 1
2! = 2 X 1 --->2 X 1
3! = 3 X 2 --->3 X 2 X 1
.
. 
10! = 10 X 9!
  
"""

def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
      return n*fact_rec(n-1)

number=int(input("enter the value:"))
res=fact_rec(number)

print("the factorial of {} is {}.".format(number,res))