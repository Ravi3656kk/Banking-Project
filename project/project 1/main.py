'''
1 for snake 
-1 for water
0 for gun
'''

import random

# Computer's random choice
computer = random.choice([-1, 0, 1])

# User input
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

# Mapping inputs
youDict = {"s": 1, "w": -1, "g": 0}
reversedDict = {1: "snake", -1: "water", 0: "gun"}

# Check for invalid input
if youstr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
    exit()

# Convert user choice to number
you = youDict[youstr]

# Display choices
print(f"You chose {reversedDict[you]}")
print(f"Computer chose {reversedDict[computer]}")

# Game logic
if computer == you:
    print("It's a tie!")

# Snake beats Water
elif you == 1 and computer == -1:
    print("You win!")

# Water beats Gun
elif you == -1 and computer == 0:
    print("You win!")

# Gun beats Snake
elif you == 0 and computer == 1:
    print("You win!")

# Otherwise, you lose
else:
    print("You lose!")
