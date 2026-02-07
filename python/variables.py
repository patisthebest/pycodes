# variables are named storage / containers that store a value that can be changed later on in the program
#variablename=value

first_name="Patrick"
course="Full Stack Development"
country="Kenya"
age=19
hobby="Playing Badminton, Drawing, Photography and gaming"
student_home="Nairobi"
print(first_name)
print(course)
print(country)
print(age)
print (student_home)


#diplaying strings and variables
print("Hello, my name is " + first_name)
print("I am " + str(age) + " years old")
print("I am learning " + course)
print("I live in " + country)
print("My hobbies include " + hobby)
print("I am " + str(age) + " years old and I live in " + country + ". I am learning " + course + " and my hobbies include " + hobby + ".")

#reassigning variables
age=25
print(age)
num1=10
num2=43
print(f"The sum of {num1} and {num2} is {num1+num2}")
print(f"The product of {num1} and {num2} is {num1*num2}")
print(f"The quotient of {num1} and {num2} is {num1/num2}")
print(f"The modulus/remainder of {num1} and {num2} is {num1/num2}")
print(f"The difference of {num1} and {num2} is {num1-num2}")