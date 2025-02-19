# Lila Shearer, Updated Hello World

def name():
    name_input = input("Please write a name:\n").strip().capitalize()
    return (f"Hello, {name_input}!")
    
print(name())
print("Zachary"())
print(name())
print(name())
print(name())

#I decided to do user inputs on this assignment because I could. The way that it would look if it wasn't a user input would be like this:
#def name(nameVariable):
#   return (f"Hello, {nameVariable})