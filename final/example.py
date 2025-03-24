
#Chiara variables
cakeFlavor=2
frostingFlavor=1

#River varables
cakepan=2
cakeStat= 2

#Lizzie variables
frostPiped=1
allToppings = ["sprinkles", "strawberries", "fudge sauce"]
isSprinkles = True
isStrawberries = True
isFudge = False
#Lila Variables
toppings = 0
response = 0
explanationMessage = 0


if frostingFlavor == 1:
    frostingFlavor = "buttercream"
elif frostingFlavor == 2:
    frostingFlavor = "cream cheese"
else:
    frostingFlavor = "swiss meringue"

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

# This part of my code sets the toppings variable in my print statement so that it prints correctly
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


# This part of my code decides how the critic will respond by looking at what decisions werre made
if frostPiped == "very nice looking" and cakeStat == 2 and toppings != " no toppings":
    customerAnswer = "LOVED"
    explanationMessage = "Your cake was perfect!"
elif frostPiped == "very nice looking" and cakeStat == 2 and toppings == " no toppings":
    customerAnswer = "enjoyed"
    explanationMessage = "Your cake was very good, but it was a little boring on the outside."
elif frostPiped == "nonexistant" and cakeStat == 2 or frostPiped == "nonexistant" and toppings != " no toppings":
    customerAnswer = "sort of enjoyed"
    explanationMessage = "Your cake was lacking in some areas."
elif frostPiped == "very nice looking" and cakeStat >=1:
    customerAnswer = "liked"
    explanationMessage = "A few things could be improved, but overall you did a pretty good job. Consider watching the oven more closely next time."
elif frostPiped == "decent looking" and cakeStat == 2:
    customerAnswer = "liked"
    explanationMessage = "A few things could be improved, but overall you did a pretty good job. Consider improving your method for putting frosting on the cake."
else:
    customerAnswer = "hated"
    explanationMessage = "Your cake was not very good. It was lacking in several areas and was not enjoyable."

# This part of my code is the response. It takes the user's choices and puts them into a print statement.
def customerResponse(customerAnswer,cakepan,cakeFlavor,frostPiped,frostingFlavor,toppings, explanationMessage):
    print(f'The critic {customerAnswer} your {cakepan} {cakeFlavor} cake with {frostPiped} {frostingFlavor} frosting and{toppings}. {explanationMessage}')

customerResponse(customerAnswer, cakepan, cakeFlavor, frostPiped, frostingFlavor, toppings, explanationMessage)


print("\nThank you for playing baking simulator!\n")