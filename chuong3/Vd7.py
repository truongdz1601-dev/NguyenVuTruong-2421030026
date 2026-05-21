# Tạo file input.txt mẫu trước khi chạy
# Hàm kiểm tra số nguyên tố
def uoc_nguyen_to(n):
    uoc = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            uoc.append(i)
            n = n // i
        i = i + 1
    if n > 1:
        uoc.append(n)
    return uoc

f_in  = open("input.txt", "r")
f_out = open("output.txt", "w")

for dong in f_in:
    so = int(dong.strip())
    uoc = uoc_nguyen_to(so)
    f_out.write(str(uoc) + "\n")

f_in.close()
f_out.close()
print("Xong! Kết quả trong output.txt")
