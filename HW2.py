numbers = [0]
n = int(input())

def morsa_ty():
    count = 0
    while count < n:
        count += 1
        for i in range(len(numbers)):
            if n == len(numbers):
                return numbers
            if numbers[i] == 0: #если 0, то добавляем 1 в конец
                numbers.append(1)
            else:             #если 1, то добавляем 0 в конец
                numbers.append(0)
    return numbers

print(*morsa_ty())