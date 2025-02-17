'''Exercise 9: Compound Interest

Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.'''

# Define the annual interest rate
annual_interest_rate = 0.04

# Prompt the user to enter the initial deposit amount
principal = float(input("Enter the initial deposit amount: "))

# Calculate the balance after each year
balance_year_1 = principal * (1 + annual_interest_rate)
balance_year_2 = balance_year_1 * (1 + annual_interest_rate)
balance_year_3 = balance_year_2 * (1 + annual_interest_rate)

# Display the balances, rounded to 2 decimal places
print(f"Balance after 1 year: ${balance_year_1:.2f}")
print(f"Balance after 2 years: ${balance_year_2:.2f}")
print(f"Balance after 3 years: ${balance_year_3:.2f}")

