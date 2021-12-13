
#Modify this later if we want tabulate
def visual(sol, DIM, all_perms, board):
    count = []
    for x in range(DIM):
        col = []
        for y in range(DIM):
            col.append(0)
        count.append(col)
        
    for perm in all_perms:
        if sol[perm]:
            count[perm.coord.y][perm.coord.x] += 1
    
    highest = 1
    best_tiles = []
    for y in range(DIM):
        for x in range(DIM):
            if count[y][x] > highest:
                highest = count[y][x]
                best_tiles.clear()
                best_tiles.append((x,y))
            elif count[y][x] == highest:
                best_tiles.append((x,y))

    for (x,y) in best_tiles:
        board[y][x] = "A"

    print("\nA : The suggested tile to attack.")
    print("0 : A tile with a resolved hit.")
    print("X : A tile with an unresolved hit.")
    print("- : Unattacked tile.")

    print("\n  ", end="")
    for x in range(DIM):
        print("", x, end=" ")
        if x == (DIM - 1):
            print("\n")

    for x in range(DIM):
        print(x, end="  ")
        for y in range(DIM):
            print(board[x][y] + " ", end=" ")
            if y == (DIM - 1):
                print("\n")
    
    #Uncomment the line below to see the amount of valid permutations that can exist on each tile
    #print(count)