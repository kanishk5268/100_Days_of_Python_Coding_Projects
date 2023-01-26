import random

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


game_images= [rock, paper, scissors]

player = int(input("Enter 0 for rock, 1 for paper and 2 for scissors\n"))
print("Player chose:")
print(game_images[player])

computer = random.randint(0,2)

print(f"Computer chose:")
print(game_images[computer])

if (player == 0 and computer == 0):
  print("it is a draw")

elif(player == 1 and computer == 1):
    print("it is a draw")

elif (player == 2 and computer == 2):
    print("it is a draw")

elif (player == 0 and computer == 1):
  print("CPU wins")

elif(player == 0 and computer == 2):
  print("Player wins")

elif (player == 1 and computer == 2):
  print("CPU wins")
elif(player == 1 and computer == 0):
  print("Player wins")

elif (player == 2 and computer == 0):
  print("CPU wins")

elif(player == 2 and computer == 1):
  print("Player wins")

else:
    print("There might be an invalid input")



