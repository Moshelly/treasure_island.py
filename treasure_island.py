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

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right".\n')

if choice1 == "right":
   choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across.\n").lower()
   if choice2 == "wait":
    choice3 = input("You've arrived at a tunel with 3 passages. one dark. one lit. one semi-lit. Which passage do you choose?\n").lower()
    if choice3 == "dark":
        print("It's a passage full of blood sucking bats. Game Ove. ")
    elif choice3 == "lit":
        print("CONGRATULATIONS! You've found the treasure! You Win!")
    elif choice3 == "semi-lit": 
        print("Passage blocked with rocks. Game Over!") 
    else:
        print("The passage you chose Does'nt exist. Game over! ")
   else: 
    print("You've been attacked by a hungry crocodile. Game Over!")



