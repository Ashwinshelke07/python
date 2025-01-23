
'''Exercise 4: Area of a Field
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre'''

SQ_FEET_PER_ACRE = 43560  # Corrected variable name and value

length = float(input("Enter the length in Feet: "))
width = float(input("Enter the width in Feet: "))

area_sq_feet = length * width
area_acres = area_sq_feet / SQ_FEET_PER_ACRE  # Corrected variable name

print(f"Area of field: {area_acres:.3f} acres")
