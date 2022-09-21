https://tugas3-pankgeming.herokuapp.com/mywatchlist/html/
https://tugas3-pankgeming.herokuapp.com/mywatchlist/xml/
https://tugas3-pankgeming.herokuapp.com/mywatchlist/json/

1. Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON adalah singkatan dari JavaScript Object Notation. JSON didesain menjadi self-describing, sehingga JSON sangat mudah untuk dimengerti. JSON digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. Sintaks JSON merupakan turunan dari Object JavaScript. Akan tetapi format JSON berbentuk text, sehingga kode untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman.
XML adalah singkatan dari eXtensible Markup Language. XML didesain menjadi self-descriptive, jadi dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis. XML digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. XML hanyalah informasi yang dibungkus di dalam tag. Kita perlu menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut.
HTML (HyperText Markup Language) adalah suatu bahasa yang menggunakan tanda-tanda tertentu (tag) untuk menyatakan kode-kode yang harus ditafsirkan oleh browser agar halaman tersebut dapat ditampilkan secara benar. Secara umum, fungsi HTML adalah untuk mengelola serangkaian data dan informasi sehingga suatu dokumen dapat diakses dan ditampilkan di Internet melalui layanan web.
2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam mengembangkan suatu platform, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya. Data yang dikirimkan bisa bermacam-macam bentuknya. 
3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat suatu aplikasi baru bernama mywatchlist dengan perintah python manage.py startapp mywatchlist
- Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
def show_mywatchlist(request):
    return render(request, "mywatchlist.html")
from django.urls import path
from wishlist.views import show_mywatchlist

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
]
Daftarkan juga aplikasi wishlist ke dalam urls.py yang ada pada folder project_django
path('mywatchlist/', include('mywatchlist.urls')),
-  Membuat sebuah model MyWatchList
from django.db import models
class FilmWatchlist(models.Model):
    watched = models.TextField()
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()
- Menambahkan 10 data untuk objek MyWatchList contoh:
{
        "model":"mywatchlist.filmwatchlist",
        "pk":1,
        "fields":{
            "watched":"False",
            "title":"Infinity War",
            "rating":5,
            "release_date":"5 Februari 2018",
            "review":"Star Lord bodoh"
        }
    },
- Membuat fungsi untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format HTML, XML, JSON
def show_xml(request):
    data = FilmWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = FilmWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
- Membuat routing sehingga data di atas dapat diakses melalui URL:
urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]
- Melakukan deployment ke Heroku
    a. membuat berkas dpl.yml berisi kode template

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
4. Mengakses tiga URL di poin 6 menggunakan Postman, menangkap screenshot, dan menambahkannya ke dalam README.md 
https://drive.google.com/drive/folders/1K-e2xWWYpFgvcbh4ZR0yxXHZ-Y7NxrvH?usp=sharing
5. Menambahkan unit test pada tests.py untuk menguji bahwa tiga URL di poin 6 dapat mengembalikan respon HTTP 200 OK