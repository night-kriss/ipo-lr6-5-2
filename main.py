#Написать программу, которая:
#- Создает двумерную матрицу произвольного размера от 4 до 8 во высоте и ширине,
#заполненную значениями из списка **[-3, -5, -2, -12, 0, 15, 4, 7, 2]**
#- Выводит данную матрицу в форматированном виде. Пример:
#Выводит сумму всех элементов отрицательных 
import random
# Список значений
values = [-3, -5, -2, -12, 0, 15, 4, 7, 2]
# Генерация случайного размера матрицы от 4 до 8
rows = random.randint(4, 8)
cols = random.randint(4, 8)
# Создание матрицы
matrix = []
for _ in range(rows):
    row = []
    for _ in range(cols):
        row.append(random.choice(values))
    matrix.append(row)
# Вывод матрицы
for row in matrix:
    print(row)
     #Подсчет суммы всех отрицательных элементов
negative_sum = 0
for row in matrix:
    for element in row:
        if element < 0:
            negative_sum += element
print("\nСумма всех отрицательных элементов:", negative_sum)