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
frosting = 1
cakeFlavor = 2
cakepan = 0
frostPiped = 1
isSprinkles = True
isStrawberries = True
isFudge = True
cakeStat = 2

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

toppings = []  # Start with an empty list for toppings

if isSprinkles:
    toppings.append("sprinkles")
if isStrawberries:
    toppings.append("strawberries")
if isFudge:
    toppings.append("fudge")

if len(toppings) == 0:
    toppings = "no toppings"
else:
    # If there are multiple toppings, add 'and' between the last two
    if len(toppings) > 1:
        toppings[-1] = "and " + toppings[-1]
    # Join the toppings with commas
    toppings = ', '.join(toppings)


# Time to code the response
if cakeStat == 0:
    response = "didn't like"
elif cakeStat == 1:
    response = "loved"
else:
    response = "didn't like"


# Function to print customer response
def customerResponse(response, size, flavor, frostPiped, frosting, toppings):
    print(f'The customer {response} your {cakepan} {cakeFlavor} cake with {frostPiped} {frosting} frosting, and {toppings}.')

# Correct the function call here
customerResponse(response, cakepan, cakeFlavor, frostPiped, frosting, toppings)

print("\nThank you for playing baking simulator!")