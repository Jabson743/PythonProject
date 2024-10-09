#name = "John smith"
#age = 20
#is_member = True

#print("His name is ", name, ". He's ", age, "years old", "and he his a", is_member)

#name = input("What is your name: ")
#color = input("What is your favorite color? ")

#print(name + " likes " + color)

#Type Conversion
#birth_year = int(input("What is your birth year? "))
#age = 2021 - birth_year

#print(age)

#weight_lbs = int(input("What is your weight? "))
#weight_kg = weight_lbs * 0.45

#print(weight_kg)

#Strings

#Multilines string
messages = """
Hi Ola, How're you doing?
Nice to meet you!
Thanks for the assitance you rendered
"""
#print(messages)

course = "Python for Beginners"
#print(course[5:-3])
print(course.find("Python"))

#Formatted Strings

first_name = "Olakunle"
last_name = "Iyanda"

#print(f'{last_name} [{first_name}] is currently learning software engineering')

university = 'University of Ilorin'
#print(university.find('Ilorin'))

course = "Python for Beginners"
#print(course.find('Beginners'))
#print(course.replace("Beginners", "Master"))

full_name = "Iyanda Olakunle"
#print("Zee" in full_name)

z = -12.9
#print(abs(z))

import math

#print(math.ceil(3.14))
#print(math.floor(3.14))

#price = 1000000
#has_good_credit_score = False
#if has_good_credit_score:
 #   down_payment = price * 10 / 100
#else:
 #   down_payment = price * 20 / 100
#print(f"down_payment: ${down_payment}")

has_high_income = False
has_good_credit = True
#if has_good_credit or has_high_income:
 #   print("You are eligible for this loan")

name = "Yum"
#if (len(name) < 3):
  #  print("Name is too short")
#elif (len(name) > 3):
   # print("Name is too long")
#else:
  # print("Name is good")

#Guess Game
secret_number = 8
guess_count = 0
guess_limit = 3

#name = input("What is your name: ")
#print(f"Hi {name}, Welcome to My Guess Game")

#print("You can only guess the secret number three times. Goodluck!!!")

#while guess_count < guess_limit:
#    guess = int(input(f"Guess the secret number between 1 and 9: "))
#   guess_count += 1
#    if guess == secret_number:
#        print(f"Congrats {name}! You guessed the secret number!")
#        break
#    elif guess_count == guess_limit:
#        print(f"You have come to the end of your guess game {name}. Goodluck to you some other time!")
#        print("Thank you for playing!")
#    else:
#        print(f"Sorry {name}, you guessed the wrong number!")

#Car Game
#command = ""
#started = False
#rint("Kindly enter [help] to get started or [quit] to exit the program")
#while command != "quit":
    #command = input("> ").lower()
   # if command == "help":
  #      print("""
# start -> to start the car
# stop -> to stop the car
# quit -> to quit the car
#        """)
#    elif command == "start":
#        if started:
#            print("You have already started the car")
#        else:
#            started = True
#            print("The car is starting")
#    elif command == "stop":
#        if not started:
#            print("You car is already stopped")
#        else:
#            started = False
#            print("The car is stopping")
#    elif command == "quit":
#        print(f"Bye {tell_name} you exit the program!!!")
#        break
#    else:
#        print("Invalid command! kindly enter a valid command")


prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(total)

for i in range(1, 11, 3):
    print(i)

his_names = ["Ola", "Ayo", "Sam", "Tom"]
for name in his_names:
    print(name)

for x in range(4):
    for y in range(3):
        print(f"{x}, {y}")

numeric_number = [5, 2, 4, 5, 2, 3]

for num in numeric_number:
    print("X" * num)

largest_num = [12, 56, 32, 78, 107, 45]
largest_num = sorted(largest_num)
print(largest_num)
max = 0
for num in largest_num:
    if num > max:
        max = num
        print(max)

maxtrix = [
    ["Tola", "Tolu", "Titi", "Tayo"],
    ["Shayo", "Shade", "Sheyi", "Shanu"],
    ["Ayo", "Anu", "Joy", "Ola"]
]

maxtrix[2][2] = "Tom"
print(maxtrix)

subjects = ["Math", "English", "Science"]
subjects[1] = "Physics"
print(subjects)



#Dictionaries
customers = {
    "name": "Olakunle Iyanda",
    "age": 23,
    "email": "Iyanda743@gmail.com",
    "is_verified": True,
    "hobbies": {
                "singing", "dancing", "reading",
    }
}

print(customers.get("age"))

phone_number = input("Enter your phone number: ")

digit_number = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
}

output = ""
for char in phone_number:
    output += digit_number.get(char, "!") + ""
    print(output)

def greet_user():
    print("Hello everyone")

greet_user()