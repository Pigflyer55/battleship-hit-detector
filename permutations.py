# visualizing the different permuttions for each ship
# Could possibly put all these into arrays immediately instead
# of making strings

# TODO
# Decide whether to make these strings or immediately be arrays
# Some of the comments under the permutations may be incorrect. Won't affect the final output.

destroyer = []

destroyer.append([["X", "X", "-"]])
#    XX-

destroyer.append([["-", "X", "X"]])
#    -XX


destroyer.append([["X"], ["X"], ["-"]])
#   X
#   X
#   -

destroyer.append([["-"], ["X"], ["X"]])
#    -
#    X
#    X



cruiser = []


cruiser.append([["X", "X", "X", "-", "-"]])
#    XXX--

cruiser.append([["-", "-", "X", "X", "X"]])
#    --XXX

cruiser.append([["X"], ["X"], ["X"], ["-"], ["-"]])
#    X
#    X
#    X
#    -
#    -

cruiser.append([["-"], ["-"], ["X"], ["X"], ["X"]])
#    -
#    -
#    X
#    X
#    X

cruiser.append([["-", "X", "X", "X", "-"]])
#    -XXX-

cruiser.append([["-"], ["X"], ["X"], ["X"], ["-"]])
#    -
#    X
#    X
#    X
#    -



submarine = []

submarine.append([["X", "X", "X", "-", "-"]])
#    XXX--


submarine.append([["-", "-", "X", "X", "X"]])
#    --XXX


submarine.append([["X"], ["X"], ["X"], ["-"], ["-"]])
#    X
#    X
#    X
#    -
#    -


submarine.append([["-"], ["-"], ["X"], ["X"], ["X"]])
#    -
#    -
#    X
#    X
#    X


submarine.append([["-", "X", "X", "X", "-"]])
#    -XXX-


submarine.append([["-"], ["X"], ["X"], ["X"], ["-"]])
#    -
#    X
#    X
#    X
#    -


battleship = []

battleship.append([["-", "-", "-", "X", "X", "X", "X"]])
#    ---XXXX


battleship.append([["X", "X", "X", "X", "-", "-", "-"]])
#    XXXX---


battleship.append([["X"], ["X"], ["X"], ["X"], ["-"], ["-"], ["-"]])
#    X
#    X
#    X
#    X
#    -
#    -
#    -


battleship.append([["-"], ["-"], ["-"], ["X"], ["X"], ["X"], ["X"]])
#    -
#    -
#    -
#    X
#    X
#    X
#    X


battleship.append([["-", "-", "X", "X", "X", "X", "-"]])
#    --XXXX-


battleship.append([["-", "X", "X", "X", "X", "-", "-"]])
#    -XXXX--


battleship.append([["-"], ["X"], ["X"], ["X"], ["X"], ["-"], ["-"]])
#    -
#    X
#    X
#    X
#    X
#    -
#    -


battleship.append([["-"], ["-"], ["X"], ["X"], ["X"], ["X"], ["-"]])
#    -
#    -
#    X
#    X
#    X
#    X
#    -


carrier = []

carrier.append([["-", "-", "-", "-", "X", "X", "X", "X", "X"]])
#    ----XXXXX


carrier.append([["X", "X", "X", "X", "X", "-", "-", "-", "-"]])
#    XXXXX----


carrier.append([["X"], ["X"], ["X"], ["X"], ["X"], ["-"], ["-"], ["-"], ["-"]])
#    X
#    X
#    X
#    X
#    X
#    -
#    -
#    -
#    -


carrier.append([["-"], ["-"], ["-"], ["-"], ["X"], ["X"], ["X"], ["X"], ["X"]])
#    -
#    -
#    -
#    -
#    X
#    X
#    X
#    X
#    X


carrier.append([["-", "-", "-", "X", "X", "X", "X", "X", "-"]])
#    ---XXXXX-


carrier.append([["-", "X", "X", "X", "X", "X", "-", "-", "-"]])
#    -XXXXX---


carrier.append([["-"], ["X"], ["X"], ["X"], ["X"], ["X"], ["-"], ["-"], ["-"]])
#    -
#    X
#    X
#    X
#    X
#    X
#    -
#    -
#    -


carrier.append([["-"], ["-"], ["-"], ["X"], ["X"], ["X"], ["X"], ["X"], ["-"]])
#    -
#    -
#    -
#    X
#    X
#    X
#    X
#    X
#    -


carrier.append([["-", "-", "X", "X", "X", "X", "X", "-", "-"]])
#    --XXXXX--


carrier.append([["-"], ["-"], ["X"], ["X"], ["X"], ["X"], ["X"], ["-"], ["-"]])
#    -
#    -
#    X
#    X
#    X
#    X
#    X
#    -
#    -


SHIPS = {
    "destroyer": destroyer,     
    "submarine": submarine,     
    "cruiser": cruiser,         
    "battleship": battleship,   
    "carrier": carrier          
}
