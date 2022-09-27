# Tugas 4 PBP
[Tugas 4 Irfan Satya Hendrasto](https://tugas4-pankgeming.herokuapp.com/todolist/)
1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Django dibuat dengan perlindungan yang mudah digunakan terhadap Pemalsuan Permintaan Lintas Situs . Saat mengirimkan formulir melalui POSTdengan perlindungan CSRF diaktifkan, gunakan csrf_token. Serangan dapat terjadi jika tidak adanya proteksi keamanan seperti csrf_token
2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }}) Bisa
3. Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
kita dapat melakukannya secara manual jika kita mau (memungkinkan kita untuk menyusun ulang field, misalnya). Setiap field tersedia sebagai atribut dari formulir menggunakan , dan dalam templat Django, akan dirender dengan tepat. Sebagai contoh:{{ form.name_of_field }}
4. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
a.  Membuat suatu aplikasi baru bernama todolist di proyek tugas Django
```shell
python manage.py startapp todolist
```
b. Membuat sebuah model Task yang memiliki atribut sebagai berikut:
```shell
from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone

class Task(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE);
    date = models.DateField(default = timezone.now);
    title = models.CharField(max_length=255);
    description = models.TextField();

    def __str__(self) :
        return self.title
```
c. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist
```shell
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')
```
d. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
```shell
{% extends 'base.html' %}
{% block meta %}
<title>{{user.username}} todolist</title>
<h1>Halo {{user.username}}</h1>
{% endblock meta %}

{% block content %}  
    <head>
        {% load static %}
    </head>
    <h1>Todo List APP</h1>
    <button><a href="{% url 'todolist:create' %}">Tambah Tugas</a></button>

    <h4>Todos:</h4>
    <table>
        <tr>
          <th>Create Date</th>
          <th>Title</th>
          <th>Description</th>
        </tr>
        {% comment %} Add the data below this line {% endcomment %}
        {% for task in task_list %}
            <tr>
                <th>{{task.date}}</th>
                <th>{{task.title}}</th>
                <th>{{task.description}}</th>
            </tr>
        {% endfor %}
      </table>
    <h3>last login: {{last_login}}</h3>
    <button><a href="{% url 'todolist:logout' %}">Logout</a></button>

{% endblock content %}
```
e.  Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
```shell
from django.forms import ModelForm
from todolist.models import Task

class CreateTask(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', ]
```
f. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:
```shell
from django.urls import path
from todolist.views import create_task, register, login_user, logout_user,show_todolist
 #sesuaikan dengan nama fungsi yang dibuat

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist' ),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create')
]
```
<!-- Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*
-
## Pendahuluan

Repositori ini merupakan sebuah template yang dirancang untuk membantu mahasiswa yang sedang mengambil mata kuliah Pemrograman Berbasis Platform (CSGE602022) mengetahui struktur sebuah proyek aplikasi Django serta file dan konfigurasi yang penting dalam berjalannya aplikasi. Kamu dapat dengan bebas menyalin isi dari repositori ini atau memanfaatkan repositori ini sebagai pembelajaran sekaligus awalan dalam membuat sebuah proyek Django.

## Cara Menggunakan

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi:

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.
2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (_filesystem_) komputermu:

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```
3. Masuk ke dalam repositori yang sudah di-_clone_ dan jalankan perintah berikut
   untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```
4. Nyalakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
5. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara
   lokal:

   ```shell
   python manage.py runserver
   ```
7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

## Contoh Deployment 

Pada template ini, deployment dilakukan dengan memanfaatkan GitHub Actions sebagai _runner_ dan Heroku sebagai platform Hosting aplikasi. 

Untuk melakukan deployment, kamu dapat melihat instruksi yang ada pada [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0).

Untuk contoh aplikasi Django yang sudah di deploy, dapat kamu akses di [https://django-pbp-template.herokuapp.com/](https://django-pbp-template.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya. -->