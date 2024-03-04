# Import random Library Packages
import random

# Enter sample First and last names of cricketers
first_names = ["Virat", "Sachin", "Rohit", "MS", "Kane", "Joe", "Steve", "AB", "David", "Chris"]
last_names = ["Kohli", "Tendulkar", "Sharma", "Dhoni", "Williamson", "Root", "Smith", "de Villiers", "Warner", "Gayle"]

# Generates a random cricketer name
random_first_name = random.choice(first_names)
random_last_name = random.choice(last_names)

# Combines the first name and last name to generate the cricketer's name
random_cricketer_name = f"{random_first_name} {random_last_name}"

# Prints the random cricketer's name 
print(random_cricketer_name)
