# Lila Shearer, Financial Calculator - Python

print(" ")
# print statement that welcomes user and tells what program does
print("Welcome to Financial Calculator!\nThis program is designed to calculate what percentages of your income that expenses and savings take up, and show how much you have left to spend.")
# user input - what is your monthly income (variable an input)
print(" ")
income = float (input("What is your monthly income: "))
# user input - what is your monthly rent or mortgage (variable an input)
rent_mortgage = float (input("What is your monthly expense for rent or mortgage: "))
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
savings_percentage = (savings/income * 100)
# calculate spending as income-savings-rent-utilities-groceries-transportation (variable not input)
spending = (income-rent_mortgage-utilities-groceries-transportation)
# calculate percent income of rent/mortgage (rent/income * 100) (variable)
rent_mortgage_percentage = (rent_mortgage/income * 100)
# calculate percent income of utilites (utilities/income * 100) (variable)
utilities_percentage = (utilities/income * 100)
# calculate percent income of groceries (groceries/income * 100) (variable)
groceries_percentage = (groceries/income * 100)
# calculate percent income of transportation (transportation/income * 100) (variable)
transportation_percentage = (transportation/income * 100)
# calculate percent income is spending (speneding/income * 100) (variable)
spending_percentage = (spending/income * 100)
# Your rent expenses are $xx.xx, which is xx% of your income. (print)
print(" ")
print("The amount of money you spend on your rent or mortage is $",round(rent_mortgage,2), ", which is ",round(rent_mortgage_percentage, 1),"% of your monthly income.", sep = "")
# Your utilities expenses are $xx.xx, which is xx% of your income. (print)
print("The amount of money you spend on utilities is $",round(utilities,2),  ", which is ",round(utilities_percentage, 1), "% of your monthly income.", sep = "")
# Your groceries expenses are $xx.xx, which is xx% of your income. (print)
print("The amount of money you spend on groceries is $",round(groceries,2), ", which is ",round(groceries_percentage, 1), "% of your monthly income.", sep = "")
# Your transportion expenses are $xx.xx, which is xx% of your income. (print)
print("The amount of money you spend on transportation is $",round(transportation,2), ", which is ",round(transportation_percentage, 1), "% of your monthly income.", sep = "")
# You savings is $xx.xx which is xx% of your income. (print)
print("The amount of money you put into savings is $", round(savings, 2), ", which is ",round(savings_percentage,1), "% of your monthly income.", sep = "")
# Your spending is $xx.xx, which is xx% of your income. (print)
print("The amount of money you have left to spend is $",round(spending,2), ", which is ",round(spending_percentage, 1), "% of your monthly income.", sep = "")
print("Thank you for using Financial Calculator!\nHave a great day!\n")
