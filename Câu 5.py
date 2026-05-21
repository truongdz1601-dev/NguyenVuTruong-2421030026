m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

# Tính tổng chữ số của n
tong = 0
tam = n
while tam > 0:
    tong = tong + tam % 10
    tam = tam // 10

print("Tổng chữ số của n =", tong)

if m % tong == 0:
    print(m, "chia hết cho", tong)
else:
    print(m, "không chia hết cho", tong)
