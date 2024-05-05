# Generates a brand name from a list of questions inputted by the user.

print("Hi there! Welcome to the Brand Name Generator. Kindly follow all the prompts to get your cool Band name.")
user_city = input("Enter the name of city you grew up in:\n")
user_pet = input("Enter your pet name:\n")
brand_name = user_city + " " + user_pet
print("Well, " + brand_name + " could be a good brand name.")





# 💸 Bill Splitter with Tip Calculator

print("Welcome to the tip calculator")
bill = float(input("What is the total bill? "))
percent = float(input("What percentage would you like to split with? 10, 12, or 15? "))
people = int(input("How many people will split the bill? "))
split_bill = (bill/people) + ((bill/people) * (percent/100))
split_bill_round = "{:.2f}".format(split_bill, 2)
#this line fixes the formatting error of Python when it doesn't include double decimal points for zeroes. The .format(split_bill) can also be used since 2decimal point has been indicated with the :.2f.
message = f"Each person should pay: {split_bill_round}"
print(message)





# 🚨 Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
combine = name1 + name2
lower_case = combine.lower()
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
true = t + r + u + e
love = l + o + v + e
true_love = str(true) + str(love)
love_score = int(true_love)
if love_score < 10 or love_score > 90:
    message = f"Your score is {love_score}, you go together like coke and mentos."
elif love_score >= 40 and love_score <= 50:
    message = f"Your score is {love_score}, you are alright together."
else:
    message = f"Your score is {love_score}."

print(message)





# 🎲 Interactive Text-based Game - Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure. Please choose your answers wisely.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
#AFTER USING FLOWCHART TO CORDINATE THE JOURNEY BEFORE CODING.
question1 = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower()
print(question1)

if  question1 == "left":
  question2 = input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
  print(question2)
  if question2 == "wait":
    question3 = input("You got a boat and arrived at the island unharmed. But then you see a house with 3 doors: One red, one yellow, and one blue. Which color do you choose? \n").lower()
    print(question3)
    if question3 == "red":
      print("You have entered a room full of hungry beasts. Game over.")
    elif question3 == "yellow":
      question4 = input("You have entered a room full of treasures. Would you like to pack all treasures? Y or N \n").lower()
      print(question4)
      if question4 == "y":
        print("You have been killed by booby traps and landmines. Game over.")
      else:
        print("You have successfully passed the test of greed. You proceed to the next room.")
        question5 = input("You reach a big golden door that is locked, and there is a big iron hammer beside you. Two angry beasts have sighted you and are charging at you. What do you do? Type 'run' to run from the wild beasts, 'hammer' to pick the big hammer. \n").lower()
        print(question5)
        if question5 == "hammer":
          question6 = input("You picked up the hammer, what would you like to do? Type 'break' to break the door and run inside. Type 'attack' to attack the wild beasts.\n").lower()
          print(question6)
          if question6 == "break":
            print("You broke into the building but the wild beasts charged into it and tore you apart.")
          else:
            print("You attacked the wild beasts and killed them both. You win!")
        else:
          print("The beasts are too fast. They tore you apart. Game over.")
    else:
      question7 = input("You have entered another dimension world through the blue door and can't go back. You have three strange alien beings right in front of you staring at you. Type 'T' to try and talk to them. 'R' to run from them. 'F' to fight them. \n").lower()
      print(question7)
  else:
    print("Oh! The sea beasts are not merciful in feasting on flesh and blood. Game over.")
else:
  print("Bounty hunters are now everywhere. They have caught you. Game over.")





# ✂ Game: Rock-Paper-Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# code
import random
choice_image = [rock, paper, scissors]
user_choice = int(input("Welcome, kindly pick 0 for Rock, 1 for Paper, 2 for Scissors \n"))
computer_choice = random.randint(0, 2)
print(f"Computer chose {choice_image[computer_choice]}")
if user_choice < 0 or user_choice > 2 :
  print("You have entered an invalid number, please try again.")
elif computer_choice == user_choice:
  print(f"This is a tie. Why not try again. \n {choice_image[user_choice]} {choice_image[computer_choice]}")
elif user_choice == 0 and computer_choice == 2:
  print(f"You win this round. \n {choice_image[computer_choice]} {choice_image[computer_choice]}")
elif computer_choice == 0 and user_choice == 2:
  print(f"You lose this round. \n {choice_image[user_choice]} {choice_image[computer_choice]}")
elif user_choice > computer_choice:
  print(f"You win this round. {choice_image[user_choice]} {choice_image[computer_choice]}")
elif computer_choice > user_choice:
  print(f"You lose this round. {choice_image[user_choice]} {choice_image[computer_choice]}")
else:
  print(f"You lose this round. Try your luck again. {choice_image[user_choice]} {choice_image[computer_choice]}")
