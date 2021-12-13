# TODO
# Set that negated misses imply a permutation
# Possibly add constraints for negated misses

from os import system
from bauhaus import Encoding, proposition, constraint, utils, print_theory
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
from Coordinate import Coordinate
from permutations import SHIPS
from visuals import visual
from board_reader import to_board, params
import math, sys, time

sys.setrecursionlimit(10000)

E = Encoding()

#   CONSTANTS
DIM = 10
#   Change this if you want a different txt file used
BOARD_FILE = 'boards/battleship.txt'

# Probably could have used a list instead
ship_Name = {
    "D": "destroyer",
    "Cr": "cruiser",
    "S": "submarine",
    "Ba": "battleship",
    "Ca": "carrier"
}


# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)  # Ship is active on board (In-game, not yet sunk)
class ShipStatus:

    def __init__(self, ship_type):
        self.ship_type = ship_type

    def __repr__(self):
        return f"ShipStatus({self.ship_type})"


D = ShipStatus('D')
S = ShipStatus('S')
Cr = ShipStatus('Cr')
B = ShipStatus('B')
Ca = ShipStatus('Ca')

dict_status = {
    "destroyer": D,
    "cruiser": S,
    "submarine": Cr,
    "battleship": B,
    "carrier": Ca
}


@proposition(E)  # Coordinate is a hit
class Hit:

    def __init__(self, coord):
        self.coord = coord

    def __repr__(self) -> str:
        return repr(f"({self.coord.x}, {self.coord.y}) is a hit!")


hit_board = []
for y in range(DIM):
    hit_col = []
    for x in range(DIM):
        hit_col.append(Hit(Coordinate(x, y)))
    hit_board.append(hit_col)


@proposition(E)  # Coordinate is a miss/out-of-bounds
class Miss:

    def __init__(self, coord):
        self.coord = coord

    def __repr__(self) -> str:
        return repr(f'({self.coord.x}, {self.coord.y}) is a miss.')


miss_board = []
for y in range(DIM):
    miss_col = []
    for x in range(DIM):
        miss_col.append(Miss(Coordinate(x, y)))
    miss_board.append(miss_col)


@proposition(E)
class ShipPerm:
    def __init__(self, coord, config_num, ship_type):
        self.coord = coord
        self.config_num = config_num
        self.ship_type = ship_type

    def __repr__(self) -> str:
        return f"ShipPerm({self.coord.x}, {self.coord.y}, {self.ship_type}, {SHIPS[self.ship_type][self.config_num]})\n"


all_perms = []

# Makes propositions for ship permutations at every (x,y) on the board.
for ship in ship_Name.values():
    for i in range(len(SHIPS[ship])):
        for x in range(DIM):
            for y in range(DIM):
                coord = Coordinate(x, y)
                perm = ShipPerm(coord, i, ship)
                all_perms.append(perm)
                E.add_constraint(~dict_status[ship] >> ~perm)

# Constraint - No point can be both a hit and a miss.
for x in range(DIM):
    for y in range(DIM):
        E.add_constraint(~hit_board[y][x] | ~miss_board[y][x])


# Constraint
# A ship being alive implies no misses at specific coordinates which imply a permutation and permutations can not be out of bounds
# Honestly this constraint is pretty long
def perm_truth(hit_detect, board):
    for ship in all_perms:
        perm = SHIPS[ship.ship_type][ship.config_num]
        coords = []
        hits = []
        check = True
        if board[ship.coord.y][ship.coord.x] == "-":
            if len(perm) != 1:
                #To get the center point of a permutation
                adjust = math.floor(len(perm) / 2)
                #Loops through and retrieve the tiles that the permutation exists on
                for x in range(len(perm)):
                    if perm[x][0] == "X":
                        if (ship.coord.x + x - adjust) < 0 or (ship.coord.x + x - adjust) > (DIM - 1):
                            E.add_constraint(~ship)
                            check = False
                            break
                        else:
                            coords.append(miss_board[ship.coord.y][ship.coord.x + x - adjust])
                            hits.append(hit_board[ship.coord.y][ship.coord.x + x - adjust])
            if len(perm[0]) != 1:
                #To get the center point of a permutation
                adjust = math.floor(len(perm[0]) / 2)
                #Loops through and retrieve the tiles that the permutation exists on
                for y in range(len(perm[0])):
                    if perm[0][y] == "X":
                        if (ship.coord.y + y - adjust) < 0 or (ship.coord.y + y - adjust) > (DIM - 1):
                            E.add_constraint(~ship)
                            check = False
                            break
                        else:
                            coords.append(miss_board[ship.coord.y + y - adjust][ship.coord.x])
                            hits.append(hit_board[ship.coord.y + y - adjust][ship.coord.x])
        else:
            E.add_constraint(~ship)
            check = False

        # A hit on the board would imply that the permutation should exist on top of that hit.
        # otherwise the permutation only has to worry about the ship status being true and that
        # it does not exist on any miss tiles
        if check == True:
            if len(coords) == 2:
                if hit_detect == False:
                    E.add_constraint(dict_status[ship.ship_type] >> ((~coords[0] & ~coords[1]) >> ship))
                else:
                    E.add_constraint(dict_status[ship.ship_type] >>
                                     (((~coords[0] & ~coords[1]) & (hits[0] | hits[1])) >> ship))

            elif len(coords) == 3:
                if hit_detect == False:
                    E.add_constraint(dict_status[ship.ship_type] >> ((~coords[0] & ~coords[1] & ~coords[2]) >> ship))
                else:
                    E.add_constraint(dict_status[ship.ship_type] >>
                                     (((~coords[0] & ~coords[1] & ~coords[2]) & (hits[0] | hits[1] | hits[2])) >> ship))

            elif len(coords) == 4:
                if hit_detect == False:
                    E.add_constraint(
                        dict_status[ship.ship_type] >> ((~coords[0] & ~coords[1] & ~coords[2] & ~coords[3]) >> ship))
                else:
                    E.add_constraint(dict_status[ship.ship_type] >>
                                     (((~coords[0] & ~coords[1] & ~coords[2] & ~coords[3]) & (
                                                 hits[0] | hits[1] | hits[2] | hits[3])) >> ship))

            elif len(coords) == 5:
                if hit_detect == False:
                    E.add_constraint(dict_status[ship.ship_type] >> (
                                (~coords[0] & ~coords[1] & ~coords[2] & ~coords[3] & ~coords[4]) >> ship))
                else:
                    E.add_constraint(dict_status[ship.ship_type] >>
                                     (((~coords[0] & ~coords[1] & ~coords[2] & ~coords[3] & ~coords[4]) & (
                                                 hits[0] | hits[1] | hits[2] | hits[3] | hits[4])) >> ship))


# Establishes if misses or hits are true at a tile
def config_board(board):
    hit_detect = False
    for y in range(DIM):
        for x in range(DIM):
            if board[y][x] == 'X':
                hit_detect = True
                E.add_constraint(hit_board[y][x])
                E.add_constraint(~miss_board[y][x])
            elif board[y][x] == "O":
                E.add_constraint(~hit_board[y][x])
                E.add_constraint(miss_board[y][x])
            else:
                E.add_constraint(~miss_board[y][x] & ~hit_board[y][x])
    perm_truth(hit_detect, board)

#Creates constraints for the ships that do not exist
def example_theory(board, status_false, active):
    config_board(board)

    for status in status_false:
        print(status + ",", end=" ")
    print("are not active on the board")

    for status in active:
        print(ship_Name[status] + ",", end=" ")
    print("are active on the board")

    for ship in dict_status.keys():
        found = False
        for status in status_false:
            if status == ship:
                E.add_constraint(~dict_status[status])
                found = True
        if found == False:
            E.add_constraint(dict_status[ship])

    return E


if __name__ == "__main__":
    #A list representation of the  game board
    board = []
    print("X represents a hit on an unknown ship, O represents a miss or a sunken ship, - is a non attacked tile")
    board = to_board(BOARD_FILE)

    # A list of all the ships that have been destroyed.
    status_false = []
    alive_ships = params(BOARD_FILE)
    for ship in ship_Name.keys():
        found = False
        for alive in alive_ships:
            if alive == ship:
                found = True
        if found == False:
            status_false.append(ship_Name[ship])

    T = example_theory(board, status_false, alive_ships)
    print("Please wait while we load a solution. This could take a couple minutes. Go get a drink or a snack while you wait.")
    # Don't compile until you're finished adding all your constraints!
    t = time.time()
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    check = T.satisfiable()
    print("\nSatisfiable: %s" % check)
    if check == True:
        print("Hang on a bit longer. A solution has almost been obtained.")
        sol = T.solve()
        visual(sol, DIM, all_perms, board)
        print("Time to complete: %.2f seconds" % (time.time() - t))
    else:
        print("No solution found")
