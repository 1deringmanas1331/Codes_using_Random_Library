# Import the libraries Random and String
import random
import string 

# Create a function to generate the random password
def generate_password(length=12, use_digits=True, use_special_chars=True):
    
    # Converts the string characters to Lower case and upper case respectively
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if use_digits else ''
    special_chars = '!@#$%^&*()_-+=<>?/[]{}|' if use_special_chars else ''
    
   # Combining all the characters to form a random password
    characters = lowercase_letters + uppercase_letters + digits + special_chars
    
   #Find the length
    length = max(length, 4)
    
   # chooses random letters to be used in the password
    password = random.choices(characters, k=length)
    
   # Chooses random digit for the password
    if use_digits:
        password.extend(random.choice(digits))
    if use_special_chars:
        password.extend(random.choice(special_chars))
    
    # Used for jumbling a password
    random.shuffle(password)
    
   # Used to combine the password
    password = ''.join(password)
    # Finally return the password
    return password
# Finally it will generate the password using the above method
if __name__ == "__main__":
    
  # We assign the attributes of the password according to our requirement
    password = generate_password(length=16, use_digits=True, use_special_chars=True)
    # We print the generated password here
    print("Generated Password:", password)
