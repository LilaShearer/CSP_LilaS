
#Chiara variables
cakeFlavor=1
frosting=3

#River varables
cakepan=3
cakeStat= 3
ovenTemp = 3

#Lizzie variables
frostPiped=3
allToppings = ["sprinkles", "strawberries", "fudge sauce"]
isSprinkles = False
isStrawberries = False
isFudge = False
#Lila Variables
toppings = 2
response = 2
explanationMessage = 0


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
if frostPiped == "very nice looking" and cakeStat == 2 and toppings != " no toppings":
    response = "LOVED"
    explanationMessage = "Your cake was perfect!"
elif frostPiped == "very nice looking" and cakeStat == 2 and toppings == " no toppings":
    response = "enjoyed"
    explanationMessage = "Your cake was very good, but it was a little boring on the outside."
elif frostPiped == "nonexistant" and cakeStat == 2 or frostPiped == "nonexistant" and toppings != " no toppings":
    response = "almost enjoyed"
    explanationMessage = "Your cake was lacking in some areas."
elif frostPiped == "very nice looking" and cakeStat >=1:
    response = "liked"
    explanationMessage = "A few things could be improved, but overall you did a pretty good job. Consider watching the oven more closely next time."
elif frostPiped == "decent looking" and cakeStat == 2:
    response = "liked"
    explanationMessage = "A few things could be improved, but overall you did a pretty good job. Consider improving your method for putting frosting on the cake."
else:
    response = "hated"
    explanationMessage = "Your cake was not very good. It was lacking in several areas and was not enjoyable."


def customerResponse(response,cakepan,cakeFlavor,frostPiped,frosting,toppings, explanationMessage):
    print(f'The critic {response} your {cakepan} {cakeFlavor} cake with {frostPiped} {frosting} frosting and{toppings}. {explanationMessage}')

customerResponse(response, cakepan, cakeFlavor, frostPiped, frosting, toppings, explanationMessage)

print("\nThank you for playing baking simulator!\n")