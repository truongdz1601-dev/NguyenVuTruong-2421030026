a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
tong = a + b
print("Tổng a + b =", tong)

# Tìm chữ số lớn nhất trong tổng
lon_nhat = 0
tam = tong
while tam > 0:
    chu_so = tam % 10
    if chu_so > lon_nhat:
        lon_nhat = chu_so
    tam = tam // 10

print("Chữ số lớn nhất trong tổng:", lon_nhat)
