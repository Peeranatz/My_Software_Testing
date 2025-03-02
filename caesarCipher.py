def caesarCipher(s, k):
    # Write your code here
    result = []
    for char in s:
        if char.islower():
            result.append(chr((ord(char) - ord("a") + k) % 26 + ord("a")))
        elif char.isupper():
            result.append(chr((ord(char) - ord("A") + k) % 26 + ord("A")))
        else:
            result.append(char)
    return "".join(result)


# Test Cases
print(caesarCipher("middle-Outz", 2))  # Output: "okffng-Qwvb"
print(caesarCipher("abcXYZ", 26))  # Output: "abcXYZ"
print(caesarCipher("Hello-World", 0))  # Output: "Hello-World"
print(caesarCipher("123!@#", 10))  # Output: "123!@#"
print(caesarCipher("AbCdEfG", 4))  # Output: "EfGhIjK"
print(caesarCipher("Hello-World", 0))  # Output: "Hello-World" (กรณี k = 0)
print(caesarCipher("abcXYZ", 26))  # Output: "abcXYZ" (กรณี k = 26)
print(caesarCipher("123!@#", 10))  # Output: "123!@#" (กรณีสตริงมีสัญลักษณ์และตัวเลข)
