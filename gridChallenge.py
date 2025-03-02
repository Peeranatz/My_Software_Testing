def gridChallenge(grid):
    # Write your code here
    grid = ["".join(sorted(row)) for row in grid]

    for col in range(len(grid[0])):
        for row in range(1, len(grid)):
            if grid[row][col] < grid[row - 1][col]:
                return "NO"

    return "YES"


# Test Cases
print(gridChallenge(["abc", "ade", "efg"]))  # Output: "YES"
print(gridChallenge(["abc", "def", "ade"]))  # Output: "NO"
print(gridChallenge(["a"]))  # Output: "YES"
print(gridChallenge(["abcd", "efgh", "ijkl", "mnop"]))  # Output: "YES"
print(gridChallenge(["aab", "bbc", "ccd"]))  # Output: "YES"
print(gridChallenge(["abc", "def", "ghi"]))  # Output: "YES"
print(gridChallenge(["a"]))  # Output: "YES" (กรณีกริดขนาด 1x1)
print(gridChallenge(["aab", "bbc", "ccd"]))  # Output: "YES" (กรณีกริดที่มีตัวอักษรซ้ำ)
