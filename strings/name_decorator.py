# Lila Shearer, Name Decorator Python

decoration_one = "<><>"
decoration_two = "<><>"
messageone = "\nAlright, "
messagetwo = ". Here is your decorated name:\n"
print("\nHello! Welcome to Name Decorator.\nThe purpose of this program is to add decorations to your name.\n")

name = input("What is your first name?\n").strip().capitalize()

print(messageone+name+messagetwo)

print(decoration_one+name+decoration_two)
print("\n")