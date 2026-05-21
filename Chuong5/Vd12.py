n = int(input("Nhập n: "))
tong = 0
dem  = 0

for i in range(n):
    x = float(input(f"Nhập x{i+1}: "))
    if x < 0 and x > -1000 and x < -10:
        tong = tong + x
        dem  = dem  + 1

if dem > 0:
    print("Trung bình cộng =", tong / dem)
else:
    print("Không có phần tử nào thỏa mãn")
