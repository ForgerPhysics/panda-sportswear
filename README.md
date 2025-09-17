Tugas 2: Implementasi Model-View-Template (MVT) pada Django  
Nama : Ryan Gibran Purwacakra Sihaloho  
Kelas : PBP - C  
NPM : 2406419833  
Link PWS: https://ryan-gibran-pandasportswear.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

   Secara umum, saya mengikuti materi pada tutorial untuk menyelesaikan checklist, hanya saja alurnya tidak sama persis seperti di tutorial. Ada beberapa langkah yang dilompati dan dilakukan berulang agar mengikuti sesuai checklist. Selain tutorial, saya juga membuka beberapa materi pada checklist di internet untuk mendapat referensi tambahan. Berikut adalah langkah-langkah yang saya lakukan:

   1. Membuat direktori lokal dan menginisiasi proyek django
   2. Membuat aplikasi django bernama main
   3. Menambahkan aplikasi main ke dalam proyek (routing pada proyek agar aplikasi main dapat berjalan)
   4. Mengubah berkas models dengan menambahkan atribut sesuai persyaratan. Setelah itu, dilakukan migrasi database.
   5. Membuat file template html
   6. Menulis fungsi pada views.py untuk return ke template HTML
   7. Melakukan deployment ke PWS
   8. Membuat file readme
   9. Push ke direktori github

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   ![bagan request client](assets/request%20django.png)

   HTTP Request
   User mengakses sebuah URL, kemudian browser mengirim HTTP req ke server django

   URLS (urls.py)
   Django menerima permintaan HTTP request dan melihat berkas file urls.py. Django akan memeriksa URL yang diminta oleh user dan mencocokkannya dengan pola URL yang telah ditulis didalam file urls.py.

   View (views.py)
   Setelah menemukan pola URL yang cocok, urls.py akan forward permintaan tersebut ke fungsi View yang sesuai di dalam file views.py.
   Fungsi view akan memutuskan apa yang harus dilakukan selanjutnya. Berdasarkan permintaan dari user, view bisa melakukan beberapa hal, di antaranya:

   1. Berinteraksi dengan Model: Jika http req tersebut memerlukan data dari database (misalnya, menampilkan daftar produk), maka view akan berkomunikasi dengan Model.
   2. Merender Template: View akan mengambil data yang diperlukan dan memasukkannya ke dalam sebuah Template untuk menghasilkan halaman HTML.

   Model (models.py)
   Model adalah representasi dari data aplikasi. Simpelnya, setiap model biasanya mewakili satu tabel dalam database. View menggunakan model untuk melakukan operasi database seperti:
   -Membaca data (read): Mengambil informasi dari database (contoh: mengambil data produk).
   -Menulis data (write): Menyimpan, memperbarui, atau menghapus data di database.

   Template (.html)
   Template adalah file HTML yang memiliki "ruang kosong" untuk diisi dengan data dinamis(berganti-ganti). View akan mengambil data yang didapat dari Model, lalu memasukkannya ke dalam runag kosong di file Template. Proses ini disebut "rendering". Hal ini dilakukan untuk memisahkan logika (di View) dengan tampilan (di Template).

   HTTP Response (Respons HTTP)
   Setelah Template selesai di-render dan menjadi file HTML utuh, View akan "membungkus" HTML dalam sebuah HTTP Response. Respon ini dikirim ke browser pengguna. Browser menerima HTML ini dan menampilkannya sebagai halaman web yang bisa dilihat oleh user.

3. Jelaskan peran settings.py dalam proyek Django!

   File settings.py berisi modul python dengan module-level variable. File ini berisi sebagai tempat mengkonfigurasi untuk seluruh pyoek yang akan menentukan bagaimana proyek djago akan berjalan.

4. Bagaimana cara kerja migrasi database di Django?

   migrasi database membantu kita untuk mengubah struktur database secara bertahap. Ada 2 command yang dilakukan dalam migrasi database Django:

   1. python manage.py makemigrations  
      Django membandingkan kondisi models.py saat ini dengan saat command migrasi terakhir. Dari perbandingan itu, Django menghasilkan sebuah file Python baru di dalam direktori migrations. File python tersebut berisi "daftar" perubahan apa saja yang perlu dilakukan untuk memperbarui database. perintah ini masih belum mengubah database proyek kita.
   2. python manage.py migrate  
      Django memeriksa tabel khusus di database bernama django_migrations untuk melihat migrasi mana yang sudah diterapkan. Kemudian, Django mencari file migrasi baru yang belum ada di catatan tersebut. Django membaca instruksi dari file migrasi baru, lalu mengubah instruksi menjadi perintah SQL yang sesuai berdasarkan hasil perbandingan, lalu mengeksekusi perintah SQL di database. Pada tahap ini, stuktur database project kita telah diupdate ke versi terbaru.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
   1. Struktur teratur  
      Django menerapkan arsitektur MVT (model-view-template) yang memaksa developer pemula menempatkan kode di tempatnya yang sesuai.
   2. Serba lengkap  
      Django memiliki banyak fungsionalitas siap pakai yang dibutuhkan dalam pengembangan web modern. Ini termasuk Object-Relational Mapper (ORM) untuk interaksi database, sistem autentikasi pengguna, panel admin yang dibuat secara otomatis, sistem routing, template engine, dan perlindungan keamanan. Hal ini mempercepat proses pengembangan karena kita tidak perlu membangun semuanya dari nol atau mencari banyak library pihak ketiga.
   3. Menggunakan bahasa pemrograman python  
      Bahasa python adalah bahasa pemrograman yang mudah dipahami dan digunakan oleh developer pemula. Karena itu menggunakan django untuk belajar software development adalah pilihan yang bagus.
   4. Komunitas luas  
      Ketika belajar software development, tidak jarang pemula akan menemukan error ataupun kebingungan untuk melakukan sesuatu yang diinginkan. Dengan adanya dukungan komunitas, pemmula bisa bertanya dan mencari jawaban di forum dibanding melakukan percobaan percobaan yang menambahkan error dan membuang waktu.
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

   Tutorial 1 dilakukan secara online. Saya merasa cukup menyenangkan menjalani tutorial online seperti ini, karena tidak perlu untuk mengerjakan di lab dengan kondisi suasana cukup berisik (yang adalah wajar karena banyak juga yang masih bingung dan mengalami error). Dengan tutorial online, saya bisa berkomunikasi dengan asdos secara cepat melalui discord jika dibutuhkan tanpa harus "menunggu" asdos datang ke meja seperti ketika tutorial offline. Pada tutorial 1, saya merasa asdos telah melakukan pekerjaannya dengan cukup baik, karna saya melihat asdos stay di room discord dan menyampaikan bahwa asdos bersedia dihubungi pada sesi tutorial untuk tanya jawab. Semoga asdos bisa tetap semangat dan sabar membimbing mahasiswa pbp tahun ajaran ini.

<br></br>
Tugas 3: Implementasi Form dan Data Delivery pada Django  
Nama : Ryan Gibran Purwacakra Sihaloho  
Kelas : PBP - C  
NPM : 2406419833  
Link PWS: https://ryan-gibran-pandasportswear.pbp.cs.ui.ac.id/  
  
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?  
   Data delivery adalah proses pengiriman data dari satu sistem (source) ke sistem lain (target) secara efisien dan aman. Dalam platform, proses ini penting karena platform tidak dapat berfungsi optimal tanpa data yang akurat dan tepat waktu.Beberapa alasan kita memerlukan data delivery adalah:  
   1) Memastikan Fungsionalitas Inti Platform  
   Platform seringkali harus terhubung ke sistem lawas yang didevelop sudah cukup lama. Data delivery membantu platform mendapatkan data ini agar bisa ditampilkan ke user.  
   Contoh:  
   mobile banking perlu terima pengiriman data saldo nasabah, riwayat transaksi, dan informasi pinjaman dari sistem perbankan inti (core banking system) untuk menampilkan informasi tersebut dengan tepat kepada user
   2) Mendukung Skalabilitas dan Pertumbuhan  
   Semakin lama proses bisnis berlangsung dan berdiri, volume data yang disimpan meningkat drastis. Arsitektur data delivery dirancang untuk menangani peningkatan beban kerja dan memastikan platform responsif meski jumlah pengguna atau transaksinya bertambah
   3) Memungkinkan Pengambilan Keputusan Real-Time  
   Data delivery membuat data mengalir secara real-time atau mendekati real-time ke dasbor analitik atau sistem business intelligence (BI)
   Contoh:  
   Platform logistik butuh data lokasi GPS dari setiap kendaraan armana secara live untuk mengoptimalkan rute pengiriman dan memberi estimasi waktu kedatangan yang akurat kepada customer. 
    
   Referensi:
   Designing Data-Intensive Applications" oleh Martin Kleppmann
   https://www.fanruan.com/en/glossary/big-data/data-delivery
   https://medium.com/orchestras-data-release-pipeline-blog/principles-of-effective-data-delivery-how-ci-cd-should-look-for-data-teams-miniseries-part-3-396deb5af97a 
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?  
   Untuk konsep pengembangan web, json lebih baik dalam hal ini. Beberapa alasannya adalah:  
   1) Dibanding xml, json lebih ringkas merepresentasikan data yang sama
   2) Struktu rdata lebih sesuai dengan API. API digunakan untuk mengirim dan menerima data terstruktur seperti informasi pengguna, produk, atau status. Struktur pasangan key-value dan array pada JSON cocok untuk merepresentasikan data
   3) Mudah dibaca dan ditulis
   4) Cocok dengan penggunaan javascript  
   JSON adalah notasi objek JavaScript. Ini membua json mudah digunakan dalam pengembangan web, di mana JavaScript adalah bahasa yang sering dipakai. Mengubah data JSON menjadi objek JavaScript (dan sebaliknya) dapat dilakukan dengan satu command baris kode(cari kodenya), tanpa memerlukan library eksternal.
3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?  
Metode is_valid memeriksa kesesuaian data, membersihkan, dan menyiapkan data sebelum dikelola oleh developer. 
Kita membutuhkan method tersebut karena:  
   1) Mencegah Data yang Tidak Valid .  
   Tanpa validasi kemanan, bisa saja aplikasi menerima sql injection. Tanpa intergari, bisa saja aplikasi menerima data yang tidak sesuai (seperti umur disimpan dalam string, nomor telepon terdapat abjad, dsb) yang menyebabkan database rusak
   2) Menyediakan data yang siap dipakai.  
   Sebelum menggunakan method, Data dari form (request.POST) masih berupa string mentah. Sesudah menggunakan method, Data di form.cleaned_data (dictionary Python yang berisi data yang sudah divalidasi dan dikonversi ke tipe data yang sesuai) sudah aman dan dalam format Python yang sesuai, bisa untuk disimpan ke database atau diolah lagi.
4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?  
   Kita butuh csrf_token di form Django untuk melindungi situs web dan penggunanya dari serangan Cross-Site Request Forgery (CSRF). Token ini berfungsi sebagai "tanda pengenal rahasia" yang memastikan request yang dikirim melalui form benar-benar berasal dari situs web yang dibuat, bukan dari situs lain yang berbahaya.  
   Jika kita tidak menyertakan {% csrf_token %} pada form, situs akan menjadi rentan terhadap serangan CSRF. Ini berarti seorang penyerang bisa "menipu" browser user yang sedang login di situs kita untuk mengirim request palsu tanpa sepengetahuan user.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   1)  Menambahkan 4 fungsi views baru untuk melihat produk yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID. Kemudian Membuat routing masing masing URL keempat fungsi views.
   2)  Membuat halaman untuk menampilkan data objek model yang memiliki tombol "Add" yang akan mengarah ke halaman form, dan tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek pada main/templates/main.html
   3)  Membuat halaman form untuk menambahkan objek model pada app sebelumnya pada berkas forms.py. Jenis data yang ingin diminta dari user akan diletakkan pada list field.
   4)  Membuat halaman yang menampilkan detail dari setiap data objek model dengan membuat berkas create_product.html dan product_detail.html
6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?  
Tidak ada
7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![POSTMAN_XML](<assets/postman_xml.png>) 
![POSTMAN_JSON](<assets/postman_json.png>) 
![POSTMAN_XML_ID](<assets/postman_xml_id.png>) 
![POSTMAN_JSON_ID](<assets/postman_json_id.png>)
![weblocalhost](<assets/web_localhost.png>)