import random

print('Welcome to the rock-paper-scissor game!\nYou are going to play against a minion!')

# ascii art from https://www.asciiart.eu/people/body-parts/hand-gestures
print("Please input your choice")
print("""
1.                 2.                           3.
    _______                 _______                      _______
---'   ____)            ---'   ____)____             ---'   ____)____
      (_____)                     ______)                      ______) 
      (_____)                     _______)                  __________)
      (____)                     _______)                  (____)
---.__(___)             ---.__________)              ---.__(___)
""") # 1 for rock; 2 for paper; 3 for scissor

# step1: get player's choice, save it in variable p_choice
p_choice = input("Press 1 to choose rock. \nPress 2 to choose paper. \nPress 3 to choose scissors. \n")
if (p_choice == 1):
    print("Player chooses rock!")
elif (p_choice == 2):
    print("Player chooses paper!")
elif (p_choice == 3):
    print("Player chooses scissors!")

# step2: generate a random choice for minion, save it in variable m_choice
m_choice = random.randint(1,3)

# status is used for the win/lose/draw of the game
# status = 1 means player wins; status = 2 means minion wins; status = 3 means draw;
# status = 4 means user gives invalid input, e.g. player inputs -1 or 4
status = 0 # initialized as 0
# step 3: given choices from player and minion, decide the game status


# step4: display the minion's choice
if (m_choice == 1):
    print("Minion chooses rock!")
elif (m_choice == 2):
    print("Minion chooses paper!")
elif (m_choice == 3):
    print("Minion chooses scissor!")

status = 0
if (p_choice == 1 and m_choice == 3):
    status = 1
elif (p_choice == 2 and m_choice == 1):
    status = 1
elif (p_choice == 3 and m_choice == 2):
    status = 1
elif (p_choice == 1 and m_choice == 1):
    status = 3
elif (p_choice == 2 and m_choice == 2):
    status = 3
elif (p_choice == 3 and m_choice == 3):
    status = 3
elif (p_choice == 1 and m_choice == 2):
    status = 2
elif (p_choice == 2 and m_choice == 3):
    status = 2
elif (p_choice == 3 and m_choice == 1):
    status = 2
    
if status == 1:
    print("You Win! Minion Loses!")
elif status == 2:
    print("You Lose! Minion Wins!")
elif status == 3:
    print('Draw!')
