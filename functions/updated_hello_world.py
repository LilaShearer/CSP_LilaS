# Lila Shearer, Updated Hello World
print("Welcome to updated Hello World! This program takes in 5 names and says hellos to them individually.\n")
def name():
    name_input = input("Please write a name:\n").strip().capitalize()
    return (f"Hello, {name_input}!")
    
print(name())
print(name())
print(name())
print(name())
print(name())

#I did user inputs for this, but in case that doesn't fit the assignment requirements, here is what it looks like if it's not user inputs:
#def name(nameVariable):
#    return (f"Hello, {nameVariable}!")
#
#print(name("Peter"))
#print(name("John"))
#print(name("Jacob"))
#print(name("Emily"))
#print(name("Charlie"))