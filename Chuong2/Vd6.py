toan = float(input("Nhập điểm toán: "))
ly   = float(input("Nhập điểm lý: "))
hoa  = float(input("Nhập điểm hóa: "))

tb = (toan + ly + hoa) / 3
print("Điểm trung bình:", round(tb, 2))

if tb < 5:
    print("Xếp loại: Yếu")
elif tb < 6.5:
    print("Xếp loại: Trung bình")
elif tb < 8:
    print("Xếp loại: Khá")
else:
    print("Xếp loại: Giỏi")
