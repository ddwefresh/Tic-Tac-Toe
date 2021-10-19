# Assignment 16 - Tic tac toe AI
# Assignment 17 - Tic tac toe full game
# Matthew Quock
# June 14, 2021

import random
import turtle
t = turtle.Turtle()
screen = turtle.Screen()
t.penup()
#t.hideturtle()
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # acceptable number choices
while True:
  t.clear() 
  def grid():
    t.goto(-50,150)
    t.pendown()
    t.goto(-50,-150)
    t.penup()
    t.goto(50,150)
    t.pendown()
    t.goto(50,-150)
    t.penup()
    t.goto(-150,50)
    t.pendown()
    t.goto(150,50)
    t.penup()
    t.goto(-150,-50)
    t.pendown()
    t.goto(150,-50)
    t.penup()
    t.goto(0,0)

  def user_x():
    for i in range(len(spots)): # counts how many taken spots currently
      i = i
    if i != 9: # if there are still spots, the game continues
      user = input("X's turn: ")
      while True: # will keep asking you to choose an appropriate number
        if user not in number:
          user = input("Please pick from 1 to 9: ")
        elif user in spots:
          user = input("Pick a diffrent number: ")
        elif user not in spots and user in number:
          break
    elif i == 9: # if there are no spots left and there isnt a win, it draws
      user = "draw"
    return user

  def user_o():
    for i in range(len(spots)):
      i = i
    if i != 9:
      user = input("O's turn: ")
      while True:
        if user not in number:
          user = input("Please pick from 1 to 9: ")
        elif user in spots:
          user = input("Pick a diffrent number: ")
        elif user not in spots and user in number:
          break
    elif i == 9:
      user = "draw"
    return user

  def ai_x():
    for i in range(len(spots)):
      i = i
    if i != 9:
      while True:
        ai = random.choice(number)
        if ai not in spots:
          print("X's turn")
          break
    elif i == 9:
      ai = "draw"

    # specific moves
    #if corners are free take it
    if gamestate[0] == '':
      ai = "1"
    if gamestate[2] == '':
      ai = "3"
    if gamestate[6] == '':
      ai = "7"
    if gamestate[8] == '':
      ai = "9"

    # if corners across from each other are taken, block
    if gamestate[0] == 'o' and gamestate[8] == 'o' and gamestate[7] == '':
      ai = "8"
    if gamestate[0] == 'o' and gamestate[8] == 'o' and gamestate[1] == '':
      ai = "2"
    if gamestate[2] == 'o' and gamestate[6] == 'o' and gamestate[1] == '':
      ai = "2"
    if gamestate[2] == 'o' and gamestate[6] == 'o' and gamestate[7] == '':
      ai = "8"

    # if opponent is in a corner across from a side, block
    if gamestate[0] == 'o' and gamestate[7] == 'o' and gamestate[8] == '':
      ai = "9"
    if gamestate[2] == 'o' and gamestate[7] == 'o' and gamestate[6] == '':
      ai = "7"
    if gamestate[2] == 'o' and gamestate[3] == 'o' and gamestate[6] == '':
      ai = "7"
    if gamestate[8] == 'o' and gamestate[3] == 'o' and gamestate[0] == '':
      ai = "1"
    if gamestate[8] == 'o' and gamestate[1] == 'o' and gamestate[0] == '':
      ai = "1"
    if gamestate[6] == 'o' and gamestate[1] == 'o' and gamestate[2] == '':
      ai = "3"
    if gamestate[6] == 'o' and gamestate[5] == 'o' and gamestate[2] == '':
      ai = "3"
    if gamestate[0] == 'o' and gamestate[5] == 'o' and gamestate[8] == '':
      ai = "9"

    # if 2 are on the same sides of a corner, block the corner
    if gamestate[1] == 'o' and gamestate[3] == 'o' and gamestate[0] == '':
      ai = "1"
    if gamestate[1] == 'o' and gamestate[5] == 'o' and gamestate[2] == '':
      ai = "3"
    if gamestate[7] == 'o' and gamestate[3] == 'o' and gamestate[6] == '':
      ai = "7"
    if gamestate[7] == 'o' and gamestate[5] == 'o' and gamestate[8] == '':
      ai = "9"

    # if there is nothing in the middle it will go first
    if gamestate[4] == '':
      ai = "5"

    # down below is for blocking the opponent
    # -
    if gamestate[0] == 'o' and gamestate[1] == 'o' and gamestate[2] == '':
      ai = "3"
    elif gamestate[0] == 'o' and gamestate[2] == 'o' and gamestate[1] == '':
      ai = "2"
    elif gamestate[1] == 'o' and gamestate[2] == 'o' and gamestate[0] == '':
      ai = "1"
    elif gamestate[3] == 'o' and gamestate[4] == 'o' and gamestate[5] == '':
      ai = "6"
    elif gamestate[3] == 'o' and gamestate[5] == 'o' and gamestate[4] == '':
      ai = "5"
    elif gamestate[4] == 'o' and gamestate[5] == 'o' and gamestate[3] == '':
      ai = "4"
    elif gamestate[6] == 'o' and gamestate[7] == 'o' and gamestate[8] == '':
      ai = "9"
    elif gamestate[6] == 'o' and gamestate[8] == 'o' and gamestate[7] == '':
      ai = "8"
    elif gamestate[7] == 'o' and gamestate[8] == 'o' and gamestate[6] == '':
      ai = "7"
    # |
    elif gamestate[0] == 'o' and gamestate[3] == 'o' and gamestate[6] == '':
      ai = "7"
    elif gamestate[0] == 'o' and gamestate[6] == 'o' and gamestate[3] == '':
      ai = "4"
    elif gamestate[3] == 'o' and gamestate[6] == 'o' and gamestate[0] == '':
      ai = "1"
    elif gamestate[1] == 'o' and gamestate[4] == 'o' and gamestate[7] == '':
      ai = "8"
    elif gamestate[1] == 'o' and gamestate[7] == 'o' and gamestate[4] == '':
      ai = "5"
    elif gamestate[4] == 'o' and gamestate[7] == 'o' and gamestate[1] == '':
      ai = "2"
    elif gamestate[2] == 'o' and gamestate[5] == 'o' and gamestate[8] == '':
      ai = "9"
    elif gamestate[2] == 'o' and gamestate[8] == 'o' and gamestate[5] == '':
      ai = "6"
    elif gamestate[5] == 'o' and gamestate[8] == 'o' and gamestate[2] == '':
      ai = "3"
    # \
    elif gamestate[0] == 'o' and gamestate[4] == 'o' and gamestate[8] == '':
      ai = "9"
    elif gamestate[0] == 'o' and gamestate[8] == 'o' and gamestate[4] == '':
      ai = "5"
    elif gamestate[4] == 'o' and gamestate[8] == 'o' and gamestate[0] == '':
      ai = "1"
    # /
    elif gamestate[2] == 'o' and gamestate[4] == 'o' and gamestate[6] == '':
      ai = "7"
    elif gamestate[2] == 'o' and gamestate[6] == 'o' and gamestate[4] == '':
      ai = "5"
    elif gamestate[4] == 'o' and gamestate[6] == 'o' and gamestate[2] == '':
      ai = "3"

    # down below is if there is a winning spot
    # - win
    if gamestate[0] == 'x' and gamestate[1] == 'x' and gamestate[2] == '':
      ai = "3"
    if gamestate[0] == 'x' and gamestate[2] == 'x' and gamestate[1] == '':
      ai = "2"
    if gamestate[1] == 'x' and gamestate[2] == 'x' and gamestate[0] == '':
      ai = "1"
    if gamestate[3] == 'x' and gamestate[4] == 'x' and gamestate[5] == '':
      ai = "6"
    if gamestate[3] == 'x' and gamestate[5] == 'x' and gamestate[4] == '':
      ai = "5"
    if gamestate[4] == 'x' and gamestate[5] == 'x' and gamestate[3] == '':
      ai = "4"
    if gamestate[6] == 'x' and gamestate[7] == 'x' and gamestate[8] == '':
      ai = "9"
    if gamestate[6] == 'x' and gamestate[8] == 'x' and gamestate[7] == '':
      ai = "8"
    if gamestate[7] == 'x' and gamestate[8] == 'x' and gamestate[6] == '':
      ai = "7"
    # |
    if gamestate[0] == 'x' and gamestate[3] == 'x' and gamestate[6] == '':
      ai = "7"
    if gamestate[0] == 'x' and gamestate[6] == 'x' and gamestate[3] == '':
      ai = "4"
    if gamestate[3] == 'x' and gamestate[6] == 'x' and gamestate[0] == '':
      ai = "1"
    if gamestate[1] == 'x' and gamestate[4] == 'x' and gamestate[7] == '':
      ai = "8"
    if gamestate[1] == 'x' and gamestate[7] == 'x' and gamestate[4] == '':
      ai = "5"
    if gamestate[4] == 'x' and gamestate[7] == 'x' and gamestate[1] == '':
      ai = "2"
    if gamestate[2] == 'x' and gamestate[5] == 'x' and gamestate[8] == '':
      ai = "9"
    if gamestate[2] == 'x' and gamestate[8] == 'x' and gamestate[5] == '':
      ai = "6"
    if gamestate[5] == 'x' and gamestate[8] == 'x' and gamestate[2] == '':
      ai = "3"
    # \
    if gamestate[0] == 'x' and gamestate[4] == 'x' and gamestate[8] == '':
      ai = "9"
    if gamestate[0] == 'x' and gamestate[8] == 'x' and gamestate[4] == '':
      ai = "5"
    if gamestate[4] == 'x' and gamestate[8] == 'x' and gamestate[0] == '':
      ai = "1"
    # /
    if gamestate[2] == 'x' and gamestate[4] == 'x' and gamestate[6] == '':
      ai = "7"
    if gamestate[2] == 'x' and gamestate[6] == 'x' and gamestate[4] == '':
      ai = "5"
    if gamestate[4] == 'x' and gamestate[6] == 'x' and gamestate[2] == '':
      ai = "3"
    return ai

  def ai_o():
    for i in range(len(spots)):
      i = i
    if i != 9:
      while True:
        ai = random.choice(number)
        if ai not in spots:
          print("O's turn")
          break
    elif i == 9:
      ai = "draw"

    # specific moves
    #if corners are free take it
    if gamestate[0] == '':
      ai = "1"
    if gamestate[2] == '':
      ai = "3"
    if gamestate[6] == '':
      ai = "7"
    if gamestate[8] == '':
      ai = "9"

    # if corners across from each other are taken, block
    if gamestate[0] == 'x' and gamestate[8] == 'x' and gamestate[7] == '':
      ai = "8"
    if gamestate[0] == 'x' and gamestate[8] == 'x' and gamestate[1] == '':
      ai = "2"
    if gamestate[2] == 'x' and gamestate[6] == 'x' and gamestate[1] == '':
      ai = "2"
    if gamestate[2] == 'x' and gamestate[6] == 'x' and gamestate[7] == '':
      ai = "8"

    # if opponent is in a corner across from a side, block
    if gamestate[0] == 'x' and gamestate[7] == 'x' and gamestate[8] == '':
      ai = "9"
    if gamestate[2] == 'x' and gamestate[7] == 'x' and gamestate[6] == '':
      ai = "7"
    if gamestate[2] == 'x' and gamestate[3] == 'x' and gamestate[6] == '':
      ai = "7"
    if gamestate[8] == 'x' and gamestate[3] == 'x' and gamestate[0] == '':
      ai = "1"
    if gamestate[8] == 'x' and gamestate[1] == 'x' and gamestate[0] == '':
      ai = "1"
    if gamestate[6] == 'x' and gamestate[1] == 'x' and gamestate[2] == '':
      ai = "3"
    if gamestate[6] == 'x' and gamestate[5] == 'x' and gamestate[2] == '':
      ai = "3"
    if gamestate[0] == 'x' and gamestate[5] == 'x' and gamestate[8] == '':
      ai = "9"

    # if 2 are on the same sides of a corner, block the corner
    if gamestate[1] == 'x' and gamestate[3] == 'x' and gamestate[0] == '':
      ai = "1"
    if gamestate[1] == 'x' and gamestate[5] == 'x' and gamestate[2] == '':
      ai = "3"
    if gamestate[7] == 'x' and gamestate[3] == 'x' and gamestate[6] == '':
      ai = "7"
    if gamestate[7] == 'x' and gamestate[5] == 'x' and gamestate[8] == '':
      ai = "9"

    # if there is nothing in the middle it will go first
    if gamestate[4] == '':
      ai = "5"
  
    # down below is for blocking the opponent
    # -
    if gamestate[0] == 'x' and gamestate[1] == 'x' and gamestate[2] == '':
      ai = "3"
    elif gamestate[0] == 'x' and gamestate[2] == 'x' and gamestate[1] == '':
      ai = "2"
    elif gamestate[1] == 'x' and gamestate[2] == 'x' and gamestate[0] == '':
      ai = "1"
    elif gamestate[3] == 'x' and gamestate[4] == 'x' and gamestate[5] == '':
      ai = "6"
    elif gamestate[3] == 'x' and gamestate[5] == 'x' and gamestate[4] == '':
      ai = "5"
    elif gamestate[4] == 'x' and gamestate[5] == 'x' and gamestate[3] == '':
      ai = "4"
    elif gamestate[6] == 'x' and gamestate[7] == 'x' and gamestate[8] == '':
      ai = "9"
    elif gamestate[6] == 'x' and gamestate[8] == 'x' and gamestate[7] == '':
      ai = "8"
    elif gamestate[7] == 'x' and gamestate[8] == 'x' and gamestate[6] == '':
      ai = "7"
    # |
    elif gamestate[0] == 'x' and gamestate[3] == 'x' and gamestate[6] == '':
      ai = "7"
    elif gamestate[0] == 'x' and gamestate[6] == 'x' and gamestate[3] == '':
      ai = "4"
    elif gamestate[3] == 'x' and gamestate[6] == 'x' and gamestate[0] == '':
      ai = "1"
    elif gamestate[1] == 'x' and gamestate[4] == 'x' and gamestate[7] == '':
      ai = "8"
    elif gamestate[1] == 'x' and gamestate[7] == 'x' and gamestate[4] == '':
      ai = "5"
    elif gamestate[4] == 'x' and gamestate[7] == 'x' and gamestate[1] == '':
      ai = "2"
    elif gamestate[2] == 'x' and gamestate[5] == 'x' and gamestate[8] == '':
      ai = "9"
    elif gamestate[2] == 'x' and gamestate[8] == 'x' and gamestate[5] == '':
      ai = "6"
    elif gamestate[5] == 'x' and gamestate[8] == 'x' and gamestate[2] == '':
      ai = "3"
    # \
    elif gamestate[0] == 'x' and gamestate[4] == 'x' and gamestate[8] == '':
      ai = "9"
    elif gamestate[0] == 'x' and gamestate[8] == 'x' and gamestate[4] == '':
      ai = "5"
    elif gamestate[4] == 'x' and gamestate[8] == 'x' and gamestate[0] == '':
      ai = "1"
    # /
    elif gamestate[2] == 'x' and gamestate[4] == 'x' and gamestate[6] == '':
      ai = "7"
    elif gamestate[2] == 'x' and gamestate[6] == 'x' and gamestate[4] == '':
      ai = "5"
    elif gamestate[4] == 'x' and gamestate[6] == 'x' and gamestate[2] == '':
      ai = "3"

    # down below is if there is a winning spot
    # - win
    if gamestate[0] == 'o' and gamestate[1] == 'o' and gamestate[2] == '':
      ai = "3"
    if gamestate[0] == 'o' and gamestate[2] == 'o' and gamestate[1] == '':
      ai = "2"
    if gamestate[1] == 'o' and gamestate[2] == 'o' and gamestate[0] == '':
      ai = "1"
    if gamestate[3] == 'o' and gamestate[4] == 'o' and gamestate[5] == '':
      ai = "6"
    if gamestate[3] == 'o' and gamestate[5] == 'o' and gamestate[4] == '':
      ai = "5"
    if gamestate[4] == 'o' and gamestate[5] == 'o' and gamestate[3] == '':
      ai = "4"
    if gamestate[6] == 'o' and gamestate[7] == 'o' and gamestate[8] == '':
      ai = "9"
    if gamestate[6] == 'o' and gamestate[8] == 'o' and gamestate[7] == '':
      ai = "8"
    if gamestate[7] == 'o' and gamestate[8] == 'o' and gamestate[6] == '':
      ai = "7"
    # |
    if gamestate[0] == 'o' and gamestate[3] == 'o' and gamestate[6] == '':
      ai = "7"
    if gamestate[0] == 'o' and gamestate[6] == 'o' and gamestate[3] == '':
      ai = "4"
    if gamestate[3] == 'o' and gamestate[6] == 'o' and gamestate[0] == '':
      ai = "1"
    if gamestate[1] == 'o' and gamestate[4] == 'o' and gamestate[7] == '':
      ai = "8"
    if gamestate[1] == 'o' and gamestate[7] == 'o' and gamestate[4] == '':
      ai = "5"
    if gamestate[4] == 'o' and gamestate[7] == 'o' and gamestate[1] == '':
      ai = "2"
    if gamestate[2] == 'o' and gamestate[5] == 'o' and gamestate[8] == '':
      ai = "9"
    if gamestate[2] == 'o' and gamestate[8] == 'o' and gamestate[5] == '':
      ai = "6"
    if gamestate[5] == 'o' and gamestate[8] == 'o' and gamestate[2] == '':
      ai = "3"
    # \
    if gamestate[0] == 'o' and gamestate[4] == 'o' and gamestate[8] == '':
      ai = "9"
    if gamestate[0] == 'o' and gamestate[8] == 'o' and gamestate[4] == '':
      ai = "5"
    if gamestate[4] == 'o' and gamestate[8] == 'o' and gamestate[0] == '':
      ai = "1"
    #/
    if gamestate[2] == 'o' and gamestate[4] == 'o' and gamestate[6] == '':
      ai = "7"
    if gamestate[2] == 'o' and gamestate[6] == 'o' and gamestate[4] == '':
      ai = "5"
    if gamestate[4] == 'o' and gamestate[6] == 'o' and gamestate[2] == '':
      ai = "3"
    return ai

  def draw_x(m):
    # draws the X
    x = 0
    y = 0
    if m == "1":
      x = -100
      y = 100
    if m == "2":
      x = 0
      y = 100
    if m == "3":
      x = 100
      y = 100
    if m == "4":
      x = -100
      y = 0
    if m == "5":
      x = 0
      y = 0
    if m == "6":
      x = 100
      y = 0
    if m == "7":
      x = -100
      y = -100
    if m == "8":
      x = 0
      y = -100
    if m == "9":
      x = 100
      y = -100
    t.goto(x,y)
    t.goto(x-25,y+25)
    t.pendown()
    t.goto(x+25,y-25)
    t.penup()
    t.goto(x+25,y+25)
    t.pendown()
    t.goto(x-25,y-25)
    t.penup()

  def draw_o(m):
    # draws the O
    x = 0
    y = 0
    if m == "1":
      x = -100
      y = 100
    if m == "2":
      x = 0
      y = 100
    if m == "3":
      x = 100
      y = 100
    if m == "4":
      x = -100
      y = 0
    if m == "5":
      x = 0
      y = 0
    if m == "6":
      x = 100
      y = 0
    if m == "7":
      x = -100
      y = -100
    if m == "8":
      x = 0
      y = -100
    if m == "9":
      x = 100
      y = -100
    t.goto(x,y-30)
    t.pendown()
    t.circle(32)
    t.penup()

  def winh(h):
    # draws a line for a horizontal win
    t.pencolor("white")
    x = 0
    y = 0
    if h == "1":
      y = 100
    if h == "2":
      y = 0
    if h == "3":
      y = -100
    t.goto(x-150,y)
    t.pendown()
    t.goto(x+150,y)
    t.penup()

  def winv(h):
    # draws a line for a vertical win
    t.pencolor("white")
    x = 0
    y = 0
    if h == "4":
      x = -100
    if h == "5":
      x = 0
    if h == "6":
      x = 100
    t.goto(x,y-150)
    t.pendown()
    t.goto(x,y+150)
    t.penup()

  def wind(h):
    # draws a line for a diagonal win
    t.pencolor("white")
    if h == "7":
      t.goto(-150,150)
      t.pendown()
      t.goto(150,-150)
      t.penup()
    if h == "8":
      t.goto(-150,-150)
      t.pendown()
      t.goto(150,150)
      t.penup()

  t.speed(10)
  t.pensize(3)
  screen.bgcolor("black")
  t.pencolor("white")
  grid() # draws grid

  print("Placement")
  print("1|2|3\n4|5|6\n7|8|9")
  print()

  players = input("How many players? 1/2: ")
  if players == "1":
    print()
    player = input("Who will you be? X/O: ").lower() # if you just press enter then it autoplays
  elif players == '2':
    player = 0
  else:
    print("Not sure how many. Assuming 1") # if you dont write anything it will continue against the AI
    print()
    player = input("Who will you be? X/O: ").lower() # if you just press enter then it autoplays
  print()

  gamestate = ['', '', '', '', '', '', '', '', '']
  spots = [""] # spots taken 
  while True:
    # these if statements detect wins
    if gamestate[0] == 'o' and gamestate[1] == 'o' and gamestate[2] == 'o':
      win = "1"
      print()
      print('O wins')
      winh(win)
      break
    if gamestate[3] == 'o' and gamestate[4] == 'o' and gamestate[5] == 'o':
      win = "2"
      print()
      print('O wins')
      winh(win)
      break
    if gamestate[6] == 'o' and gamestate[7] == 'o' and gamestate[8] == 'o':
      win = "3"
      print()
      print('O wins')
      winh(win)
      break
    if gamestate[0] == 'o' and gamestate[3] == 'o' and gamestate[6] == 'o':
      win = "4"
      print()
      print('O wins')
      winv(win)
      break
    if gamestate[1] == 'o' and gamestate[4] == 'o' and gamestate[7] == 'o':
      win = "5"
      print()
      print('O wins')
      winv(win)
      break
    if gamestate[2] == 'o' and gamestate[5] == 'o' and gamestate[8] == 'o':
      win = "6"
      print()
      print('O wins')
      winv(win)
      break
    if gamestate[0] == 'o' and gamestate[4] == 'o' and gamestate[8] == 'o':
      win = "7"
      print()
      print('O wins')
      wind(win)
      break
    if gamestate[2] == 'o' and gamestate[4] == 'o' and gamestate[6] == 'o':
      win = "8"
      print()
      print('O wins')
      wind(win)
      break
    else: # if there is no win it will continue to play
      if player == "x":
        m = user_x()
      elif players == "2": # if there is 2 plyers then this happens
        m = user_x()
      elif player != "x" and players != "2": 
        m = ai_x()

      if m != "draw":
        t.pencolor("cyan")
        draw_x(m)
        if m not in spots:
          spots.append(m)
        gamestate[int(m) - 1] = "x"
      elif m == "draw":
        print()
        print("Draw")
        break
  
    # these if statements detect wins    
    if gamestate[0] == 'x' and gamestate[1] == 'x' and gamestate[2] == 'x':
      win = "1"
      print()
      print('X wins')
      winh(win)
      break
    if gamestate[3] == 'x' and gamestate[4] == 'x' and gamestate[5] == 'x':
      win = "2"
      print()
      print('X wins')
      winh(win)
      break
    if gamestate[6] == 'x' and gamestate[7] == 'x' and gamestate[8] == 'x':
      win = "3"
      print()
      print('X wins')
      winh(win)
      break
    if gamestate[0] == 'x' and gamestate[3] == 'x' and gamestate[6] == 'x':
      win = "4"
      print()
      print('X wins')
      winv(win)
      break
    if gamestate[1] == 'x' and gamestate[4] == 'x' and gamestate[7] == 'x':
      win = "5"
      print()
      print('X wins')
      winv(win)
      break
    if gamestate[2] == 'x' and gamestate[5] == 'x' and gamestate[8] == 'x':
      win = "6"
      print()
      print('X wins')
      winv(win)
      break
    if gamestate[0] == 'x' and gamestate[4] == 'x' and gamestate[8] == 'x':
      win = "7"
      print()
      print('X wins')
      wind(win)
      break
    if gamestate[2] == 'x' and gamestate[4] == 'x' and gamestate[6] == 'x':
      win = "8"
      print()
      print('X wins')
      wind(win)
      break
    else: # if there is no win it will continue to play
      if player == "o":
        m = user_o()
      elif players == "2":  # if there is 2 plyers then this happens
        m = user_o()
      elif player != "o" and players != "2":
        m = ai_o()
      
      if m != "draw":
        t.pencolor("orange")
        draw_o(m)
        if m not in spots:
          spots.append(m)
        gamestate[int(m) - 1] = "o"
      if m == "draw":
        print()
        print("Draw")
        break

  t.goto(-175,175)
  d = "yes"
  print()
  replay = input("Replay?: ").lower()
  if replay == "yes" or replay == "y":
    print()
  elif replay == "no" or replay == "n":
    break
  else:
    while True:
      m = input('What was that?: ').lower()
      if m == "yes" or m == "y":
        print()
        break
      elif m == "no" or m == "n":
        d = "no"
        break
  if d == "no":
    break
print("End")