'''Exercise 5: Bottle Deposits
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.'''


# Constants for deposit amounts
DEPOSIT_SMALL = 0.10  # Deposit for containers 1 liter or less
DEPOSIT_LARGE = 0.25  # Deposit for containers more than 1 liter

def main():
    try:
        # Prompt user for the number of small and large containers
        small_containers = int(input("Enter the number of containers 1 liter or less: "))
        large_containers = int(input("Enter the number of containers more than 1 liter: "))

        # Ensure the input numbers are non-negative
        if small_containers < 0 or large_containers < 0:
            print("The number of containers cannot be negative.")
            return

        # Calculate the total refund
        total_refund = (small_containers * DEPOSIT_SMALL) + (large_containers * DEPOSIT_LARGE)

        # Display the total refund, formatted to two decimal places
        print(f"Total refund: ${total_refund:.2f}")

    except ValueError:
        print("Invalid input. Please enter whole numbers for the number of containers.")

if __name__ == "__main__":
    main()
