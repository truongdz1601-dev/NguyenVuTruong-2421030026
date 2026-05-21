n = int(input("Nhập số phần tử: "))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử {i+1}: "))
    day_so.append(x)

f = open("C:/dulieu.txt", "w")
for so in day_so:
    f.write(str(so) + "\n")
f.close()
print("Đã ghi vào C:/dulieu.txt")
