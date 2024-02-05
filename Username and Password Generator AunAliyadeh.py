import random
import pyfiglet as pfg

# Function to generate a random password
def generate_password():
    special_characters = "!@#$%^&*"
    capitalized = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    small="abcdefghijklnmopqrstuvwxyz"
    password = random.choice(capitalized) + random.choice(small)+ random.choice(small) + random.choice(digits) + random.choice(small) + random.choice(small) + random.choice(small) + random.choice(small) + random.choice(small) + random.choice(special_characters) + random.choice(digits) + random.choice(digits) + random.choice(digits) 
    return password

# Function to generate a username
def generate_username(first_name, last_name, city_of_birth,age):
    username = random.choice(first_name) + random.choice(last_name) + random.choice(city_of_birth) + age
    return username

# Main function
def main():
    print(pfg.figlet_format("Welcome to username and password generator", font="digital"))
    first_name = input("State your first name: ")
    last_name = input("State your last name: ")
    city_of_birth = input("State your city of birth: ")
    age=str(input("State your age: "))

    username = generate_username(first_name, last_name, city_of_birth,age)
    password = generate_password()

    # Printing username and password
    print("Your username would be:", username)
    print("Your password is:", password)
main()