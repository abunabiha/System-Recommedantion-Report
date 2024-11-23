# %% [markdown]
# ## Loading Data

# %%
# Import library yang diperlukan
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
def load_data(file_path):
    encodings = ['latin-1', 'iso-8859-1', 'cp1252']
    
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            print(f"Data berhasil dimuat dengan encoding: {encoding}")
            return df
        except:
            continue
    
    raise Exception("Gagal membaca file. Silakan periksa format file CSV Anda")

# Load data
df = load_data('data.csv')

# Tampilkan informasi dasar
print("\nInformasi Dataset:")
print(df.info())
print("\nSample Data:")
print(df.head())

# %% [markdown]
# Analisis Output:
# 1. Informasi Umum Dataset:
# - Total baris data: 541,909 entries
# - Memiliki 8 kolom (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country)
# - Menggunakan memori sebesar 33.1+ MB
# 2. Status Missing Values:
# - Description: memiliki 1,454 missing values (540,455 non-null dari 541,909)
# - CustomerID: memiliki 135,080 missing values (406,829 non-null dari 541,909)
# - Kolom lainnya terisi lengkap (541,909 non-null)
# 3. Tipe Data:
# - Object (string): InvoiceNo, StockCode, Description, InvoiceDate, Country
# - Integer: Quantity
# - Float: UnitPrice, CustomerID
# 4. Sample Data Menunjukkan:
# - Data transaksi retail dengan detail produk
# - Semua sampel dari pelanggan yang sama (CustomerID: 17850.0)
# - Semua transaksi dari United Kingdom
# - Tanggal transaksi sama (12/1/2010 8:26)
# - Harga produk berkisar antara £2.55 hingga £3.39

# %% [markdown]
# ## Data Preparation
# 
# Proses data preparation adalah langkah penting untuk memastikan bahwa data siap digunakan dalam analisis dan model rekomendasi. Berikut adalah langkah-langkah yang dilakukan secara berurutan:
# 
# 1. Loading Data
#     Data diload dari file CSV menggunakan berbagai encoding (latin-1, iso-8859-1, cp1252) untuk memastikan bahwa data dapat dibaca dengan benar. Ini penting untuk menghindari kesalahan dalam pembacaan data yang dapat menyebabkan hilangnya informasi.
# 2. Informasi Dataset
#     Setelah data dimuat, informasi dasar tentang dataset ditampilkan, termasuk jumlah total entri, kolom yang ada, dan tipe data masing-masing kolom. Ini membantu dalam memahami struktur data dan mengidentifikasi potensi masalah, seperti missing values.
# 3. Menghapus Spasi Berlebih pada Kolom String:
#     Pada tahap ini, spasi berlebih dihapus dari kolom string (seperti InvoiceNo, StockCode, Description, dan Country). Proses ini dilakukan untuk memastikan bahwa tidak ada kesalahan dalam pencocokan string yang dapat mempengaruhi analisis dan rekomendasi.
# 4. Konversi Format Tanggal
#     Kolom InvoiceDate yang awalnya dalam format string dikonversi menjadi format datetime. Ini penting untuk analisis waktu dan untuk memastikan bahwa operasi yang melibatkan tanggal dapat dilakukan dengan benar.
# 5. Penanganan Outlier
#     Data yang tidak valid, seperti transaksi dengan Quantity atau UnitPrice yang kurang dari atau sama dengan nol, dihapus. Ini dilakukan untuk memastikan bahwa hanya data yang valid yang digunakan dalam analisis dan model rekomendasi.
# 6. Pembuatan Pivot Tabel untuk Sistem Rekomendasi
#     Setelah data dibersihkan, pivot tabel dibuat untuk memudahkan analisis dan rekomendasi. Pivot tabel ini dapat digunakan untuk melihat interaksi antara pelanggan dan produk, yang sangat penting untuk model rekomendasi.
# 7. Status Missing Values
#     Setelah semua langkah di atas, status missing values diperiksa kembali. Semua kolom harus terisi lengkap tanpa missing values, memastikan bahwa data siap untuk analisis lebih lanjut.
# 

# %%
def clean_data(df):
    """
    Membersihkan data dari nilai tidak valid dan standardisasi format
    """
    print("Jumlah data awal:", len(df))
    
    # Copy dataframe
    df = df.copy()
    
    # Hapus spasi berlebih pada kolom string
    #spasi berlebih dihapus dari kolom string 
    # (seperti InvoiceNo, StockCode, Description, dan Country).
    
    string_columns = df.select_dtypes(include=['object']).columns
    for col in string_columns:
        df[col] = df[col].str.strip()
    
    # Filter data yang valid
    # Data yang tidak valid, seperti transaksi dengan Quantity atau 
    # UnitPrice yang kurang dari atau sama dengan nol, dihapus.
    
    df = df[
        (df['Quantity'] > 0) &  # Hapus quantity negatif
        (df['UnitPrice'] > 0) &  # Hapus harga negatif
        (df['CustomerID'].notna())  # Hapus CustomerID yang kosong
    ]
    
    # Konversi format tanggal
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    print("\nJumlah data setelah cleaning:", len(df))
    print("\nJumlah missing values:")
    print(df.isnull().sum())
    
    return df

# Terapkan cleaning
df_clean = clean_data(df)

# %% [markdown]
# Analisis Output:
# 1. Perubahan Jumlah Data:
# - Data berkurang 144,025 baris (26.6%)
# - Data awal: 541,909 baris
# - Data setelah cleaning: 397,884 baris
# 2. Penyebab Pengurangan Data:
# - Penghapusan transaksi dengan CustomerID kosong
# - Penghapusan transaksi dengan Quantity ≤ 0 (retur atau pembatalan)
# - Penghapusan transaksi dengan UnitPrice ≤ 0 (item gratis atau error)
# 3. Status Missing Values:
# - Setelah cleaning, tidak ada lagi missing values di semua kolom
# - Semua kolom (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country) terisi lengkap
# - Data siap untuk analisis lanjutan tanpa perlu penanganan missing values tambahan
# 4. Kualitas Data:
# - Data sekarang lebih bersih dan valid
# - Hanya berisi transaksi dengan informasi lengkap
# - Tidak ada nilai negatif atau nol yang bisa mempengaruhi analisis

# %% [markdown]
# 3. Feature Engineering

# %%
def add_features(df):
    """
    Menambahkan fitur baru yang berguna untuk analisis
    """
    # Copy dataframe
    df = df.copy()
    
    # Tambah fitur waktu
    df['Year'] = df['InvoiceDate'].dt.year
    df['Month'] = df['InvoiceDate'].dt.month
    df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
    
    # Hitung total per transaksi
    df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
    
    # Kategorisasi produk
    df['PriceCategory'] = pd.qcut(df['UnitPrice'], q=4, labels=['Low', 'Medium', 'High', 'Premium'])
    
    print("Fitur baru yang ditambahkan:")
    print(df[['Year', 'Month', 'DayOfWeek', 'TotalAmount', 'PriceCategory']].head())
    
    return df

# Terapkan feature engineering
df_featured = add_features(df_clean)

# %% [markdown]
# Analisis Output:
# 
# 1. Fitur Waktu:
# - Semua transaksi pada sampel terjadi di tahun 2010
# - Bulan transaksi adalah Desember (12)
# - DayOfWeek = 2 menunjukkan hari Rabu (0=Senin, 1=Selasa, 2=Rabu)
# - Pola ini menunjukkan transaksi yang terjadi pada hari yang sama
# 2. TotalAmount:
# - Nilai transaksi berkisar antara 15.30 hingga 22.00
# - Terdapat beberapa transaksi dengan nilai yang sama (20.34)
# - Menunjukkan kemungkinan pembelian produk yang sama atau kombinasi produk dengan total yang sama
# 3. PriceCategory:
# - Semua transaksi dalam sampel masuk kategori "High"
# - Ini menunjukkan bahwa produk-produk yang dibeli memiliki harga di rentang yang tinggi
# - Perlu dilihat distribusi keseluruhan untuk memastikan tidak ada bias dalam kategorisasi
# 4. Pola Transaksi:
# - Data menunjukkan transaksi yang terjadi pada waktu yang sama (2010-12-Rabu)
# - Nilai transaksi yang berulang (20.34) menunjukkan kemungkinan pembelian produk yang sama oleh beberapa pelanggan
# - Kategori harga yang seragam (High) menunjukkan fokus pembelian pada produk-produk premium

# %% [markdown]
# 4. Penanganan Outlier

# %%
def handle_outliers(df):
    """
    Menangani outlier menggunakan metode IQR
    """
    print("Statistik sebelum penanganan outlier:")
    print(df[['Quantity', 'UnitPrice']].describe())
    
    # Copy dataframe
    df = df.copy()
    
    # IQR method untuk Quantity dan UnitPrice
    for column in ['Quantity', 'UnitPrice']:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        df = df[
            (df[column] >= lower_bound) &
            (df[column] <= upper_bound)
        ]
    
    print("\nStatistik setelah penanganan outlier:")
    print(df[['Quantity', 'UnitPrice']].describe())
    
    return df

# Terapkan penanganan outlier
df_final = handle_outliers(df_featured)

# %% [markdown]
# Analisis Output Penanganan Outlier:
# 1. Perubahan Jumlah Data:
# - Data awal: 397,884 baris
# - Data setelah penanganan outlier: 338,151 baris
# - Pengurangan: 59,733 baris (15% dari data awal)
# 2.  Perubahan pada Quantity:
# - Mean turun drastis dari 12.99 menjadi 7.48
# - Standar deviasi turun signifikan dari 179.33 menjadi 6.77
# - Nilai maksimum turun dari 80,995 menjadi 27
# - Nilai minimum tetap 1
# - Median (50%) tetap di angka 6
# 3. Perubahan pada UnitPrice:
# - Mean turun dari 3.12 menjadi 2.19
# - Standar deviasi turun drastis dari 22.10 menjadi 1.54
# - Nilai maksimum turun dari 8,142.75 menjadi 7.50
# - Nilai minimum tetap 0.001
# - Median turun sedikit dari 1.95 menjadi 1.65
# 4. Dampak Penanganan Outlier:
# - Data menjadi lebih terdistribusi normal
# - Menghilangkan nilai-nilai ekstrem yang tidak wajar
# - Range data menjadi lebih masuk akal untuk analisis retail

# %% [markdown]
# ## Explorasi data

# %%
import matplotlib.pyplot as plt
import seaborn as sns

# Set style seaborn
sns.set_style("whitegrid")

# 1. Distribusi Pembelian per Bulan
plt.figure(figsize=(12, 6))
monthly_sales = df_final.groupby('Month')['Quantity'].sum()
plt.bar(monthly_sales.index, monthly_sales.values)
plt.title('Total Pembelian per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Quantity')
plt.xticks(range(1, 13))  # Memastikan semua bulan ditampilkan
plt.show()

# 2. Top 10 Produk Terlaris
plt.figure(figsize=(12, 6))
top_products = df_final.groupby('Description')['Quantity'].sum().nlargest(10)
sns.barplot(y=top_products.index, x=top_products.values)
plt.title('10 Produk Terlaris')
plt.xlabel('Total Quantity')
plt.tight_layout()
plt.show()

# 3. Distribusi Harga Produk
plt.figure(figsize=(10, 6))
plt.hist(df_final['UnitPrice'], bins=50, edgecolor='black')
plt.title('Distribusi Harga Produk')
plt.xlabel('Harga')
plt.ylabel('Frekuensi')
plt.show()

# 4. Pola Pembelian Harian
plt.figure(figsize=(10, 6))
days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
daily_sales = df_final.groupby('DayOfWeek')['Quantity'].sum()

# Pastikan panjang array sama
plt.bar(range(len(daily_sales)), daily_sales.values)
plt.xticks(range(len(daily_sales)), days, rotation=45)
plt.title('Pola Pembelian Harian')
plt.xlabel('Hari')
plt.ylabel('Total Quantity')
plt.tight_layout()
plt.show()

# 5. Analisis Negara
plt.figure(figsize=(12, 6))
country_sales = df_final.groupby('Country')['Quantity'].sum().nlargest(10)
sns.barplot(y=country_sales.index, x=country_sales.values)
plt.title('Top 10 Negara berdasarkan Total Pembelian')
plt.xlabel('Total Quantity')
plt.tight_layout()
plt.show()

# 6. Scatter Plot Quantity vs Total Amount
plt.figure(figsize=(10, 6))
plt.scatter(df_final['Quantity'].sample(1000), 
            df_final['TotalAmount'].sample(1000), 
            alpha=0.5)
plt.title('Hubungan Quantity dan Total Amount')
plt.xlabel('Quantity')
plt.ylabel('Total Amount')
plt.show()

# Ringkasan Statistik
print("\nRingkasan Statistik:")
print("\nTop 5 Produk Terlaris:")
top_5_products = df_final.groupby('Description')['Quantity'].sum().nlargest(5)
print(top_5_products)

print("\nDistribusi Pembelian per Kategori Harga:")
price_category_dist = df_final['PriceCategory'].value_counts()
print(price_category_dist)

# Definisikan country_avg sebelum mencetak
country_avg = df_final.groupby('Country')['Quantity'].mean().nlargest(5)
print("\nRata-rata Pembelian per Negara:")
print(country_avg)

# %%
# Membuat pivot table untuk sistem rekomendasi
# Pivot tabel ini dapat digunakan untuk melihat interaksi antara pelanggan dan produk, yang sangat penting untuk model rekomendasi.

pivot_table = df_final.pivot_table(
    index='CustomerID',
    columns='StockCode',
    values='Quantity',
    aggfunc='sum',
    fill_value=0
)

# Normalisasi data menggunakan MinMaxScaler
scaler = MinMaxScaler()
pivot_normalized = pd.DataFrame(
    scaler.fit_transform(pivot_table),
    index=pivot_table.index,
    columns=pivot_table.columns
)

# Hitung similarity matrix
item_similarity = cosine_similarity(pivot_normalized.T)
item_similarity_df = pd.DataFrame(
    item_similarity,
    index=pivot_table.columns,
    columns=pivot_table.columns
)

print("Dimensi pivot table:", pivot_table.shape)
print("\nSample pivot table (5 baris pertama, 5 kolom pertama):")
print(pivot_table.iloc[:5, :5])
print("\nDimensi similarity matrix:", item_similarity_df.shape)

# %% [markdown]
# Penjelasan Kode:
# Pivot Table:
# Membuat pivot table dengan CustomerID sebagai index dan StockCode sebagai kolom.
# Nilai dalam tabel adalah jumlah pembelian (Quantity) untuk setiap produk oleh setiap pelanggan.
# Menggunakan aggfunc='sum' untuk menjumlahkan pembelian jika ada lebih dari satu transaksi untuk kombinasi pelanggan dan produk yang sama.
# fill_value=0 digunakan untuk menggantikan nilai kosong dengan 0, menunjukkan bahwa pelanggan tidak membeli produk tersebut.
# 2. Normalisasi Data:
# Menggunakan MinMaxScaler untuk menormalkan data dalam rentang [0, 1].
# Normalisasi penting untuk memastikan bahwa semua fitur memiliki skala yang sama saat menghitung similarity.
# Similarity Matrix:
# Menghitung cosine similarity antara produk berdasarkan pivot table yang dinormalisasi.
# Hasilnya adalah matriks simetris di mana setiap sel menunjukkan seberapa mirip dua produk berdasarkan pembelian pelanggan.
# 

# %% [markdown]
# - 4191 pelanggan unik (CustomerID)
# - 3392 produk unik (StockCode)
# - Ini menunjukkan bahwa dataset memiliki variasi yang cukup besar dalam hal pelanggan dan produk yang terlibat.
# 
# - Semua nilai dalam sample pivot table adalah 0 untuk pelanggan yang ditampilkan.
# Ini menunjukkan bahwa pelanggan-pelanggan ini tidak membeli produk yang ditampilkan (10002, 10080, 10120, 10123C, 10124A).
# Hal ini bisa terjadi jika produk tersebut tidak populer atau pelanggan tersebut tidak tertarik pada produk tersebut.
# 
# - Matriks berukuran 3392 x 3392 menunjukkan bahwa ada 3392 produk yang dibandingkan satu sama lain.
# Setiap sel dalam matriks menunjukkan tingkat kemiripan antara dua produk berdasarkan pembelian pelanggan.
# Kesimpulan:
# Data Sparse: Dengan banyak nilai 0 dalam pivot table, ini menunjukkan bahwa data sangat sparse, yang umum terjadi dalam dataset transaksi retail. Banyak pelanggan mungkin hanya membeli beberapa produk dari total produk yang tersedia.
# Rekomendasi: Meskipun ada banyak nilai 0, sistem rekomendasi masih dapat berfungsi dengan baik jika ada cukup data untuk produk yang sering dibeli bersama.
# Analisis Lanjutan: Anda mungkin ingin mengeksplorasi lebih lanjut untuk memahami pola pembelian pelanggan dan produk yang lebih populer.

# %% [markdown]
# ## Modelling

# %% [markdown]
# Matriks Similarity

# %%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# 1. Split Data menjadi 80% untuk pelatihan dan 20% untuk validasi
df_train, df_valid = train_test_split(df_final, test_size=0.2, random_state=42)

# 2. Membuat pivot table untuk sistem rekomendasi dari data pelatihan
pivot_table = df_train.pivot_table(
    index='CustomerID',
    columns='StockCode',
    values='Quantity',
    aggfunc='sum',
    fill_value=0
)

# 3. Normalisasi data menggunakan MinMaxScaler
scaler = MinMaxScaler()
pivot_normalized = pd.DataFrame(
    scaler.fit_transform(pivot_table),
    index=pivot_table.index,
    columns=pivot_table.columns
)

# 4. Hitung similarity matrix
item_similarity = cosine_similarity(pivot_normalized.T)
item_similarity_df = pd.DataFrame(
    item_similarity,
    index=pivot_table.columns,
    columns=pivot_table.columns
)

# Output dimensi dan sample pivot table
print("Dimensi pivot table:", pivot_table.shape)
print("\nSample pivot table (5 baris pertama, 5 kolom pertama):")
print(pivot_table.iloc[:5, :5])
print("\nDimensi similarity matrix:", item_similarity_df.shape)

# %% [markdown]
# Output yang Anda berikan menunjukkan hasil dari pembuatan pivot table dan similarity matrix setelah membagi data menjadi 80% untuk pelatihan dan 20% untuk validasi. Mari kita analisis hasil tersebut:
# Analisis Output
# Dimensi Pivot Table:
# Dimensi pivot table: (4176, 3345)
# - 4176 pelanggan unik (CustomerID)
# 3345 produk unik (StockCode)
# Ini menunjukkan bahwa dataset memiliki variasi yang cukup besar dalam hal pelanggan dan produk yang terlibat.
# Sample Pivot Table:
# Semua nilai dalam sample pivot table adalah 0 untuk pelanggan yang ditampilkan.
# Ini menunjukkan bahwa pelanggan-pelanggan ini tidak membeli produk yang ditampilkan (10002, 10080, 10120, 10123C, 10124A).
# Hal ini bisa terjadi jika produk tersebut tidak populer atau pelanggan tersebut tidak tertarik pada produk tersebut.
# 3. Dimensi Similarity Matrix:
#    Matriks berukuran 3345 x 3345 menunjukkan bahwa ada 3345 produk yang dibandingkan satu sama lain.
# Setiap sel dalam matriks menunjukkan tingkat kemiripan antara dua produk berdasarkan pembelian pelanggan.
# Kesimpulan:
# Data Sparse: Dengan banyak nilai 0 dalam pivot table, ini menunjukkan bahwa data sangat sparse, yang umum terjadi dalam dataset transaksi retail. Banyak pelanggan mungkin hanya membeli beberapa produk dari total produk yang tersedia.
# Rekomendasi: Meskipun ada banyak nilai 0, sistem rekomendasi masih dapat berfungsi dengan baik jika ada cukup data untuk produk yang sering dibeli bersama.
# Analisis Lanjutan: Anda mungkin ingin mengeksplorasi lebih lanjut untuk memahami pola pembelian pelanggan dan produk yang lebih populer.
# Langkah Selanjutnya:
# Jika Anda ingin melanjutkan ke tahap berikutnya, Anda dapat:
# Menyiapkan fungsi untuk mendapatkan rekomendasi berdasarkan similarity matrix.
# Menyiapkan fungsi untuk mengevaluasi model menggunakan precision dan recall.

# %% [markdown]
# 1. Content-Based Filtering:

# %%


# Dapatkan rekomendasi untuk pelanggan yang ada di data validasi
recommendations = pd.DataFrame()

for customer_id in df_valid['CustomerID'].unique():
    purchased_items = df_valid[df_valid['CustomerID'] == customer_id]['StockCode'].unique()
    
    if len(purchased_items) > 0:
        sample_product = purchased_items[0]
        
        if sample_product in item_similarity_df.columns:
            recs = get_recommendations(sample_product, n_recommendations=5)
            recs['CustomerID'] = customer_id
            recommendations = pd.concat([recommendations, recs], ignore_index=True)

# Hasil evaluasi
precision_list, recall_list = evaluate_recommendations(df_valid, recommendations)

# Tampilkan top-n rekomendasi
top_n = 5  # Ganti dengan jumlah rekomendasi yang diinginkan
print(f"\nTop-{top_n} Rekomendasi:")
print(recommendations[['CustomerID', 'StockCode', 'Description', 'Similarity']].head(top_n))

# Visualisasi Precision dan Recall
plt.figure(figsize=(12, 6))

# Bar Chart untuk Precision dan Recall
sns.barplot(x=['Precision', 'Recall'], y=[sum(precision_list) / len(precision_list), sum(recall_list) / len(recall_list)])
plt.title('Precision dan Recall Model Rekomendasi')
plt.ylabel('Nilai')
plt.ylim(0, 1)
plt.show()

# Histogram untuk Distribusi Precision dan Recall
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(precision_list, bins=10, kde=True)
plt.title('Distribusi Precision')
plt.xlabel('Precision')
plt.ylabel('Frekuensi')

plt.subplot(1, 2, 2)
sns.histplot(recall_list, bins=10, kde=True)
plt.title('Distribusi Recall')
plt.xlabel('Recall')
plt.ylabel('Frekuensi')

plt.tight_layout()
plt.show()


# %% [markdown]
# Keterangan :
# - Top-5 rekomendasi menunjukkan bahwa model dapat memberikan rekomendasi yang relevan dan bermanfaat untuk pelanggan tertentu. Dengan terus mengembangkan dan mengoptimalkan model, Anda dapat meningkatkan pengalaman pelanggan dan potensi penjualan.
# - Semua rekomendasi ditujukan untuk pelanggan dengan CustomerID 14096. Ini menunjukkan bahwa model berhasil memberikan rekomendasi yang relevan untuk pelanggan tertentu berdasarkan riway
# - Rekomendasi mencakup berbagai produk, mulai dari tas (BLUE DISCO HANDBAG) hingga peralatan rumah tangga (TWO DOOR CURIO CABINET). Ini menunjukkan bahwa model dapat merekomendasikan produk yang beragam, yang mungkin menarik bagi pelanggan tersebut.
# - Nilai similarity berkisar antara 0.345528 hingga 0.467172. Ini menunjukkan bahwa produk-produk ini memiliki tingkat kemiripan yang cukup baik dengan produk yang sebelumnya dibeli oleh pelanggan.
# -  Nilai similarity yang lebih tinggi menunjukkan bahwa produk tersebut lebih relevan dengan preferensi pelanggan, yang dapat meningkatkan kemungkinan pelanggan untuk membeli produk tersebut.
# 

# %% [markdown]
# 2. Collaborative Filtering:

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pastikan df_valid dan item_similarity_df sudah didefinisikan sebelumnya

# Fungsi untuk mendapatkan rekomendasi
def get_recommendations(item_code, n_recommendations=5):
    if item_code not in item_similarity_df.columns:
        raise ValueError(f"StockCode {item_code} tidak ditemukan")
    
    similar_items = item_similarity_df[item_code].sort_values(ascending=False)
    similar_items = similar_items[similar_items > 0.1].drop(item_code)
    
    recommendations = pd.DataFrame(similar_items.head(n_recommendations))
    recommendations.columns = ['Similarity']
    recommendations['StockCode'] = recommendations.index
    recommendations['Description'] = recommendations['StockCode'].map(
        df_final.groupby('StockCode')['Description'].first()
    )
    
    return recommendations[['StockCode', 'Description', 'Similarity']]

# Fungsi evaluasi
def evaluate_recommendations(test_data, recommendations, n_recommendations=5):
    relevant_items = test_data.groupby('CustomerID')['StockCode'].apply(list)
    
    precision_list = []
    recall_list = []
    
    for customer_id, recommended_items in recommendations.groupby('CustomerID'):
        if customer_id in relevant_items.index:
            true_items = set(relevant_items[customer_id])
            recommended_items_set = set(recommended_items['StockCode'].head(n_recommendations))
            
            true_positives = len(true_items.intersection(recommended_items_set))
            precision = true_positives / len(recommended_items_set) if len(recommended_items_set) > 0 else 0
            recall = true_positives / len(true_items) if len(true_items) > 0 else 0
            
            precision_list.append(precision)
            recall_list.append(recall)
    
    return precision_list, recall_list

# Dapatkan rekomendasi untuk pelanggan yang ada di data validasi
recommendations = pd.DataFrame()

for customer_id in df_valid['CustomerID'].unique():
    purchased_items = df_valid[df_valid['CustomerID'] == customer_id]['StockCode'].unique()
    
    if len(purchased_items) > 0:
        sample_product = purchased_items[0]
        
        if sample_product in item_similarity_df.columns:
            recs = get_recommendations(sample_product, n_recommendations=5)
            recs['CustomerID'] = customer_id
            recommendations = pd.concat([recommendations, recs], ignore_index=True)

# Hasil evaluasi
precision_list, recall_list = evaluate_recommendations(df_valid, recommendations)

# Visualisasi Precision dan Recall
plt.figure(figsize=(12, 6))

# Bar Chart untuk Precision dan Recall
sns.barplot(x=['Precision', 'Recall'], y=[sum(precision_list) / len(precision_list), sum(recall_list) / len(recall_list)])
plt.title('Precision dan Recall Model Rekomendasi')
plt.ylabel('Nilai')
plt.ylim(0, 1)
plt.show()

# Histogram untuk Distribusi Precision dan Recall
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(precision_list, bins=10, kde=True)
plt.title('Distribusi Precision')
plt.xlabel('Precision')
plt.ylabel('Frekuensi')

plt.subplot(1, 2, 2)
sns.histplot(recall_list, bins=10, kde=True)
plt.title('Distribusi Recall')
plt.xlabel('Recall')
plt.ylabel('Frekuensi')

plt.tight_layout()
plt.show()

# %%


# %%
# ... existing code ...

# Dapatkan rekomendasi untuk pelanggan yang ada di data validasi
recommendations = pd.DataFrame()

for customer_id in df_valid['CustomerID'].unique():
    purchased_items = df_valid[df_valid['CustomerID'] == customer_id]['StockCode'].unique()
    
    if len(purchased_items) > 0:
        sample_product = purchased_items[0]
        
        if sample_product in item_similarity_df.columns:
            recs = get_recommendations(sample_product, n_recommendations=5)
            recs['CustomerID'] = customer_id
            recommendations = pd.concat([recommendations, recs], ignore_index=True)

# Hasil evaluasi
precision_list, recall_list = evaluate_recommendations(df_valid, recommendations)

# Tampilkan top-n rekomendasi
top_n = 5  # Ganti dengan jumlah rekomendasi yang diinginkan
print(f"\nTop-{top_n} Rekomendasi:")
print(recommendations[['CustomerID', 'StockCode', 'Description', 'Similarity']].head(top_n))

# Visualisasi Precision dan Recall
plt.figure(figsize=(12, 6))

# Bar Chart untuk Precision dan Recall
sns.barplot(x=['Precision', 'Recall'], y=[sum(precision_list) / len(precision_list), sum(recall_list) / len(recall_list)])
plt.title('Precision dan Recall Model Rekomendasi')
plt.ylabel('Nilai')
plt.ylim(0, 1)
plt.show()

# Histogram untuk Distribusi Precision dan Recall
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(precision_list, bins=10, kde=True)
plt.title('Distribusi Precision')
plt.xlabel('Precision')
plt.ylabel('Frekuensi')

plt.subplot(1, 2, 2)
sns.histplot(recall_list, bins=10, kde=True)
plt.title('Distribusi Recall')
plt.xlabel('Recall')
plt.ylabel('Frekuensi')

plt.tight_layout()
plt.show()
# ... existing code ...

# %% [markdown]
# Keterangan :
# - Top-5 rekomendasi menunjukkan bahwa model dapat memberikan rekomendasi yang relevan dan bermanfaat untuk pelanggan tertentu. Dengan terus mengembangkan dan mengoptimalkan model, Anda dapat meningkatkan pengalaman pelanggan dan potensi penjualan.
# - Semua rekomendasi ditujukan untuk pelanggan dengan CustomerID 14096. Ini menunjukkan bahwa model berhasil memberikan rekomendasi yang relevan berdasarkan riwayat pembelian pelanggan tersebut.
# - Rekomendasi mencakup berbagai jenis produk, mulai dari aksesori fashion (BLUE DISCO HANDBAG) hingga peralatan rumah tangga (TWO DOOR CURIO CABINET). Ini menunjukkan bahwa model dapat merekomendasikan produk dari berbagai kategori, yang dapat menarik minat pelanggan.
# - Deskripsi produk memberikan konteks yang jelas tentang apa yang direkomendasikan. Misalnya, "BLUE DISCO HANDBAG" adalah produk yang menarik perhatian, sementara "HARDMAN MUG 3 ASSORTED" menunjukkan variasi dalam pilihan mug.
# - Nilai similarity berkisar antara 0.345528 hingga 0.467172. Nilai ini menunjukkan tingkat kemiripan produk dengan produk yang sebelumnya dibeli oleh pelanggan.
# - Nilai similarity yang lebih tinggi (seperti 0.467172 untuk tas) menunjukkan bahwa produk tersebut lebih relevan dengan preferensi pelanggan, yang dapat meningkatkan kemungkinan pembelian.
# 
# 
# Strategi Rekomendasi hasil dari kedua model 
# 1. Personalisasi:
#     Rekomendasi yang ditargetkan untuk pelanggan tertentu menunjukkan bahwa model dapat memberikan pengalaman belanja yang lebih personal. Ini dapat meningkatkan kepuasan pelanggan dan loyalitas.
# 2. Diversifikasi Produk:
#     Dengan merekomendasikan produk dari berbagai kategori, model dapat membantu pelanggan menemukan produk baru yang mungkin tidak mereka pertimbangkan sebelumnya. Ini dapat meningkatkan penjualan lintas kategori.
# 
# 
# 
# 

# %%
pip freeze requirement.txt


