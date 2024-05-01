def solve(nb_queens) -> bool :
    """nb_queens is the number of queens to place on a nb_queens x nb_queens board. If the function succeeds, then it
    returns the positions of the queens
    """
  
    def solve_rec(queen) -> bool:
        """this function tries to find a place for the queen "queen". If possible, it returns true, else it returns false.
        """
        nonlocal cols
        nonlocal diag1
        nonlocal diag2
        if queen==nb_queens:
            return True
        for c in range(1,nb_queens+1):
            # Impossible to place the queen in column c
            if c in cols or diag1[queen+c-1]==1 or diag2[queen-c+nb_queens]==1:continue

            #it is possible to place the queen on position c, try to place the other queens
            cols[queen]=c
            diag1[queen+c-1]=1
            diag2[queen-c+nb_queens]=1

            #the solver fails to place the other queens, so it will try the next position for the queen. But first, it should cancel the actions.
            if solve_rec(queen+1):return True
            cols[queen]=0
            diag1[queen+c-1]=0
            diag2[queen-c+nb_queens]=0
        return False
    
    cols=[0]*nb_queens
    diag1=[0]*(2*nb_queens-1)
    diag2=[0]*(2*nb_queens-1)
    if solve_rec(0):return cols
    else:return []

def display(cols):
    """this function pretty prints a solution
    """
    print("\n".join(["".join(["[X]" if i+1==c else "[ ]" for i in range(len(cols))]) for c in cols]))

# try different for the parameter and observe the performance.
display(solve(8))
