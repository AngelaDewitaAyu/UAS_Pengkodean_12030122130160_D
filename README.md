# UAS Mata Kuliah Pengkodean dan Pemrograman

<br> Nama  : Angela Dewita Ayu
<br> NIM   : 12030122130160
<br> Kelas : D

Kasus : Menganalisis Pengaruh Diskon, Jumlah Followers Influencer dan Review Terhadap Unit Penjualan

<br> Sumber data 
<br> Dataset 1 : Penjualan dan Diskon
| Nama Produk            | Unit Penjualan | Platform Penjualan | Diskon | Harga Setelah Diskon |
|------------------------|----------------|--------------------|--------|----------------------|
| Gentle Cleanser        | 900            | Shopee             | 10%    | 135000               |
| Brightening Toner      | 1000           | Tokopedia          | 15%    | 127500               |
| Vitamin C Serum        | 1500           | Lazada             | 20%    | 240000               |
| Hydrating Moisturizer  | 500            | Sociolla           | 5%     | 190000               |
| Sunscreen SPF 50       | 900            | Blibli             | 10%    | 162000               |
| Acne Spot Treatment    | 700            | JD.ID              | 25%    | 112000               |
| Retinol Night Cream    | 600            | Shopee             | 30%    | 245000               |
| Eye Cream              | 1100           | Tokopedia          | 10%    | 189000               |
| Exfoliating Scrub      | 950            | Lazada             | 15%    | 127500               |
| Sheet Mask (Pack of 5) | 1300           | Sociolla           | 20%    | 120000               |

<br> Dataset 2 : Penjualan dan Jumlah Followers Influencer
| Nama Produk            | Unit Penjualan | Nama Influencer    | Jumlah Followers | Platform Penjualan |
|------------------------|----------------|--------------------|------------------|---------------------|
| Gentle Cleanser        | 1200           | Beauty_ Enthusiast | 500000           | Shopee              |
| Brightening Toner      | 1000           | Skincare_Lover     | 750000           | Tokopedia           |
| Vitamin C Serum        | 900            | Glowing _Goddess   | 1200000          | Lazada              |
| Hydrating Moisturizer  | 750            | Radiant_ Beauty    | 2000000          | Sociolla            |
| Sunscreen SPF 50       | 1100           | Sun_Safe_Queen     | 800000           | Blibli              |
| Acne Spot Treatment    | 900            | Clear Skin Goals   | 600000           | JD.ID               |
| Retinol Night Cream    | 1500           | Youthful_Glow      | 400000           | Shopee              |
| Eye Cream              | 1000           | Bright_Eyes        | 900000           | Tokopedia           |
| Exfoliating Scrub      | 850            | Smooth Skin Secrets| 700000           | Lazada              |
| Sheet Mask (Pack of 5) | 1500           | Masking_Maven      | 1500000          | Sociolla            |

<br> Dataset 3 : Penjualan dan Review
| Nama Produk              | Unit Penjualan | Platform Review | Review (Bintang) |
|--------------------------|----------------|-----------------|------------------|
| Gentle Cleanser          | 1100           | FD Studio       | 4,5              |
| Brightening Toner        | 950            | Female Daily    | 4,2              |
| Vitamin C Serum          | 1400           | Sociolla        | 4,8              |
| Hydrating Moisturizer    | 1700           | MakeupAlley     | 4,6              |
| Sunscreen SPF 50         | 1000           | Beautynesia     | 4,3              |
| Acne Spot Treatment      | 850            | FD Studio       | 4,1              |
| Retinol Night Cream      | 750            | Female Daily    | 4,4              |
| Eye Cream                | 1200           | Sociolla        | 4,7              |
| Exfoliating Scrub        | 1050           | MakeupAlley     | 4                |
| Sheet Mask (Pack of 5)   | 1500           | Beautynesia     | 4,9              |

## Visualisasi Data
- Scatterplot Penjualan dan Harga Diskon


![scatter2_penjualan_diskon](https://github.com/AngelaDewitaAyu/UAS_Pengkodean_12030122130160_D/assets/167239973/c56b0cb8-b8ed-4ffd-a421-c3baa9c3e666)


- Scatterplot Penjualan dan Jumlah Followers Influencer
![scatter3_penjualan_followers](https://github.com/AngelaDewitaAyu/UAS_Pengkodean_12030122130160_D/assets/167239973/a53d83b4-cdb2-492e-bc51-457dd5467a27)


- Scatterplot Penjualan dan Review
![scatter1_penjualan_review](https://github.com/AngelaDewitaAyu/UAS_Pengkodean_12030122130160_D/assets/167239973/ea823494-ff74-4cef-a106-f382df261e82)

- Pie Chart Komposisi Produk terhadap Penjualan
![pie1_penjualan_namaproduk](https://github.com/AngelaDewitaAyu/UAS_Pengkodean_12030122130160_D/assets/167239973/c907743c-7ca2-43fe-9908-b32771d318b2)
  
- Pie Chart Komposisi Platform Review terhadap Penjualan
![pie2_penjualan_platformreview](https://github.com/AngelaDewitaAyu/UAS_Pengkodean_12030122130160_D/assets/167239973/7e3058fe-0e29-4a29-84ff-8105813939f5)

- Pie Chart Komposisi Platform Penjualan terhadap Penjualan
![pie3_penjualan_platformpenjualan](https://github.com/AngelaDewitaAyu/UAS_Pengkodean_12030122130160_D/assets/167239973/56b684a2-08b2-459e-94d7-61043413ffca)

- Histogram Distribusi Unit Penjualan
![histogram](https://github.com/AngelaDewitaAyu/UAS_Pengkodean_12030122130160_D/assets/167239973/251a8470-cfe2-4286-90e4-2ecde8590091)

- Heatmap
![heatmap](https://github.com/AngelaDewitaAyu/UAS_Pengkodean_12030122130160_D/assets/167239973/a1bc7d1b-d688-4b88-bb14-0fcaf71f9010)



## Hasil Analisis
1. Scatterplot: Scatterplot menunjukan pengaruh beberapa faktor terhadap unit penjualan. Berdasarkan ke-3 scatterplot tersebut, terlihat hubungan positif antara review dan unit penjualan meski cenderung memiliki korelasi yang cenderung lemah. Produk dengan rating tinggi maupun rendah bisa memiliki penjualan yang tinggi atau rendah. Sehingga dapat disimpulkan bahwa terdapat faktor lain yang berpengaruh terhadap penjualan. Sedangkan pada faktor lainnya, scatterplot menunjukan tidak ada korelasi dengan unit penjualan.
2. Pie Chart : Pie Chart menunjukan komposisi yang berkontribusi paling banyak terhadap unit penjualan. Hasil visualisasi menunjukkan bahwa produk Sheet Mask mendominasi penjualan sebesar 13,8% dari total penjualan sebanyak 31.650 unit. Platform penjualan seperti Shopee dan Tokopedia mendominasi penjualan sebanyak 15,9% dan 22,2%, sementara platform lain memiliki porsi yang lebih kecil. Selain itu dapat disimpulkan bahwa review pada MakeupAlley paling mempengaruhi keputusan pembeli menggunakan produk
3. Histogram : Berdasarkan visualisasi data tersebut, dalam data terdapat puncak distribusi di rentang penjualan tertentu. Misalnya, banyak produk memiliki penjualan sekitar 900 unit.Standar deviasi dari data menunjukkan adanya variabilitas dalam unit penjualan. Produk memiliki penjualan yang bervariasi dari beberapa ratus hingga beberapa ribu unit. Distribusi dapat menunjukkan skewness, misalnya skewed ke kanan, yang berarti ada beberapa produk dengan penjualan yang sangat tinggi dibandingkan dengan sebagian besar produk lainnya.
4. Heatmap: Visualisasi menunjukkan nilai korelasi antara unit penjualan dan harga setelah diskon menunjukkan korelasi positif atau negatif tergantung pada bagaimana harga setelah diskon disesuaikan dengan diskon yang diberikan. Korelasi yang rendah menunjukkan bahwa harga setelah diskon mungkin tidak banyak mempengaruhi penjualan.

## Kesimpulan
Berdasarkan analisis yang sudah dilakukan, dapat diketahui bahwa 	produk Sheet mask(pack of 5) berkontribusi paling banyak pada total penjualan. Selain itu, e-commerce Shopee dan Tokopedia menyumbang pendapatan terbanyak dibanding e-commerce lainnya.
Dalam upaya meningkatkan jumlah unit penjualan, perusahaan memberikan harga diskon dan bekerjasama dengan influencer. Namun, analisis menunjukan bahwa harga diskon dan pengaruh influencer tidak serta merta menaikkan penjualan	Dalam penelitian ini, terdapat faktor lainnya yang berpengaruh menentukan unit penjualan yaitu review dari pelanggan. Scatterplot menunjukkan bahwa semakin tinggi review semakin tinggi tingkat penjualannya. 
Oleh karena itu, penulis menyimpulkan bahwa untuk penjualan periode selanjutnya, fokus perusahaan adalah pada pengembangan dan inovasi produk terutama produk pada unggulannya yaitu Sheet Mask dan mengutamakan kepuasan pelanggan mendapat review baik dari pelanggan untuk meningkatkan unit penjualan. 
.


