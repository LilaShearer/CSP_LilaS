# Lila Shearer, Loops Notes Python


#1)What is a loop? 

# A section of code that repeats multiple times

#2)What are the two types of loops?

    #for loop
nums = [12,3,66,7,3,3,2]
for num in nums:
    print(num)

    #while loop
x=0
while x < 10:
    print(x)
    x+= 1

#3)What is iteration

# IMPORTANT VOCAB WORD! An iteration just one instance of the loop. One particular instance of a loop. Iteration without the an is just the number of times you are looping through

#4)What are lists? 

# A list is a group of many things that are related. IN PYTHON, a list is a variable that stores multiple values. 

nums = [1,2,3,4,5,6,7,8,21]

siblings = ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Hailey"]
#print(nums) # don't print like this EVER. It's UGLY.
print(siblings[3]) #computers start counting at 0. This prints just one of the things in the list. It will print Vienna.

siblings[7] = "Jake" # This changes the name in spot 7 - Hailey - to Jake.

siblings.pop(5) #This will remove number 5 from the list. 

siblings.insert(1, "Jayshree") # This tells it where we want it to go in the list. 

siblings.insert(2, ["Joe", "Noah", "Zee"]) #This inserts the items in this list into the list.
#To see these changes you have to print again.

#5)How do you make lists in python? 

# Step 1) use brackets.
# Step 2) add in items with CORRECT DATA TYPES. Strings have quotations marks, integers do not.
# Step 3) add a comma between each item.


#6)How do you make for loops in python? 

for sibling in siblings: #When you make a list, use a plural word. Then you put the singular version
    print(sibling)


for x in range(1,5): #This is a for loop that doesn't require a list. To change what it counts by, add another number ex: for x in range(0,101, 20) <- this will count all the way to 100 by 20s
    print(x) #It only counts to 4 because it stops at the number you give it. To get it to print to five, tell it to go to six.

#7)How do you make while loops in python?

import random # random is a library that lets you randomize numbers

goose = random.randint(1, 20) #start with some sort of variable that will keep count of the iteration.
print("Welcome to Duck Duck Goose!")
while x <= 20:
    if x == goose:
        print("Goose!")
        break #tells the loop to stop.
    else:
        print("Duck")
    x+= 1 #Every time the loop iterates, it will increase x by one. This doesn't go in an else statement.

#continue stops an iteration and moves on to the next iteration. It sends it back to while.