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
   Integrasi Template: Saat kita (pengembang) merender sebuah formulir menggunakan metode POST, developer wajib menyertakan tag template {% csrf_token %}. Tag ini akan membuat input tersembunyi <br input type="hidden"> yang berisi CSRF token tadi.  
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

Berikut adalah dua buah akun yang diregistrasi beserta produk yang dibuat:  

username: user1  
password: 12qwerty345  
Produk:  
- F50 Messi League Firm/Multi-Ground Boots
- Chelsea F.C. 2025/26 Match Home
- SAUDI PRO LEAGUE BALL  

username: user2  
password: 12qwerty345  
produk:  
- Real Madrid Terrace Icons Track Top
- Samba Indoor Football Boots
- Copa Pure 3 League Firm/Multi-Ground Boots

<br></br>
Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS
Nama : Ryan Gibran Purwacakra Sihaloho  
Kelas : PBP - C  
NPM : 2406419833  
Link PWS: https://ryan-gibran-pandasportswear.pbp.cs.ui.ac.id/  
  
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!  
CSS selector adalah pola yang developer gunakan untuk memilih elemen HTML yang ingin kita stylong. Urutan pengambilannya ditentukan oleh CSS Specificity. Berikut adalah urutan prioritasnya, dimulai dari yang paling diprioritaskan hingga paling tidak diprioritaskan:  
   1) selector apapun yang diakhiri dengan "!important"
   2) Inline Style, merupakan style yang ditulis langsung didalam atribut "style" pada page html
   3) Selector yang menggunakan ID Selector(#)
   4) Class Selector(.), Attribute Selector([]), dan Pseudo-class(:)
   5) Element selector(p) dan Pseudo-element(::)    

   referensi: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Specificity


2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!  
User mengakses web bisa dari beberapa kemungkinan device. Tentunya tiap device memiliki ukuran layar yang berbeda beda. Agar tampilan web bisa terlihat jelas oleh user, diperlukan responsive design yang dapat beradaptasi mengikuti ukuran layar device user.  
Contoh aplikasi web yang sudah menerapkan responsive design: instagram.
terlihat sekali perbedaannya ketika web tersebut dibuka dengan PC dan hanphone, ukuran tombol dan letaknya optimal untuk tiap device.  
Contoh aplikasi web yang belum menerapkan responsive design: https://www.berkshirehathaway.com/  ketika diakses dengan ponsel, tampilan tulisan sangat kecil, banyak dan tidak nyaman dibaca.  
3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!  
Secara sederhana: luar | margin | border | padding | dalam.  
Padding adalah space kosong diantara konten (dalam) dan border  
Border adalah garis yang mengelilingi padding
Margin adalah space kosong transparan diluar border
Untuk mengimplementasi css, bisa dengan membuat kelas dan mendeklarasikan atributnya. Contohnya sebagai berikut.  
   ```
   HTML  
   <div class="kotak-margin-border-padding">
     Ini adalah konten, posisinya didalam kotak
   </div>
   ```
   ```
   CSS
   .kotak-margin-border-padding {
     /* Menetapkan padding 20px untuk semua sisi (atas,kanan, bawah, kiri) */
     padding: 20px;

     /* Menetapkan border dengan tebal 5px, stylea solid (garis lurus), dan warna merah */
     border: 5px solid red;

     
     /* menetapkan margin 30px untuk semua sisi */
     margin: 30px;
     
     /* Properti tambahan */
     background-color: #f0f0f0;
     width: 300px;
   }
   ```  

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!  
   Flexbox: model layout yang dimana item alam sebuah kontainer diatur secara fleksibel di sepanjang satu sumbu utama yang dipilih. Flexbox mengatur konten dalam komponen. Biasanya digunakan untuk membuat navbar, mengatur layout komponen, menengahkan elemen.  
   Gridlayout: sistem layout berbasis kisi-kisi dua dimensi. Gridlayout mengatur komponen pada page. Biasanya digunakan untuk mendesain main page, galeri, dan desain yang letaknya sesuka sukanya developer.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!  
   1) mendefinisikan fungsi edit_product dan delete_product pada views.py, melakukan routing url, dan membuat page html untuk kedua fungsi.
   2) melakukan konfigursi static files dan menulis script tailwind pafa file base.html.
   3) Membuat page navbar html
   4) Melakukan styling css pada setiap dile html di direktori main/templates
   5) Menambahkan gambar no-product.png di direktori static/image untuk ditampilkan di main.html ketika belum ada produk yang dibuat.
   6) Supaya navbar responsive:  
      a. menu navigasi desktop mobile disembunyikan
      b. Tombol "burger" ditampilkan pada mobile device dengan kode  
      ```
      <div class="md:hidden flex items-center">
          <button class="mobile-menu-button ...">
              </button>
      </div>
      ``` 
      c. Menu dropdown ditampilkan saat burger di klik  
      ```
      <script>
          const btn = document.querySelector("button.mobile-menu-button");
          const menu = document.querySelector(".mobile-menu");

          btn.addEventListener("click", () => {
              menu.classList.toggle("hidden");
          });
      </script>
      ```

<br></br>
Tugas 6: Javascript dan AJAX
Nama : Ryan Gibran Purwacakra Sihaloho  
Kelas : PBP - C  
NPM : 2406419833  
Link PWS: https://ryan-gibran-pandasportswear.pbp.cs.ui.ac.id/    

1. Apa perbedaan antara synchronous request dan asynchronous request?  
syncronus request memblokir proses lain hingga selesai
asyncronus request berjalan di background tidak memblokir proses lain yang sedang berjalan  

   syncronus request
tugas-tugas dieksekusi satu per satu berurutan. Jika sebuah request dikirim (misalnya, meminta data dari server), aplikasi akan berhenti dan menunggu sampai respons diterima sebelum lanjut mengerjakan  tugas berikutnya.
Jika proses rewuest membutuhkan waktu lama (misalnya, mengunduh file besar), seluruh interface user bisa "freeze" (tidak responsif), sehingga user experience terhadap aplikasi tersebut buruk.

   asynchronus request
Kita bisa mengirim request dan melanjutkan pekerjaan lain tanpa menunggu respons. Ketika respons sudah terkirim, ada mekanisme (seperti callback function atau promise) yang akan menangani data tersebut. Aplikasi akan tetap lancar karena tugas berat yang memakan waktu lama tidak menghentikan proses kerja tugas lainnya.  
2. Bagaimana AJAX bekerja di Django (alur request–response)?  
   1. Aksi User (Client-Side)
   User melakukan aksi yang memicu sebuah event JavaScript.
   Contoh: User klik tombol "like" pada sebuah postingan.

   2. JavaScript Mengirim Request (Client-Side)
   Event listener pada tombol "like" akan menjalankan fungsi JavaScript. Fungsi ini menggunakan Fetch API (atau XMLHttpRequest) untuk membuat permintaan HTTP asinkron ke server Django.  
   Request ini membawa informasi:  
   -URL: Alamat spesifik di server Django yang akan menangani permintaan ini (misalnya, /like-post/5/).  
   -Method: Biasanya POST untuk mengubah data (seperti menambahkan suka) atau GET untuk mengambil data.  
   -Headers: Informasi tambahan, seperti CSRF token   
   -Body: Data yang dikirim ke server (jika ada).

   3. URL Routing (Django Server-Side)
   Rquestn dari JavaScript tiba di Django. Seperti mengurus request biasanya, Django melihat file urls.py untuk mencocokkan URL yang diminta dengan view yang sesuai.
   Contoh: URL /like-post/5/ dicocokkan dengan pola path('like-post/<int:post_id>/', views.like_post_view). Django kemudian memanggil fungsi like_post_view dan memberikan post_id=5 sebagai argumen.

   4. Views Memproses Logika (Django Server-Side)
   Fungsi Views yang dipanggil akan melakukan logika yang diperlukan:
   -Menerima data dari request (misalnya, post_id).  
   -Berinteraksi dengan database (misalnya, mengambil objek Postingan, menambah jumlah suka, dan menyimpannya).  
   -Menyiapkan data yang akan dikirim kembali sebagai respons, dan sebagainya sesuai dengan logika views yang dibuat developer.

   5. Views Merreturn JsonResponse (Django Server-Side)
   Ini adalah perbedaan AJAX dibanding request biasa. views tidak akan merender template HTML dengan render(), tetapi view akan mengembalikan objek JsonResponse. JsonResponse secara otomatis akan mengubah dictionary Python menjadi format JSON (JavaScript Object Notation), yang nantinya dibaca oleh JavaScript.
   Contoh: return JsonResponse({'status': 'ok', 'new_likes_count': 101})

   6. JavaScript Menerima Respons dan Mengupdate Halaman (Client-Side)
   Kembali ke browser, Fetch API yang tadi dikirim kini menerima respons JSON dari Django. Kode JavaScript kemudian:  
   -membaca data JSON dari respons.  
   -Menggunakan data tersebut untuk memanipulasi DOM (Document Object Model) secara langsung (tanpe refresh).
   Contoh: JavaScript mengambil 'new_likes_count': 101 dari respons dan memperbarui teks di dalam elemen <span id="like-count"> menjadi "101".
3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?  
   1. Mengurangi Beban Server dan Bandwidth
   AJAX secara signifikan lebih efisien dalam hal penggunaan sumber daya.  
   Tanpa AJAX (hanya Render Biasa), Server terus-menerus merender ulang template HTML yang besar dlalu mengirim melalui internet. proses Ini memakan lebih banyak resource CPU di server dan menghabiskan lebih banyak bandwidth.
   Dengan AJAX, server cuku perlu mengirimkan beberapa baris data dalam format JSON. Ukuran data yang ditransfer lebih kecil, sehingga mengurangi load server dan menghemat kuota internet user.  
   2. Memisahkan Logika (Separation of Concerns)  
   AJAX mendorong arsitektur di mana front-end (tampilan) dan back-end (logika) lebih terpisah. Django bertindak sebagai API (Application Programming Interface) yang memberikan data. Sementara itu, JavaScript di clien side menampilkan data tersebut. Pemisahan ini membuat kode lebih mudah dikelola, diuji, dan didevelop secara paralel oleh programmer yang berbeda.  
   3. User experience yang lebih bagus  
   Interaksi di halaman web terasa lebih cepat, mulus, dan responsif, mirip seperti menggunakan aplikasi desktop.
   Tanpa AJAX (Render Biasa): Setiap kali user mengklik tombol "like", berkomentar, atau memfilter produk, browser akan mengirim request ke Django. Django memprosesnya, merender ulang seluruh template HTML (termasuk header, footer, sidebar), dan mengirimkannya kembali. User akan melihat halaman berkedip (flash) saat me refresh.
   Dengan AJAX: Ketika user mengklik tombol like, hanya request kecil untuk data yang relevan (misal, "increment like_var pada post ID 5") yang dikirim ke server. Server hanya merespons dengan data minimal (misalnya, {'like_var': 102}). JavaScript hanya mengupdate jumlah like di page postingan. Tidak ada flash ataupun refresh yang terjadi
4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?  
   1)Pada tutorial dan tugas ini, kita gunakan logika validasi dan login yang telah disediakan django, yaitu AuthenticarionForm dan UserCreationForm. Keduanya sudah dibuat dengan aman dan teruji. Kita cukup menggunakannya saja, tanpa perlu membuat dari awal.  
2)Melakukan validasi di serverside, yaitu pada logika views.py  
3)membatasi jumlah upaya login yang gagal dari satu alamat IP atau untuk satu username, bisa dengan menggunakan django-ratelimit  
4)Mereturn message yang "aman". Jangan mengembalikan warning dengan {'error': 'Password salah untuk user pand@Kecil'}. Message ini mengimplikasikan bahwa ada user dengan username pand@Kecil. Lebih baik mereturn message {'error': 'Username atau password salah'}. Tidak ada informasi yang berarti untuk digunakan peretas.
5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?  
   AJAX mengubah pengalaman pengguna (User Experience/UX) dengan membuat website terasa lebih cepat, responsif, dan interaktif, mirip seperti menggunakan aplikasi desktop atau mobile.
Tanpa AJAX, setiap interaksi kecil (seperti mengklik "suka", memfilter produk, atau mengirim komentar) memaksa browser untuk reload seluruh page. Proses ini mmembuat experience yang lambat dan terputus-putus.

   AJAX menghilangkan masalah ini dengan cara berikut:  
   1)Membuat respon instan  
   Saat "bagian" kecil dari data yang dikirim dan diterima dari server di latar belakang, aksi user mendapat respons yang terasa cepat
   Sebelum AJAX: Mengklik "Tambah ke Keranjang" akan reload seluruh, bisa memakan waktu beberapa detik.
   Dengan AJAX: Mengklik "Tambah ke Keranjang" hanya akan menampilkan ikon keranjang yang diperbarui atau notifikasi kecil dalam sepersekian detik. User bisa langsung melanjutkan aktivitasnya.  
   2) Meningkatkan Efisiensi dan Penghematan Data  
   Dengan hanya mentransfer data yang benar-benar diperlukan , AJAXmengurangi jumlah data yang harus diunduh oleh User. Konsep Ini membuat website lebih cepat diakses pada koneksi internet yang lebih lambat dan lebih hemat kuota bagi user mobile device.  
   3)Interaksi Tanpa Gangguan   
   AJAX memungkinkan pengguna untuk berinteraksi dengan halaman tanpa kehilangan konteks atau posisi mereka saat ini.
   Sebelum AJAX: Ketika user sedang mengisi formulir panjang dan ada satu "kecerobohan" saat user menekan tombol "kirim". Seluruh page akan dimuat ulang, dan mungkin semua data yang sudah user isi hilang.
   Dengan AJAX: Jika ada error pada formulir, message kesalahan akan muncul tepat di sebelah bidang yang salah tanpa reload halaman. User tetap berada di formulir dan dapat langsung memperbaikinya. Contoh lain adalah infinite scroll di media sosial, di mana konten baru ditambahkan ke bagian bawah halaman tanpa mengganggu posisi User saat ini.  
   4)Feedback Real-Time  
   AJAX memungkinkan website untuk memberikan feedback langsung kepada usr saat mereka melakukan sesuatu
   Pengecekan Username: Saat mendaftar, sistem bisa langsung memberitahu "Username sudah dipakai" atau "Username tersedia" saat user selesai mengetik, bukan setelah user mengirim seluruh formulir.
   Simpan Otomatis (Autosave): Misalnya di Google Docs, perubahan disimpan secara otomatis di background setiap beberapa detik. Usermerasa aman karena tahu pekerjaan mereka tidak akan hilang.

