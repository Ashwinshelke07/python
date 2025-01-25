'''Exercise 6: Tax and Tip
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places'''

'''Prompt the User for the Meal Cost:

Use the input() function to read the cost of the meal from the user. Since input() returns a string, convert it to a floating-point number using float().
Define the Tax Rate and Tip Percentage:

Set your local tax rate as a decimal (e.g., for a 5% tax rate, use 0.05).
Define the tip percentage as 18%, represented as 0.18.
Calculate the Tax Amount:

Multiply the meal cost by the tax rate to determine the tax amount.
Calculate the Tip Amount:

Multiply the meal cost by the tip percentage to determine the tip amount.
Compute the Total Cost:

Sum the meal cost, tax amount, and tip amount to get the total cost.
Display the Results:

Print the tax amount, tip amount, and total cost, each formatted to two decimal places.'''

cost_of_meal=float(input("the cost of the meal from the user:$"))
tax_rate=5
tip_percentage=18
tax_amount=cost_of_meal*tax_rate
tip_amount=cost_of_meal*tip_percentage
total_cost=cost_of_meal+tax_amount+tip_amount
'''print(f"{tax_amount=:.2f}")
print(f"{tip_amount=:.2f}")
print(f"{total_cost=:.2f}")'''
print(f"{tax_amount=: .2f}")
print(f"{tip_amount=: .2f}")
print(f"{total_cost=: .2f}")