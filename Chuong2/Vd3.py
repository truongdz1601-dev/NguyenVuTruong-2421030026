a = int(input("Nhập số 1: "))
b = int(input("Nhập số 2: "))
c = int(input("Nhập số 3: "))

# Tìm max
lon_nhat = a
if b > lon_nhat:
    lon_nhat = b
if c > lon_nhat:
    lon_nhat = c

# Tìm min
nho_nhat = a
if b < nho_nhat:
    nho_nhat = b
if c < nho_nhat:
    nho_nhat = c

print("Max:", lon_nhat)
print("Min:", nho_nhat)
