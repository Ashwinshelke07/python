'''Exercise 7: Sum of tIntegershe First n Positive 
(Solved—12 Lines)
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum =
(n)(n + 1)
2'''

n=int(input("Enter THE number of intrger:"))
if n <= 0:
    print("Enter the positive number")
else:
    sum_formula = n * ( n + 1 ) // 2
    #print(f"sum: {sum_formula}")   
    print("The sum of the first 10 positive integers is:", sum_formula)    
    
'''sum = 0
for i in range (1, n + 1):
        sum += i
        print(f"sum :{sum}")


      #print(f"sum: {sum_formula}")

n = int(input("Enter a positive integer: "))

# Ensure the input is positive
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Method 1: Using the formula
    sum_formula = n * (n + 1) // 2

    # Method 2: Using a loop
    sum_loop = 0
    for i in range(1, n + 1):
        sum_loop += i

    # Display the results
    print(f"sum: {sum_formula}")
    print(f"Sum using loop: {sum_loop}")'''


