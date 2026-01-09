# 1.if number is zero print like "The num is zero"

#n = int(input())
#if n == 0:
 #   print("The number is zero")
#print("Program Done")
                                                            
#------------------------------------------

# 2.Checkif number is zero or not

# approch 1

#num = int(input("Enter the Number:"))
#if num == 0:
 #   print("The Given Number is Zero")
#else:
 #   print("The Given Number is not zero")

# approch 2

'''num = int(input("Enter the Number:"))
if num != 0:
    print("The Number is Not Zero")
else:
    print("The Number is zero")'''



num= int(input("Enter the Number: "))
if num % 2 == 0 and num >= 0:
    print("The Number is +ve even")
elif num % 2 == 0 and num <= 0:
    print("The Number is -ve even")
elif num % 2 != 0 and num >= 0:
    print("The Number is +ve Odd")
elif num % 2 != 0 and num <= 0:
    print("The number is -ve Odd")
else:
    print(" program Done")

