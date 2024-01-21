# This program is by Yoyo Liu
# Complete June 2022 
# Uploaded to Github 1/21/2024

from random import randint
import copy 

end_game = False

def print_board(board):
  for row in board:
    print(" ".join(row))#print board function


def get_that_grid(level, size):
  board_orginial = level + 1
  board = []
  list_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']#set the board column header

  while len(list_alpha) > level:
    list_alpha.pop()#delete all unnecessary items
  board.append(list_alpha)#add header to board

  for x in range(level):
    board.append(["-"] * level)#make everything -

  for i in range(board_orginial):
    board[i].append(str(i))#row header

  board [0][level] = ' '#change the top right corner to blank

  print("\nLet's play Battleship!")
  print("-: unknown; \nX: correct ship location; \nO: incorrect location, no ship")
  print_board(board)#print board
  return(board)

def placeship(board, size, num):
  size = int(size)#make the size integar
  nice_ship = False
  num_should = num*size#figure out the blocks should be taken
  loop2 = False
  board_this = copy.deepcopy(board)#make a copy of the original data
  while loop2 == False: 
    while nice_ship == False: 
      list_place = []#make a list of ships
      location_row = randint(1, len(board_this)-1)
      location_column = randint(0, len(board_this)-2)
      #find a place for the head of ths ship ^
      if board_this[location_row][location_column] == 'O':# if the block is not taken
        direction = randint(1, 4)#find a direction to go
        if direction == 1:#if the direction is down, then it goes down
          list_place.append("down")
          for i in range(0,size):
            list_place.append(location_row)#append the location data into the new list
            location_row += 1
        if direction == 2:#similar to the down
          list_place.append("up")
          for i in range(0, size):
            list_place.append(location_row)
            location_row -= 1
        if direction == 3:
          list_place.append("right")
          for i in range(0, size):
            list_place.append(location_column)
            location_column += 1
        if direction == 4:
          list_place.append("left")
          for i in range(0, size):
            list_place.append(location_column)
            location_column -= 1

        if direction == 3 or direction == 4:
          for i in range(1, len(list_place)):
            if int(list_place[i]) >=len(board_this)-1 or int(list_place[i]) < 0:#see if the ship is within board range
              nice_ship = False
              board_this = copy.deepcopy(board)
            else: 
              nice_ship = True
              board_this[location_row][list_place[i]] = 'X'#if yes, place ship
      
        if direction == 1 or direction == 2:#similar to the previous one
          for i in range(1, len(list_place)):
            if int(list_place[i]) >len(board_this)-1 or int(list_place[i]) < 1:
              nice_ship = False
              board_this = copy.deepcopy(board)
            else: 
              nice_ship = True
              board_this[list_place[i]][location_column] = 'X'
    num_real = sum(row.count('X') for row in board_this)#find total # of block with ship
    if num_real == num_should:#if the number is the same, then break the loop
      loop2 = True
      break
    else: 
      nice_ship = False#if there's overlapping, restart
      board_this = copy.deepcopy(board)
  return board_this

def battlefield(level, size, board):

  board2 = copy.deepcopy(board)#make a copy of the board w/out changing original data

  for i in range(1, len(board)):
      for x in range(len(board[i])-1):
        board2 [i][x] = 'O'#make everything into O

  ship1 = placeship(board2, size, 1)
  ship2 = placeship(ship1, size, 2)
  ship3 = placeship(ship2, size, 3)#place the three ships

  print_board(ship3)#print answer board (for easy grading only, NOT included when playing actual game)

  return ship3

def user_try(answer_board, user_board, size):
  game_end = False
  try_num = 20
  while game_end == False: 
    try: 
      try_num = str(try_num)
      print("You have " + try_num + " tries left.")
      row = int(input("Please enter a row(#): "))
      column = ord(input("Please enter a colume(lowercase letter): ")) - 97#tell the user to enter guesses
      if user_board [row][column] == '-': 
        if answer_board [row] [column] == 'X':
          print("HIT")
          user_board [row][column] = 'X'
          print_board(user_board)#detect if hit and place X when hit
        elif answer_board [row] [column] == 'O': 
          print("MISS")
          user_board [row][column] = 'O'
          print_board(user_board)#place O when not hit
        else:
          print(3/0)#create error, re-run
      else:
        print(3/0)#create error, re-run the whole thing
      ship_found = sum(row.count('X') for row in user_board)#find amount of ship block found
      ship_not_found = sum(row.count('O') for row in user_board)#find amount of ship block not found
      try_used = ship_not_found + ship_found#track try number
      if ship_found == int(size)*3:
        game_end = True#end game if all ships are found
        print("Congrats! You beat the computer!")
      try_num = 20 - try_used
      if try_num == 0:#end game if all tries are used
        print("Uh Oh! You used all your try")
        game_end = True
    except: 
      print("Sorry, please enter a valide input.")

again = 'y'

while again == 'y': 
  print("Welcome to the Battleship Game.\n")
  print("I hope you know how to play the game, if you don't... Too bad, you will have to figure it out! \nAnyway, let's get started!\n")
  level = False
  size = False
  while level == False:
    select_level = input("What level are you at? (Enter the grid you want to use!) \n5 - beginner mode - 5x5\n7 - casual mode - 7x7\n10 - advanced mode - 10x10\n")#select level
    if select_level.isnumeric():
      if int(select_level) ==5 or int(select_level) ==7 or int(select_level) == 10:
        select_level = int(select_level)
        level = True
      else:
        print("Sorry, please enter 5, 7 or 10.")
    else:
      print("Sorry, please enter 5, 7 or 10.")

  while size == False:#select size
    select_size = input("There will be 3 ships in the gird. What size do you want the ship to be?\n2 - 2 grid/ship\n3 - 3 grid/ship\n4 - 4 grid/ship\n")
    if select_size.isnumeric():
      if int(select_size) == 2 or int(select_size) ==3 or int(select_size) == 4:
        select_level = int(select_level)
        size = True
      else:
        print("Sorry, please enter 2, 3 or 4.")
    else:
      print("Sorry, please enter 2, 3 or 4.")

  start_game = get_that_grid(select_level, select_size)#get grid
  battle_start = battlefield(select_level, select_size, start_game)#get answer board
  game = user_try(battle_start, start_game, select_size)#ask user to try

  print("Here is the answer board!")#display answer board when game is over
  print_board(battle_start)
  try: 
    again = input("Play again? [y/n]")#ask if the user want to re-play
  except: 
    print("Sorry, please enter 'y' or 'n'. ") 
print("Thank you for playing! Have a nice day!")