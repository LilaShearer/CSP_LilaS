
#Chiara variables
cakeFlavor=2
frosting=2

#River varables
cakepan=2
cakeStat= 2
ovenTemp = 2

#Lizzie variables
frostPiped=3
allToppings = ["sprinkles", "strawberries", "fudge sauce"]
isSprinkles = False
isStrawberries = True
isFudge = False
notoppings = 2
toppings = 2
response = 2

print("\nIt's time to present your creation!\n") 

if frosting == 1:
    frosting = "buttercream"
elif frosting == 2:
    frosting = "cream cheese"
else:
    frosting = "swiss meringue"

if cakeFlavor == 1:
    cakeFlavor = "vanilla"
elif cakeFlavor == 2:
    cakeFlavor = "chocolate"
else:
    cakeFlavor = "strawberry"

if cakepan == 1:
    cakepan = "circle"
elif cakepan == 2:
    cakepan = "square"
else:
    cakepan = "multi-tiered"

if frostPiped == 1:
    frostPiped = "very nice looking"
elif frostPiped == 2:
    frostPiped = "decent looking"
else:
    frostPiped = "nonexistant"


if isSprinkles == True and isStrawberries == True and isFudge == True:
    toppings = " sprinkles, strawberries, and fudge"
elif isSprinkles == True and isStrawberries == True and isFudge == False:
    toppings = " sprinkles and strawberries"
elif isSprinkles == True and isStrawberries == False and isFudge == True:
    toppings = " sprinkles and fudge"
elif isSprinkles == False and isStrawberries == True and isFudge == True:
    toppings = " strawberries and fudge"
elif isSprinkles == True and isStrawberries == False and isFudge == False:
    toppings == " sprinkles"
elif isSprinkles == False and isStrawberries == True and isFudge == False:
    toppings = " strawberries"
elif isSprinkles == False and isStrawberries == False and isFudge == True:
    toppings = " fudge"
else:
    toppings = " no toppings"


#This is my code for the response
if frostPiped == "very nice looking" and cakeStat == 2:
    response = "loved"
elif frostPiped == "nonexistant" and cakeStat == 2 or frostPiped == "nonexistant" and toppings != " no toppings":
    response = "almost enjoyed"
elif frostPiped == "very nice looking" and cakeStat == 1 or cakeStat == 2:
    response = "liked"
elif frostPiped == "decent looking" and cakeStat == 2:
    response = "liked"
else:
    response = "hated"



def customerResponse(response,cakepan,cakeFlavor,frostPiped,frosting,toppings):
    print(f'The critic {response} your {cakepan} {cakeFlavor} cake with {frostPiped} {frosting} frosting and{toppings}.')

customerResponse(response, cakepan, cakeFlavor, frostPiped, frosting, toppings)

print("\nThank you for playing baking simulator!")