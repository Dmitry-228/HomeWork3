rows = int(input("Введите количество строк: ")) # задаем размерность массива
cols = int(input("Введите количество столбцов: "))
my_array = [[0] * cols for i in range(rows)] # создаем пустой массив заданной размерности
for i in range(rows): # заполняем массив значениями, вводимыми с клавиатуры
    for j in range(cols):
        my_array[i][j] = int(input(f"Введите значение для элемента [{i}][{j}]: "))
print(my_array)
for i in range(len(my_array)):
    for j in range(len(my_array[i])):
        if my_array[i] == my_array[j]:
          print("YES")
