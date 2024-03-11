import numpy as np
import random

# Define the global variables
turn = 0
# Initialize the game matrix
game = np.array([[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]])


# Function used to verify if a player has won
def verif_win(game):
    for x in range(1, 3):
        # Verify the diagonals
        if (game[0][0] == game[1][1] == game[2][2] == x) or (game[2][0] == game[1][1] == game[0][2] == x):
            return x

        for i in range(len(game)):
            # Verify the row
            if np.array_equal(game[i], [x, x, x]):
                return x

            # Verify the column
            elif np.array_equal(game[:, i], [x, x, x]):
                return x

            # Verify if there is a tie
            elif not np.isin(game, 0).any():
                return 404
    else:
        return 0


def AI(level):
    if level == 1:
        # Default level, play randomly
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        return x, y
    elif level == 2:
        # Complex level, play randomly but check if there is a winning move

        # Check the diagonals \
        if np.array_equal(np.diag(game), [1, 1, 0]) or np.array_equal(np.diag(game), [1, 0, 1]) or np.array_equal(
                np.diag(game), [0, 1, 1]):
            x = np.diag(game).tolist().index(0)
            print("AI beet you :O (ID3)")
            return x, x

        # Check the inverted diagonals /
        if np.array_equal(np.diag(np.fliplr(game)), [1, 1, 0]) or np.array_equal(np.diag(np.fliplr(game)),
                                                                                 [1, 0, 1]) or np.array_equal(
            np.diag(np.fliplr(game)), [0, 1, 1]):
            y = np.diag(np.fliplr(game)).tolist().index(0)
            print("AI beet you :O (ID4)")
            x = abs(y - 2)
            return x, y

        for y in range(len(game)):

            # Check the columns
            if np.array_equal(game[y], [0, 1, 1]) or np.array_equal(game[y], [1, 1, 0]) or np.array_equal(game[y],
                                                                                                          [1, 0,
                                                                                                           1]):
                x = game[y].tolist().index(0)
                print("AI beet you :O (ID1)")
                return x, y

            # Check the rows
            elif np.array_equal(game[:, y], [1, 1, 0]) or np.array_equal(game[:, y], [0, 1, 1]) or np.array_equal(
                    game[:, y], [1, 0, 1]):
                x = game[:, y].tolist().index(0)
                print("AI beet you :O (ID2)")
                # Cause of the way the matrix is built, we need to return y, x
                return y, x

            else:
                # If no winning move, continue and play randomly
                continue

        x = random.randint(0, 2)
        y = random.randint(0, 2)
        return x, y

    elif level == 3:

        #diagonals \
        if np.array_equal(np.diag(game), [2, 2, 0]) or np.array_equal(np.diag(game), [2, 0, 2]) or np.array_equal(
                np.diag(game), [0, 2, 2]):
            x = np.diag(game).tolist().index(0)
            print("AI beet you :O (ID3)")
            return x, x

        #diagonals /
        elif np.array_equal(np.diag(np.fliplr(game)), [2, 2, 0]) or np.array_equal(np.diag(np.fliplr(game)),
                                                                                   [2, 0, 2]) or np.array_equal(
            np.diag(np.fliplr(game)), [0, 2, 2]):
            y = np.diag(np.fliplr(game)).tolist().index(0)
            print("AI beet you :O (ID4)")
            x = abs(y - 2)
            return x, y

        for y in range(len(game)):

            #columns
            if np.array_equal(game[y], [0, 2, 2]) or np.array_equal(game[y], [2, 2, 0]) or np.array_equal(game[y],
                                                                                                          [2, 0,
                                                                                                           2]):
                x = game[y].tolist().index(0)
                print("AI beet you :O (ID1)")
                return x, y

            #row
            elif np.array_equal(game[:, y], [2, 2, 0]) or np.array_equal(game[:, y], [0, 2, 2]) or np.array_equal(
                    game[:, y], [2, 0, 2]):
                x = game[:, y].tolist().index(0)
                print("AI beet you :O (ID2)")
                # Cause of the way the matrix is built, we need to return y, x
                return y, x

        #diagonals \
        if np.array_equal(np.diag(game), [1, 1, 0]) or np.array_equal(np.diag(game), [1, 0, 1]) or np.array_equal(
                np.diag(game), [0, 1, 1]):
            x = np.diag(game).tolist().index(0)
            print("AI beet you :O (ID3)")
            return x, x

        #diagonals /
        elif np.array_equal(np.diag(np.fliplr(game)), [1, 1, 0]) or np.array_equal(np.diag(np.fliplr(game)),
                                                                                   [1, 0, 1]) or np.array_equal(
            np.diag(np.fliplr(game)), [0, 1, 1]):
            y = np.diag(np.fliplr(game)).tolist().index(0)
            print("AI beet you :O (ID4)")
            x = abs(y - 2)
            return x, y

        for y in range(len(game)):

            #columns
            if np.array_equal(game[y], [0, 1, 1]) or np.array_equal(game[y], [1, 1, 0]) or np.array_equal(game[y],
                                                                                                          [1, 0,
                                                                                                           1]):
                x = game[y].tolist().index(0)
                print("AI beet you :O (ID1)")
                return x, y

            #row
            elif np.array_equal(game[:, y], [1, 1, 0]) or np.array_equal(game[:, y], [0, 1, 1]) or np.array_equal(
                    game[:, y], [1, 0, 1]):
                x = game[:, y].tolist().index(0)
                print("AI beet you :O (ID2)")
                # Cause of the way the matrix is built, we need to return y, x
                return y, x

            else:
                continue

        x = random.randint(0, 2)
        y = random.randint(0, 2)
        return x, y


    else:
        return 0, 0


# Function used to display the result of the game
def result():
    print(game)
    # Check if user 1 has won
    if verif_win(game) == 1:
        print("Joueur 1 gagnant")
    # Check if user 2 has won
    elif verif_win(game) == 2:
        print("Joueur 2 gagnant")
    # Check if there is a tie
    elif verif_win(game) == 404:
        print("Egalité")
    # If no result, continue the game
    else:
        play()


def play():
    global turn
    global levelAI

    # Using the global variable turn to know which player is playing
    if turn == 0:
        print("Joueur 1 : à toi de jouer")
        x = int(input("Entre x : "))
        y = int(input("Entre y : "))

        # Check if matrix is already occupied
        if game[y][x] == 2 or game[y][x] == 1:
            print("Endroit occupé")
            play()
        else:
            # Update the matrix
            game[y][x] = 1
            # Change the turn
            turn = 1
            result()
    else:
        if levelAI != 0:
            x, y = AI(levelAI)
            if game[y][x] == 2 or game[y][x] == 1:
                play()
            else:
                print("IA : à toi de jouer")
                game[y][x] = 2
                turn = 0
                result()
        else:
            print("Joueur 2 : à toi de jouer")
            x = int(input("Entre x : "))
            y = int(input("Entre y : "))

            if game[y][x] == 2 or game[y][x] == 1:
                print("Endroit occupé")
                play()
            else:
                game[y][x] = 2
                turn = 0
                result()


# Function called to start the game
levelAI = int(input("Niveau de l'IA (1-3) : "))
play()
