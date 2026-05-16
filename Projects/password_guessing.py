import random

easy_words = ["apple", "tiger", "money", "india", "Bihar"]
medium_words = ["java", "javascripts", "Munger", "Chappra" ]
hard_words = ["Excelent", "fantastic", "avacado","rainbow" ]

print("welcome to the password guessing game")
print("choose a difficult level: easy, medium or hard")

level = input("enter difficulty:").lower()  #user Easy or easy aise hi hard medium kuch bhi likh sakta hai to sab condition ke liye if else nhi lga ke direct lower() function ko use kr lenge isse user kaise bhi likhe sab lower letter mai hi ayega 
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. defaulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
print("Guess the secret password")

while True:
    guess = input("Enter your guess:").lower()
    attempts += 1 #for counting attempts to guess the correct password


    if guess == secret:
        print(f"congratulations! you guessed it in {attempts} attempts.")
        break

    #code for hints.
    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "-"

        print("Hint:", hint)
print("Game over")


