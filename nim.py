# Prologue Comments
# Title: EECS 348 Assignment 3
# Description: 2-player game of nim

# Inputs: Player1 row number and stars to remove, Player2 row number and stars to remove
# Outputs: Displays the current game board to the players in the console or errors if appropriate

# Collaborators: None
# Sources: ChatGPT

# Author: Marie Biernacki
# Creation Date: September 12th, 2025

#needed to create a copy of the currentBoard for comparison
import copy

# function to determine if the game is over
# SOURCE: Myself
def gameOver(currentBoard):

    # initialize a variable to hold the total stars in the board
    totalStars = 0

    # iterate through the 2D array of the currentBoard using a for loop
    # first, iterate through each row
    for row in range(len(currentBoard)):
        # iterate through each col of that row
        for col in range(len(currentBoard[row])):
            # if the col has a star
            if currentBoard[row][col] == "*":
                # increment the total stars by 1
                totalStars += 1

    #if the total stars is still 0 after the for loop, return true
    if totalStars == 0:
        return True
    #otherwise return false
    else:
        return False

# function to check if the currentBoard and updatedBoard are equal
# SOURCE: Myself
def boardsAreEqual(currentBoard, updatedBoard):

    # use a for loop to iterate through the currentBoard and updatedBoard to compare values

    # iterate through the 2D array of the currentBoard using a for loop
    # first, iterate through each row
    for row in range(len(currentBoard)):
        # iterate through each col of that row
        for col in range(len(currentBoard[row])):
            # compare the value of the currentBoard with the value of the updatedBoard
            # if they are not equal, return False
            if currentBoard[row][col] != updatedBoard[row][col]:
               return False

    # after the for loop runs, return True
    return True



# function to update the current game board
# SOURCE: ChatGPT, Myself
def updateBoard(currentBoard, rowNum, starNum):
    newBoard = copy.deepcopy(currentBoard)
    rowIndex = rowNum - 1

    # Find indices of actual stars in the row
    starIndices = [i for i, val in enumerate(newBoard[rowIndex]) if val == '*']

    # Remove stars from the **end** of the row
    for i in range(min(starNum, len(starIndices))):
        newBoard[rowIndex][starIndices[-1 - i]] = ' '

    return newBoard


# function to obtain input from the current player, verify inputs, and update the board appropriately
# SOURCE: Myself
def playerPrompt(playerNum, currentBoard):
    # display the player number
    print(f"\nPlayer {playerNum}")

    # obtain the row number and the number of stars to remove from the current player
    rowNum = input("Enter a row number: ")
    starNum = input("Stars to remove: ")

    # verify the input rowNum and starNum are integers
    # print appropriate error messages and return the currentBoard as needed
    if not rowNum.isdigit():
        print("ERROR: Row number must be an integer.")
        return currentBoard

    if not starNum.isdigit():
        print("ERROR: Star number must be an integer.")
        return currentBoard

    # if the move is valid
    if isValidMove(currentBoard, int(rowNum), int(starNum)):
        # call updateBoard function to update, store the results in newBoard and return
        newBoard = updateBoard(currentBoard, int(rowNum), int(starNum))
        return newBoard

    # otherwise the move is not valid
    else:
        # return the currentBoard
        return currentBoard


# function to determine if the current move is valid
# SOURCE: Myself
def isValidMove(currentBoard, rowNum, starNum):

    # check that the rowNum is a valid option (can only be 1 through 5)
    if rowNum not in range(1,6):
        return False

    # the following code checks that there are stars in that row to be removed

    # initialize starCount to track the number of stars currently in the rowNum provided
    starCount = 0

    # iterate through the 2D array of the currentBoard using a for loop
    # first, iterate through each row
    for row in range(len(currentBoard)):
        # get to the rowNum provided by the user
        if rowNum == row + 1:
            # iterate through each col of that row
            for col in range(len(currentBoard[row])):

                # if the value is equal to a *
                if currentBoard[row][col] == "*":
                    # increment the starCount by 1
                    starCount += 1

    # if the starCount == 0 after the for loop, then return false
    if starCount == 0:
        # display an error message
        print(f"ERROR: No stars in row {rowNum} to remove")
        return False

    # else if the number of stars to remove is larger than the current stars in the row, return false
    elif starNum > starCount:
        # display an error message
        print(f"ERROR: Cannot remove {starNum} stars from row {rowNum}, there are only {starCount} stars available to remove.")
        return False

    # otherwise return true
    else:
        return True



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

    # use a 2D array to initialize the game board
    currentBoard = [
        ['*','*','*','*','*'],
        ['*','*','*','*'],
        ['*','*','*'],
        ['*','*'],
        ['*']]


    # keep track of the number of rounds (used to determine the currentPlayer number)
    round = 1

    # while the game is not over
    while not gameOver(currentBoard):
        # if the round is even, the current player is player 2
        if round % 2 == 0:
            currentPlayer = 2
        # otherwise the round is odd and the current player is player 1
        else:
            currentPlayer = 1

        # display the currentBoard
        displayCurrentBoard(currentBoard)

        # call playerPrompt function, which will return the updated board
        updatedBoard = playerPrompt(currentPlayer, currentBoard)

        # if updatedBoard and the currentBoard are NOT the same
        # meaning changes were made (because there were no errors)
        if not boardsAreEqual(currentBoard, updatedBoard):
            # set the currentBoard equal to the updatedBoard
            currentBoard = updatedBoard
            # increment the round number by 1 to advance to the next player
            round += 1
            print()
        else:
            print()

    # if the PREVIOUS ROUND is even, the lastPlayer is player 2
    if (round - 1) % 2 == 0:
        lastPlayer = 2
    # otherwise the PREVIOUS ROUND is odd and the lastPlayer is player 1
    else:
        lastPlayer = 1

    print(f'Congratulations, Player {lastPlayer}! You win!')

if __name__ == '__main__':
    # call playNim to start the program
    playNim()
