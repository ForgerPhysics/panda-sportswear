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
