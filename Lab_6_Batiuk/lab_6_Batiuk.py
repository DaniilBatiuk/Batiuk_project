# Task1

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
        
        
        
# Task2


def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month < 1 or month > 12:
        return None

    if month == 2 and is_year_leap(year):
        return 29

    return month_lengths[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")





# Task3


def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month < 1 or month > 12:
        return None

    if month == 2 and is_year_leap(year):
        return 29

    return month_lengths[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None

    day_count = day

    for m in range(1, month):
        day_count += days_in_month(year, m)

    return day_count

print(day_of_year(2000, 12, 31))
print(day_of_year(2023, 9, 29))
print(day_of_year(2023, 13, 1))
print(day_of_year(2023, 2, 30))




# Task4



def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


# Task5


def liters_100km_to_miles_gallon(liters_per_100km):
    miles_per_gallon = 100 / (liters_per_100km / 3.785411784)
    return miles_per_gallon/1.609344

def miles_gallon_to_liters_100km(miles_per_gallon):
    liters_per_100km = 100 / (miles_per_gallon * 1.609344)
    return liters_per_100km * 3.785411784

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))



# Task6

def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

print(is_a_triangle(3, 4, 5))
print(is_a_triangle(1, 2, 4))



# Task7


def is_a_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    return a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2

print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(5, 12, 13))
print(is_a_right_triangle(1, 2, 3))



# Контрольні запитання

def message(): 
    alt = 1
    print("Hello, World!")

print(alt)


a = 1

def fun(): 
    a = 2
    print(a)

fun()
print(a)


a = 1

def fun():
    global a
    a = 2
    print(a)

fun()
a = 3
print(a)


a = 1

def fun():
    global a
    a = 2
    print(a)

a = 3
fun()
print(a)