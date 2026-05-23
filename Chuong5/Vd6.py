m = int(input("nhap m: "))
n = int(input("nhap n: "))

tong = m + n

max_digit = 0
temp = tong

while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit 
    temp //= 10

print("tong = ", tong)
print("chu so lon nhat trong tong la: " , max_digit)