n = int(input("Nhập số phần tử n: "))

tong = 0
dem = 0

for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))

    if -1000 < x < -10:
        tong += x
        dem += 1

if dem > 0:
    tbc = tong / dem
    print("Trung bình cộng =", tbc)
else:
    print("Không có phần tử thỏa mãn")