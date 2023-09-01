import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scisorrs = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_objectives = [rock,paper,scisorrs]
game_objectives_string = ['rock','paper','scisorrs']

how_many_round = int(input("How many round do you want to play? \n"))

player_win = 0
computer_win = 0

while True:
  select = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))


  if select == 0:
    print("You choose:")
    print('rock')
    print(rock)
  elif select == 1:
    print("You choose:")
    print('paper')
    print(paper)
  elif select == 2:
    print("You choose:")
    print('scisorrs')
    print(scisorrs)
  else:
    print("You can only select 0,1,2")

  computer_choose = random.randint(0, 2)

  print('Computer choose:')
  print(game_objectives_string[computer_choose])
  print(game_objectives[computer_choose])

  if select == 0 and computer_choose == 1:
    print("Computer wins!")
    computer_win += 1
  elif select == 1 and computer_choose == 2:
    print('Computer wins!')
    computer_win += 1
  elif select == 2 and computer_choose == 1:
    print("You win!")
    player_win += 1
  elif select == 0  and computer_choose == 0:
    print("Draw!")
  elif select == 1  and computer_choose == 1:
    print("Draw!")
  elif select == 2  and computer_choose == 2:
    print("Draw!")
  elif select == 2 and computer_choose == 0:
    print("Computer wins!")
    computer_win += 1
  elif select == 1 and computer_choose == 0:
    print("You win!")
    player_win += 1
  elif select == 0 and computer_choose == 2:
    print("You win!")
    player_win += 1


  if player_win == how_many_round:
    print(f'Score: P {player_win} - {computer_win} C')
    print("Player wins the game, congratulations!")
    player_win = 0
    break
  elif computer_win == how_many_round:
    print(f'Score: P {player_win} - {computer_win} C')
    print("Computer wins the game, congratulations!")
    computer_win = 0
    break



