# Lila Shearer, Financial Calculator Update - Python

print("\nWelcome to Financial Calculator!\nThis program is designed to calculate what percentage of your income that expenses and savings take up, and show how much you have left to spend.\n")
print("When answering questions, please write numbers and do not include the dollar sign (example: 256.78). Thanks!\n")  

income = float(input("What is your income?\n"))

def info(cost, income, type):
    percent = (cost/income * 100)
    print(f"That amount of money that goes to {type} is ${cost:.2f}, which is {percent:.1f}% of your monthly income.")

def userInfo(expense):
    return float(input(f"How much do you spend on {expense}?\n"))

rent = userInfo("rent")
utilities = userInfo("utilities")
groceries = userInfo("groceries")
transportation = userInfo("transportation")

savings = income/10
spending = income-rent-utilities-groceries-transportation-savings

print("\nHere are your results!\n")

info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")

print("\nThank you for using Financial Calculator!\nHave a great day!\n")