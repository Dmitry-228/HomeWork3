lst = []
for i in range(int(input())):
    lst.append(int(input()))
n = len(lst) #Переменная n присваивает длину списка A. 
last = lst[n-1] #Переменная last присваивает значение последнего элемента списка A. 
for i in range(n-1, 0, -1):
    lst[i] = lst[i-1]
lst[0] = last
print(lst)

# цикл for, который проходит по всем элементам списка A, начиная с индекса n-1 (предпоследний элемент списка)
# и заканчивая индексом 1 (второй элемент списка). 
# На каждой итерации текущий элемент списка A[i] заменяется на предыдущий элемент A[i-1].