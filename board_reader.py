# Returns 2-dimensional character list representation of board in txt file input
def to_board(txt):
    with open(txt, "r") as file:
        file.readline() # Ignores params line
        board = []
        for line in file:

            row = list(line.rstrip('\n'))

            print(row)
            board.append(row)
        file.close()
        return board


# Returns list of string parameters from first line of input txt file
def params(txt):
    with open(txt, "r") as file:
        ships = file.readline()
        ships = ships.rstrip('\n')
        ships = ships.split(", ")
        return ships


