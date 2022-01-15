def traverse(grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return []
    ROW = len(grid)
    COL = len(grid[0])
    print('Number of Rows: ' + str(ROW))
    print('Number of Columns: ' + str(COL))
    result = []
    for ri in range(ROW+COL-1):
        if ri < COL:
            row = 0
        else:
            row = ri - (COL - 1)

        if ri < COL:
            col = ri
        else:
            col = COL - 1

        while row < ROW and col > -1:
            result.append(grid[row][col])
            row += 1
            col -= 1
    return result

grid = [[i+j for i in range(5)] for j in range(4)]
grid[0][1] = 20
grid[0][2] = 22
grid[1][2] = 10
grid[2][3] = 5
grid[3][3] = 2
grid[3][4] = 1
print("[")
for r in grid:
    print("\t"+str(r))
print("]")

print(traverse(grid))

