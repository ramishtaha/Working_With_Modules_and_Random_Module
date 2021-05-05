# Importing the Modules
import random

# Importing my own Custom Module
import my_module

# Generating an printing some random numbers
random_int = random.randint(1, 10)
random_float = random.random() * 5
print("Random Integer", random_int)
print("Random Float", random_float)

# Printing out the Variable from My Custom Module
print(my_module.name)

# Generating a Random Love Score
love_score = random.randint(1, 100)

# Printing out the Love Score using F-String.
print(f"Your Love score is {love_score}")