Tugas 2: Implementasi Model-View-Template (MVT) pada Django
Nama : Ryan Gibran Purwacakra Sihaloho
Kelas : PBP - C
NPM : 2406419833
Link PWS: https://ryan-gibran-pandasportswear.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Secara umum, saya mengikuti materi pada tutorial untuk menyelesaikan checklist, hanya saja alurnya tidak sama persis seperti di tutorial. Ada beberapa langkah yang dilompati dan dilakukan berulang agar mengikuti sesuai checklist. Selaiin tutorial, saya juga membuka beberapa materi pada checklist di internet untuk mendapat referensi tambahan.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   ![bagan request client](assets/request%20django.png)
3. Jelaskan peran settings.py dalam proyek Django!
   File settings.py berisi modul python dengan module-level variable. File ini berisi sebagai tempat mengkonfigurasi untuk seluruh pyoek yang akan menentukan bagaimana proyek djago akan berjalan.
4. Bagaimana cara kerja migrasi database di Django?
   migrasi database membantu kita untuk mengubah struktur database secara bertahap. Ada 2 command yang dilakukan dalam migrasi database Django:
   *python manage.py makemigrations
   Django membandingkan kondisi models.py saat ini dengan saat command migrasi terakhir. Dari perbandingan itu, Django menghasilkan sebuah file Python baru di dalam direktori migrations. File python tersebut berisi "daftar" perubahan apa saja yang perlu dilakukan untuk memperbarui database. perintah ini masih belum mengubah database proyek kita.
   *python manage.py migrate
   Django memeriksa tabel khusus di database bernama django_migrations untuk melihat migrasi mana yang sudah diterapkan. Kemudian, Django mencari file migrasi baru yang belum ada di catatan tersebut. Django membaca instruksi dari file migrasi baru, lalu mengubah instruksi menjadi perintah SQL yang sesuai berdasarkan hasil perbandingan, lalu mengeksekusi perintah SQL di database. Pada tahap ini, stuktur database project kita telah diupdate ke versi terbaru.
5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
