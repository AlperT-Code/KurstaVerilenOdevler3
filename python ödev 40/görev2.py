def books():
    kitap_adlari = ["Kitap A", "Kitap B", "Kitap C", "Kitap D"]
    yayin_yillari = [2020, 2018, 2022, 2019]

    while True:
        print("\nBooks Menüsü:")
        print("1. Kitap adına göre sırala")
        print("2. Yayın yıllarına göre sırala")
        print("3. Kitaplar ve yayın yılları ile listeyi görüntüle")
        print("4. Çıkış")
        
        secim = input("Bir seçenek girin (1-4): ")

        if secim == '1':
            kitap_adlari, yayin_yillari = zip(*sorted(zip(kitap_adlari, yayin_yillari)))
            print("Kitap adına göre sıralandı.")

        elif secim == '2':
            yayin_yillari, kitap_adlari = zip(*sorted(zip(yayin_yillari, kitap_adlari)))
            print("Yayın yıllarına göre sıralandı.")

        elif secim == '3':
            print("\nKitap Adı\tYayın Yılı")
            for kitap, yil in zip(kitap_adlari, yayin_yillari):
                print(f"{kitap}\t\t{yil}")

        elif secim == '4':
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

books()
