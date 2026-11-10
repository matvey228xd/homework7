n = int(input("Введіть число N: "))

total = 0

for number in range(2, n + 1):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        total += number

print(f"Сума простих чисел від 2 до {n}: {total}")