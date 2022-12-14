# -*- coding: utf-8 -*-
"""movie_recomendation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18r8-ahQOXHULMMtWgPvUJv-iALPDerBE

Pertama-tama, karena menggunakan dataset kaggle, maka harus mengupload kaggle.json berisi username akun kaggle. Untuk keamanan data tersebut, dapat menggunakan chmod 600

---
"""

from google.colab import files
!pip install -q kaggle
files.upload()
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 /root/.kaggle/kaggle.json

"""Masuk kedalam direktori yang kita kehendaki untuk mendownload dataset tersebut

---

"""

import os

os.chdir("/content/drive/MyDrive/recomendation")

"""Mendownload dataset yang diinginkan dan melakukan unzip data tersebut

---
"""

!kaggle datasets download -d danielgrijalvas/movies --unzip

"""Melakukan import library yang dibutuhkan dan melakukan load data csv yang telah di download

---
"""

import pandas as pd
data_movies=pd.read_csv('/content/drive/MyDrive/recomendation/movies.csv')

"""Mengetahui tipe data dalam data frame"""

data_movies.info()

"""Mengetahui keadaan deskripitif data"""

data_movies.describe()

"""Mengecek isi data 2 teratas

---
"""

data_movies.head(2)

"""Melakukan drop column yang tidak dibutuhkan

---
"""

data_movies.drop(
    labels = ['year','released','votes','budget','gross','runtime'],
    axis=1,
    inplace=True
)

"""Menginisiasi data kedalam variable baru untuk mengantisipasi apabila ada kesalahan

---
"""

df_cad = data_movies
df_cad

"""Mengecek apakah terdapat null values di dalam dataframe

---
"""

df_cad.isnull().sum()

"""Menghilangkan missing data pada dataframe

---
"""

df_cad.dropna()

import seaborn as sns
import matplotlib.pyplot as plt
title = "Film Genres"
count = df_cad["genre"].value_counts()
count = count.sort_values().tail(5)
percent = 100*df_cad["genre"].value_counts(normalize=True)
count.plot(kind='barh', title=title, figsize=(10,6), color = "#4CAF50");

"""Melakukan inisiasi TfidfVectorizer() <br> Teknik ini digunakan untuk menemukan representasi dari nama genre film yang ada pada dataframe

---
"""

from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer()
tf.fit(df_cad['genre']) 
tf.get_feature_names()

"""Tahapan ini dilakukan untuk mentransformasi data nama genres yang ada menjadi matrix

---
"""

tfidf_matrix = tf.fit_transform(df_cad['genre']) 

tfidf_matrix.shape

"""Setelah mendapatkan bentuk matrix dari tahapan di atas, kemudian untuk menghasilkan vector dari tdidf menggunakan method todense()

---
"""

tfidf_matrix.todense()

"""Membuat data frame untuk melihat isi matrix tfidf dengan nama genre dengan nama film

---
"""

pd.DataFrame(
    tfidf_matrix.todense(), 
    columns=tf.get_feature_names(),
    index=df_cad.name
).sample(22, axis=1,replace=True).sample(10, axis=0,replace=True)

"""Menghitung derajat kesamaan (similarity degree) antar games dengan teknik cosine similarity.

---
"""

from sklearn.metrics.pairwise import cosine_similarity
 
# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix) 
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama resto
cosine_sim_df = pd.DataFrame(cosine_sim, index=df_cad['name'], columns=df_cad['name'])
print('Shape:', cosine_sim_df.shape)
 
# Melihat similarity matrix pada setiap resto
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""Membuat method untuk memberikan rekomendasi berdasarkan nama film

---
"""

def movie_recommendations(nama_movie, similarity_data=cosine_sim_df, items=df_cad[['name', 'genre','score','company']], k=5):
   
    index = similarity_data.loc[:,nama_movie].to_numpy().argpartition(
        range(-1, -k, -1))
    
    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    
    # Drop nama_movie agar nama movie yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama_movie, errors='ignore')
 
    return pd.DataFrame(closest).merge(items).head(k)

"""Menampilkan hasil rekomendasi berdasarkan content based filter

---
"""

genre_recomendation = movie_recommendations('The Blue Lagoon')
genre_recomendation

"""Membuat dataframe baru untuk menampung data dengan nama The Blue Lagoon

---
"""

genre_cad = df_cad[df_cad['name'] == 'The Blue Lagoon']

"""Menampung nama genre rekomendasi yang dikeluarkan program

---
"""

get_feature_genre=[]
for i in range(len(genre_cad.genre)):
    for x in genre_cad.genre.str.split(','):
        if x not in get_feature_genre:
            get_feature_genre.append(x)

"""Menghitung hasil presisi dari nama genre yang dikeluarkan oleh model

---
"""

for i in get_feature_genre[0]:
  print(i + ": " + str((
      (genre_recomendation['genre'].str.contains(i).count()/genre_recomendation['genre'].count())*100)
  ))