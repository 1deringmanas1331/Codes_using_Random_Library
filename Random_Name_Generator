# Import the Random library
import random
# We enter the names in the list 
# Enter the starting and ending words
syllables = ["ra", "mi", "do", "so", "la", "ti", "di", "ze", "fi", "po", "ni", "ko"]
endings = ["an", "el", "or", "ius", "ious", "ara", "ella", "inda", "oria", "ette"]

# We Generate the Random name in this function
def generate_random_name():
    name_length = random.randint(2, 3)  

    name = ""
    for _ in range(name_length):
        name += random.choice(syllables)
    name += random.choice(endings)

    return name.capitalize()

if __name__ == "__main__":
    # Ask the user how many random names are required
    num_names = int(input("Enter the number of random names to generate: "))
    
    random_names = [generate_random_name() for _ in range(num_names)]

    print("Random Names:")
    for i, name in enumerate(random_names, 1):
        print(f"{i}. {name}")
