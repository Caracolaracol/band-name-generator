#print to the console
print("Hello world!")
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# new line

print("Hello world!\nHellow world!")

print("Hello" + " " + "Angela 🥰") 


#Fix the code below 👇

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# input

print("Hello " + input("what is your name?"))


#Write your code below this line 👇
## print(len(input("what is your name?")))
name = input("what is your name?")
length = len(name)
print(length)

# switch program exercise

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
algo = a
algo2 = b
b = algo
a = algo2
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# 100daysofcode 
# band name generator
print("Hello, welcome to the band name generator")
city = input("what's name of the city you grew up in?\n")
pet = input("what's name of your pet?\n")

print("your band name should be " + city + " " + pet )