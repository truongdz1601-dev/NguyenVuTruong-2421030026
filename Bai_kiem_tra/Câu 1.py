n = int(input("Nhập số phần tử n: "))

tong = 0
dem = 0

for i in range(n):
    x = float(input(f"Nhập x[{i}]: "))

    if 0 < x < 1000:
        tong += x
        dem += 1

if dem > 0:
    tbc = tong / dem
    print("Trung bình cộng =", tbc)
else:
    print("Không có phần tử phù hợp")
