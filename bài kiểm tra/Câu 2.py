n = int(input("Nhập số nguyên dương n: "))

tong = 0
temp = n

while temp > 0:
    tong += temp % 10
    temp //= 10

print("Tổng chữ số =", tong)

if tong % 3 == 0:
    print("Tổng chữ số chia hết cho 3")
else:
    print("Tổng chữ số không chia hết cho 3")