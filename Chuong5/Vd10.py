m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

matran = []
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input(f"Nhập phần tử [{i}][{j}]: "))
        hang.append(x)
    matran.append(hang)

f = open("C:/matran.txt", "w")
for hang in matran:
    for j in range(len(hang)):
        if j < len(hang) - 1:
            f.write(str(hang[j]) + " ")
        else:
            f.write(str(hang[j]))
    f.write("\n")
f.close()
print("Đã ghi vào C:/matran.txt")
