# Prologue Comments
# Title: EECS 348 Assignment 3
# Description: 2-player game of nim

# Inputs: Player1 row number and stars to remove, Player2 row number and stars to remove
# Outputs: Displays the current game board to the players in the console or errors if appropriate

# Collaborators: None
# Sources: ChatGPT, FIXME probably more

# Author: Marie Biernacki
# Creation Date: September 12th, 2025

def updateBoard(currentBoard, rowNum, starNum):
    #update the current board

def playerPrompt(playerNum):
    # collect player choices here?

# function to determine if the current move is valid
def isValidMove(currentBoard, rowNum, starNum):
    #FIXME check that the rowNum entered is valid
    # check the stars can be removed from that row

# function to display the current nim board
# SOURCE: Myself
def displayCurrentBoard(currentBoard):

    # iterate through the 2D array of the currentBoard using a for loop
    # first, iterate through each row
    for row in range(len(currentBoard)):
        # print the row number
        print(f"{row + 1}:", end=" ")

        # iterate through each star of that row
        for col in range(len(currentBoard[row])):
            # print the star at [row][col]
            # use end=" " to ensure they are on the same line
            print(currentBoard[row][col], end=" ")

        # after iterating through the row, create a newline for the next row
        print()

# function to initialize and play a game of nim until the user decides to quit
# SOURCE: Myself
def playNim():

    # use a 2D array to define the initial game board
    currentBoard = [
        ['*','*','*','*','*'],
        ['*','*','*','*'],
        ['*','*','*'],
        ['*','*'],
        ['*']]

    displayCurrentBoard(currentBoard)

if __name__ == '__main__':
    playNim()

    #display the starting board
        # check if game is finished
        # if yes, display the current player as the winner (they made the board empty) and end loop
        # otherwise continue

    # prompt player 1
        #display Player 1
        # ask player 1 for row num
        # ask player 1 for stars to remove

        # determine if the move is valid
            # if yes
                # update the board and display
                    # check if game is finished
                    # if yes, display the current player as the winner (they made the board empty) and end loop
                    # otherwise continue
            # if no
                # error
                # re-display the current board and re-prompt current player

    # prompt player 2
        # display Player 2
        # ask player 2 for row num
        # ask player 2 for stars to remove

        # determine if the move is valid
            # if yes
                # update the board and display
                    # check if game is finished
                    # if yes, display the current player as the winner (they made the board empty) and end loop
                    # otherwise continue
            # if no
                # error
                # re-display the current board and re-prompt current player
