def alternatingCharacters(s):
    # Write your code here
    deletions = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            deletions += 1
    return deletions


# Test Cases
print(alternatingCharacters("AABAAB"))  # Output: 2
print(alternatingCharacters("ABABAB"))  # Output: 0
print(alternatingCharacters("AAAAA"))  # Output: 4
print(alternatingCharacters("AB" * 50000000))  # Output: 0 (สำหรับสตริงยาว)
print(alternatingCharacters("A"))  # Output: 0
print(alternatingCharacters("aaaaa"))  # Output: 4 (กรณีสตริงมีตัวอักษรซ้ำกันทั้งหมด)
print(alternatingCharacters("abcdef"))  # Output: 0 (กรณีสตริงไม่มีตัวอักษรซ้ำกันเลย)
