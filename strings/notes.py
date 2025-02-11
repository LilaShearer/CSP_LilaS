# Lila Shearer, Strings Notes Python

#string is a data type that holds informaiton surrounded by " " or ' '

#print("Hello, World") is a string. 
#note = "Hello, World" is also a string
#note = 'Vienna's class' is not a string because computers cannot distinguish between apostrophes
#  and single quotes.
#every opening must have a closing. 

sentence = "The quick brown fox jumps over the lazy dog."

name = input("What is your first name?\n").strip().capitalize()
#this is concatenation
print(f"Hello {name}, welcome to my program!")

print("this is your name: "+ name)
#when we get syntax errors, it is because we didn't do things right. 

#check the line before when debugging to make sure that the issue isn't on the line before. 

# a run time error happens when the code can run until it stops doing the thing. 

#concaitation means putting two strings together. In python we yse the addition symbol. 
# This is concatenation print("this is your name"+ name)

sentence = "The quick brown fox jumps over the lazy dog."

print(len(sentence))

print(sentence[4:7])

print(sentence.find("fox"))

print(sentence[16:19])