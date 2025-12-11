'''
Randomness=> Mersenne Twister
integer=>
import random
random_integer = random.randint(1, 10)
print(random_integer)

floating numbers=>
import random
random_number_0_to_1 = random.random()
print(random_number_0_to_1)
OR
random_float = random.uniform(1,10)
print(random_float)

#head tail using random
import random
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

list[]=>
states_of_India = ["Goa"," Uttarakhand", "Maharashtra","Odisha"]
print(states_of_India[1])
states_of_India.append("Tamil Nadu")
print(states_of_India)
num_of_states = len(states_of_India)
print(num_of_states)

https://docs.python.org/3/library/random.html
https://docs.python.org/3/tutorial/datastructures.html
https://www.delish.com/food-news/a26872638/dirty-dozen-foods-list-2019/

who will pay the bill?=>
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

dirty dozens=>
fruits = ["apple", "chikoo", "guava", "mango"]
vegetables= ["potato", "tomato", "cucumber", "spinach", "beans", "carrot"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)


'''
print("Click Run to run the final project you will build")

# ASCII art
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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissor]

# User input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lose!")
else:
    print(game_images[user_choice])

    # Computer choice
    import random
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_images[computer_choice])

    # Game logic
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("You lose!")


