'''Exercise 10: Arithmetic
(Solved—20 Lines)
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b'''

a = int(input("enter first integer:"))
b = int(input("enter the sencond integer:"))
sum_ab= a + b
product_ab = a * b
differance_ab = a - b
print(f" the sum od {a} and {b} is : {product_ab}")
print(f"the difference when {b} is substracted from {a} :{differance_ab}")
print(f" the product of {a} and {b} : {sum_ab}")