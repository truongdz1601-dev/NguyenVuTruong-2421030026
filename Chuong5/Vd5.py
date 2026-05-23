a = int(input("nhap a: "))
b = int(input("nhap b: "))

temp = b
min_cs = 9

while temp > 0:
    cs = temp % 10

    if cs < min_cs and cs != 0:
        min_cs = cs

    temp = temp // 10

print("chu so nho nhat cua b la: ", min_cs)

if a % min_cs == 0:
    print(a, "chia het cho ", min_cs)
else:
    print(a, "khong chia het cho ", min_cs)