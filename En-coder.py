def metni_sifrele(metin, anahtar):
    sifrelenmis_metin = ""
    for karakter in metin:
        ascii_degeri = ord(karakter)  # Karakterin ASCII değerini bulma
        sifreli_ascii_degeri = ascii_degeri + anahtar  # Anahtar ile ASCII değerini toplama
        sifreli_binary = bin(sifreli_ascii_degeri)[2:]  # ASCII değerini binary'e dönüştürme
        sifrelenmis_metin += sifreli_binary + " "  # Sifrelenmis metine binary değerini ekleme
    return sifrelenmis_metin.strip()  # Sondaki fazladan boşluğu kaldırma

metin = input("Enter text: ")
anahtar = int(input("Enter key: "))

# Şifreleme işlemini gerçekleştirme ve sonucu yazdırma
sifrelenmis_metin = metni_sifrele(metin, anahtar)
print("Şifrelenmiş Metin: ", sifrelenmis_metin)