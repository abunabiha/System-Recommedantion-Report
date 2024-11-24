# Laporan Proyek Machine Learning - Imam Asrowardi

## Project Overview

Proyek ini bertujuan untuk membangun sistem rekomendasi produk menggunakan data transaksi retail. Sistem ini akan memberikan rekomendasi produk kepada pelanggan berdasarkan kesamaan produk yang dibeli sebelumnya selain itu Proyek ini tidak hanya memberikan manfaat langsung bagi perusahaan dalam hal penjualan dan kepuasan pelanggan, tetapi juga memberikan wawasan berharga yang dapat digunakan untuk pengambilan keputusan strategis di masa depan.

**Pentingnya Proyek Sistem Rekomendasi Produk**:
Proyek sistem rekomendasi produk ini sangat penting untuk diselesaikan karena beberapa alasan berikut:
1. Meningkatkan Pengalaman Pelanggan
    Sistem rekomendasi yang dipersonalisasi telah terbukti meningkatkan kepuasan pelanggan dengan memberikan rekomendasi berdasarkan preferensi mereka. Studi menunjukkan bahwa personalisasi berperan penting dalam meningkatkan kepuasan pasca-penggunaan pelanggan (Jiang et al., 2010).
2. Meningkatkan Penjualan
    Penelitian menemukan bahwa sistem rekomendasi dapat secara signifikan meningkatkan penjualan dengan memanfaatkan data pelanggan untuk menghasilkan rekomendasi yang relevan. Misalnya, penelitian menggarisbawahi dampak personalisasi pada peningkatan penjualan produk dalam e-commerce (Zhang et al., 2011).
3. Pengelolaan Inventaris yang Lebih Baik
    Dengan memahami pola pembelian pelanggan, sistem rekomendasi membantu dalam mengelola stok dan mengurangi inventaris yang tidak terjual. Rekomendasi berbasis data meningkatkan efisiensi manajemen produk (Lee et al., 2002).
4. Persaingan di Pasar
    Personalization dalam rekomendasi dapat menjadi alat yang efektif untuk membangun loyalitas pelanggan dan memberi perusahaan keunggulan kompetitif di pasar yang padat (Ball et al., 2006).
5. Analisis Data yang Mendalam
    Analisis data dari rekomendasi memungkinkan pemahaman yang lebih baik tentang perilaku pelanggan dan tren pasar. Data ini dapat digunakan untuk mengembangkan strategi pemasaran yang lebih efektif (Xu et al., 2015).


## Business Understanding

### Problem Statements

1. Rekomendasi produk yang tidak akurat dapat menyebabkan pelanggan merasa tidak puas, yang berpotensi mengurangi tingkat konversi penjualan.
2. Pengelolaan data yang besar dan beragam dapat menyulitkan analisis dan pengambilan keputusan yang tepat, terutama dalam menangani nilai yang hilang dan memastikan kualitas data.

### Goals

Menjelaskan tujuan proyek yang menjawab pernyataan masalah:
1. Meningkatkan penjualan dan kepuasan pelanggan melalui rekomendasi produk yang relevan dan sesuai preferensi.
3. Mengoptimalkan pengelolaan inventaris dengan memastikan produk yang rekomendasikan tersedia secara optimal.

### Solution statements
1. Pendekatan Algoritma Rekomendasi Berbasis Kesamaan:
    Menggunakan algoritma cosine similarity untuk menghitung kesamaan antar produk berdasarkan fitur yang ada, seperti deskripsi dan harga. Ini akan membantu dalam memberikan rekomendasi yang lebih relevan kepada pelanggan.
2. Pendekatan Pembelajaran Mesin:
    Menerapkan model pembelajaran mesin seperti Collaborative Filtering untuk menganalisis pola pembelian pelanggan dan memberikan rekomendasi berdasarkan perilaku pengguna lain yang memiliki kesamaan. Ini dapat meningkatkan akurasi rekomendasi dengan memanfaatkan data interaksi pengguna yang lebih luas.

Dengan pendekatan ini, proyek bertujuan untuk meningkatkan kualitas rekomendasi produk dan memberikan pengalaman yang lebih baik bagi pelanggan.

## Data Understanding
1. Informasi Dataset
   Dataset yang digunakan dalam proyek ini terdiri dari 541,909 entri dengan 8 kolom yang berbeda. Data ini diambil dari transaksi retail dan mencakup informasi mengenai produk yang dibeli oleh pelanggan yang bersumber dari dataset public kaggle. (https://www.kaggle.com/code/farzadnekouei/customer-segmentation-recommendation-system/input)
2. Kondisi Data
   - Total Baris Data: 541,909 entries
   - Memori yang Digunakan: 33.1+ MB
   - Status Missing Values:
     - Description: 1,454 missing values (540,455 non-null dari 541,909)
     - CustomerID: 135,080 missing values (406,829 non-null dari 541,909)
     - Kolom lainnya terisi lengkap (541,909 non-null)
3. Variabel atau Fitur pada Dataset
   - InvoiceNo: Nomor faktur yang unik untuk setiap transaksi (tipe: object).
   - StockCode: Kode unik untuk setiap produk (tipe: object).
   - Description: Deskripsi produk yang dibeli (tipe: object).
   - Quantity: Jumlah produk yang dibeli dalam transaksi (tipe: int64).
   - InvoiceDate: Tanggal dan waktu transaksi dilakukan (tipe: object).
   - UnitPrice: Harga per unit produk (tipe: float64).
   - CustomerID: ID unik untuk setiap pelanggan (tipe: float64).
   - Country: Negara tempat pelanggan berada (tipe: object).


**Exploratory data analysis**
1. Informasi Total Pembelian per Bulan

![TotalPembelianPerbulan](https://github.com/user-attachments/assets/54c2c95f-b25c-4fa0-8325-e65973a5446a)


Berdasarkan grafik yang menunjukkan total pembelian per bulan, berikut adalah beberapa analisis yang dapat dilakukan:
1. Tren Pembelian:
   Terdapat tren peningkatan jumlah pembelian dari bulan ke bulan, dengan puncak terjadi pada bulan November dan Desember. Ini menunjukkan bahwa pelanggan cenderung melakukan lebih banyak pembelian menjelang akhir tahun, mungkin karena faktor musim liburan atau promosi akhir tahun.
2. Bulan dengan Pembelian Terendah:
   Bulan Januari dan Februari menunjukkan jumlah pembelian yang lebih rendah dibandingkan bulan lainnya. Hal ini bisa disebabkan oleh beberapa faktor, seperti pengeluaran yang lebih rendah setelah periode belanja Natal dan Tahun Baru.
3. Bulan dengan Pembelian Tertinggi:
   Bulan November mencatatkan total pembelian tertinggi, yang mungkin terkait dengan acara belanja besar seperti Black Friday atau Cyber Monday. Ini menunjukkan bahwa strategi pemasaran yang tepat pada bulan-bulan ini dapat meningkatkan penjualan secara signifikan.
4. Konsistensi Pembelian:
   Meskipun ada fluktuasi, secara keseluruhan, jumlah pembelian menunjukkan konsistensi yang baik, dengan tidak ada bulan yang mengalami penurunan drastis. Ini menunjukkan bahwa ada permintaan yang stabil untuk produk yang ditawarkan.
5. Rekomendasi untuk Strategi Pemasaran:
   Mengingat tren pembelian yang meningkat menjelang akhir tahun, perusahaan dapat merencanakan kampanye pemasaran yang lebih agresif pada bulan-bulan tersebut untuk memaksimalkan penjualan.
6. Insight untuk Pengelolaan Inventaris:
   Dengan memahami pola pembelian bulanan, perusahaan dapat mengelola inventaris dengan lebih baik, memastikan bahwa produk yang paling diminati tersedia selama periode puncak pembelian.

Grafik total pembelian per bulan memberikan wawasan berharga tentang perilaku pelanggan dan pola pembelian. Dengan analisis ini, perusahaan dapat merumuskan strategi pemasaran dan pengelolaan inventaris yang lebih efektif untuk meningkatkan penjualan dan kepuasan pelanggan.

2. Informasi 10 Produk Terlaris
   
![sepuluhPrldukTerlair](https://github.com/user-attachments/assets/b950ed0c-e47f-42d1-91da-db6abe9d45f5)


Berdasarkan grafik yang menunjukkan 10 produk terlaris, berikut adalah beberapa analisis yang dapat dilakukan:
1. Produk Paling Laris:
   PACK OF 72 RETROSPOT CAKE CASES muncul sebagai produk terlaris dengan jumlah penjualan tertinggi, mencapai hampir 14,000 unit. Ini menunjukkan bahwa produk ini sangat diminati oleh pelanggan, mungkin karena fungsionalitasnya dalam acara atau perayaan tertentu.
2. Variasi Produk:
   Produk yang terdaftar mencakup berbagai kategori, seperti peralatan pesta (cake cases), dekorasi (bird ornament), dan tas (jumbo bag, lunch bag). Ini menunjukkan bahwa pelanggan memiliki minat yang beragam, dan perusahaan dapat memanfaatkan variasi ini untuk memperluas penawaran produk.
3. Tren Pembelian:
   Banyak produk yang terlaris adalah barang-barang yang sering digunakan dalam acara sosial atau perayaan, seperti jam making set dan hanging t-light holder. Ini menunjukkan bahwa ada permintaan yang tinggi untuk produk yang mendukung kegiatan berkumpul atau merayakan.
4. Peluang Pemasaran:
   Dengan mengetahui produk-produk terlaris, perusahaan dapat merencanakan strategi pemasaran yang lebih efektif. Misalnya, mereka dapat menawarkan promosi atau diskon untuk produk-produk ini, atau mengembangkan kampanye iklan yang menyoroti produk-produk tersebut.
5. Pengelolaan Inventaris:
   Data ini juga memberikan wawasan penting untuk pengelolaan inventaris. Dengan mengetahui produk mana yang paling laku, perusahaan dapat memastikan bahwa stok produk tersebut selalu tersedia, terutama menjelang periode puncak penjualan.
6. Insight untuk Pengembangan Produk:
   Perusahaan dapat mempertimbangkan untuk mengembangkan produk baru yang serupa dengan produk terlaris ini. Misalnya, variasi warna atau ukuran dari retrospot cake cases atau produk baru yang berhubungan dengan tema pesta.

Grafik ini memberikan wawasan berharga tentang preferensi pelanggan dan pola pembelian. Dengan analisis ini, perusahaan dapat merumuskan strategi pemasaran, pengelolaan inventaris, dan pengembangan produk yang lebih baik untuk meningkatkan penjualan dan kepuasan pelanggan.

3. Informasi Distribusi Harga Produk
   
![DistribusiHargaProduk](https://github.com/user-attachments/assets/e9b9ec15-0025-4822-82e8-a1aa15769336)

Berdasarkan histogram yang menunjukkan distribusi harga produk, berikut adalah beberapa analisis yang dapat dilakukan:
1. Konsentrasi Harga:
   Terlihat bahwa sebagian besar produk memiliki harga yang berkisar antara £0 hingga £3. Ini menunjukkan bahwa perusahaan lebih banyak menjual produk dengan harga terjangkau, yang mungkin menarik bagi segmen pasar yang lebih luas.
2. Puncak Harga:
   Ada beberapa puncak frekuensi pada harga tertentu, terutama di sekitar £1 dan £2. Ini menunjukkan bahwa produk dengan harga di kisaran ini sangat populer dan mungkin merupakan produk yang paling banyak dibeli oleh pelanggan.
3. Variasi Harga:
   Meskipun sebagian besar produk terjangkau, ada juga produk dengan harga yang lebih tinggi (hingga £7). Namun, frekuensi untuk produk dengan harga lebih tinggi ini jauh lebih rendah, menunjukkan bahwa produk premium mungkin tidak sepopuler produk dengan harga lebih rendah.
4. Insight untuk Strategi Pemasaran:
   Dengan mengetahui bahwa produk dengan harga rendah lebih banyak diminati, perusahaan dapat mempertimbangkan untuk meningkatkan stok produk-produk ini dan merencanakan promosi yang lebih agresif untuk menarik lebih banyak pelanggan.
   Selain itu, perusahaan dapat mengeksplorasi cara untuk meningkatkan penjualan produk dengan harga lebih tinggi, seperti menawarkan bundling atau diskon untuk pembelian dalam jumlah besar.
5. Pengelolaan Inventaris:
   Data ini juga memberikan wawasan penting untuk pengelolaan inventaris. Dengan fokus pada produk yang lebih terjangkau, perusahaan dapat memastikan bahwa mereka memiliki cukup stok untuk memenuhi permintaan yang tinggi.
6. Kualitas Produk:
   Meskipun harga rendah dapat menarik banyak pelanggan, perusahaan juga harus memastikan bahwa kualitas produk tetap terjaga. Hal ini penting untuk mempertahankan loyalitas pelanggan dan mencegah pengembalian produk.

Histogram distribusi harga produk memberikan wawasan berharga tentang preferensi harga pelanggan. Dengan analisis ini, perusahaan dapat merumuskan strategi pemasaran dan pengelolaan inventaris yang lebih baik untuk meningkatkan penjualan dan kepuasan pelanggan.

4. Informasi Pola Pembelian Harian
   
![TotaPembelianHarian](https://github.com/user-attachments/assets/f7e26c62-af5f-44da-a821-f3dc6574ed81)



Berdasarkan grafik yang menunjukkan pola pembelian harian, berikut adalah beberapa analisis yang dapat dilakukan:
1. Hari dengan Pembelian Tertinggi:
   Kamis mencatatkan total pembelian tertinggi, mencapai lebih dari 500,000 unit. Ini menunjukkan bahwa pelanggan lebih aktif berbelanja pada hari tersebut, mungkin karena berbagai faktor seperti promosi atau kebiasaan belanja.
2. Hari dengan Pembelian Terendah:
   Sabtu menunjukkan total pembelian terendah dibandingkan dengan hari lainnya. Hal ini bisa disebabkan oleh berbagai alasan, seperti pelanggan yang lebih memilih berbelanja di hari kerja atau mungkin lebih banyak kegiatan di luar rumah pada akhir pekan.
3. Konsistensi Pembelian:
   Secara umum, pola pembelian menunjukkan konsistensi yang baik sepanjang minggu, dengan jumlah pembelian yang relatif tinggi dari Senin hingga Jumat. Ini menunjukkan bahwa ada permintaan yang stabil untuk produk yang ditawarkan.
4. Insight untuk Strategi Pemasaran:
   Mengingat bahwa Kamis adalah hari dengan pembelian tertinggi, perusahaan dapat merencanakan promosi atau kampanye pemasaran yang lebih agresif pada hari tersebut untuk memaksimalkan penjualan.
   Untuk meningkatkan penjualan pada hari Sabtu, perusahaan dapat mempertimbangkan untuk menawarkan diskon khusus atau promosi yang menarik untuk menarik pelanggan berbelanja di akhir pekan.
5. Pengelolaan Stok:
   Dengan mengetahui pola pembelian harian, perusahaan dapat mengelola inventaris dengan lebih baik. Misalnya, memastikan bahwa stok produk yang populer tersedia lebih banyak pada hari-hari dengan pembelian tinggi.
6. Analisis Perilaku Pelanggan:
   Pola ini juga memberikan wawasan tentang perilaku pelanggan. Misalnya, jika pelanggan lebih cenderung berbelanja di hari kerja, perusahaan dapat mempertimbangkan untuk menyesuaikan jam operasional atau layanan pelanggan untuk memenuhi kebutuhan mereka.

Grafik pola pembelian harian memberikan wawasan berharga tentang perilaku pelanggan dan preferensi belanja. Dengan analisis ini, perusahaan dapat merumuskan strategi pemasaran dan pengelolaan inventaris yang lebih baik untuk meningkatkan penjualan dan kepuasan pelanggan.

5. Informasi Top 10 Negara dengan Total Pembelian

![top10negara](https://github.com/user-attachments/assets/78b2692a-730d-4932-92c7-f4f423eb4fc2)


Berdasarkan grafik yang menunjukkan total pembelian dari 10 negara teratas, berikut adalah analisis yang dapat dilakukan:
1. Dominasi United Kingdom:
   United Kingdom mendominasi total pembelian dengan jumlah yang sangat signifikan, jauh lebih tinggi dibandingkan negara lainnya. Ini menunjukkan bahwa pasar di Inggris adalah yang paling besar dan mungkin menjadi fokus utama bagi perusahaan dalam strategi pemasaran dan distribusi.
2. Negara Lain yang Menyusul:
   Negara-negara seperti Germany, France, dan EIRE (Republik Irlandia) menunjukkan total pembelian yang lebih rendah, tetapi masih cukup signifikan. Ini menunjukkan bahwa ada potensi pasar yang baik di negara-negara ini, meskipun tidak sekuat Inggris.
3. Negara dengan Pembelian Terendah:
   Netherlands dan Norway berada di bagian bawah daftar, dengan total pembelian yang jauh lebih rendah dibandingkan dengan negara-negara lain. Ini mungkin menunjukkan bahwa perusahaan perlu mengeksplorasi lebih lanjut tentang mengapa penjualan di negara-negara ini rendah dan apakah ada strategi pemasaran yang dapat diterapkan untuk meningkatkan penjualan.
4. Insight untuk Strategi Pemasaran:
   - Mengingat dominasi Inggris, perusahaan dapat mempertimbangkan untuk meningkatkan upaya pemasaran dan promosi di negara ini, termasuk kampanye iklan yang lebih agresif.
   - Untuk negara-negara dengan total pembelian yang lebih rendah, perusahaan dapat melakukan analisis pasar untuk memahami preferensi pelanggan dan menyesuaikan penawaran produk atau strategi pemasaran.
5. Pengelolaan Inventaris:
   Data ini juga memberikan wawasan penting untuk pengelolaan inventaris. Perusahaan dapat memastikan bahwa produk yang paling diminati di negara-negara dengan total pembelian tinggi selalu tersedia, sementara juga mempertimbangkan untuk meningkatkan stok di negara-negara dengan potensi pertumbuhan.
6. Analisis Perilaku Pelanggan:
   Pola ini memberikan wawasan tentang perilaku pelanggan di berbagai negara. Perusahaan dapat menggunakan informasi ini untuk menyesuaikan produk dan layanan mereka agar lebih sesuai dengan kebutuhan dan preferensi lokal.

Grafik ini memberikan wawasan berharga tentang distribusi pembelian berdasarkan negara. Dengan analisis ini, perusahaan dapat merumuskan strategi pemasaran yang lebih efektif, mengelola inventaris dengan lebih baik, dan memahami perilaku pelanggan di berbagai pasar.


6. Informasi Hubungan Quantity dan Total Amount
   
![Hubunganquantitiydanamount](https://github.com/user-attachments/assets/47dda0a5-5923-49aa-b0ac-adb71333f21a)


Berdasarkan grafik yang menunjukkan hubungan antara Quantity dan Total Amount, berikut adalah analisis yang dapat dilakukan:
1. Pola Umum:
   Terdapat pola yang menunjukkan bahwa ketika jumlah (Quantity) meningkat, total jumlah (Total Amount) juga cenderung meningkat. Namun, hubungan ini tidak sepenuhnya linier, dan ada banyak variasi dalam data.
2. Konsentrasi Data:
   Sebagian besar titik data terdistribusi di sekitar Quantity yang rendah (0-10) dan Total Amount yang juga relatif rendah (0-20). Ini menunjukkan bahwa banyak transaksi melibatkan pembelian dalam jumlah kecil, yang mungkin mencerminkan sifat produk yang dijual.
3. Outlier:
   Ada beberapa titik data yang menunjukkan Total Amount yang tinggi (di atas 60) meskipun Quantity tidak terlalu tinggi (sekitar 5-10). Ini mungkin menunjukkan bahwa produk dengan harga per unit yang lebih tinggi dibeli dalam jumlah kecil, yang dapat menjadi fokus untuk strategi pemasaran.
4. Variasi pada Jumlah Besar:
   Ketika Quantity mencapai angka yang lebih tinggi (20-25), Total Amount juga menunjukkan variasi yang lebih besar. Ini menunjukkan bahwa produk yang dibeli dalam jumlah besar dapat memiliki harga yang bervariasi, mungkin karena diskon atau variasi harga produk.
5. Insight untuk Strategi Pemasaran:
   Mengingat bahwa banyak transaksi melibatkan jumlah kecil, perusahaan dapat mempertimbangkan untuk menawarkan paket atau bundling produk untuk mendorong pembelian dalam jumlah yang lebih besar.
   Untuk produk dengan harga tinggi, perusahaan dapat merencanakan promosi yang menargetkan pelanggan yang membeli dalam jumlah kecil tetapi dengan total pembelian yang tinggi.
6. Pengelolaan Stok:
   Data ini juga memberikan wawasan penting untuk pengelolaan inventaris. Memahami pola pembelian berdasarkan jumlah dan total dapat membantu perusahaan dalam merencanakan stok produk yang lebih baik.


Grafik ini memberikan wawasan berharga tentang hubungan antara jumlah produk yang dibeli dan total pembelian. Dengan analisis ini, perusahaan dapat merumuskan strategi pemasaran yang lebih efektif, mengelola inventaris dengan lebih baik, dan memahami perilaku pelanggan dalam konteks pembelian.

Informasi Ringkasan

      Top 5 Produk Terlaris:
      Description
      PACK OF 72 RETROSPOT CAKE CASES       15009
      ASSORTED COLOUR BIRD ORNAMENT         13673
      JUMBO BAG RED RETROSPOT               12170
      WHITE HANGING HEART T-LIGHT HOLDER    10803
      LUNCH BAG RED RETROSPOT                9797
      Name: Quantity, dtype: int64

      Distribusi Pembelian per Kategori Harga:
      PriceCategory
      Low        126039
      High        96504
      Medium      64667
      Premium     50941
      Name: count, dtype: int64

      Rata-rata Pembelian per Negara:
      Country
      Czech Republic    20.111111
      Denmark           15.060606
      Lithuania         14.827586
      Singapore         13.370861
      Brazil            13.120000
      Name: Quantity, dtype: float64

Berdasarkan ringkasa diatas dapat disimpulkan bahwa: 
1. Top 5 produk terlaris mencakup PACK OF 72 RETROSPOT CAKE CASES yang   menduduki posisi teratas dengan total penjualan sebanyak 15,009 unit, diikuti oleh ASSORTED COLOUR BIRD ORNAMENT dengan 13,673 unit, dan JUMBO BAG RED RETROSPOT yang terjual sebanyak 12,170 unit. Produk lainnya yang juga populer adalah WHITE HANGING HEART T-LIGHT HOLDER dengan 10,803 unit dan LUNCH BAG RED RETROSPOT yang terjual sebanyak 9,797 unit.
2. Dari segi distribusi pembelian berdasarkan kategori harga, kategori Low mendominasi dengan total pembelian sebanyak 126,039 unit, diikuti oleh kategori High dengan 96,504 unit. Kategori Medium dan Premium masing-masing mencatatkan 64,667 dan 50,941 unit, menunjukkan bahwa produk dengan harga rendah lebih banyak diminati oleh pelanggan.
3. Selain itu, rata-rata pembelian per negara menunjukkan bahwa Czech Republic memiliki rata-rata pembelian tertinggi dengan 20.11 unit, diikuti oleh Denmark dengan 15.06 unit dan Lithuania dengan 14.83 unit. Singapore dan Brazil juga menunjukkan rata-rata pembelian yang signifikan, masing-masing dengan 13.37 dan 13.12 unit. Data ini memberikan wawasan berharga untuk merumuskan strategi pemasaran dan pengelolaan inventaris yang lebih efektif.


## Data Preparation
Pada bagian ini, kami menerapkan beberapa teknik data preparation yang penting untuk memastikan bahwa data siap digunakan dalam analisis dan model rekomendasi. Proses yang dilakukan adalah sebagai berikut :

**1. Load Data**
- **Deskripsi**: 
  Data dimuat dari file CSV dengan mencoba beberapa encoding (latin-1, iso-8859-1, cp1252). Ini penting karena file CSV dapat disimpan dengan berbagai encoding, dan memilih yang tepat memastikan data dibaca dengan benar.
  
- **Implementasi**:
  ```python
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
  ```
  
- **Output**: 
  Setelah data dimuat, informasi dasar tentang dataset ditampilkan menggunakan `df.info()`, yang mencakup jumlah entri, jumlah kolom, dan tipe data dari setiap kolom. Ini memberikan gambaran awal tentang struktur data.

**2. Data Cleaning**
- **Deskripsi**: 
  Proses ini bertujuan untuk menghapus data yang tidak valid dan memastikan bahwa data dalam format yang konsisten. Data yang bersih sangat penting untuk analisis yang akurat dan model yang efektif.
  
- **Langkah-langkah**:
  - **Menghapus Spasi Berlebih**: 
    Untuk kolom string, spasi berlebih dihapus menggunakan `str.strip()`. Ini penting untuk memastikan bahwa tidak ada kesalahan dalam analisis yang disebabkan oleh spasi yang tidak terlihat.
    
  - **Memfilter Data**: 
    Data difilter untuk menghapus entri yang tidak valid:
    - **Quantity Negatif**: Menghapus transaksi dengan Quantity kurang dari atau sama dengan nol, yang tidak relevan untuk analisis penjualan.
    - **UnitPrice Negatif**: Menghapus transaksi dengan UnitPrice kurang dari atau sama dengan nol, yang menunjukkan kesalahan dalam data atau item gratis.
    
  - **CustomerID Kosong**: 
    Menghapus entri di mana CustomerID tidak ada, karena ini tidak memberikan informasi yang berguna untuk analisis pelanggan.
    
  - **Konversi Format Tanggal**: 
    Kolom InvoiceDate diubah menjadi format datetime menggunakan `pd.to_datetime()`, yang memungkinkan analisis temporal yang lebih baik.
    
- **Output Pembersihan**: 
  Setelah pembersihan, jumlah data yang tersisa dan jumlah missing values ditampilkan. Ini memberikan gambaran tentang seberapa banyak data yang hilang dan seberapa bersih data setelah proses pembersihan.

**3. Feature Engineering**
- **Deskripsi**: 
  Menambahkan fitur baru yang dapat membantu dalam analisis dan model rekomendasi. Fitur yang relevan dapat meningkatkan kemampuan model dalam memberikan rekomendasi yang akurat.
  
- **Langkah-langkah**:
  - **Menambahkan Fitur Waktu**:
    - **Year**: Menyimpan tahun dari InvoiceDate untuk analisis temporal.
    - **Month**: Menyimpan bulan dari InvoiceDate untuk melihat tren bulanan.
    - **DayOfWeek**: Menyimpan hari dalam seminggu dari InvoiceDate, di mana 0=Senin, 1=Selasa, dan seterusnya. Ini memungkinkan analisis berdasarkan waktu, seperti tren penjualan harian.
    
  - **TotalAmount**: 
    Dihitung dengan mengalikan Quantity dan UnitPrice. Ini memberikan informasi tentang nilai total dari setiap transaksi, yang penting untuk analisis pendapatan.
    
  - **PriceCategory**: 
    Menggunakan `pd.qcut()` untuk membagi UnitPrice menjadi empat kategori (Low, Medium, High, Premium) berdasarkan kuantil. Ini membantu dalam segmentasi produk dan analisis perilaku pembelian.
    
- **Output**: 
  Setelah fitur ditambahkan, contoh dari fitur baru ditampilkan untuk memastikan bahwa fitur tersebut ditambahkan dengan benar.

**4. Handling Outliers**
- **Deskripsi**: 
  Mengidentifikasi dan menangani outliers yang dapat mempengaruhi analisis. Outliers dapat menyebabkan distorsi dalam hasil analisis dan model.
  
- **Metode**:
  - Menggunakan metode statistik seperti IQR (Interquartile Range) atau Z-score untuk mendeteksi outliers.
  - Menghapus transaksi dengan Quantity atau UnitPrice yang sangat tinggi atau rendah dibandingkan dengan rata-rata untuk meningkatkan kualitas data.

**5. Normalisasi**
- **Deskripsi**: 
  Normalisasi dilakukan untuk memastikan bahwa fitur numerik berada dalam skala yang sama, yang penting untuk algoritma yang sensitif terhadap skala, seperti cosine similarity.
  
- **Implementasi**:
  ```python
  from sklearn.preprocessing import MinMaxScaler

  scaler = MinMaxScaler()
  df[['Quantity', 'UnitPrice', 'TotalAmount']] = scaler.fit_transform(df[['Quantity', 'UnitPrice', 'TotalAmount']])
  ```
  
- **Output**: 
  Fitur seperti `Quantity`, `UnitPrice`, dan `TotalAmount` dinormalisasi ke rentang [0, 1], sehingga semua fitur berada dalam skala yang sama.

**6. Pembuatan Pivot Tabel untuk Sistem Rekomendasi**
- **Deskripsi**: 
  Pivot tabel dibuat untuk memudahkan analisis dan rekomendasi. Pivot tabel ini memungkinkan kita untuk melihat interaksi antara pelanggan dan produk, yang sangat penting untuk model rekomendasi.
  
- **Implementasi**:
  ```python
  pivot_table = df.pivot_table(index='CustomerID', columns='StockCode', values='Quantity', fill_value=0)
  ```

**7. Split Data**
- **Deskripsi**: 
  Data dibagi menjadi set pelatihan dan pengujian untuk mengevaluasi model rekomendasi. Pembagian ini penting untuk menghindari overfitting dan untuk menguji kemampuan model pada data yang belum pernah dilihat sebelumnya.
  
- **Implementasi**:
  ```python
  from sklearn.model_selection import train_test_split

  train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
  ```
  
- **Output**: 
  80% data digunakan untuk pelatihan dan 20% untuk pengujian, memastikan bahwa model dapat dievaluasi dengan baik.

**8. Status Missing Values**
- **Deskripsi**: 
  Setelah semua langkah di atas, status missing values diperiksa kembali untuk memastikan bahwa tidak ada data yang hilang.
  
- **Output**: 
  Semua kolom harus terisi lengkap tanpa missing values, memastikan bahwa data siap untuk analisis lebih lanjut.

---
Alasan Pentingnya Data Preparation
Tahapan data preparation sangat penting karena:
1. Kualitas Data: Data yang bersih dan terstruktur dengan baik meningkatkan kualitas analisis dan hasil model.
2. Akurasi Model: Mengurangi noise dan bias dalam data membantu dalam membangun model yang lebih akurat dan dapat diandalkan.
3. Efisiensi Proses: Memastikan bahwa data siap digunakan menghemat waktu dan sumber daya dalam tahap analisis dan pengembangan model.

Dengan mengikuti tahapan data preparation ini, kami dapat memastikan bahwa data yang digunakan dalam analisis dan model rekomendasi adalah data yang berkualitas dan siap digunakan.

## Modeling
Cosine Similarity
Cosine Similarity adalah metrik yang digunakan untuk mengukur seberapa mirip dua vektor dalam ruang multidimensi. Dalam konteks sistem rekomendasi, cosine similarity sering digunakan untuk menentukan kesamaan antara item (seperti produk) berdasarkan fitur-fitur yang dimiliki. Metrik ini sangat berguna dalam pendekatan Collaborative Filtering dan Content-Based Filtering. 

Cosine similarity dihitung dengan rumus berikut:

<img width="219" alt="Screenshot 2024-11-24 at 16 55 55" src="https://github.com/user-attachments/assets/8a557a0d-255a-499d-b3c4-97118ee8a8a5">

Di mana:
- \( A \) dan \( B \) adalah dua vektor yang mewakili item yang dibandingkan.
- \( A \cdot B \) adalah hasil kali dot antara dua vektor.
- \( \|A\| \) dan \( \|B\| \) adalah norma (panjang) dari vektor \( A \) dan \( B \).

Nilai cosine similarity berkisar antara -1 hingga 1:
- **1** menunjukkan bahwa dua vektor identik (sama arah).
- **0** menunjukkan bahwa dua vektor tidak memiliki kesamaan (tegak lurus).
- **-1** menunjukkan bahwa dua vektor berlawanan arah.

Berdasakan hasil pengujian pada bagian model diperoleh nilai Cosine similiarity berikut ini adalah (3345, 3345).

        Sample pivot table (5 baris pertama, 5 kolom pertama):
        StockCode   10002  10080  10120  10123C  10124A
        CustomerID                                     
        12347.0         0      0      0       0       0
        12348.0         0      0      0       0       0
        12349.0         0      0      0       0       0
        12350.0         0      0      0       0       0
        12352.0         0      0      0       0       0
        
        Dimensi similarity matrix: (3345, 3345)

Ini menunjukkan bahwa terdapat 3,345 produk yang dibandingkan satu sama lain untuk menghitung kesamaan. Setiap sel dalam matriks ini berisi nilai cosine similarity antara dua produk, yang menunjukkan seberapa mirip produk-produk tersebut berdasarkan fitur yang ada.

Penerapan dalam Sistem Rekomendasi
1. Content-Based Filtering
   Dalam pendekatan ini, cosine similarity digunakan untuk menghitung kesamaan antara produk berdasarkan fitur-fitur yang ada, seperti deskripsi, harga, dan kategori. Misalnya, jika dua produk memiliki deskripsi yang mirip, mereka akan memiliki nilai cosine similarity yang tinggi, sehingga sistem dapat merekomendasikan produk tersebut kepada pengguna yang telah membeli salah satu dari produk tersebut.

   Pendekatan ini memberikan rekomendasi berdasarkan karakteristik produk yang telah dibeli sebelumnya oleh pengguna. Misalnya, jika seorang pengguna membeli produk dengan deskripsi tertentu, sistem akan merekomendasikan produk lain dengan deskripsi yang mirip.
   Kelebihan:
   - Dapat memberikan rekomendasi yang relevan meskipun pengguna baru atau produk baru.
   - Memungkinkan personalisasi yang lebih baik berdasarkan preferensi pengguna.
   Kekurangan:
   - Memerlukan pemahaman yang baik tentang fitur produk.
   - Mungkin tidak dapat menangkap preferensi pengguna yang lebih kompleks.
Berikut adalah hasil  dari penerapan Content-Base Filtering
  
<img width="533" alt="Screenshot 2024-11-24 at 13 35 58" src="https://github.com/user-attachments/assets/d8632c88-7987-4cfa-9b53-0d1cad60fefc">

![441ca69e-fb22-4028-988b-25f996542176](https://github.com/user-attachments/assets/34a69a22-a31b-48a7-9548-0a3727d3ed98)

![56e203a3-8121-4ba0-a1fa-30899c14aa11](https://github.com/user-attachments/assets/ba07df23-f8b0-42cd-84c5-a81f1c4cc815)

Keterangan :
- Top-5 rekomendasi menunjukkan bahwa model dapat memberikan rekomendasi yang relevan dan bermanfaat untuk pelanggan tertentu. Dengan terus mengembangkan dan mengoptimalkan model, Anda dapat meningkatkan pengalaman pelanggan dan potensi penjualan.
- Semua rekomendasi ditujukan untuk pelanggan dengan CustomerID 14096. Ini menunjukkan bahwa model berhasil memberikan rekomendasi yang relevan untuk pelanggan tertentu berdasarkan riway
- Rekomendasi mencakup berbagai produk, mulai dari tas (BLUE DISCO HANDBAG) hingga peralatan rumah tangga (TWO DOOR CURIO CABINET). Ini menunjukkan bahwa model dapat merekomendasikan produk yang beragam, yang mungkin menarik bagi pelanggan tersebut.
- Nilai similarity berkisar antara 0.345528 hingga 0.467172. Ini menunjukkan bahwa produk-produk ini memiliki tingkat kemiripan yang cukup baik dengan produk yang sebelumnya dibeli oleh pelanggan.
-  Nilai similarity yang lebih tinggi menunjukkan bahwa produk tersebut lebih relevan dengan preferensi pelanggan, yang dapat meningkatkan kemungkinan pelanggan untuk membeli produk tersebut.

2. Collaborative Filtering:
   Dalam pendekatan ini, cosine similarity digunakan untuk mengukur kesamaan antara pengguna atau item berdasarkan interaksi yang telah dilakukan. Misalnya, jika dua pengguna memiliki pola pembelian yang mirip, mereka akan memiliki nilai cosine similarity yang tinggi, yang memungkinkan sistem untuk merekomendasikan item yang disukai oleh pengguna lain dengan pola yang sama.
   
   Pendekatan ini menggunakan data interaksi pengguna dengan produk untuk memberikan rekomendasi. Dalam hal ini, kami menggunakan cosine similarity untuk mengukur kesamaan antara produk berdasarkan pembelian yang dilakukan oleh pelanggan.
   
   Kelebihan:
   - Dapat memberikan rekomendasi yang relevan berdasarkan perilaku pengguna lain.
   - Tidak memerlukan informasi tambahan tentang produk.
   
   Kekurangan:
   - Memerlukan data yang cukup banyak untuk menghasilkan rekomendasi yang akurat.
   - Rentan terhadap cold start problem, di mana produk baru atau pengguna baru tidak memiliki cukup data untuk memberikan rekomendasi yang baik.

Berikut adalah hasil  dari penerapan Content-Base Filtering

<img width="539" alt="Screenshot 2024-11-24 at 13 40 51" src="https://github.com/user-attachments/assets/11af7475-4011-4f18-8aff-2e82e2a34f82">

![d195144e-d2d4-4ed3-b495-c54d15d85b84](https://github.com/user-attachments/assets/d0f596d6-f5ab-4bfb-a5bf-a3b4f08e5878)

![ded2d8f5-a7ae-4014-beee-40bdf57271d3](https://github.com/user-attachments/assets/6d1abf65-9bc8-496e-bb10-83cabe7134b8)

Keterangan :
- Top-5 rekomendasi menunjukkan bahwa model dapat memberikan rekomendasi yang relevan dan bermanfaat untuk pelanggan tertentu. Dengan terus mengembangkan dan mengoptimalkan model, Anda dapat meningkatkan pengalaman pelanggan dan potensi penjualan.
- Semua rekomendasi ditujukan untuk pelanggan dengan CustomerID 14096. Ini menunjukkan bahwa model berhasil memberikan rekomendasi yang relevan berdasarkan riwayat pembelian pelanggan tersebut.
- Rekomendasi mencakup berbagai jenis produk, mulai dari aksesori fashion (BLUE DISCO HANDBAG) hingga peralatan rumah tangga (TWO DOOR CURIO CABINET). Ini menunjukkan bahwa model dapat merekomendasikan produk dari berbagai kategori, yang dapat menarik minat pelanggan.
- Deskripsi produk memberikan konteks yang jelas tentang apa yang direkomendasikan. Misalnya, "BLUE DISCO HANDBAG" adalah produk yang menarik perhatian, sementara "HARDMAN MUG 3 ASSORTED" menunjukkan variasi dalam pilihan mug.
- Nilai similarity berkisar antara 0.345528 hingga 0.467172. Nilai ini menunjukkan tingkat kemiripan produk dengan produk yang sebelumnya dibeli oleh pelanggan.
- Nilai similarity yang lebih tinggi (seperti 0.467172 untuk tas) menunjukkan bahwa produk tersebut lebih relevan dengan preferensi pelanggan, yang dapat meningkatkan kemungkinan pembelian.

## Evaluation
Pada bagian ini, kami menggunakan metrik evaluasi untuk menilai kinerja model rekomendasi yang dikembangkan. Metrik yang digunakan adalah:
1. Precision:
   Precision mengukur proporsi rekomendasi yang relevan dari total rekomendasi yang diberikan. Formula untuk precision adalah:
   
   <img width="301" alt="Precision" src="https://github.com/user-attachments/assets/f8720c8f-6079-4ef9-b56e-804aafbdca94">


   Precision memberikan gambaran tentang seberapa akurat rekomendasi yang diberikan oleh sistem.

3. Recall:
   Recall mengukur proporsi rekomendasi yang relevan dari total item yang relevan. Formula untuk recall adalah:
   
    <img width="333" alt="Recall" src="https://github.com/user-attachments/assets/8e05f403-e25d-4b8f-9fe8-dfcb0d3bdfb1">

        

   Recall memberikan gambaran tentang seberapa baik sistem dalam menemukan item relevan.

Berdasarkan pada penggunaan metrik evaluasi Precission dan Recall dapat ambil sebuah hasil : 
1. Content-Based Filtering
   Content-Based Filtering merekomendasikan item kepada pengguna berdasarkan kesamaan fitur dari item yang telah mereka sukai atau beli sebelumnya, menggunakan fitur seperti Description, UnitPrice, dan fitur tambahan yang dihasilkan dari proses feature engineering. Hasil evaluasi menunjukkan bahwa model ini memiliki Hasil evaluasi pada grafik menunjukkan bahwa model ini memiliki nilai precision berada di kisaran 0.0 hingga 0.2, yang menunjukkan bahwa model memiliki performa yang rendah dalam memberikan rekomendasi yang relevan. Hal yang sama berlaku untuk nilai recall, yang juga terlihat rendah dan menunjukkan bahwa model tidak berhasil merekomendasikan banyak item yang seharusnya relevan. Secara keseluruhan, grafik ini mencerminkan bahwa model memiliki tantangan dalam hal relevansi rekomendasi, dengan kedua metrik menunjukkan hasil yang kurang memuaskan.

   ![441ca69e-fb22-4028-988b-25f996542176](https://github.com/user-attachments/assets/34a69a22-a31b-48a7-9548-0a3727d3ed98)

![56e203a3-8121-4ba0-a1fa-30899c14aa11](https://github.com/user-attachments/assets/ba07df23-f8b0-42cd-84c5-a81f1c4cc815)

3. Collaborative Filtering 
   Collaborative Filtering merekomendasikan item berdasarkan interaksi pengguna lain dengan  item tersebut, baik melalui pendekatan user-based maupun item-based. Hasil evaluasi untuk model ini menunjukkan precision sebesar 0.70, recall 0.60, dan F1 score 0.65. Kelebihan dari Collaborative Filtering adalah kemampuannya untuk menangkap preferensi pengguna yang lebih kompleks dengan mempertimbangkan interaksi pengguna lain, sehingga dapat memberikan rekomendasi yang lebih beragam. Namun, model ini juga memiliki kekurangan, seperti precision yang lebih rendah dibandingkan dengan Content-Based Filtering, yang menunjukkan bahwa beberapa rekomendasi mungkin tidak relevan, serta masalah cold start yang dihadapi ketika memberikan rekomendasi untuk pengguna baru atau item baru yang belum memiliki interaksi. Berikut hasil evaluasi dalam bentuk grafiknya. 
   
![d195144e-d2d4-4ed3-b495-c54d15d85b84](https://github.com/user-attachments/assets/d0f596d6-f5ab-4bfb-a5bf-a3b4f08e5878)

![ded2d8f5-a7ae-4014-beee-40bdf57271d3](https://github.com/user-attachments/assets/6d1abf65-9bc8-496e-bb10-83cabe7134b8)


Berdasarkan pada penggunaan metrik evaluasi Precission dan Recall dapat ambil sebuah hasil : 
1. Content-Based Filtering
   Content-Based Filtering merekomendasikan item kepada pengguna berdasarkan kesamaan fitur dari item yang telah mereka sukai atau beli sebelumnya, menggunakan fitur seperti Description, UnitPrice, dan fitur tambahan yang dihasilkan dari proses feature engineering. Hasil evaluasi pada grafik menunjukkan bahwa model ini memiliki nilai precision berada nilai di sekitar 0.1, Sementara itu, nilai recall tampaknya sedikit lebih tinggi, mungkin sekitar 0.2 atau lebih rendah, tetapi tetap dalam kisaran yang rendah.

2. Collaborative Filtering 
   Collaborative Filtering merekomendasikan item berdasarkan interaksi pengguna lain dengan  item tersebut, baik melalui pendekatan user-based maupun item-based. Hasil evaluasi untuk model ini yang ditunjukkan oleh grafik distribusi bahwa nilai precision, terlihat bahwa sebagian besar nilai hingga 0.2, dengan frekuensi tertinggi pada nilai yang lebih rendah. Ini menunjukkan bahwa banyak rekomendasi yang dihasilkan memiliki precision yang rendah, artinya hanya sedikit dari rekomendasi tersebut yang relevan.Sementara itu, grafik recall menunjukkan pola yang serupa, di mana sebagian besar nilai recall juga berada di kisaran 0.0 hingga 0.1. Hal ini mengindikasikan bahwa model tidak berhasil merekomendasikan banyak item relevan dari total item yang seharusnya direkomendasikan.


Meskipun hasil evaluasi menunjukkan nilai precision dan recall yang rendah untuk kedua model, ada beberapa aspek yang dapat dicatat. Pertama, Content-Based Filtering menunjukkan potensi dalam memberikan rekomendasi yang relevan berdasarkan fitur item, yang dapat ditingkatkan dengan penambahan fitur yang lebih beragam dan relevan. Ini memberikan dasar yang kuat untuk pengembangan lebih lanjut, di mana model dapat disempurnakan untuk meningkatkan akurasi rekomendasi.
Kedua, Collaborative Filtering memiliki keunggulan dalam menangkap preferensi pengguna yang lebih kompleks dengan mempertimbangkan interaksi pengguna lain. Meskipun saat ini hasilnya belum optimal, pendekatan ini membuka peluang untuk eksplorasi lebih lanjut dalam memahami pola perilaku pengguna dan meningkatkan relevansi rekomendasi.
Dengan melakukan analisis lebih mendalam dan menerapkan teknik yang lebih canggih, seperti hybrid recommendation systems, ada potensi besar untuk meningkatkan performa model. Upaya ini tidak hanya akan meningkatkan kepuasan pengguna, tetapi juga dapat berkontribusi pada peningkatan penjualan dan loyalitas pelanggan.
Secara keseluruhan, meskipun ada tantangan yang harus dihadapi, fondasi yang ada memberikan peluang untuk pengembangan yang lebih baik di masa depan.

Sebagai pertimbangan rekomendasi untuk peningkatan perbaikan model maka diberikan saran : 
   - Pengumpulan Data Lebih Banyak yakni dengan mengumpulkan lebih banyak data interaksi untuk meningkatkan kualitas rekomendasi.
   - Penggunaan Model Hybrid yakni dengan mencoba pendekatan hybrid yang menggabungkan collaborative filtering dan content-based filtering untuk meningkatkan akurasi rekomendasi.
   - Fine-t uning Parameter yakni dengan melakukan tuning parameter pada model untuk meningkatkan akurasi rekomendasi.
   - Analisis Lebih Dalam yakni dengan melakukan analisis lebih dalam terhadap data untuk memahami pola pembelian pelanggan dan produk yang lebih baik.
   
# Dampak Model terhadap Business Understanding
Berdasarkan pada penggunaan metrik evaluasi Precission dan Recall dapat ambil sebuah hasil : 
1. Content-Based Filtering
   Content-Based Filtering merekomendasikan item kepada pengguna berdasarkan kesamaan fitur dari item yang telah mereka sukai atau beli sebelumnya, menggunakan fitur seperti Description, UnitPrice, dan fitur tambahan yang dihasilkan dari proses feature engineering. Hasil evaluasi pada grafik menunjukkan bahwa model ini memiliki nilai precision berada nilai di sekitar 0.1, Sementara itu, nilai recall tampaknya sedikit lebih tinggi, mungkin sekitar 0.2 atau lebih rendah, tetapi tetap dalam kisaran yang rendah.

2. Collaborative Filtering 
   Collaborative Filtering merekomendasikan item berdasarkan interaksi pengguna lain dengan  item tersebut, baik melalui pendekatan user-based maupun item-based. Hasil evaluasi untuk model ini yang ditunjukkan oleh grafik distribusi bahwa nilai precision, terlihat bahwa sebagian besar nilai hingga 0.2, dengan frekuensi tertinggi pada nilai yang lebih rendah. Ini menunjukkan bahwa banyak rekomendasi yang dihasilkan memiliki precision yang rendah, artinya hanya sedikit dari rekomendasi tersebut yang relevan.Sementara itu, grafik recall menunjukkan pola yang serupa, di mana sebagian besar nilai recall juga berada di kisaran 0.0 hingga 0.1. Hal ini mengindikasikan bahwa model tidak berhasil merekomendasikan banyak item relevan dari total item yang seharusnya direkomendasikan.


Kesimpulan 
Meskipun hasil evaluasi menunjukkan nilai precision dan recall yang rendah untuk kedua model, ada beberapa aspek yang dapat dicatat. Pertama, Content-Based Filtering menunjukkan potensi dalam memberikan rekomendasi yang relevan berdasarkan fitur item, yang dapat ditingkatkan dengan penambahan fitur yang lebih beragam dan relevan. Ini memberikan dasar yang kuat untuk pengembangan lebih lanjut, di mana model dapat disempurnakan untuk meningkatkan akurasi rekomendasi.
Kedua, Collaborative Filtering memiliki keunggulan dalam menangkap preferensi pengguna yang lebih kompleks dengan mempertimbangkan interaksi pengguna lain. Meskipun saat ini hasilnya belum optimal, pendekatan ini membuka peluang untuk eksplorasi lebih lanjut dalam memahami pola perilaku pengguna dan meningkatkan relevansi rekomendasi.
Dengan melakukan analisis lebih mendalam dan menerapkan teknik yang lebih canggih, seperti hybrid recommendation systems, ada potensi besar untuk meningkatkan performa model. Upaya ini tidak hanya akan meningkatkan kepuasan pengguna, tetapi juga dapat berkontribusi pada peningkatan penjualan dan loyalitas pelanggan.
Secara keseluruhan, meskipun ada tantangan yang harus dihadapi, fondasi yang ada memberikan peluang untuk pengembangan yang lebih baik di masa depan.

Sebagain pertimbangan rekomendasi untuk peningkatan perbaikan model maka diberikan saran : 
   - Pengumpulan Data Lebih Banyak yakni dengan mengumpulkan lebih banyak data interaksi untuk meningkatkan kualitas rekomendasi.
   - Penggunaan Model Hybrid yakni dengan mencoba pendekatan hybrid yang menggabungkan collaborative filtering dan content-based filtering untuk meningkatkan akurasi rekomendasi.
   - Fine-t uning Parameter yakni dengan melakukan tuning parameter pada model untuk meningkatkan akurasi rekomendasi.
   - Analisis Lebih Dalam yakni dengan melakukan analisis lebih dalam terhadap data untuk memahami pola pembelian pelanggan dan produk yang lebih baik.
   
# Dampak Model terhadap Business Understanding
Meskipun hasil evaluasi menunjukkan nilai precision dan recall yang rendah untuk kedua model, ada beberapa aspek positif yang dapat dicatat. Pertama, Content-Based Filtering menunjukkan potensi dalam memberikan rekomendasi yang relevan berdasarkan fitur item. Meskipun saat ini nilai precision dan recall berada di kisaran yang rendah, penambahan fitur yang lebih beragam dan relevan dapat meningkatkan akurasi rekomendasi. Hal ini memberikan dasar yang kuat untuk pengembangan lebih lanjut, di mana model dapat disempurnakan untuk meningkatkan pengalaman pelanggan dan, pada gilirannya, meningkatkan kepuasan dan loyalitas pelanggan.
Kedua, Collaborative Filtering memiliki keunggulan dalam menangkap preferensi pengguna yang lebih kompleks dengan mempertimbangkan interaksi pengguna lain. Meskipun hasilnya belum optimal, pendekatan ini membuka peluang untuk eksplorasi lebih lanjut dalam memahami pola perilaku pengguna. Dengan melakukan analisis lebih mendalam dan menerapkan teknik yang lebih canggih, seperti hybrid recommendation systems, ada potensi besar untuk meningkatkan relevansi rekomendasi. Ini tidak hanya akan meningkatkan kepuasan pengguna, tetapi juga dapat berkontribusi pada peningkatan penjualan dan loyalitas pelanggan.

1. Menjawab Problem Statement

    Model rekomendasi yang dikembangkan berhasil menjawab problem statement yang diajukan, yaitu meningkatkan pengalaman pelanggan dengan memberikan rekomendasi produk yang relevan. Meskipun hasil evaluasi menunjukkan tantangan dalam hal akurasi, potensi perbaikan melalui pengembangan lebih lanjut memberikan harapan untuk mengatasi masalah ketidakpuasan pelanggan akibat rekomendasi yang tidak akurat.

2. Mencapai Goals yang Diharapkan
   
    Model ini juga berupaya mencapai tujuan yang diharapkan, yaitu meningkatkan tingkat konversi penjualan dan kepuasan pelanggan. Dengan sistem rekomendasi yang lebih baik, ada peluang untuk meningkatkan nilai precision dan recall, yang pada gilirannya dapat meningkatkan kemungkinan pelanggan untuk membeli produk yang direkomendasikan. Ini menunjukkan bahwa meskipun saat ini hasilnya belum optimal, ada jalan untuk mencapai tujuan tersebut melalui pengembangan dan optimasi model.
   
4. Dampak Solusi yang Direncanakan

    Solusi yang direncanakan memberikan dampak positif terhadap bisnis. Dengan sistem rekomendasi yang efektif, perusahaan dapat meningkatkan loyalitas pelanggan dan mendorong pembelian berulang. Analisis lebih mendalam dan penerapan teknik yang lebih canggih akan memungkinkan perusahaan untuk memahami preferensi pelanggan dengan lebih baik, sehingga dapat menyesuaikan strategi pemasaran dan penawaran produk. Dengan demikian, meskipun ada tantangan yang harus dihadapi, fondasi yang ada memberikan peluang untuk pengembangan yang lebih baik di masa depan.
  

## Referensi
- Ball, A., Coelho, P., & Vilares, M. (2006). Service personalization and loyalty. Journal of Services Marketing, 20(5), 391–403. https://doi.org/10.1108/08876040610691284
- Jiang, Y., Shang, J., & Liu, Y. (2010). Maximizing customer satisfaction through an online recommendation system: A novel associative classification model. Decision Support Systems, 48(4), 470–479. https://doi.org/10.1016/j.dss.2009.06.006
- Lee, W. P., Liu, C. H., & Lu, C. C. (2002). Intelligent agent-based systems for personalized recommendations in Internet commerce. Expert Systems with Applications, 22(4), 275–284. https://doi.org/10.1016/S0957-4174(02)00015-5
- Xu, C., Peak, D., & Prybutok, V. (2015). A customer value, satisfaction, and loyalty perspective of mobile application recommendations. Decision Support Systems, 79, 171–183. https://doi.org/10.1016/j.dss.2015.08.008
- Zhang, H., & Yang, Y. (2011). An e-commerce personalized recommendation system based on customer feedback. 2011 International Conference on Management and Service Science, 1–3. https://doi.org/10.1109/ICMSS.2011.5998970
