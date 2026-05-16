# #FAKE NEW HEADLINE GENERATOR PROJECT
# #FAKE AND FUNNY NEWS HEADLINE USING LIST OF WORDS 

# CONECPT USING:- LISTS, PRINT(), WHILE LOOP, STRING CONCATINATION AND FORwarder STRING.
# ALSO IMPORT RANDOM.CHOICE() LIBRARY

# HOW OUR PROGRAM WOKS 
# STEP1 IMPORT RANDOM Module
# STEP2 CREATE A list
# STEP3 USE RANDOM.CHOICE()
# STEP4 COMBINE WORDS
# STEP5 PRINT HEADLINE
# STEP6 ASK THE USER IF THEY WANT ANOTHER HEADLINE
# STEP7 IF YES, REPEAT: IF NO STOP THE PROGRAM


#steps 1 import random library
import random

#2- create subjects action & places
subjects = [
    "Sharukh khan",
    "Virat kohli",
    "Niramala sitaraman",
    "a group of monkey",
    "prime minister Modi",
    "Auto rickshae driver from delhi",
    "muskan",
    "chandani"
]



actions = [
    "launches",
    "cancels",
    "dance with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
    "fly",
    "reverse"
]

place_or_things = [
    "red fort",
    "in mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ghat",
    "during ipl match",
    "at india gate",
    "language lab",
    "Vaishali bhawan"
]


#step 3 starts the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print(headline)

    user_input = input("/n Do You want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

#print goodbye message
print("/nThanks for using ")



