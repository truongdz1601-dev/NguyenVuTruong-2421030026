print("Các mã dân tộc:")
print("1 - Kinh")
print("2 - Tày")
print("3 - Thái")
print("4 - Mường")
print("5 - Khác")

ma = int(input("Nhập mã dân tộc: "))
if ma == 1:
    print("Dân tộc: Kinh")
elif ma == 2:
    print("Dân tộc: Tày")
elif ma == 3:
    print("Dân tộc: Thái")
elif ma == 4:
    print("Dân tộc: Mường")
else:
    print("Dân tộc: Khác")
