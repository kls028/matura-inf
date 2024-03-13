def is_palindrome(word):
    return word == word[::-1]


with open("hasla.txt") as file:
    passwords = file.readlines()
    passwords = [x.strip() for x in passwords]

even_count = 0
odd_count = 0
palindromes = []
sum_220 = []
for password in passwords:
    length = len(password)
    if length % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if is_palindrome(password):
        palindromes.append(password + "\n")

    for i in range(length - 1):
        if ord(password[i]) + ord(password[i + 1]) == 220:
            sum_220.append(password + "\n")
            break

with open("wynik4a.txt", "w") as file:
    file.write("parzyste: " + str(even_count) + "\n")
    file.write("nieparzyste: " + str(odd_count) + "\n")

with open("wynik4b.txt", "w") as file:
    file.writelines(palindromes)

with open("wynik4c.txt", "w") as file:
    file.writelines(sum_220)
