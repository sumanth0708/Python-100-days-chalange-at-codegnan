# 1.Nested Conditional ststements

'''n = int(input())

if n%2==0:
    if n>-1:
        print("Number is +ve even")
    else:
        print("Number is -ve even")
else:
    if n>-1:
        print("Number is +ve Odd")
    else:
        print("Number is -ve Odd")'''
#--------------------------------------

# 2.Check which one is even number or Odd number in the given list of numbers

'''lst=[2,4,3,5,6,7,9]

for num in lst:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is Odd")
print("Program done")'''
#---------------------------------------

# 3.Check which one is +ve number or -ve number in the given list of numbers

'''lst=[2,4,-3,5,-6,-7,9]

for num in lst:
    if num >= 0:
        print(num, "is positive")
    else:
        print(num, "is Negative")
print("Program done")'''
#---------------------------------------

# 4.Print 1 to 20 numbers using range function

'''for num in range(1,21,1):
    print(num)'''
#----------------------------------------

# 5.Print even numbers in between 0 to 20 using range function

for num in range(0,21,2):
    print(num, end = " ")
