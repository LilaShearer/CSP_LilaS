cakeFlavor = 0
frosting = 0
cakepan = 0
cakeStat = 0
ovenTemp = 0
frostPiped = 0
isSprinkles = False
isStrawberries = False
isFudge = False
notoppings = 0
toppings = 0

# General ideas, I was thinking two inputs for each person - River
#frosting = 1
#cakeFlavor = 2
#cakepan = 0
#frostPiped = 1
#isSprinkles = True
#isStrawberries = True
#isFudge = True
#cakeStat = 2

print("\nIt's time to present your creation!\n")

# Frosting logic
if frosting == 0:
    frosting = "buttercream"
elif frosting == 1:
    frosting = "cream cheese"
else:
    frosting = "swiss meringue"

# Cake flavor logic
if cakeFlavor == 0:
    cakeFlavor = "vanilla"
elif cakeFlavor == 1:
    cakeFlavor = "chocolate"
else:
    cakeFlavor = "strawberry"

# Cake pan logic
if cakepan == 0:
    cakepan = "circle"
elif cakepan == 1:
    cakepan = "square"
else:
    cakepan = "tiny"

# Frosting piped logic
if frostPiped == 0:
    frostPiped = "very nice looking"
elif frostPiped == 1:
    frostPiped = "ok looking"
else:
    frostPiped = "nonexistent"


# if isSprinkles == true and isStrawberries == true and isFudge == true:
    #print all of the toppings
# sprinkles, strawberries, no fudge
# sprinlkes no strawberries, fudge
# no sprinkles, strawberries, fudge
# sprinkles, no straw, no fudge
#no sprinkles, straw, no fudge
# no sprinkles, no straw, fudge
# nothing

if isSprinkles == True and isStrawberries == True and isFudge == True:
    toppings = " sprinkles, strawberries, and fudge"
elif isSprinkles == True and isStrawberries == True and isFudge == False:
    toppings = " sprinkles and strawberries"
else:
    print("HI")








#CODE for response
# if frostPiped == "very nice looking" and cakestat == 2:
#   response = "loved"
# elif frostPiped == "very nice looking" and cakestat == 1 or cake stat == 2:
#   response = "liked"
# elif frostPiped == "decent looking" and cakestat == 2:
#   response = "liked"
# elif frostPiped == "nonexistant" and cakestat == 2:
#   response = "almost enjoyed"
# else:
#   response = "hated"






# Function to print customer response
def customerResponse(response, cakepan, cakeFlavor, frostPiped, frosting, toppings):
    print(f'The customer {response} your {cakepan} {cakeFlavor} cake with {frostPiped} {frosting} frosting, and {toppings}.')

# Correct the function call here
customerResponse(response, cakepan, cakeFlavor, frostPiped, frosting, toppings)

print("\nThank you for playing baking simulator!")