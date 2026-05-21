n = int(input("nhap so phan tu n: "))
while n <= 0 or n > 100:
    n = int(input("nhap lai n(0<n<100): "))

tong = 0
dem = 0

for i in range(n):
    x = float(input("nhap phan tu thu " + str(i + 1) + ": "))
    if -100 < x < -10:
        tong += x
        dem += 1

if dem > 0:
    tbc = tong / dem
    print("Trung binh cong cac phan tu thoa man la: ", tbc)
else:
    print("khong co phan tu nao thoa man")