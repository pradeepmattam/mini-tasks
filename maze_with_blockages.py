
grid = [[0 for i in range(4)] for j in range(4)]
grid[1][1] = -1
grid[2][0] = -1

print("initial grid:\n[")
for row in grid:
    print(" "+str(row), end=",\n")
print("]")

def calculate_paths(grid,m,n):
    #if starting point is blocked, no path to the destination
    if grid[0][0] == -1:
        return 0
    #initializing the first row and column
    for i in range(m):
        if grid[i][0] != -1:
            grid[i][0] = 1
        else:
            break # no path after a blockage
    for j in range(n):
        if grid[0][j] != -1:
            grid[0][j] = 1
        else:
            break #no path after a blockage
    print("after row and column set: \n[")
    for row in grid:
        print(" "+str(row), end=",\n")
    print("]")
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == -1:
                continue
            # If we can reach grid[i][j] from grid[i-1][j] then increment the count.
            if grid[i-1][j] > 0:
                grid[i][j] = grid[i-1][j] + grid[i][j]
            # If we can reach grid[i][j] from grid[i][j-1] then increment the count.
            if grid[i][j-1] > 0:
                grid[i][j] = grid[i][j] + grid[i][j-1]
            print("on each column navigation: \n[")
            for row in grid:
                print(" "+str(row), end=",\n")
            print("]")
    if grid[m-1][n-1] > 0:
        return grid[m-1][n-1]
    else:
        return 0
print(f"paths {calculate_paths(grid, 4,4)}")
