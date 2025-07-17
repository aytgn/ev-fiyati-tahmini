# Ev Fiyatı Tahmin Modeli

Bu proje, temel makine öğrenmesi prensiplerini kullanarak ev özelliklerine göre fiyat tahmini yapan basit bir Lineer Regresyon modelini içerir. Bu belge, sıfırdan makine öğrenmesi öğrenme yolculuğunun bir parçası olarak oluşturulmuştur.

## Kurulum ve Çalıştırma

Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/aytgn/ev-fiyati-tahmini.git](https://github.com/aytgn/ev-fiyati-tahmini.git)
    ```
2.  **Proje Dizinine Gidin:**
    ```bash
    cd ev-fiyati-tahmini
    ```
3.  **Sanal Ortam Oluşturun ve Aktifleştirin (Windows):**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
4.  **Gerekli Kütüphaneleri Kurun:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Modeli Eğitin ve Kaydedin:**
    ```bash
    python main.py
    ```
6.  **Yeni Bir Tahmin Yapın:**
    ```bash
    python tahmin_yap.py
    ```

## Dosya Yapısı

-   `main.py`: Veriyi yükler, modeli eğitir, değerlendirir ve `ev_fiyati_modeli.joblib` olarak kaydeder.
-   `tahmin_yap.py`: Kayıtlı modeli yükleyerek yeni, örnek bir ev verisi için tahmin yapar.
-   `data/ev_veriseti.csv`: Modelin eğitimi için kullanılan örnek veri setidir.
-   `requirements.txt`: Projenin çalışması için gereken Python kütüphanelerini ve versiyonlarını listeler.
-   `.gitignore`: Git'in takip etmemesi gereken dosyaları belirtir.