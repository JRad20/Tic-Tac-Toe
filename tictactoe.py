import time
import sys




def restart():
    restart_game = input('Would you like to restart the game y/n \n')
    if restart_game == 'y':


        startGame()
    if restart_game == 'n':
        print('Closing application...')
        time.sleep(3)
        sys.exit()
    else:
        restart()


def checkTie():
    global remaining_moves
    remaining_moves -= 1

    if remaining_moves <= 0:
        print('Game has ended in a tie! ')
        restart()

def checkWin():
    # X checks
    # X checks; across
    if moves['1'] == 'X' and moves['2'] == 'X' and moves['3'] == 'X':
        print('Player1 has won the game!')
        restart()
    if moves['4'] == 'X' and moves['5'] == 'X' and moves['6'] == 'X':
        print('Player1 has won the game!')
        restart()
    if moves['7'] == 'X' and moves['8'] == 'X' and moves['9'] == 'X':
        print('Player1 has won the game!')
        restart()
    # X checks; across
    # X checks; down
    if moves['1'] == 'X' and moves['4'] == 'X' and moves['7'] == 'X':
        print('Player1 has won the game!')
        restart()
    if moves['2'] == 'X' and moves['5'] == 'X' and moves['8'] == 'X':
        print('Player1 has won the game!')
        restart()
    if moves['3'] == 'X' and moves['6'] == 'X' and moves['9'] == 'X':
        print('Player1 has won the game!')
        restart()
    # X checks; down
    # X checks; diagonal
    if moves['1'] == 'X' and moves['5'] == 'X' and moves['9'] == 'X':
        print('Player1 has won the game!')
        restart()
    if moves['7'] == 'X' and moves['5'] == 'X' and moves['3'] == 'X':
        print('Player1 has won the game!')
        restart()
    # X checks; diagonal
    # X checks
    # O checks
    # O checks; across
    if moves['1'] == 'O' and moves['2'] == 'O' and moves['3'] == 'O':
        print('Player2 has won the game!')
        restart()
    if moves['4'] == 'O' and moves['5'] == 'O' and moves['6'] == 'O':
        print('Player2 has won the game!')
        restart()

    if moves['7'] == 'O' and moves['8'] == 'O' and moves['9'] == 'O':
        print('Player2 has won the game!')
        restart()
    # O checks; across
    # O checks; down
    if moves['1'] == 'O' and moves['4'] == 'O' and moves['7'] == 'O':
        print('Player2 has won the game!')
        restart()
    if moves['2'] == 'O' and moves['5'] == 'O' and moves['8'] == 'O':
        print('Player2 has won the game!')
        restart()
    if moves['3'] == 'O' and moves['6'] == 'O' and moves['9'] == 'O':
        print('Player2 has won the game!')
        restart()
    # O checks; down
    # O checks; diagonal
    if moves['1'] == 'O' and moves['5'] == 'O' and moves['O'] == 'O':
        print('Player2 has won the game!')
        restart()
    if moves['7'] == 'O' and moves['5'] == 'O' and moves['3'] == 'O':
        print('Player2 has won the game!')
        restart()
    # O checks; diagonal
    # O Checks


def startGame():
    global remaining_moves
    global moves

    remaining_moves = 9



    moves = {

        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }



    current_board = str(moves['1']) + '|' + str(moves['2']) + '|' + str(moves['3']) + '\n' + str(moves['4']) + '|' + str(moves['5']) + '|' + str(moves['6']) + '\n' + str(moves['7']) + '|' + str(moves['8']) + '|' + str(moves['9'])
    print(current_board + '\n')
    # Start With letting player one make the first move
    playerOneMove()
def playerOneMove():
    p1 = input('P1 Enter Move\n')
    # We need to check if the move has already been played
    if moves[p1] == 'X':
        print('Move has already been played')
        playerOneMove()
    if moves[p1] == 'O':
        print('Move has already been played')
        playerOneMove()
    else:
        moves[p1] = 'X'
        current_board = str(moves['1']) + '|' + str(moves['2']) + '|' + str(moves['3']) + '\n' + str(moves['4']) + '|' + str(moves['5']) + '|' + str(moves['6']) + '\n' + str(moves['7']) + '|' + str(moves['8']) + '|' + str(moves['9'])
        print(current_board)
        checkWin()
        checkTie()
        playerTwoMove()
def playerTwoMove():
    p2 = input('P2 Enter Move\n')
    # We need to check if the move has already been played
    if moves[p2] == 'X':
        print('Move has already been played')
        playerTwoMove()
    if moves[p2] == 'O':
        print('Move has already been played')
        playerTwoMove()
    else:
        moves[p2] = 'O'
        current_board = str(moves['1']) + '|' + str(moves['2']) + '|' + str(moves['3']) + '\n' + str(moves['4']) + '|' + str(moves['5']) + '|' + str(moves['6']) + '\n' + str(moves['7']) + '|' + str(moves['8']) + '|' + str(moves['9'])
        print(current_board)
        checkWin()
        checkTie()
        playerOneMove()


if __name__ == '__main__':
    startGame()
