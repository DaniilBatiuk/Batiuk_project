# Task1

hat_list = [1, 2, 3, 4, 5]

new_number = int(input("Введіть ціле число для заміни середнього числа: "))
hat_list[2] = new_number

hat_list.pop()

print("Довжина списку:", len(hat_list))

print(hat_list)

# Task2

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

my_list = [64, 25, 12, 22, 11]
bubble_sort(my_list)

print("Відсортований список у порядку зростання:")
print(my_list)


# Task3


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print("The list with unique elements only:")
print(unique_list)


# Task4

chessboard = [['_'] * 8 for _ in range(8)]

chessboard[0][0] = 'R'
chessboard[0][7] = 'R'
chessboard[7][0] = 'R'
chessboard[7][7] = 'R'

for row in chessboard:
    print(' '.join(row))
    
    
# Контрольні запитання

list_1 = ["A","B","C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]
          
print(list_3)


list_1 = ["A","B","C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2
          
print(list_3)


list_1 = ["A","B","C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]
          
print(list_3)




list_1 = ["A","B","C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]
          
print(list_3)