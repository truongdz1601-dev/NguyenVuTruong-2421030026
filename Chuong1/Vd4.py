#Ví dụ dùng while tính tổng từ 1 đến n
n = int(input("Nhập n: "))

i = 1
tong = 0

while i <= n:
    tong = tong + i
    i = i + 1

print("Tổng từ 1 đến", n, "là:", tong)