"""
 * File:simpleBattleshi[.h
 * Author: Jacket Demby's
 * Creation date: 12/21/2018
"""

# Import the necessary libraries
from random import randint

# This section implements the functions to be used for the board game 
def print_board(board):
  for row in board:
    print " ".join(row)
    
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def main():
	print "Ready, you're about to play a simple one player battleship game\n"

	# This section implements the board game
	# Set game board as an empty list
	board = []
	board_width = int(raw_input("How wide would you like your board to be: "))
	number_of_turn = int(raw_input("How many guessing chances would you like to be given: "))

	for element in range(board_width):
	  board.append(["O"] * board_width)

	print "Turn 0\n"
	print_board(board)
	print "\n"

	# Assign a random location to the hidden shi
	ship_row = random_row(board)
	ship_col = random_col(board)
	#print ship_row
	#print ship_col

	# Everything from here on should go in your for loop!
	# Be sure to indent four spaces!
	for turn in range(number_of_turn):
	  print "Turn", turn + 1
	  
	  guess_row = int(raw_input("Guess Row: "))
	  guess_col = int(raw_input("Guess Col: "))

	  if guess_row == ship_row and guess_col == ship_col:
	    print("Congratulations! You sunk the hidden battleship!\n")
	    break
	  else:
	    if (guess_row < 0 or guess_row > board_width-1) or (guess_col < 0 or guess_col > board_width-1):
	      print("The location you provided is not in the game board\n")
	    elif(board[guess_row][guess_col] == "X"):
	      print(";-), sorry , but you already guessed that location\n")
	    else:      
	      print ("You missed the battleship!\n")
	      board[guess_row][guess_col] = "X"
	    # Print (turn + 1) here!
	    if turn == number_of_turn-1:
	        print "Game Over\n"
	        print "Look at this, you went all over the places \nAnd completely missed the hidden ship ;-)"
	        print "The ship was actually here:[" + str(ship_row) + "][" + str(ship_col) + "]"
	    print_board(board)
	    print "\n"

if __name__=="__main__":
	main()