
#İlk olarak sayıları yazalım.
tek_sayilar = []
cift_sayilar = []
for sayi in range(1, 5001):
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)
    else:
        tek_sayilar.append(sayi)
print("Tek Sayılar:",tek_sayilar)
print("Çift Sayılar:",cift_sayilar)


#Şimdi toplama işlemini yapalım.
tek_Toplam=0
cift_Toplam=0

for b in range(1,5001):
    if b%2==0:
        cift_Toplam=b+cift_Toplam

    else:
        tek_Toplam=b+tek_Toplam

print("1 ile 5000 Arasındaki Tek Sayıların Toplamı:",tek_Toplam,"dır.")
print("1 ile 5000 arasındaki çift sayıların toplamı:",cift_Toplam,"dır.")




