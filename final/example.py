
#Chiara variables
cakeFlavor=1
frostingFlavor=2

#River varables
cakepan=1
cakeStat= 2
ovenTemp = 0

#Lizzie variables
frostPiped=1
allToppings = ["sprinkles", "strawberries", "fudge sauce"]
isSprinkles = False
isStrawberries = False
isFudge = False
notoppings = 0
toppings = 0
response = 0
explanationMessage = 0
customerAnswer = 0


def toppingRequest(theTopping):
    global response
    response = input(f"Would you like {theTopping} (Yes or No)?\n").strip().upper()
    print(response)

for item in allToppings:
    toppingRequest(item)
    if response == "YES" and item == "sprinkles":
        isSprinkles = True
    else:
        isSprinkles = False

    if response == "YES" and item == "strawberries":
        isStrawberries = True
    else:
        isStrawberries = False

    if response == "YES" and response == "fudge sauce":
        isFudge = True
    else:
        isFudge = False

print(isSprinkles)
print(isStrawberries)
print(isFudge)