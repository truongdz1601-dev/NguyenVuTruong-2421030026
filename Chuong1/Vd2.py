matran = ()
for i in range(4):
    hang = ()
    for j in range(3):
        x = int(input(f"Nhập phần tử [{i}][{j}]: "))
        hang = hang + (x,)
    matran = matran + (hang,)

print("Ma trận 4x3 dạng tuple:")
for hang in matran:
    print(hang)
