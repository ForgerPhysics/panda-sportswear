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
  
<br></br>
Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django  
Nama : Ryan Gibran Purwacakra Sihaloho  
Kelas : PBP - C  
NPM : 2406419833  
Link PWS: https://ryan-gibran-pandasportswear.pbp.cs.ui.ac.id/

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.  
   AuthenticationForm adalah sebuah kelas formulir bawaan framework Django yang dirancang  untuk proses autentikasi / login user. Cara kerjanya adalah sebagai "sebuah formulir untuk memasukkan user ke dalam sistem" (A form for logging a user in). Formulir ini memberikan fungsi standar yang diperlukan untuk memverifikasi kredensial (username dan password) yang dimasukkan oleh user.  
   Secara default, formulir ini memiliki dua field: username dan password. Ketika user mengirim data melalui formulir ini, AuthenticationForm akan melakukan validasi untuk memeriksa apakah nama user tersebut ada dan apakah kata sandi yang diberikan cocok.
2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?    
   **Autentikasi** merupakan proses verifikasi "siapa" akun ini.  
   Tujuan: Memverifikasi dan memastikan identitasuser  
   Proses: Memeriksa kredensial seperti username & password, token, biometrik, dan sebagainya  
   Contoh: Proses login ke akun SSO UI pada scele.  
   **Otorisasi** merupakan proses verifikasi bahwa akun tersebut memiliki akses terhadap sesuatu  
   Tujuan: Menentukan hak akses atau izin yang dimiliki user terhadap resource yang ada pada organisasi/perusahaan.  
   Proses: Memeriksa aturan, role, atau grup yang melekat pada identitas user.  
   Contoh: Seorang "Admin" bisa membaca menulis, mengedit, dan menghapus unggahan, sementara "User" biasa hanya bisa membaca.  
   **Implementasi Autentikasi** pada Django:  
   Django menangani autentikasi melalui model User dan beberapa fungsi helper.  
   Komponen Inti yang digunakan:  
   a. Model User: Model bawaan yang memiliki kolom seperti username, password (disimpan dalam bentuk hash), email, first_name, last_name, dan berbagai atribut lainnya berdasarkan pendefinisian model  
   b. Fungsi authenticate(): Fungsi ini menerima request, username, dan password. Jika kredensial valid, fungsi akan mereturn objek User. Jika tidak, fungsi mereturn None.  
   c. Fungsi login(): Setelah authenticate() berhasil, fungsi akan membuat sesi untuk user, sehingga pada request berikutnya, user akan dikenali sebagai login.  
   d. Fungsi logout(): Menghapus data sesi user.  
   *Bentuk implementasi*  
   Cara Melindungi Halaman (Views):  
   Django menyediakan cara mudah untuk membatasi akses ke halaman hanya untuk pengguna yang sudah login.  
   Untuk Untuk Function-Based Views (FBV), kita bisa gunakan decorator @login_required sementara untuk Class-Based Views (CBV), kita bisa pakai LoginRequiredMixin  
   **Implementasi Otorisasi** pada Django:  
   Otorisasi di Django diimplementasikan melalui sistem Permissions dan Groups.  
   Komponen Inti yang digunakan:  
   a. Permissions: Setiap model yang kita buat di Django secara otomatis mendapatkan empat izin dasar: add, change, delete, dan view. Misalnya, untuk model User, akan ada izin user.add_post, user.change_post, dsb. kita juga bisa membuat izin custom.  
   b. Groups: Grup adalah cara untuk mengelola izin secara kolektif. Kita bisa membuat grup (misalnya, "Editor", "Moderator"), memberikan sejumlah izin ke grup tersebut, lalu memasukkan userke dalam grup. user akan mewarisi (inheritance) semua izin dari grup tempat user tersebut berada  
   *Bentuk Implementasi*  
   Cara Memeriksa dan Membatasi Akses:  
   Kita bisa memeriksa izin user didalam views atau template  
   Mengecek izin di views: menggunakan @permission_required  
   Mengecek izin di templates: menggunakan kondisional elemen html.
3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?  
   Session dan cookies, keduanya  dibuat untuk mengatasi masalah mendasar HTTP, yaitu protokol yang stateless. Artinya, setiap request dari user ke server dianggap sebagai kejadian yang terisolasi, server tidak "mengingat" request sebelumnya.  
   **Cookies** adalah file teks kecil yang disimpan langsung di browser user (client-side). Server mengirimkan cookie ke browser, dan browser akan mengirimkan kembali cookie yang sama pada setiap request berikutnya ke server tersebut.  
   ++Kelebihan:  
   +)Karena penyimpanan dilakukan di device klien, cookies tidak akan membebani resource server.  
   +)Cookie dapat diatur untuk memiliki masa berlaku yang sangat lama, cocok untuk fitur "remember me"  
   +)Mudah dibuat dan dibaca baik dari sisi server maupun klien karena menggunakan javascript  
   --Kekurangan:  
   -)Size coockies biasanya terbatas hanya 4kB per domain.  
   -)Karena disimpan di sisi klien, data dalam cookie dapat dilihat, dimodifikasi, atau dicuri oleh user atau melalui serangan Cross-Site Scripting (XSS), sehingga tidak cocok untuk menyimpan data sensitif  
   -)Cookie dikirimkan pada setiap HTTP request ke domain yang sama, termasuk permintaan untuk gambar, file CSS, dan JavaScript. Hal ini bisa menambah ukuran request header dan memperlambat transfer data jika ukuran cookie cukup besar.  
   **Session** adalah mekanisme menyimpan data user di sisi server (server-side). Saat session dimulai, server membuat ID unik (Session ID) yang dikirim ke browser dan disimpan dalam sebuah cookie. Pada permintaan selanjutnya, browser hanya mengirimkan Session ID ini, dan server menggunakannya untuk mengambil data sesi yang sesuai.  
   ++Kelebihan:  
   +)Klien hanya memegang "kunci" (Session ID), sementara data disimpan pada server. Hal ini membuat session lebih aman untuk menyimpan informasi sensitif.  
   +)Semua data user tersimpan di satu tempat (server),sehingga data lebih mudah dikelola dan diamankan  
   +)Batas penyimpanan jauh lebih besar daripada cookie, karena hanya dibatasi oleh sumber daya server (memori atau database)  
   --Kekurangan:  
   -)Kita perlu memastikan bahwa request dari satu user selalu diarahkan ke server yang sama atau menggunakan penyimpanan session terpusat (seperti Redis atau database) yang bisa diakses oleh semua server.  
   -)Session biasanya akan berakhir secara otomatis setelah user tidak aktif selama periode waktu tertentu (timeout) atau saat browser ditutup, kecuali dikonfigurasi secara khusus.  
   -)Jika situs memiliki ribuan user aktif secara bersamaan, session bisa menjadi beban yan berat bagi server
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?    
   Penggunaan cookies tidak aman secara default. Cookies sebenarnya hanya file teks yang disimpan di browser pengguna, sehingga rentan terhadap pencurian dan manipulasi jika tidak diamankan dengan benar.  
   Ada beberapa risiko yang bisa muncul dengan penggunaan cooki. dua diantaranya dalah:  
   1. Cross-Site Scripting (XSS)  
   Ini adalah serangan di mana penyerang berhasil menyuntikkan skrip berbahaya (biasanya JavaScript) ke dalam situs web yang dipercayai. Jika cookie tidak diamankan, skrip ini bisaa dengan mudah membaca isi cookie (misalnya, session ID) dan mengirimkannya ke penyerang. Dengan session ID tersebut, penyerang bisa membajak sesi user dan masuk ke akun user tanpa perlu password.  
   2. Cross-Site Request Forgery (CSRF)  
   Serangan ini menipu browser user yang sudah terautentikasi (login) untuk mengirimkan request palsu ke sebuah situs web. Misalnya, Kita sedang login di mbanking. Kita kemudian membuka tab baru dan mengunjungi situs berbahaya. Situs tersebut bisa memiliki formulir tersembunyi yang secara otomatis mengirimkan request ke situs bank untuk mentransfer uang. Karena browser kita secara otomatis mengirimkan cookie autentikasi bersama request tersebut, situs bank akan menganggapnya sebagai permintaan yang sah dari pengguna.    

   Bbeberapa mekanisme yang ada pada Django untuk menangani bahaya ini adalah sebagai berikut  
   1. Mitigasi XSS dengan Atribut HttpOnly  
   Django secara default mengatur atribut HttpOnly pada cookie yang berisi session ID. Atribut HttpOnly memberitahu browser bahwa cookie tersebut tidak boleh diakses melalui skrip dari sisi klien (JavaScript). Meskipun penyerang berhasil melakukan serangan XSS, skrip mereka tidak akan bisa membaca cookie session pengguna. document.cookie tidak akan menampilkan cookie tersebut, sehingga pencurian session ID dapat dicegah. Hal ini bisa dilihat dan dikonfigurasi di file settings.py  
   2. Mitigasi CSRF dengan Token Anti-CSRF  
   Django memiliki sistem perlindungan CSRF yang sangat kuat dan aktif secara default.Berikut adalah cara kerjanya:  
   CSRF Middleware: Django memiliki CsrfViewMiddleware yang aktif secara otomatis.  
   CSRF Token: Untuk setiap session user, Django menghasilkan sebuah token rahasia (CSRF token) yang hanya diketahui oleh server dan klien tersebut.  
   Integrasi Template: Saat kita (pengembang) merender sebuah formulir menggunakan metode POST, developer wajib menyertakan tag template {% csrf_token %}. Tag ini akan membuat input tersembunyi < input type="hidden"> yang berisi CSRF token tadi.  
   Validasi: Ketika formulir dikirim, CsrfViewMiddleware akan membandingkan CSRF token yang dikirim dari formulir dengan token yang seharusnya ada di session user. Jika keduanya tidak cocok, permintaan akan ditolak dengan error 403 (Forbidden).
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).  
   Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya  
   - Mengimport beberapa atribut yang diperlukan dari ibrary Django. Mendefinisikan fungsi def register(request) pada views.py, kemudian membuat file html baru pada direktori template sebagai halaman registrasi. Setelah itu dilakukan routing dengan menambah path register di berkas urls.py  
   - Mengimport beberapa atribut yang diperlukan dari library Django. mendefinisikan fungsi def login_user(request) pada views.py, kemudian membuat file html baru pada direktori template sebagai halaman login tempat user menginput data. Setelah itu dilakukan routing dengan menambah path login di berkas urls.py  
   - Mengimport beberapa atribut yang diperlukan dari library Django. mendefinisikan fungsi def logout_user(request) pada views.py, kemudian menambah button logout pada template . Setelah itu dilakukan routing dengan menambah path logout di berkas urls.py  
  
   Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.  
   - Mencari enam produk mengenai sepakbola dari internet secara random, mencatat nama, harga, deskripsi, dan link gambar. kemudian saya buat 2 akun, dengan username user1 dan user2. Tiap akun akan menambahkan produk masing masing sebanyak 3 produk.  
   
   Menghubungkan model Product dengan User.  
   -Model Product pada file models.py didefinisikan ulang dengan menambah atribut user, melakukan migrasi database, kemudian mendefiniskan kembali fungsi create_product pada views.py agar menset atribut produk yang dibuat dengan user yang membuat produk tersebut.

   Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.  
   -untuk menampilkan username, berkas main.html ditambahkan line yang mengakses atribut username yang sedang login dari database, dengan template {{ user.username }}  
   -untuk menerapkan cookies, fungsi form.is_valid() pada views.py diubah agar menyimpan waktu saat user login sebagai cookie. Tentunya digunakan beberapa library dari Django untuk melakukan hal ini. Dilakukan juga perubahan pada fungi show_main pada bagian context dengan mendefinisikan atribut 'last_login'.Setelah itu, untuk menampilkan data last_login di halaman website, pada berkas main.html ditambahkan template {{ last_login }}.


