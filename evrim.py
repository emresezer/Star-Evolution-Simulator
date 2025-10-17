import matplotlib.pyplot as plt
print("🌟 Yıldız Evrimi Simülatörü")
print("---------------------------")
while True:
    try:
        mass = float(input("Yıldızın kütlesini girin (Güneş kütlesi cinsinden, M☉): "))
        if mass <= 0:
            print("Kütle sıfır veya negatif olamaz! Lütfen tekrar girin.")
            continue
        break
    except ValueError:
        print("Geçersiz giriş! Lütfen bir sayı girin.")
ana_kol_yillari = 1e10 * (mass ** -2.5)
kirmizi_dev_yillari = ana_kol_yillari * 0.1
if mass < 8:
    son_evre = "Beyaz Cüce"
elif mass < 20:
    son_evre = "Nötron Yıldızı"
else:
    son_evre = "Kara Delik"
evreler = ["Ana Kol", "Kırmızı Dev", "Son Evre"]
sureler = [ana_kol_yillari, kirmizi_dev_yillari, 1]
kumulatif = [0, ana_kol_yillari, ana_kol_yillari + kirmizi_dev_yillari]
print("\n🔭 Tahmini Yaşam Döngüsü:")
print(f"Ana Kol Evresi: {ana_kol_yillari:.2e} yıl")
print(f"Kırmızı Dev Evresi: {kirmizi_dev_yillari:.2e} yıl")
print(f"Son Evre: {son_evre}")
