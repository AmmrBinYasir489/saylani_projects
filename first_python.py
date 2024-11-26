#this is my first python program
print('i like to code!')
print("i want to become bro code!")

print("1", "2", "3", end='\n' , sep=",")

# variable declaration ( string integer float boolean)

full_name = "ammar bin yasir" # ---> string
age = 20    # ---> integer
gpa = 3.64    # ---> float
is_student = True

print(f"hello {full_name}")   #_---> f mean format  using this we can add variable any where in string
print(f"you are {age} year old")
print(f"your {gpa} year old")
print(f"you are student? {is_student}")


#  arithmetic operators  = +(addition)  -(subtract)  /(float division)  //(integer division)  *(multiplication)  %(modulus)  **(square)

friend = 25
friend += 10 #augumented arithmetic operator   # note: in python no (++) increment operator
print(friend)

num_one = 20
num_two = 5
print(f"the division will give following answer {num_one // num_two}")
print(f"the division will give following answer {num_one / num_two}")
print(f"the division will give following answer {num_one ** num_two}")

#  typecasting = the process of converting a variable from one datatype to another
#           str(),  int(),  float(), bool()

full_name = "ammar bin yasir" # ---> string
age = 20    # ---> integer
gpa = 3.64    # ---> float
is_student = True

print(type(full_name))
print(type(age))
print(type(gpa))
print(type(is_student))
print(f"converting float {gpa} to integer {int(gpa)}")
print(f"converting integer {age} to float {float(age)}")

# str to bool give different value
# if the string is empty then (false) else (true)
print(f"converting str {full_name} to bool {bool(full_name)}")

name = ""
print(f"converting str {name} to bool {bool(name)}")


# if else statements
age = int(input("enter your age "))

if age >= 18:
    print("you are adult")
elif age < 0:
    print("you haven't born yet")
else:
    print("you are child")


# logical operators

temp = int(input("enter temperature in celcius "))
is_raining = False

if temp > 35 or is_raining or temp < 0:
    print("cancel outdoor activity 😔")
else:
    print("the outdoor event is still scheduled  😂😂")

if 28 > temp > 0 and is_raining == False:
    print("temperatur is normal outside 😎(●'◡'●)")
else:
    print("stay home 😔🥲")


# while loop

name = input("enter your name ")
while name == "":
    name = input("enter your name ")

print(f"hello {name} !")


#for loop

for i in range(1, 10):   # i = index, counter     range = function
    print(i)

# list [] = mutable, most flexible
# tuple () = immutable, faster
# set {} = mutable (add/remove), unordered,  no duplicate, best for membership testing

# these are similar to arrays

fruits = ['apple', 'banana', 'orange', 'strawberry']
print(fruits)
print(fruits[0])
print(fruits[-1])

fruits[0] = "pineapple"
print(fruits)

fruits.append("mango")
print(fruits)

fruits.remove("mango")
print(fruits)

fruits.pop(2)
print(fruits)

fruits.clear()

country = ("pakistan", "china")
#country[0] = "iran" # dosnot support item assignment that is immutable also not able to apply append remove so on...

names = {"ammar", "naeem", "waseem", "ali"}
print(names) #change order each time only add and remove
names.add("saim")
print(names)
names.remove("ali")
print(names)