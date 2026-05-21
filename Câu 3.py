n = int(input("Nhập n: "))
tich = 1
tam = n
while tam > 0:
    tich = tich * (tam % 10)
    tam = tam // 10

if tich % 2 == 0 and tich > 20:
    print("Tích chữ số =", tich, "=> Là số chẵn và lớn hơn 20")
else:
    print("Tích chữ số =", tich, "=> Không thỏa mãn")
