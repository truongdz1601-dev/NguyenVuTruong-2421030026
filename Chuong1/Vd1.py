chuoi = input("Nhập chuỗi số cách nhau bởi dấu cách: ")
phan_tu = chuoi.split(" ")
danh_sach = []
tong = 0
for i in range(len(phan_tu)):
    so = int(phan_tu[i])
    danh_sach.append(so)
    tong = tong + so

print("List:", danh_sach)
print("Tổng:", tong)
