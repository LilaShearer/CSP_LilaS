# Lila Shearer, Financial Calculator Update - Python



def info(cost, income, type):
    percent = (cost/income * 100)
    print(f"Your expenses for {type} is ${cost:.2f}, which is {percent}% of your monthly income.\n")

def input(expense):
    return input(f"How much do you spend on {expense}:\n")

rent = input("rent")
utilities = input("utilities")
groceries = input("groceries")
transportation = input("transportation")

def income():
    return input("What is your income:\n")


savings = (income/10)
spending = (income-rent-utilities-groceries-transportation-savings)
print(" ")
print("Welcome to Financial Calculator!\nThis program is designed to calculate what percentage of your income that expenses and savings take up, and show how much you have left to spend.")
print(" ")
print("Here are your results!")

info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")
print(" ")
print("Thank you for using Financial Calculator!\nHave a great day!\n")







