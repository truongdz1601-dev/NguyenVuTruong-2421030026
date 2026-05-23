#Đếm số nguyên tố trong đoạn từ 1 đến n
n = int(input("n = "))

for i in range(2, n + 1):

    ktra = 0
    t = 2

    while t < i:
        if i % t == 0:
            ktra = 1
        t = t + 1

    if ktra == 0:
        print(i, "là số nguyên tố")