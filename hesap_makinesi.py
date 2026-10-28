def hesap_makinesi():
    print("--- Basit Hesap Makinesi ---")
    print("1. Toplama (+)")
    print("2. Çıkarma (-)")
    print("3. Çarpma (*)")
    print("4. Bölme (/)")
    
    secim = input("Yapmak istediğiniz işlemin numarasını seçin (1/2/3/4): ")
    
    if secim in ('1', '2', '3', '4'):
        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Geçersiz giriş! Lütfen bir sayı girin.")
            return

        if secim == '1':
            print(f"Sonuç: {sayi1} + {sayi2} = {sayi1 + sayi2}")
        elif secim == '2':
            print(f"Sonuç: {sayi1} - {sayi2} = {sayi1 - sayi2}")
        elif secim == '3':
            print(f"Sonuç: {sayi1} * {sayi2} = {sayi1 * sayi2}")
        elif secim == '4':
            if sayi2 != 0:
                print(f"Sonuç: {sayi1} / {sayi2} = {sayi1 / sayi2}")
            else:
                print("Hata: Bir sayı sıfıra bölünemez!")
    else:
        print("Geçersiz seçim! Lütfen 1, 2, 3 veya 4 girin.")

if __name__ == "__main__":
    hesap_makinesi()
