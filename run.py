from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
from Coordinate import Coordinate
import Ship

E = Encoding()

#   Constants
DIM = 10

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


@proposition(E)  # Coordinate is a hit
class Hit(Coordinate):

    def __repr__(self) -> str:
        return repr(f"({self.x}, {self.y}) is a hit!")


@proposition(E)  # Coordinate is a miss/out-of-bounds
class Miss(Coordinate):

    def __repr__(self) -> str:
        return repr(f"({self.x}, {self.y}) is a miss.")


@constraint.implies_all(E, right=D)  # Destroyer(origin, config_num) -> D (if ship is here, then ship must be active)
@proposition(E)  # Destroyer occupies point (x, y) - 4 available permutations
class Destroyer(Ship):

    def __init__(self, origin, config_num):
        self.origin = origin
        if config_num in range(0, 4):
            self.config_num = config_num

            i = self.origin.x
            j = self.origin.y
            # Permutations 1 - 4 Constraints - If permutation exists, then nearby squares are also occupied.
            if self.config_num == 0:
                c1 = Coordinate(i, j)
                c2 = Coordinate(i+1, j)
                constraint.implies_all(Hit(c), Hit(c2))
                #   -
                # - X x
                #   -
            elif self.config_num == 1:
                c1 = Coordinate(i, j)
                c2 = Coordinate(i-1, j)
                constraint.implies_all(Hit(c1), Hit(c2))
                #   -
                # x X -
                #   -
            elif self.config_num == 2:
                c1 = Coordinate(i, j)
                c2 = Coordinate(i, j+1)
                constraint.implies_all(Hit(c1), Hit(c2))
                #   -
                # - X -
                #   x
            elif self.config_num == 3:
                c1 = Coordinate(i, j)
                c2 = Coordinate(i, j-1)
                constraint.implies_all(Hit(c1), Hit(c2))
                #   x
                # - X -
                #   -

        else:
            raise ValueError(f"{config_num} not a valid permutation!")

    def __repr__(self) -> str:
        return repr(f"Ship: Destroyer \nPermutation #: {self.config_num} \n Anchor Point: ({repr(self.origin)})")


@constraint.implies_all(E, right=Cr)  # Cruiser(origin, config_num) -> Cr (if ship is here, then ship must be active)
@proposition(E)  # Cruiser occupies point (x, y) - 6 available permutations
class Cruiser(Ship):

    def __init__(self, origin, config_num):
        self.origin = origin
        if config_num in range(0, 6):
            self.config_num = config_num

            i = self.origin.x
            j = self.origin.y
            # Permutations 1 - 6 Constraints - If permutation exists, then nearby squares are also occupied.
            c1 = Coordinate(i, j)
            c2 = Coordinate(i+1, j)
            c3 = Coordinate(i+2, j)
            c4 = Coordinate(i-1, j)
            c5 = Coordinate(i-2, j)
            c6 = Coordinate(i, j-1)
            c7 = Coordinate(i, j-2)
            c8 = Coordinate(i, j+1)
            c9 = Coordinate(i, j+2)
            if self.config_num == 0:
                constraint.implies_all(Hit(c1), Hit(c2), Hit(c3))
                #     -
                #     -
                # - - X x x
                #     -
                #     -
            elif self.config_num == 1:
                constraint.implies_all(Hit(c1), Hit(c4), Hit(c2))
                #     -
                #     -
                # - x X x -
                #     -
                #     -
            elif self.config_num == 2:
                constraint.implies_all(Hit(c1), Hit(c5), Hit(c4))
                #     -
                #     -
                # x x X - -
                #     -
                #     -
            elif self.config_num == 3:
                constraint.implies_all(Hit(c1), Hit(c6), Hit(c7))
                #     -
                #     -
                # - - X - -
                #     x
                #     x
            elif self.config_num == 4:
                constraint.implies_all(Hit(c1), Hit(c6), Hit(c8))
                #     -
                #     x
                # - - X - -
                #     x
                #     -
            elif self.config_num == 3:
                constraint.implies_all(Hit(c1), Hit(c8), Hit(c9))
                #     x
                #     x
                # - - X - -
                #     -
                #     -

        else:
            raise ValueError(f"{config_num} not a valid permutation!")

    def __repr__(self) -> str:
        return repr(f"Ship: Cruiser \nPermutation #: {self.config_num} \n Anchor Point: ({repr(self.origin)})")


@constraint.implies_all(E, right=S)  # Submarine(origin, config_num) -> S (if ship is here, then ship must be active)
@proposition(E)  # Submarine occupies point (x, y) - 6 available permutations
class Submarine(Ship):

    def __init__(self, origin, config_num):
        self.origin = origin
        if config_num in range(0, 6):
            self.config_num = config_num

            i = self.origin.x
            j = self.origin.y
            # Permutations 1 - 6 Constraints - If permutation exists, then nearby squares are also occupied.
            c1 = Coordinate(i, j)
            c2 = Coordinate(i+1, j)
            c3 = Coordinate(i+2, j)
            c4 = Coordinate(i-1, j)
            c5 = Coordinate(i-2, j)
            c6 = Coordinate(i, j+1)
            c7 = Coordinate(i, j+2)
            c8 = Coordinate(i, j-1)
            c9 = Coordinate(i, j-2)
            if self.config_num == 0:
                constraint.implies_all(Hit(c1), Hit(c2), Hit(c3))
                #     -
                #     -
                # - - X x x
                #     -
                #     -
            elif self.config_num == 1:
                constraint.implies_all(Hit(c1), Hit(c4), Hit(c2))
                #     -
                #     -
                # - x X x -
                #     -
                #     -
            elif self.config_num == 2:
                constraint.implies_all(Hit(c1), Hit(c5), Hit(c4))
                #     -
                #     -
                # x x X - -
                #     -
                #     -
            elif self.config_num == 3:
                constraint.implies_all(Hit(c1), Hit(c8), Hit(c9))
                #     -
                #     -
                # - - X - -
                #     x
                #     x
            elif self.config_num == 4:
                constraint.implies_all(Hit(c1), Hit(c6), Hit(c8))
                #     -
                #     x
                # - - X - -
                #     x
                #     -
            elif self.config_num == 3:
                constraint.implies_all(Hit(c1), Hit(c6), Hit(c7))
                #     x
                #     x
                # - - X - -
                #     -
                #     -


        else:
            raise ValueError(f"{config_num} not a valid permutation!")

    def __repr__(self) -> str:
        return repr(f"Ship: Submarine \nPermutation #: {self.config_num} \n Anchor Point: ({repr(self.origin)})")


@constraint.implies_all(E, right=B)  # Battleship(origin, config_num) -> B (if ship is here, then ship must be active)
@proposition(E)  # Battleship occupies point (x, y) - 8 available permutations
class Battleship(Ship):

    def __init__(self, origin, config_num):
        self.origin = origin
        if config_num in range(0, 8):
            self.config_num = config_num

            i = self.origin.x
            j = self.origin.y
            # Permutations 1 - 8 Constraints - If permutation exists, then nearby squares are also occupied.
            c1 = Coordinate(i, j)
            c2 = Coordinate(i+1, j)
            c3 = Coordinate(i+2, j)
            c4 = Coordinate(i-1, j)
            c5 = Coordinate(i-2, j)
            c6 = Coordinate(i, j+1)
            c7 = Coordinate(i, j+2)
            c8 = Coordinate(i, j-1)
            c9 = Coordinate(i, j-2)
            c10 = Coordinate(i, j-3)
            c11 = Coordinate(i, j+3)
            c12 = Coordinate(i-3, j)
            c13 = Coordinate(i+3, j)
            if self.config_num == 0:
                constraint.implies_all(Hit(c1), Hit(c2), Hit(c3), Hit(c13))
                #       -
                #       -
                #       -
                # - - - X x x x
                #       -
                #       -
                #       -
            elif self.config_num == 1:
                constraint.implies_all(Hit(c1), Hit(c4), Hit(c2), Hit(c3))
                #       -
                #       -
                #       -
                # - - x X x x -
                #       -
                #       -
                #       -
            elif self.config_num == 2:
                constraint.implies_all(Hit(c1), Hit(c5), Hit(c4), Hit(c2))
                #       -
                #       -
                #       -
                # - x x X x - -
                #       -
                #       -
                #       -
            elif self.config_num == 3:
                constraint.implies_all(Hit(c1), Hit(c12), Hit(c5), Hit(c4))
                #       -
                #       -
                #       -
                # x x x X - - -
                #       -
                #       -
                #       -
            elif self.config_num == 4:
                constraint.implies_all(Hit(c1), Hit(c6), Hit(c7), Hit(c11))
                #       -
                #       -
                #       -
                # - - - X - - -
                #       x
                #       x
                #       x
            elif self.config_num == 5:
                constraint.implies_all(Hit(c1), Hit(c8), Hit(c6), Hit(c7))
                #       -
                #       -
                #       x
                # - - - X - - -
                #       x
                #       x
                #       -
            elif self.config_num == 6:
                constraint.implies_all(Hit(c1), Hit(c9), Hit(c8), Hit(c6))
                #       -
                #       x
                #       x
                # - - - X - - -
                #       x
                #       -
                #       -
            elif self.config_num == 7:
                constraint.implies_all(Hit(c1), Hit(c10), Hit(c9), Hit(c8))
                #       x
                #       x
                #       x
                # - - - X - - -
                #       -
                #       -
                #       -

        else:
            raise ValueError(f"{config_num} not a valid permutation!")

    def __repr__(self) -> str:
        return repr(f"Ship: Battleship \nPermutation #: {self.config_num} \n Anchor Point: ({repr(self.origin)})")


@constraint.implies_all(E, right=Ca)  # Carrier(origin, config_num) -> Ca (if ship is here, then ship must be active)
@proposition(E)  # Carrier occupies point (x, y) - 10 available permutations
class Carrier(Ship):

    def __init__(self, origin, config_num):
        self.origin = origin
        if config_num in range(0, 10):
            self.config_num = config_num

            i = self.origin.x
            j = self.origin.y
            # Permutations 1 - 10 Constraints - If permutation exists, then nearby squares are also occupied.
            c1 = Coordinate(i, j)
            c2 = Coordinate(i+1, j)
            c3 = Coordinate(i+2, j)
            c4 = Coordinate(i+3, j)
            c5 = Coordinate(i+4, j)
            c6 = Coordinate(i-1, j)
            c7 = Coordinate(i-2, j)
            c8 = Coordinate(i-3, j)
            c9 = Coordinate(i-4, j)
            c10 = Coordinate(i, j+1)
            c11 = Coordinate(i, j+2)
            c12 = Coordinate(i, j+3)
            c13 = Coordinate(i, j+4)
            c14 = Coordinate(i, j-1)
            c15 = Coordinate(i, j-2)
            c16 = Coordinate(i, j-3)
            c17 = Coordinate(i, j-4)
            if self.config_num == 0:
                constraint.implies_all(Hit(c1), Hit(c2), Hit(c3), Hit(c4), Hit(c5))
                #         -
                #         -
                #         -
                #         -
                # - - - - X x x x x
                #         -
                #         -
                #         -
                #         -
            elif self.config_num == 1:
                constraint.implies_all(Hit(c1), Hit(c6), Hit(c2), Hit(c3), Hit(c4))
                #         -
                #         -
                #         -
                #         -
                # - - - x X x x x -
                #         -
                #         -
                #         -
                #         -
            elif self.config_num == 2:
                constraint.implies_all(Hit(c1), Hit(c7), Hit(c6), Hit(c2), Hit(c3))
                #         -
                #         -
                #         -
                #         -
                # - - x x X x x - -
                #         -
                #         -
                #         -
                #         -
            elif self.config_num == 3:
                constraint.implies_all(Hit(c1), Hit(c8), Hit(c7), Hit(c6), Hit(c2))
                #         -
                #         -
                #         -
                #         -
                # - x x x X x - - -
                #         -
                #         -
                #         -
                #         -
            elif self.config_num == 4:
                constraint.implies_all(Hit(c1), Hit(c6), Hit(c7), Hit(c8), Hit(c9))
                #         -
                #         -
                #         -
                #         -
                # x x x x X - - - -
                #         -
                #         -
                #         -
                #         -
            elif self.config_num == 5:
                constraint.implies_all(Hit(c1), Hit(c10), Hit(c11), Hit(c12), Hit(c13))
                #         -
                #         -
                #         -
                #         -
                # - - - - X - - - -
                #         x
                #         x
                #         x
                #         x
            elif self.config_num == 6:
                constraint.implies_all(Hit(c1), Hit(c14), Hit(c10), Hit(c11), Hit(c12))
                #         -
                #         -
                #         -
                #         x
                # - - - - X - - - -
                #         x
                #         x
                #         x
                #         -
            elif self.config_num == 7:
                constraint.implies_all(Hit(c1), Hit(c15), Hit(c14), Hit(c10), Hit(c11))
                #         -
                #         -
                #         x
                #         x
                # - - - - X - - - -
                #         x
                #         x
                #         -
                #         -
            elif self.config_num == 8:
                constraint.implies_all(Hit(c1), Hit(c16), Hit(c15), Hit(c14), Hit(c10))
                #         -
                #         x
                #         x
                #         x
                # - - - - X - - - -
                #         x
                #         -
                #         -
                #         -
            elif self.config_num == 9:
                constraint.implies_all(Hit(c1), Hit(c17), Hit(c16), Hit(c15), Hit(c14))
                #         x
                #         x
                #         x
                #         x
                # - - - - X - - - -
                #         -
                #         -
                #         -
                #         -

        else:
            raise ValueError(f"{config_num} not a valid permutation!")

    def __repr__(self) -> str:
        return repr(f"Ship: Carrier \nPermutation #: {self.config_num} \n Anchor Point: ({repr(self.origin)})")

# Constraint - Ships cannot overlap; any point can only be occupied by one ship permutation.
for x in range(1, DIM + 1):
    for y in range(1, DIM + 1):
        coord = Coordinate(x, y);
        perms_list = []
        for i in range(0, 4):
            perms_list.append(Destroyer(coord, i))
        for i in range(0, 6):
            perms_list.append(Cruiser(coord, i))
        for i in range(0, 6):
            perms_list.append(Submarine(coord, i))
        for i in range(0, 8):
            perms_list.append(Battleship(coord, i))
        for i in range(0, 10):
            perms_list.append(Carrier(coord, i))
        constraint.add_exactly_one(E, *perms_list)


# Constraint - No point can be both a hit and a miss.
for x in range(1, DIM + 1):
    for y in range(1, DIM + 1):
        c = Coordinate (x, y)
        constraint.add(~(Hit(c) & Miss(c)))



@proposition(E)
class BasicPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"


# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
@proposition(E)
class FancyPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"


# Call your variables whatever you want
a = BasicPropositions("a")
b = BasicPropositions("b")
c = BasicPropositions("c")
d = BasicPropositions("d")
e = BasicPropositions("e")
# At least one of these will be true
x = FancyPropositions("x")
y = FancyPropositions("y")
z = FancyPropositions("z")


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    # Add custom constraints by creating formulas with the variables you created.
    E.add_constraint((a | b) & ~x)
    # Implication
    E.add_constraint(y >> z)
    # Negate a formula
    E.add_constraint((x & y).negate())
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    constraint.add_exactly_one(E, a, b, c)

    return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v, vn in zip([a, b, c, x, y, z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
