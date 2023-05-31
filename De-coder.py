def metni_desifrele(sifreli_metin, anahtar):
    desifrelenmis_metin = ""
    sifreli_karakterler = sifreli_metin.split()  # Şifrelenmiş metni boşluklardan ayırarak karakterlere bölelim
    for sifreli_karakter in sifreli_karakterler:
        sifreli_ascii_degeri = int(sifreli_karakter, 2)  # Binary değeri ASCII değerine dönüştürme
        ascii_degeri = sifreli_ascii_degeri - anahtar  # Anahtar değerini ASCII değerinden çıkarma
        karakter = chr(ascii_degeri)  # ASCII değerini karaktere dönüştürme
        desifrelenmis_metin += karakter  # Desifrelenmiş metine karakteri ekleme
    return desifrelenmis_metin

# Kullanıcıdan girişleri alma
sifreli_metin = input("Enter En-coded text: ")
anahtar = int(input("Enter the 'key': "))

# Şifreyi çözme işlemini gerçekleştirme ve sonucu yazdırma
desifrelenmis_metin = metni_desifrele(sifreli_metin, anahtar)
print("Çözülmüş Metin: ", desifrelenmis_metin)