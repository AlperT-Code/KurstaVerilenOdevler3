def rehber():
    kimlik_kodlari = [123, 456, 789, 101]
    telefonlar = ["555-1234", "555-5678", "555-8765", "555-4321"]

    while True:
        print("\nRehber Menüsü:")
        print("1. Kimlik kodlarına göre sırala")
        print("2. Telefon numaralarına göre sırala")
        print("3. Kimlik kodları ve telefonlarla listeyi görüntüle")
        print("4. Çıkış")
        
        secim = input("Bir seçenek girin (1-4): ")

        if secim == '1':
            kimlik_kodlari, telefonlar = zip(*sorted(zip(kimlik_kodlari, telefonlar)))
            print("Kimlik kodlarına göre sıralandı.")

        elif secim == '2':
            telefonlar, kimlik_kodlari = zip(*sorted(zip(telefonlar, kimlik_kodlari)))
            print("Telefon numaralarına göre sıralandı.")

        elif secim == '3':
            print("\nKimlik Kodu\tTelefon Numarası")
            for kod, telefon in zip(kimlik_kodlari, telefonlar):
                print(f"{kod}\t\t{telefon}")

        elif secim == '4':
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

rehber()
