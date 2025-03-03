metin = input("Bir metin gir: ")
cumleler = [cumle.strip() for cumle in metin.replace("!",".").replace("?",".").split(".") if cumle.strip()]
print(f"Cümle sayısı: {len(cumleler)}")
