import joblib
import pandas as pd

# 1. Kayıtlı modeli dosyadan yükle
model_dosyasi = 'ev_fiyati_modeli.joblib'
yuklenen_model = joblib.load(model_dosyasi)
print(f"'{model_dosyasi}' dosyasından model yüklendi.")

# 2. Tahmin yapmak için yeni bir ev verisi oluştur
# ÖNEMLİ: Veri, modelin eğitildiği formatla BİREBİR aynı olmalı.
# Yani aynı sütun adları ve aynı sırada olmalı.
yeni_ev_verisi = {
    'Metrekare': [140],  # Değerleri bir liste içinde verdiğimize dikkat edin
    'OdaSayisi': [3],
    'BinaYasi': [1]
}

# Veriyi pandas DataFrame'ine dönüştür
yeni_ev_df = pd.DataFrame(yeni_ev_verisi)
print("\nTahmin yapılacak yeni ev özellikleri:")
print(yeni_ev_df)

# 3. Fiyat tahmini yap
# .predict() metodu her zaman bir liste/dizi döndürür.
# Tek bir tahmin yaptığımız için sonucun ilk elemanını ([0]) alıyoruz.
tahmin_edilen_fiyat = yuklenen_model.predict(yeni_ev_df)[0]

# 4. Sonucu ekrana yazdır
print("\n--- TAHMİN SONUCU ---")
print(f"Bu özelliklerdeki bir evin tahmini fiyatı: {tahmin_edilen_fiyat:.2f} TL")