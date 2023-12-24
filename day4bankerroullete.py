# we gonna give you a list of a name and generate random names from them and that person is going to pay for the bill 
import random

names_input = input("Enter the list of names you want to choose from separated by commas: ")
name_list = names_input.split(", ")
random_names = random.sample(name_list,k=1)  # Adjust the value of k as needed

print(f"{','.join(random_names)} are going to pay the bill.")
