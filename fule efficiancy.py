''''Exercise 11: Fuel Efficiency
In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.'''


# Function to convert MPG to L/100 km
def mpg_to_l_per_100km(mpg):
    # Conversion factors
    miles_to_km = 1.60934
    gallon_to_liters = 3.78541
    
    # Apply the conversion formula
    l_per_100km = (100 * gallon_to_liters) / (miles_to_km * mpg)
    return l_per_100km

# Read MPG value from the user
mpg = float(input("Enter fuel efficiency in miles per gallon (MPG): "))

# Convert MPG to L/100 km
l_per_100km = mpg_to_l_per_100km(mpg)

# Display the result
print(f"The equivalent fuel efficiency in liters per 100 kilometers (L/100 km) is: {l_per_100km:.2f}")
