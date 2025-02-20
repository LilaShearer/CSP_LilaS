# Lila Shearer, Financial Calculator Update - Python

def info(cost, income, type):
    percent = (cost/income * 100)
    print(f"The amount of money you spend on {type} is ${cost:.2f}, which is {percent}% of your monthly income.")

print(" ")
# print statement that welcomes user and tells what program does
print("Welcome to Financial Calculator!\nThis program is designed to calculate what percentage of your income that expenses and savings take up, and show how much you have left to spend.")
# user input - what is your monthly income (variable an input)
print(" ")
income = float (input("What is your monthly income: "))
# user input - what is your monthly rent or mortgage (variable an input)
rent = float (input("What is your monthly expense for rent or mortgage: "))
# user input - what is your monthly utilities bill (variable an input)
utilities = float (input("What is your monthly expense for utility: "))
# user input - what is your monthly expense on groceries (variable an input)
groceries = float (input("What is your monthly expense for groceries: "))
# user input - what is your monthly expense for transportation (variable an input)
transportation = float(input("What is your monthly expense for transportation: "))
# calculate savings as 10% of income (income * 0.1) (variable not input)
print(" ")
print("Here are your results!")
savings = (income/10)
spending = (income-rent-utilities-groceries-transportation-savings)

# Your rent expenses are $xx.xx, which is xx% of your income. (print)
info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")
print(" ")
print("Thank you for using Financial Calculator!\nHave a great day!\n")







