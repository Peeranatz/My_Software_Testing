def gridChallenge(grid):
    # Write your code here
    grid = ["".join(sorted(row)) for row in grid]

    for col in range(len(grid[0])):
        for row in range(1, len(grid)):
            if grid[row][col] < grid[row - 1][col]:
                return "NO"

    return "YES"
