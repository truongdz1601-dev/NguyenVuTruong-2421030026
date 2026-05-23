def la_so_nguyen_to(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

n = int(input("nhap n: "))
day = [int(input("nhap phan tu thu {i+1}: ")) for i in range(n)]

tong = sum(so for so in day if la_so_nguyen_to(so))
print("tong cac so nguyen to la: ", tong)

if tong % 2 != 0 and tong > 50:
    print("tong la so le va lon hon 50")
else:
    print("tong khong thoa man dieu kien")