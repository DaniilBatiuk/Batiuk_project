import math

#Task1

def gaussian_function(x, mu, sigma):
    exponent = -(x - mu) ** 2 / (2 * sigma ** 2)
    result = 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(exponent)
    return result

mu = 0
sigma = 1
x = 1.5

gaussian_value = gaussian_function(x, mu, sigma)

print(f"Значення функції Гауса для x = {x}, mu = {mu}, sigma = {sigma}: {gaussian_value}")

#Task2
john = 3
mary = 5
adam = 6

print(f"Джон: {john}, Мері: {mary}, Адам: {adam}")

total_apples = john + mary + adam

print("Загальна кількість яблук:", total_apples)

#Task3
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")


#Task4
x =  -1
x = float(x)
y = 3 * x ** 3 - 2 * x ** 2 + 3 ** x - 1
print("y =", y)


#Task6
a = float(input("Введіть значення для a: "))
b = float(input("Введіть значення для b: "))

if b == 0:
    print("Помилка: неможливо ділити на нуль.")
else:
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b

    print("Результат додавання:", addition)
    print("Результат віднімання:", subtraction)
    print("Результат множення:", multiplication)
    print("Результат ділення:", division)

print("\nThat's all, folks!")


#Task7 

x = float(input("Enter value for x: "))

y = 1 / (x + 1 / (x + 1 / (x + 1 / (x + 1 / x))))

print("y =", y)


#Task8

hour = int(input("Початковий час (години): "))
mins = int(input("Початковий час (хвилини): "))
dura = int(input("Тривалість події (хвилини): "))

end_hour = (hour + (mins + dura) // 60) % 24
end_mins = (mins + dura) % 60

print(f"Подія закінчується о {end_hour:02d}:{end_mins:02d}")