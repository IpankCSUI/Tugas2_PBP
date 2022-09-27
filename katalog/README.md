https://aplikasi-pankgemingg.herokuapp.com/katalog/


1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

https://1.bp.blogspot.com/-u-n0WYPhc3o/X9nFtvNZB-I/AAAAAAAADrE/kD5gMaz4kNQIZyaUcaJJFVpDxdKrfoOwgCLcBGAsYHQ/s602/3.%2BPython%2BDjango%2B-%2BModul%2B2_Page2_Image5.jpg

Alur permintaan yang sedang diproses di Django adalah sebagai berikut. Pertama, permintaan ke server Django akan ditangani melalui URL untuk diteruskan ke tampilan yang ditentukan pengembang untuk pemrosesan permintaan. Jika ada proses yang memerlukan keterlibatan database, tampilan selanjutnya akan meminta model dan database akan mengembalikan hasil kueri untuk tampilan tersebut. Setelah permintaan diproses, hasil proses dipetakan ke dalam kode HTML yang telah ditentukan sebelum HTML final dikembalikan ke pengguna sebagai tanggapan.

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment berfungsi untuk memisahkan pengaturan dan package yang diinstal pada setiap proyek Django sehingga perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Kita masih dapat bekerja tanpa virtual environment. Yang perlu dilakukan hanyalah menginstal libraries secara global.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
      1. membuat fungsi show_katalog 

         def show_katalog(request):

               return render(request, "katalog.html")

      2. Menambahkan kode urls.py pada folder katalog

      from katalog.views import show_katalog

      app_name = 'katalog'

      urlpatterns = [
         path('', show_katalog, name='show_katalog'),
      ]

      3. Menggunakan sintaks khusus template yang ada pada Django, yakni {{data}}

      {% comment %} Add the data below this line {% endcomment %}

         {% for barang in list_barang %}

         <tr>

            <th>{{barang.item_name}}</th>

            <th>{{barang.item_price}}</th>

            <th>{{barang.item_stock}}</th>

            <th>{{barang.description}}</th>

            <th>{{barang.rating}}</th>

            <th>{{barang.item_url}}</th>

         </tr>

      {% endfor %}

      4. a. membuat berkas dpl.yml berisi kode template

         b. membuat sebuah berkas .gitignore berisi kode template dari website https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/

         c. menambah beberapa konfigurasi pada file settings.py proyek Django

         import os

         PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

         STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

         d. menambah * ke dalam ALLOWED_HOSTS pada settings.py untuk dapat memberikan akses ke semua host

         e. menambah middleware baru ke dalam variabel MIDDLEWARE di settings.py

         f. Add, commit, dan push perubahan yang dilakukan ke GitHub pribadi.

         g. menambah aplikasi baru di heroku.

         h. membuka konfigurasi repositori GitHub dan membuka bagian Secrets untuk GitHub Actions (Settings -> Secrets -> Actions).

         i. menambah variabel repository secret 
         (NAME)HEROKU_APP_NAME
         (VALUE)HEROKU_API_KEY

         j. Simpan variabel-variabel tersebut.
         
         k. membuka tab GitHub Actions dan jalankan kembali workflow yang gagal.