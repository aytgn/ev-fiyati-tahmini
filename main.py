# 1. Kütüphaneleri İçeri Aktarma
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 2. Veriyi Yükleme ve Ayırma
veri_yolu = 'data/ev_veriseti.csv'
veri = pd.read_csv(veri_yolu)
X = veri.drop('Fiyat', axis=1) 
y = veri['Fiyat']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Modeli Oluşturma ve Eğitme
model = LinearRegression()
model.fit(X_train, y_train)
print("--- Model Eğitimi Tamamlandı ---")

# 4. Tahmin Yapma
y_pred = model.predict(X_test)
print("\n--- Model Tahminleri vs Gerçek Değerler ---")
# Tahminleri ve gerçek değerleri daha okunaklı göstermek için döngü kuralım
for i in range(len(y_test)):
    print(f"Gerçek Fiyat: {y_test.values[i]}, Tahmin Edilen Fiyat: {y_pred[i]:.2f}")


# 5. Model Performansını Değerlendirme
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("\n--- Model Performansı ---")
print("Ortalama Kareli Hata (MSE):", mse)
print("Karekök Ortalama Kareli Hata (RMSE):", rmse)
print(f"Modelimiz ev fiyatlarını ortalama olarak yaklaşık {rmse:.2f} TL hata ile tahmin etmektedir.")

# 6. Modeli Dosyaya Kaydetme
dosya_adi = 'ev_fiyati_modeli.joblib'
joblib.dump(model, dosya_adi)

print(f"\n--- Model Kaydedildi ---\nModel başarıyla '{dosya_adi}' olarak kaydedildi.")