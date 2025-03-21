cakeFlavor=0
frosting=0
cakepan=0
cakeStat= 0
ovenTemp = 0
frostPiped=0
isSprinkles = False
isStrawberries = False
isFudge = False
notoppings = 0
toppings = 0
#general ideas,  I was thinking two inputs for each person -River

#welcome banner, intro 
print("\nWelcome to baking simulator. In this game you will get to bake a cake and have a critic try it. The critic will give feedback based on your cake!")
#customer speech EX: Bake me your best cake!

#Chiara What kind of cake? EX: vanilla, chocolate, strawberry 
# 0 = vanilla, 1 = choco, 2 = strawberry
# Make user input a function   

#Chiara what kind of frosting EX: Buttercream, cream cheese, swiss meringue
# 0 = buttercream, 1 = cream cheese, 2 = swiss meringue

#River Cake pans EX: circle, square, cupcakes # IMPORtANT: It is hard to do cupcakes in my print statement without having to change everything. Could we change this to be a tiny cake instead? That will make it easier for me to do my print statement - Lila
# 0 = circle, 1 = square, 2 = cupcakes

#River temperature EX: 325-375 normal bake, under is underbaked, over by like 20 is overbaked any further is broken and on fire oven
# 0 = underbaked, 1 = perfect, 2 = overbaked
# make temp a conditional
# if checks if underbacked (majorly)
# elif check 


#Lizzie frosting EX: pipped on, spooned on, none 
# 0 = piped, 1 = spooned, 2 = none

#Lizzie toppings EX: sprinkles, strawberries, fudge sauce
# 0 =  sprinkles, 1 = strawberries, 2 = fudge
# use a loop to loop through all topping options
# use a funtion to print out eat topping request statement

#Lila results EX: The customer loved your (size, flavor, topping) cake! The custom demanded a refund as their cake was over/under baked
# change type for each variable. Use if statement to replace number with what it is (ex: if cakeFlavor = 1 then change it to cakeFlavor = 'chocolate')
# Use function to print out The customer (love, liked, dislike, hated) your (size) (flavor) cake with (frosting type) frosting and (topping or no toppings)


frosting = 1
cakeFlavor = 0
cakepan = 2
frostPiped = 0
isSprinkles = True
isStrawberries = True
isFudge = False
cakeStat = 1

print("\nIt's time to present your creation!\n")

if frosting == 0:
    frosting = "buttercream"
elif frosting == 1:
    frosting = "cream cheese"
else:
    frosting = "swiss meringue"

if cakeFlavor == 0:
    cakeFlavor = "vanilla"
elif cakeFlavor == 1:
    cakeFlavor = "chocolate"
else:
    cakeFlavor = "strawberry"

if cakepan == 0:
    cakepan = "circle"
elif cakepan == 1:
    cakepan = "square"
else:
    cakepan = "tiny"

if frostPiped == 0:
    frostPiped = "very nice looking"
elif frostPiped == 1:
    frostPiped = "ok looking"
else:
    frostPiped = "nonexistant"

if isSprinkles == False:
    notoppings = notoppings+1
else:
    if isStrawberries == True:
        isSprinkles= " sprinkles,"
    else: 
        toppings = " sprinkles"

if isStrawberries == False:
    notoppings = notoppings+1
else:
    if isSprinkles == True and isFudge == True:
        isStrawberries = " and strawberries,"
    elif isSprinkles == True and isFudge == False:
        isStrawberries = " and strawberries"
        toppings = isSprinkles+isStrawberries
    else:
        toppings = " strawberries"

if isFudge == False:
    notoppings = notoppings+1
else:
    if isStrawberries == True:
        isFudge = " and fudge"
        toppings = isStrawberries+isFudge
    else:
        toppings = " fudge"
        


if notoppings == 3:
    isSprinkles+isStrawberries
    toppings = isSprinkles+isFudge
    toppings = "no toppings"
else:
    1+1 #place holder.

# Time to code the response

if cakeStat == 0:
    response = "didn't like"
elif cakeStat == 1:
    response = "loved"
else:
    response = "didn't like"


def customerResponse(response,size,flavor,frostPiped,frosting, toppings):
    print(f'The customer {response} your {cakepan} {cakeFlavor} cake with {frostPiped} {frosting} frosting and{toppings}.')

customerResponse(response, cakepan, cakeFlavor, frostPiped, frosting, toppings)

print("\nThank you for playing baking simulator!")