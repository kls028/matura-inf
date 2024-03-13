def is_palindrome(word):
    return word == word[::-1]

with open("dane.txt") as file:
    words = file.readlines()
    words = [x.strip() for x in words]
    palindromes = [x + "\n" for x in words if is_palindrome(x)]

with open("zadanie4.txt", "w") as file:
    file.writelines(palindromes)
