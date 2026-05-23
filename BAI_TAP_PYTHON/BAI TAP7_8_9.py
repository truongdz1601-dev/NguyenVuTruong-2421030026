# Câu 9
a = int(input("Nhap so nguyen duong a : "))
b = int(input("Nhap so nguyen duong b : "))
c = int(input("Nhap so nguyen duong c : "))
tong = a + b + c
print(F" Tổng {a} + {b} + {c} = {tong}")
dem_chan = 0
temp = tong 
while temp > 0:
    chu_so = temp % 10
    if chu_so % 2 == 0:
        dem_chan += 1
        temp //= 10

print(f" Trong tong co {dem_chan} chu so chan")




#Câu 8 
x = int(input("Nhap so nguyen duong x : "))
y = int(input("Nhap so nguyen duong y : "))
z = int(input("Nhap so nguyen duong z : "))
tich = x * y * z 
print(f"Tich {x} * {y} * {z} = {tich}")
so_chu_so = len(str(tich))
print(f"Tích có {so_chu_so} chu so")
chu_so_lon_nhat = 0 
temp = tich
while temp > 0:
    chu_so = temp % 10 
    if chu_so > chu_so_lon_nhat:
        chu_so_lon_nhat = chu_so
    temp //= 10

print(f"Chu so lon nhat trong tich la: {chu_so_lon_nhat}") 




#Câu 7
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhap so phan tu n (0 < n < 100): "))
while n <= 0 or n >= 100:
    n = int(input("Nhap lai n (0 < n < 100): "))
day_so = []
for i in range(n):
    x = int(input(f"Nhap phan tu thu {i+1}: "))
    day_so.append(x)
tong_nguyen_to = 0
for so in day_so:
    if la_so_nguyen_to(so):
        tong_nguyen_to += so

print(f"Tong cac so nguyen to: {tong_nguyen_to}")
if tong_nguyen_to % 2 != 0 and tong_nguyen_to > 50:
    print("Tong la so le va lon hon 50")
else:
    print("Tong KHONG thoa man dieu kien (so le va lon hon 50)")
