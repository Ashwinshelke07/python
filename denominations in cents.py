'''Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.
A one dollar coin was introduced in Canada in 1987. It is referred to as a
loonie because one side of the coin has a loon (a type of bird) on it. The two
dollar coin, referred to as a toonie, was introduced 9 years later. Its name is
derived from the combination of the number two and the name of the loonie.'''
2
def calculate_change(cents):
    # Define the denominations in cents
    coin_denominations = {
        "toonie": 200,  # 2 dollars in cents
        "loonie": 100,  # 1 dollar in cents
        "quarter": 25,  # 25 cents
        "dime": 10,     # 10 cents
        "nickel": 5,    # 5 cents
        "penny": 1      # 1 cent
    }

    # For each denomination, calculate how many coins of that denomination are needed
    change = {}
    for coin, value in coin_denominations.items():
        coin_count = cents // value  # Integer division to determine how many coins
        if coin_count > 0:
            change[coin] = coin_count  # Store the coin count in the result
        cents %= value  # Update remaining cents to be the remainder after using this denomination

    return change

# Main part of the program
def main():
    # Read the amount of change (in cents) from the user
    try:
        cents = int(input("Enter the amount of change in cents: "))
        if cents < 0:
            print("The amount must be a positive integer.")
            return
        
        # Calculate the change
        change = calculate_change(cents)
        
        # Display the result
        print("The change should be given as:")
        for coin, count in change.items():
            print(f"{count} {coin}(s)")
    
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

