# Lila Shearer, Conditionals Notes Python


#AN IF STATEMENT SHOULD NEVER BE ON ITS OWN. IT SHOULD ALWAYS COME WITH AN ELSE IN CASE THE CONDITION IS FALSE.

#1) What puts something inside of the “if” statement?
#if condition:
#    then do action
name = input("\nWhat is your name?\n")
if name == "LaRose":
    print("Hi, Ms. LaRose!")
#) The tab at the front is what puts something inside of an if statement


#2) What do if statements do?

# If statements check a condition and if it is true it will do a thing. 
if name == "LaRose": #<- this is the condition!
    print("Hi, Ms. LaRose!") #<- this is what it does if true
else:
    print(f"Hello, {name}. You are not as cool as Ms. LaRose.\n") #<- this is what it does if it is not true. 

#3) What are boolean statements? 

# The part of your conditional that is either true or false. It's a true or false statement
name = input("\nWhat is your name?\n")
if name == "LaRose": #<- this is the boolean statement. 
    print("Hi, Ms. LaRose!")
else:
    print(f"Hello, {name}. You are not as cool as Ms. LaRose.\n")

#4) What do else statements do?

# If the boolean is false, the else statement happens. 
if name == "LaRose": #<- this is the condition!
    print("Hi, Ms. LaRose!") #<- this is what it does if true
else:
    print(f"Hello, {name}. You are not as cool as Ms. LaRose.\n") #<- this is what it does if it is not true. 

#5) What kind of statement do you use if you have more than 2 needed outcomes?
num = int(input("\nHow many are there?\n"))
if num == 0: #<- if always starts the conditional
    print("\nThere are none.\n")
elif num == 1: #<- everything in between else and if should be elif. 
    print("\nThere is one.\n")
elif num <4:
    print("\nThere are a couple.\n")
elif num <10:
    print("\nThere are a few.\n")
else: #<- else always ends the conditional
    print("\nThere are many.\n")
#COMPUTERS READ CODE TOP DOWN. THIS WHY WE STARTED WITH 0 AND WORKED OUR WAY UP INSTEAD OF STARTING WITH <10. 
#You check least likely to most likely. If you were doing a program to check who won a rock paper scissors match, you would check if it was a tie first. 

#6) What do each of the different symbols mean in conditionals?
# NOTE: SOME OF THESE DON'T GET USED IN PYTHON
#<   Less than

#>   Greater than

#<=  Less than or equal to

#>=  Greater than or equal to

#==  This is equal to. Just one equal is setting a variable or value. 

#===  THIS DOESN'T EXIST IN PYTHON

#!   This means not. (!false. It's funny becaues it's true!)

# The ! checks the opposite of a condition when placed by one. 
num = int(input("\nHow many are there?\n"))
if num == 0: #<- if always starts the conditional
    print("\nThere are none.\n")
elif num != 1: #<- NOW IT IS CHECKING IF IT IS NOT ONE.
    print("\nThere is one.\n")
elif num <4:
    print("\nThere are a couple.\n")
elif num <10:
    print("\nThere are a few.\n")
else: #<- else always ends the conditional
    print("\nThere are many.\n")



#7) What are the 3 logical operators?
if num <10 and num > 5: #<- there are two boolean statements here. You are connecting them together using the keyword 'and'. And is for when both booleans are true.,
    print("Wow. That is a a big single digit number.\n")
elif num <10 or num >5: #<- or means that one of them must be true.
    print("This is a single digit number.")
elif not num <10: #<- not changes to check if false. 
    print("That is not a single digit number.\n")

# The 3 logical operators are AND, OR, and NOT
else: 
    print("Why didn't you choose a number between 5-10?\ln")
#

#8) What are logical operators for?

# allows the code to handle more difficult questions and increases complexity.

#9) What does a nested conditional statement do?
if num <10:
    if num ==8:
        print("This prints when the number is eight. ")
    else:
        print("The number is less than 10. ")
else:
    print("This prints when it is more than 10.\n")
# This is an if statement inside of an if statement. 





#10) How do you write an if statement in C?

#11) How do you write else statements in C?


#How do you write elif/ else if statements in C?


#How do you write the 3 logical operators in C?
