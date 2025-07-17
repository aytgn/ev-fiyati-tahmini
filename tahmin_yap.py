import joblib
import pandas as pd

# 1. Kayıtlı modeli dosyadan yükle
model_dosyasi = 'ev_fiyati_modeli.joblib'
yuklenen_model = joblib.load(model_dosyasi)
print(f"'{model_dosyasi}' dosyasından model yüklendi.")

# 2. Tahmin yapmak için YENİ ev verileri oluştur
yeni_evler_verisi = {
    'Metrekare': [140, 80, 210, 165],
    'OdaSayisi': [3, 2, 5, 4],
    'BinaYasi':  [1, 12, 0, 3]
}

# Veriyi pandas DataFrame'ine dönüştür
yeni_evler_df = pd.DataFrame(yeni_evler_verisi)
print("\nTahmin yapılacak yeni evlerin özellikleri:")
print(yeni_evler_df)

# 3. Fiyat tahminlerini yap
tahminler = yuklenen_model.predict(yeni_evler_df)

# 4. Sonuçları daha anlaşılır bir şekilde ekrana yazdır
print("\n--- TAHMİN SONUÇLARI ---")
for i in range(len(yeni_evler_df)):
    ev_ozellikleri = yeni_evler_df.iloc[i]
    tahmin_fiyat = tahminler[i]
    print(f"Ev {i+1} ({ev_ozellikleri['Metrekare']}m², {ev_ozellikleri['OdaSayisi']} oda, {ev_ozellikleri['BinaYasi']} yaş) -> Tahmini Fiyat: {tahmin_fiyat:.2f} TL")