def funnyString(s):
    # Write your code here
    r = s[::-1]

    diff_s = [abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1)]

    diff_r = [abs(ord(r[i]) - ord(r[i + 1])) for i in range(len(r) - 1)]

    if diff_s == diff_r:
        return "Funny"
    else:
        return "Not Funny"


# Test Cases
print(funnyString("acxz"))  # Output: Funny
print(funnyString("bcxz"))  # Output: Not Funny
print(funnyString("ab"))  # Output: Funny (กรณีขอบเขต)
print(funnyString("a" * 10000))  # Output: "Funny"
print(funnyString("a"))  # Output: "Funny"
