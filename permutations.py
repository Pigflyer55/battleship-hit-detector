#visualizing the different permuttions for each ship
#Could possibly put all these into arrays immediately instead
# of making strings

#TODO
#Decide whether to make these strings or immediately be arrays
#If strings than do conversion def at bottom.

destroyer = []
dperm1 = []

dperm1.append("""
    XX-
""")

dperm1.append("""
    -XX
""")

dperm1.append("""
    X
    X
    -
""")

dperm1.append("""
    -
    X
    X
""")

destroyer.append(dperm1)

cruiser = []
crperm1 = []
crperm2 = []

crperm1.append("""
    XXX--
""")

crperm1.append("""
    --XXX
""")

crperm1.append("""
    X
    X
    X
    -
    -
""")

crperm1.append("""
    -
    -
    X
    X
    X
""")

crperm2.append("""
    -XXX-
""")

crperm2.append("""
    -
    X
    X
    X
    -
""")

cruiser.append(crperm1)
cruiser.append(crperm2)

submarine = []
sbperm1 = [] #sb initial used instead of s cause...
sbperm2 = []

sbperm1.append("""
    XXX--
""")

sbperm1.append("""
    --XXX
""")

sbperm1.append("""
    X
    X
    X
    -
    -
""")

sbperm1.append("""
    -
    -
    X
    X
    X
""")

sbperm2.append("""
    -XXX-
""")

sbperm2.append("""
    -
    X
    X
    X
    -
""")

submarine.append(sbperm1)
submarine.append(sbperm2)

battleship = []
bperm1 = []
bperm2 = []

bperm1.append("""
    ---XXXX
""")

bperm1.append("""
    XXXX---
""")

bperm1.append("""
    X
    X
    X
    X
    -
    -
    -
""")

bperm1.append("""
    -
    -
    -
    X
    X
    X
    X
""")

bperm2.append("""
    --XXXX-
""")

bperm2.append("""
    -XXXX--
""")

bperm2.append("""
    -
    X
    X
    X
    X
    -
    -
""")

bperm2.append("""
    -
    -
    X
    X
    X
    X
    -
""")

battleship.append(sbperm1)
battleship.append(sbperm2)


carrier = []
caperm1 = []
caperm2 = []
caperm3 = []

caperm1.append("""
    ----XXXXX
""")

caperm1.append("""
    XXXXX----
""")

caperm1.append("""
    X
    X
    X
    X
    X
    -
    -
    -
    -
""")

caperm1.append("""
    -
    -
    -
    -
    X
    X
    X
    X
    X
""")

caperm2.append("""
    ---XXXXX-
""")

caperm2.append("""
    -XXXXX---
""")

caperm2.append("""
    -
    X
    X
    X
    X
    X
    -
    -
    -
""")

caperm2.append("""
    -
    -
    -
    X
    X
    X
    X
    X
    -
""")

caperm3.append("""
    --XXXXX--
""")

caperm3.append("""
    -
    -
    X
    X
    X
    X
    X
    -
    -
""")

carrier.append(caperm1)
carrier.append(caperm2)
carrier.append(caperm3)


def usableShip(ship):
    x = ship.strip()
    
    #for y in x.split("\n"):
        

SHIPS = {
    "destroyer": destroyer,
    "submarine": submarine,
    "cruiser": cruiser,
    "battleship": battleship,
    "carrier": carrier
}