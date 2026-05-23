a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

b_str = str(b)

min_digit = 9

for ch in b_str:
    so = int(ch)

    if so < min_digit and so != 0:
        min_digit = so

print("Chữ số nhỏ nhất của b là:", min_digit)

if a % min_digit == 0:
    print(a, "chia hết cho", min_digit)
else:
    print(a, "không chia hết cho", min_digit)