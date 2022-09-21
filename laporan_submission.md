# Laporan Proyek Machine Learning - Dini Mustika
## Project Overview
Menonton film merupakan kegiatan yang amat populer akhir-akhir ini. Tidak terbatas hanya pada orang dewasa namun juga anak-anak dapat menikmatinya, dengan berbagai genre yang tersedia misalnya Drama, Horor, Thriller, Komedi dan lain sebagainya. Untuk meningkatkan user experience dalam menemukan film yang menarik dan yang sesuai dengan genre kesukaan pengguna, maka sistem rekomendasi adalah solusi brillian untuk diterapkan. Pengguna akan dapat menemukan film yang sesuai dengan mudah sesuai dengan preferensi pengguna.

## Business Understanding

### Problem Statements

- Bagaimana cara memberikan rekomendasi film dengan pendekatan _Content-Based Filtering_?

### Goals

- Mengetahui cara membangun sistem rekomendasi untuk rekomendasi film dengan pendekatan _Content-Based Filtering_

### Solution statements
Menggunakan pendekatan _Content-Based Filtering_ untuk memberikan rekomendasi judul film

## Data Understanding
Pada proyek kali ini, dataset yang digunakan adalah Movie Industry dataset yang didapatkan dari [Kaggle](https://www.kaggle.com/datasets/danielgrijalvas/movies). Dataset ini merupakan kumpulan data film _IMDb_ yang di-_scrape_ menggunakan Python. Memiliki sekitar 7000+ baris dan 9 kolom.

### Variabel-variabel pada Movie Industry dataset adalah sebagai berikut:
- `budget` : anggaran film. Beberapa film tidak memiliki ini, sehingga muncul sebagai 0
- `company`: perusahaan produksi
- `country`: negara asal
- `director`: sutradara
- `genre`: genre utama film.
- `gross`: pendapatan film
- `title`: nama film
- `rating`: rating film (R, PG, dll.)
- `released`: tanggal rilis (YYYY-MM-DD)
- `runtime`: durasi film
- `score`: peringkat pengguna IMDb
- `votes`: jumlah suara pengguna
- `star`: aktor/aktris utama
- `writer`: penulis film
- `year`: tahun rilis

### Exploratory Data Analysis
Untuk melakukan proses investigasi awal pada data untuk menganalisis karakteristik, menemukan pola, anomali, dan memeriksa asumsi pada data, saya menggunakan EDA. 
- Mengetahui keadaan deskriptif dari dataset <br>
Untuk menunjukkan keadaan deskriptif dari data, saya menggunakan fungsi describe() yang dapat mengembalikan nilai meliputi nilai *count*, mean, *standard deviation*, quantil data dan lain sebagainya <br>
![image](https://user-images.githubusercontent.com/73211764/191458118-c234e048-e1fa-4e71-b0e4-9be6e0bc2d8b.png)

- Menangani *Missing values* <br>
Untuk menunjukkan apakah terdapat missing value didalam dataset, saya menggunakan fungsi bawaan yang dimiliki oleh *pandas* library. Pada bagian ini saya menggunakan fungsi dropna() untuk menghilangkan data yang kosong.

### Visualisasi Data

![image](https://user-images.githubusercontent.com/73211764/191458593-3fe7df41-bc03-44a8-bc67-69c9047fc86a.png)

Dari bar tersebut dapat disimpulkan bahwa:
- Genre Comedy adalah genre utama film kebanyakan
- Dalam 5 besar data genre terbanyak, Biography menempati urutan ke 5


## Data Preparation

1. Menduplikasi dataset `data_movies` kedalam dataframe `df_cad`, sehingga dataset original tidak berubah dan dapat digunakan saat terdapat kesalahan atau keinginan mengembangkannya dilain kesempatan

## Modeling

Pada proyek sistem rekomendasi kali ini, saya menggunakan pendekatan _Content-Based Filtering_. Acuan yang akan digunakan adalah genre film.

1. ### TF-IDF Vectorizer <br>
Teknik ini digunakan untuk menemukan representasi dari nama genre film yang ada pada dataframe. Fungsi yang saya gunakan adalah tfidfvectorizer() dari library sklearn. <br>

2. ### Fit and Transform <br>
Tahapan ini dilakukan untuk mentransformasi data nama games yang ada menjadi matrix. Untuk menghitung derajat kesamaan (similarity degree) antar film, saya menggunakan teknik cosine similarity dengan fungsi cosine_similarity dari library sklearn. 

3. ### Argpartition <br>
Teknik ini mengambil data dengan similarity terbesar dari index yang ada. Kemudian melakukan penghapusan nama_movie agar nama movie yang dicari tidak muncul dalam daftar rekomendasi. 

4. ### Hasil <br>
Kemudian saya ingin mendapatkan rekomendasi berdasarkan judul film "The Blue Lagoon". Berikut adalah output yang tersedia
![image](https://user-images.githubusercontent.com/73211764/191462038-c85a9ea4-17ec-42ac-9fb3-a65509c295e7.png)


## Evaluation
Pada tahap evaluasi, saya akan menggunakan metrics Precision. Precision adalah sebuah metrics yang digunakan untuk mengukur berapa jumlah prediksi benar yang telah dibuat.
![image](https://user-images.githubusercontent.com/73211764/191462294-86b0daab-8b99-4437-8b25-c6ed30068c01.png)<br>
_Catatan_
TP – True Positives
FP – False Positives
Precision – Accuracy of positive predictions.
Precision = TP/(TP + FP)

- Kelebihan Precision
  - Sangat baik untuk klasifikasi
  - Dokumen yang dipilih secara acak dari kumpulan dokumen yang diambil adalah relevan.
  - Precision bagus untuk kasus di mana kelasnya seimbang
- Kekurangan Precision
  - Tidak baik untuk data yang *Imbalance*
  - hanya hasil teratas yang dikembalikan oleh sistem

Kemudian, hasil yang saya dapatkan adalah
```python
Adventure: 100.0
```

Referensi: <br>
[1] IBM Cloud. "Exploratory Data Analysis". Diakses pada 20 September 2022. <br>
[2] Scikit-learn Documentation. Tersedia: tautan. Diakses pada: 20 September 2022. <br>
[3] Vajjala, Sowrnya, et al. "Practical Natural Language Processing". O'Reilly Media. 2020.  <br>
[4] Scikit-learn Documentation. "TfidfVectorizer". Diakses 20 September 2022 <br>
