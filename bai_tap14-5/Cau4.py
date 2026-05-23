m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

tong = m + n

print("Tổng =", tong)

tong_str = str(tong)

max_digit = 0

for ch in tong_str:
    so = int(ch)

    if so > max_digit:
        max_digit = so

print("Chữ số lớn nhất là:", max_digit)