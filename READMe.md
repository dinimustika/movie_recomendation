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

### Visualisasi Data

![image](https://user-images.githubusercontent.com/73211764/191458593-3fe7df41-bc03-44a8-bc67-69c9047fc86a.png) <br>
Gambar 1. Distribusi genres <br>

Dari Gambar 1. tersebut dapat disimpulkan bahwa:
- Genre Comedy adalah genre utama film kebanyakan
- Dalam 5 besar data genre terbanyak, Biography menempati urutan ke 5


## Data Preparation

1. Menduplikasi dataset `data_movies` kedalam dataframe `df_cad`, sehingga dataset original tidak berubah dan dapat digunakan saat terdapat kesalahan atau keinginan mengembangkannya dilain kesempatan
2. Exploratory Data Analysis <br>
Untuk melakukan proses investigasi awal pada data untuk menganalisis karakteristik, menemukan pola, anomali, dan memeriksa asumsi pada data, saya menggunakan EDA. 
- Mengetahui keadaan deskriptif dari dataset <br>
Untuk menunjukkan keadaan deskriptif dari data, saya menggunakan fungsi describe() yang dapat mengembalikan nilai meliputi nilai *count*, mean, *standard deviation*, quantil data dan lain sebagainya <br>

|       	| year        	| score       	| votes        	| budget       	| gross        	| runtime     	|
|-------	|-------------	|-------------	|--------------	|--------------	|--------------	|-------------	|
| count 	| 7668.000000 	| 7665.000000 	| 7.665000e+03 	| 5.497000e+03 	| 7.479000e+03 	| 7664.000000 	|
| mean  	| 2000.405451 	| 6.390411    	| 8.810850e+04 	| 3.558988e+07 	| 7.850054e+07 	| 107.261613  	|
| std   	| 11.153508   	| 0.968842    	| 1.633238e+05 	| 4.145730e+07 	| 1.657251e+08 	| 18.581247   	|
| min   	| 1980.000000 	| 1.900000    	| 7.000000e+00 	| 3.000000e+03 	| 3.090000e+02 	| 55.000000   	|
| 25%   	| 1991.000000 	| 5.800000    	| 9.100000e+03 	| 1.000000e+07 	| 4.532056e+06 	| 95.000000   	|
| 50%   	| 2000.000000 	| 6.500000    	| 3.300000e+04 	| 2.050000e+07 	| 2.020576e+07 	| 104.000000  	|
| 75%   	| 2010.000000 	| 7.100000    	| 9.300000e+04 	| 4.500000e+07 	| 7.601669e+07 	| 116.000000  	|
| max   	| 2020.000000 	| 9.300000    	| 2.400000e+06 	| 3.560000e+08 	| 2.847246e+09 	| 366.000000  	|

- Menangani *Missing values* <br>
Untuk menunjukkan apakah terdapat missing value didalam dataset, saya menggunakan fungsi bawaan yang dimiliki oleh *pandas* library. Pada bagian ini saya menggunakan fungsi dropna() untuk menghilangkan data yang kosong.

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
|   | name                      | genre     | score | company              |
|---|---------------------------|-----------|-------|----------------------|
| 0 | Shanghai Surprise         | Adventure | 3.2   | HandMade Films       |
| 1 | Dunston Checks In         | Adventure | 5.4   | Joe Wizan/Todd Black |
| 2 | Stand by Me               | Adventure | 8.1   | Columbia Pictures    |
| 3 | Robin Hood: Men in Tights | Adventure | 6.7   | Brooksfilms          |
| 4 | Black Beauty              | Adventure | 6.6   | Warner Bros.         |


## Evaluation
Pada tahap evaluasi, saya akan menggunakan metrics Precision. Precision adalah sebuah metrics yang digunakan untuk mengukur berapa jumlah prediksi benar yang telah dibuat.
![image](https://user-images.githubusercontent.com/73211764/191462294-86b0daab-8b99-4437-8b25-c6ed30068c01.png)<br>
Gambar 2. Rumus precision <br>
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

Adventure: 100.0

Hasil tersebut menunjukkan bahwa ketepatan model berada diangka 100, dan menunjukkan bahwa model sudah baik.

Referensi: <br>
[1] IBM Cloud. "Exploratory Data Analysis". Diakses pada 20 September 2022. <br>
[2] Scikit-learn Documentation. Tersedia: tautan. Diakses pada: 20 September 2022. <br>
[3] Vajjala, Sowrnya, et al. "Practical Natural Language Processing". O'Reilly Media. 2020.  <br>
[4] Scikit-learn Documentation. "TfidfVectorizer". Diakses 20 September 2022 <br>
