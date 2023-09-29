# Task1

n = int(input("Введіть число: "))

result = n >= 100

print(result)


# Task2

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

if num1 > num2:
    largest = num1
else:
    largest = num2

print("Найбільше число:", largest)


# Task3

input_str = input("Введіть рядок: ")

if input_str[0].isupper():
    print("Yes - Spathiphyllum is the best plant ever!")
elif input_str[0].islower():
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {input_str}!")
    
    
# Task4


income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = (income - 85528) * 0.32 + 14839.02

if tax < 0:
    tax = 0

rounded_tax = round(tax, 0)

print("The tax is:", rounded_tax, "thalers")


# Task5


year = int(input("Введіть номер року: "))

if year >= 1582:
    if (year % 4 != 0) or ((year % 100 == 0) and (year % 400 != 0)):
        print("Common year")
    else:
        print("Leap year")
else:
    print("Not within the Gregorian calendar period")
    
    
    
# Task6


secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    user_number = int(input("Введіть ціле число: "))
    
    if user_number == secret_number:
        print("Молодець, магле! Тепер ти вільний.")
        break
    else:
        print("Ха-ха! Ви застрягли у моїй петлі!")
        
        
         
# Task7   


import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")


# Task8


print("Введіть слово. Щоб вийти з циклу, введіть 'chupacabra'.")

while True:
    word = input("Введіть слово: ")

    if word == 'chupacabra':
        print("You've successfully left the loop.")
        break 

# Task9


user_word = input("Введіть слово: ")

user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)
    
    

# Task10


print("Введіть слово:")

user_word = input().upper()

word_without_vowels = ""

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter
    
print(word_without_vowels)



# Task11


blocks = int(input("Введіть кількість блоків: "))

height = 0
blocks_in_layer = 1

while blocks >= blocks_in_layer:
    height += 1
    blocks -= blocks_in_layer
    blocks_in_layer += 1

print("The height of the pyramid: " + str(height))


# Task12


c0 = int(input("Введіть натуральне число: "))

steps = 0

while c0 != 1:
    
    if steps != 0:
        print(c0)
    
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    
    steps += 1

print(c0)
print("steps:", steps)



# ## Контрольні запитання

x = 5
y = 10
z = 8

print(x > y)
print(y > z)



x, y, z = 5, 10, 8
print(x > z)
print((y - 5) == x)


x, y, z = 5, 10, 8
x, y, z = z, y, x
print(x > z)
print((y - 5) == x)

