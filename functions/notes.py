# Lila Shearer, Functions Notes Python

#functions hold actions to be reused

#def add():
   # numOne = int(input("Please tell me a number:\n"))
  #  numTwo = int(input("Please tell me another number:\n"))
   # print(numOne+numTwo)






#number = int(input("Please type a number:\n"))
#def add(numOne, numTwo):
 #   return numOne+numTwo

#print (add(number,21))

#add(5,5)
print("Welcome to updated Hello World! This program takes in 5 names and says hellos to them individually.\n")
def name():
    name_input = input("Please write a name:\n").strip().capitalize()
    return (f"Hello, {name_input}!")
    
print(name())
print(name())
print(name())
print(name())
print(name())





def values(type):
    return input(f"Please give me a {type}\n")

name = values("name")
place = values("place")
verb = values("verb (past tense)")

print(f"{name} was really fast getting to {place} because they {verb} the whole way there.\n")