n = int(input("Nhập số phần tử n: "))

tong = 0

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))

    if x % 2 == 0:
        tong += x

print("Tổng các phần tử chẵn =", tong)

if tong % 7 == 0 and tong < 200:
    print("Tổng chia hết cho 7 và nhỏ hơn 200")
else:
    print("Không thỏa mãn điều kiện")