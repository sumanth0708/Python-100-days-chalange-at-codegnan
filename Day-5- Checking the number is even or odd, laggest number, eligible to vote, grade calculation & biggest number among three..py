# 1.Check wether the number is Even or Odd.

'''n = int(input("Enter any Number: "))
if n%2==0:
    print("The number is Even number")
else:
    print("The number is Odd number")'''
#--------------------------------------------

# 2.Largest of Two Numbers.

'''n1 = int(input("Enter any Number: "))
n2 = int(input("Enter the another Number: "))
if n1<n2:
    print("The Largest Number is: ",n2)
elif n1>n2:
    print("The Largest Number is: ",n1)
else:
    print("The Number's are Equal")'''
#--------------------------------------------

# 3.Checking the vote eligibility of a person.

'''age = int(input("Enter the age: "))
if age<18:
    print("You'r Age is not eligible to vote")
elif age>=18:
    print("Your'r Age is perfect to vote")'''
#--------------------------------------------

# 4.Grade Calculation.

'''m = int(input("Enter you'r total marks: "))
if m>=90:
    print("Grade A")
elif 75<=m<90:
    print("Grade B")
elif 50<=m<75:
    print("Grade C")
elif m<50:
    print("Fail")
else:
    print("Thank you")'''
#------------------------------------------

# 5.Biggest Number among Three.

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the Second number: "))
n3 = int(input("Enter the Third number: "))
if n1<n2<n3:
    print("The Biggest number is: ", n3)
elif n3<n2<n1:
    print("The Biggest number is: ", n1)
elif n3<n1<n2:
    print("The Biggest number is: ", n3)
elif n1==n2==n3:
    print("All are equal")
elif n1==n2<n3:
    print("The Biggest number is: ", n3)
elif n1==n3<n2:
    print("The Biggest number is: ", n2)
elif n2==n3<n1:
    print("The Biggest number is: ", n1)
elif n1==n2>n3:
    print("The Biggest number is: ", n1)
elif n1==n3>n2:
    print("The Biggest number is: ", n3)
elif n2==n3>n1:
    print("The Biggest number is: ", n2)

    




