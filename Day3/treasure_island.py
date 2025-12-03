'''
if-else statement=>
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller beore you can ride")

comparison operator=> >,,, >=, <=, ==(check equality),!=
# = => assigning th value
modulo operator % => return remainder
nested if else=> if, elif, else
multiple if=> every condition is checked. 3 in if-e;se only one condition is  checked and returned
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
        elif age >= 45 and age <= 55:
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want to have a photo take ? type y for Yes and n for No")
    if wants_photo == "y":
        bill = bill + 3 #bill += 3
    print(f"Your final bill is $ {bill}")
else:
    print("Sorry you have to grow taller beore you can ride")


******Python Pizza******
print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid pizza size!")
    exit()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1
print(f"Your total bill is: ${bill}")

logical operator=> and, or, not


coding exercise 5=>
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")
'''

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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("YOur mission is to find the treasure.")
choice1= input('YOu\'re at a crossroad, where do you want to go? Type "left" or "right" ').lower()

if choice1=="left":
    choice2 = input('You \'ve come to a lake, there is an island in the middle of the lake.Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is house with 3 doors. One red, one yellow and one blue. Which colour do you choose? Choose wisely !!\n').lower()
        if choice3 == "red":
            print("It is a room full of fire. Game Over")
        elif choice3== "blue":
                print("You enter a room of beasts. Game Over.")
        elif choice3 == "yellow":
                    print("You found the treasure. You Win!")
        else:
                        print("YOU choose a door that doesn't exist. Game Over.")
        
    else:
            print("YOu got attacked by an angry trout. Game Over")
else:
 print("You fell in to a hole. Game Over.")
