#list datastructure
#ordered, indexes, duplicate, changeable

countries=["Tanzania","United Kingdom","Kenya"]
print(countries)
countries[0]="USA"
print(f"i am from {countries[2]}")
# ttuple datastructure normal brackets -unchangeable
fruits=("banana","apple","mango","oranges","avocados")
print (fruits)

print(f"I love eating {fruits[1]}")

#set datastructures
#unordered,unindexed
cars={"Howo","Nissan","Mercedes","Mazda"}
print(cars)
#Dictionaries datastructure #keyvalue pair (key-name) (value-Pat)
students={"name":"Pat","course":"Data Science","age":"19"}
print(students)
print(f"Student's name:{students['name']}")
print(f"Student's course:{students['course']}")
print(f"Student's age:{students['age']}")