# Tugas 4 PBP
[Tugas 4 Irfan Satya Hendrasto](https://tugas4-pankgeming.herokuapp.com/todolist/)

1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Django dibuat dengan perlindungan yang mudah digunakan terhadap Pemalsuan Permintaan Lintas Situs . Saat mengirimkan formulir melalui POSTdengan perlindungan CSRF diaktifkan, gunakan csrf_token. Serangan dapat terjadi jika tidak adanya proteksi keamanan seperti csrf_token
2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }}) Bisa
3. Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
kita dapat melakukannya secara manual jika kita mau (memungkinkan kita untuk menyusun ulang field, misalnya). Setiap field tersedia sebagai atribut dari formulir menggunakan , dan dalam templat Django, akan dirender dengan tepat. Sebagai contoh:{{ form.name_of_field }}
4. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika pengguna mengklik submit, data dari form yang ada di client akan dikirim melalui request POST (atau GET, tergantung pada konfigurasi <form>) ke server. Server kemudian memproses input melalui views yang ada dan menyimpan, dan menyimpan data menggunakan ORM dengan method .save() atau Model.objects.create(). Setelah itu, data yang sudah disimpan dapat diakses di dalam views dengan memanggil melalui ORM model-nya (Model.objects.filter(user=request.user).all()), data tersebut ditaruh dalam context rendering HTML, dan dapat diakses sebagai variable di dalam template HTML.
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

# Tugas 5 PBP
[Tugas 5 Irfan Satya Hendrasto](https://tugas5-pankgeming.herokuapp.com/todolist/)
## Apa perbedaan dari Inline, Internal, dan External CSS Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis. 
Kelebihan :
1. Sangat membantu ketika Anda hanya ingin menguji dan melihat perubahan pada satu elemen.
2. Berguna untuk memperbaiki kode dengan cepat.
3. Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.
Kekurangan :
Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.
Kelebihan :
1. Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
2. Anda tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file.
3. Class dan ID bisa digunakan oleh internal stylesheet.
Kekurangan :
1. Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
2. Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website. 

Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.
Kelebihan :
1. Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
2. Loading website menjadi lebih cepat.
3. File CSS dapat digunakan di beberapa halaman website sekaligus. 
Kekurangan :
Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.

## Jelaskan tag HTML5 yang kamu ketahui.
```shell
Tag <section>...</section>
```
Tag <SECTION> merupakan dokumen atau aplikasi bagian generik. Hal ini dapat digunakan bersama-sama dengan h1-h6 untuk menunjukkan struktur dokumen.
```shell
Tag <article>...</article>
```
Tag <ARTICLE> merupakan sepotong independen isi dokumen, seperti sebuah blog atau artikel koran.
```shell
Tag <aside>...</aside>
```
Tag <ASIDE> merupakan gambaran dari sebagian konten yang berhubungan dengan isi halaman.
```shell
Tag <header>...</header>
```
Tag <HEADER> merupakan bagian kepala dari dukumen.
```shell
Tag <footer>...</footer>
```
Tag <FOOTER> merupakan bagian catatan kaki yang dapat berisi informasi tentang penulis, informasi hak cipta, dll
```shell
Tag <nav>...</nav>
```
Tag <NAV> merupakan bagian dari dokumen yang dimaksudkan untuk memudahkan dalam proses navigasi.
```shell
Tag <figure>...</figure>
```
Tag <FIGURE> dapat digunakan untuk menghubungkan keterangan bersama-sama dengan beberapa konten tertanam, seperti gambar atau video.

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Selektor Tag.
Selektor Tag disbut juga Type Selector. Selektor ini akan memilih elemen berdasarkan nama tag.
2. Selektor Class.
Selektor class adalah selektor yang memilih elemen berdasarkan nama class yang diberikan. Selektor class dibuat dengan tanda titik di depannya.
3. Selektor ID.
Selektor ID hampir sama dengan class. Bedanya, ID bersifat unik. Hanya boleh digunakan oleh satu elemen saja.
4. Selektor Atribut.
Selektor atribut adalah selektor yang memilik elemen berdasarkan atribut. Selektor ini hampir sama seperti selektor Tag.
5. Selektor Universal.
Selektor universal adalah selektor yang digunakan untuk menyeleksi semua elemen pada jangkaua (scope) tertentu.
6. Selektor Pseudo.
Pseudo selektor adalah selektor untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Memodifikasi kode pada base.html menjadi
```shell
{% load static %}
<!DOCTYPE html>

<nav class="navbar navbar-dark bg-warning">
  <div class="container-fluid">
    <a class="navbar-brand text-black">
      Todolist App
      <small class="nav-link" href="#">by Irfan Satya Hendrasto</small>
    </a>
     
  </div>
</nav>


<html lang="en">

<head>
  
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Bootsrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="style.css">

  {% block meta %}
  {% endblock meta %}
</head>

<body class="bg-danger">
  {% block content %}
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  {% endblock content %}
</body>

</html>
```
2. Memodifikasi kode pada register.html menjadi
```shell
{% extends 'base.html' %}

{% block meta %}
<title>Registrasi Akun</title>
{% endblock meta %}

{% block content %}  

<div class="global-container d-flex align-items-center justify-content-center">
    <div class="card bg-info">
        <div class="card-body">
            <h1 class = "card-title text-center">Formulir Registrasi</h1>
        </div>
        <div class="card-text">
            <form method="POST" >  
                {% csrf_token %}  
                <h4 class="form-label">Username</h4>
                <input type="text" class="form-control" name="username"> 
                <p>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</p>
                <h4 class="form-label">Password</h4>
                <input type="password" class="form-control" name="password">
                <p>~Your password can't be too similar to your other personal information.</p>
                <p>~Your password must contain at least 8 characters..</p>
                <p>~Your password can't be a commonly used password.</p>
                <p>~Your password can’t be entirely numeric.</p>
                <h4 class="form-label">Password Confirmation</h4>
                <input type="password" class="form-control" name="confirm">
                <p>Enter the same password as before, for verification.</p>
                <div class="text-center">
                    <button type="submit" class="btn login_btn bg-primary ">Register</button>
                </div>
            </form>
        </div>

{% endblock content %}
```
3. Memodifikasi kode pada create_task.html menjadi
```shell
{% extends 'base.html' %}
{% block content %}

    <div class="global-container d-flex align-items-center justify-content-center">
        <div class="card bg-info">
            <div class="card-body">
                <h1 class = "card-title text-center">Tambah Task</h1>
            </div>
            <div class="card-text">
                <form method="POST" >  
                    {% csrf_token %}  
                    <label class="form-label">Title</label>
                    <input type="text" class="form-control" name="title"> 
                    <label class="form-label">Description</label>
                    <input type="text" class="form-control" name="description">
                    <div class="text-center">
                        <button type="submit" class="btn login_btn bg-primary ">Tambah</button>
                    </div>
                </form>
                
            </div>

{% endblock %}
```
4. Memodifikasi kode pada login.html menjadi
```shell
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<html lang="en">


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="style.css"/>
</head>

<body>
    <div class="global-container d-flex align-items-center justify-content-center">
        <div class="card login-form bg-info">
            <div class="card-body">
                ,<h1 class = "card-title text-center">Login</h1>
            </div>
            <div class="card-text">
                <form method="POST" action="">
                    {% csrf_token %}
                    <div class="mb-3">
                      <label class="form-label">Username</label>
                      <input type="text" class="form-control" name="username">
                      
                    <div class="mb-3">
                      <label class="form-label">Password</label>
                      <input type="password" class="form-control" name="password">
                    </div>
                    <div class="mb-3 form-check vertical-center">
                      <input type="checkbox" class="form-check-input" id="exampleCheck1">
                      <label class="form-check-label" for="exampleCheck1">Check me out</label>
                    </div>
                    <div class="text-center">
                        <button type="submit" class="btn login_btn bg-primary ">Login</button>
                    </div>
                  </form>
            </div>
            {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>
            </div>
        </div>
    </div>
</body>
</html>
{% endblock content %}
```
5. Memodifikasi kode pada todolist.html menjadi 
```shell
{% extends 'base.html' %}
{% block meta %}
<title class="text-center">{{user.username}} Todolist</title>
<h1 class="text-center">{{user.username}} TodoList</h1>
{% endblock meta %}
{% block content %}  

  <style>
    .ho:hover {
      text-shadow: none !important;
      box-sizing: border-box !important;
      cursor: pointer !important;
      transition: all 0.3s ease !important;
      -webkit-transform: scale(1.1) !important;
      -ms-transform: scale(1.1) !important;
      transform: scale(1.1) !important;
      z-index: 2;
    }
  </style>
    <head>
        {% load static %}
    </head>
    <!-- Button untuk membuat tugas Bary -->
    <h2>Task List:</h2>
    <body class="w-50 text-center">
        {% comment %} Add the data below this line {% endcomment %}
        <!-- Mengiterasi data tugas pada query database -->
        {% for task in task_list %}

              <div class="card">
                <h5 class="card-header bg-warning">{{task.date}}</h5>
                <div class="card-body wow fadeInLeft slow">
                  <h5 class="card-title">{{task.title}}</h5>
                  <p class="card-text">{{task.description}}</p>
                </div>
              </div>
            </div>
            
        {% endfor %}
    </body>
    <div class="text-center">
      <button class="w-50 btn btn-lg btn-info"><a href="{% url 'todolist:create' %}">Add New Task</a></button>
    <button class="w-50 btn btn-lg btn-info"><a href="{% url 'todolist:logout' %}">Logout</a></button>
    </div>

    <script>
      $(document).ready(function () {
        new WOW().init();
      });
    </script>
    

{% endblock content %}
```

