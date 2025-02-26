# Lila Shearer, Old Enough Python

age = int(input("How old are you in years?\n"))

if age < 5:
    print("You are NOT old enough to go to school, get your learner's permit, drive, or vote.\nWhy are you running this program anyway?\nShouldn't you be playing outside or something?\n")
elif age >= 18:
    print("You are old enough to vote, drive, get your learner's permit, and go to school.\n")
elif age >= 16:
    print("You are old enough to drive. Hopefully you know what you're doing!\n")
elif age >= 15:
    print("You are old enough to get your learner's permit. Exciting!\n")
else:
    print("You are old enough to go to school.\n")