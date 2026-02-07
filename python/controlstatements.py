#nambari=int(input("Enter number:"))
#if nambari % 2 ==0:
    #print(f"{nambari} is an even number")
#else:
    #print(f"{nambari} is an odd number")

#create a script that checks the largest number
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))

#if num1<num2>num3:
   # print(f"{num1} is less than {num2} and is greater than {num3} ")
#else:
   # print(f"{num2} is less than {num3} and is greater than {num1} ")

if num1>num2 and num1>num3:
    print(f"{num1} is greater than {num2} and {num3}")
elif num2>num1 and num1>num3:
    print(f"{num2} is greater than {num1} and {num3}")
elif num3>num1 and num3>num2:
    print(f"{num3} is greater than {num1}")
else:
    print("All of the same")