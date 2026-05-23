n = int(input("nhap n: "))

tong = 0

for i in range(n):
    x = int(input("nhap phan tu thu " + str(i+1) + ": "))

    if x % 2 == 0:
        tong = tong + x

print("tong cac phan tu chan la:", tong)

if tong % 7 == 0 and tong < 200:
    print("tong chia het cho 7 va nho hon 200")
else:
    print("tong khong thoa man dieu kien")