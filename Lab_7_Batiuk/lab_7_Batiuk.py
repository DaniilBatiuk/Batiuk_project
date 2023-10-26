#Task1 

numbers = input("Введіть числа, розділені пробілами: ").split()

numbers = [int(x) for x in numbers]

n = int(input("Введіть число n: "))

result = tuple(x for x in numbers if x < n)

print("Числа менше за", n, ":", result)


#Task2

tuple_of_strings = ('Рядок 1', 'Рядок 2', 'Рядок 3')

result_string = ', '.join(tuple_of_strings)

print(result_string)


#Task3


library = {
    'Книга 1': {
        'Автор': 'Автор 1',
        'Рік видання': 2020,
        'Кількість сторінок': 300
    },
    'Книга 2': {
        'Автор': 'Автор 2',
        'Рік видання': 2019,
        'Кількість сторінок': 250
    },
    'Книга 3': {
        'Автор': 'Автор 3',
        'Рік видання': 2021,
        'Кількість сторінок': 400
    }
}

book_title = input('Введіть назву книги: ')

if book_title in library:
    book_info = library[book_title]

    print(f"Інформація про книгу '{book_title}':")
    print(f"Автор: {book_info['Автор']}")
    print(f"Рік видання: {book_info['Рік видання']}")
    print(f"Кількість сторінок: {book_info['Кількість сторінок']}")
else:
    print(f"Книга '{book_title}' не знайдена в бібліотеці.")
    
    

#Task4


students = {
    "Петров": ("Іван", (4.5, 4.8, 4.2)),
    "Сидоров": ("Петро", (4.0, 4.1, 4.2)),
    "Іванов": ("Олена", (4.9, 4.8, 5.0)),
}

surname = input("Введіть прізвище студента: ")

if surname in students:
    student_info = students[surname]
    name, grades = student_info
    print(f"Ім'я: {name}")
    print(f"Прізвище: {surname}")
    print(f"Оцінки: {grades}")
else:
    print("Студент з таким прізвищем не знайдений.")
    
    
    
#Task5

phone_book = {
    "John": ["123-456-7890", "987-654-3210"],
    "Alice": ["555-555-5555"],
    "Bob": ["111-222-3333", "999-888-7777"],
}

def add_phone_number(contact_name, phone_number):
    if contact_name in phone_book:
        phone_book[contact_name].append(phone_number)
        print(f"Номер {phone_number} успішно додано до контакту {contact_name}.")
    else:
        print(f"Контакт з іменем {contact_name} не знайдений.")

add_phone_number("John", "777-888-9999")

print("Список номерів телефонів у телефонній книзі:")
for contact, phone_numbers in phone_book.items():
    print(f"{contact}: {', '.join(phone_numbers)}")
    
#Контрольні запитання

my_tuple = (1, 2, 3)
print(my_tuple[1:])

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.get('d', 4))


my_tuple = (1, 2, 3)
my_tuple[0] = 4
print(my_tuple)

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.update({'d': 4})
print(my_dict)