
age = int(input("Enter age :"))


if age >= 18:
    print("You are qualified to be a voter")


else:
    print("You are not qualified to vote")



print()


#A python programm to return for the largest number among three numbers


first = input("Enter first number:")
second = input("Enter second number:")
third = input("Enter third number:")

if first > second and first > third :
     print(first, "is the largest number")

elif second > first and second > third :
    print(second, "is the greatest number")

else :
    print(third, "is the greatest number")


x = int(input("Enter the number :"))

if  x % 2 == 0:
    print(x,"is an even number")

elif x==0:
    print(x,"is a neutral number")

else:
    print(x, "is an odd number")