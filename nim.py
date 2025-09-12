# Prologue Comments
# Title: EECS 348 Assignment 3
# Description: 2-player game of nim

# Inputs: Player1 row number and stars to remove, Player2 row number and stars to remove
# Outputs: Displays the current game board to the players in the console or errors if appropriate

# Collaborators: None
# Sources: ChatGPT, FIXME probably more

# Author: Marie Biernacki
# Creation Date: September 12th, 2025

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
            # increment the total stars by 1
            totalStars += 1

    #if the total stars is still 0 after the for loop, return true
    if totalStars == 0:
        return True
    #otherwise return false
    else:
        return False

# function to update the current game board
# SOURCE: ChatGPT, Myself
# FIXME need to update the board with empty strings?
def updateBoard(currentBoard, rowNum, starNum):
    # convert user input to 0-based index
    rowIndex = rowNum - 1

    # safety check: is rowNum valid?
    if rowIndex < 0 or rowIndex >= len(currentBoard):
        return currentBoard

    rowLength = len(currentBoard[rowIndex])

    # remove stars from the right side
    for i in range(starNum):
        colIndex = rowLength - 1 - i
        if colIndex >= 0:
            currentBoard[rowIndex][colIndex] = " "

    return currentBoard



def playerPrompt(playerNum, currentBoard):
    # display the player number
    print(f"Player {playerNum}'s turn")

    # obtain the row number and the number of stars to remove from the current player
    rowNum = input("Enter a row number: ")
    starNum = input("Stars to remove from the row: ")

    # FIXME verify the input are integers? create a separate function to do this?
    #if not isInteger(rowNum, starNum): print ("ERROR - rowNum and starNum must be integers" and return the currentBoard)
    # if the move is valid
    if isValidMove(currentBoard, int(rowNum), int(starNum)) == True:
        # update the board
        print("FIXME UPDATE BOARD HERE")
        newBoard = updateBoard(currentBoard, int(rowNum), int(starNum))
        return newBoard
    else:
        print("ERROR -- No changes made to board")
        return currentBoard


# function to determine if the current move is valid
# SOURCE: Myself
# FIXME: add features to verify rowNum and starNum are integers?
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

                # if the value is not equal to an empty space
                if currentBoard[row][col] != " ":
                    # increment the starCount by 1
                    starCount += 1

    # if the starCount == 0 after the for loop, then return false
    if starCount == 0:
        return False

    # else if the number of stars to remove is larger than the current stars in the row, return false
    elif starNum > starCount:
        print(f"starNum given = {starNum} current starCount in {rowNum} = {starCount}")
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

    # display the starting board
    displayCurrentBoard(currentBoard)

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

        # call playerPrompt function, which will return the updated board
        updatedBoard = playerPrompt(currentPlayer, currentBoard)

        displayCurrentBoard(updatedBoard)

        # FIXME if the updatedBoard and the currentBoard are the same, then do not update the round number
            # call playerPrompt again
        # else they are different
            # increment the round number by 1

if __name__ == '__main__':
    playNim()



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
