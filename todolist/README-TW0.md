 **1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
 Asynchronous programming merupakan sebuah pendekatan pemrograman yang tidak terikat pada input output (I/O)  protocol. Ini menandakan bahwa pemrograman asynchronous tidak melakukan pekerjaannya secara old style / cara lama yaitu dengan eksekusi baris program satu persatu secara hirarki. Asynchronous programming melakukan pekerjaannya tanpa harus terikat dengan proses lain atau dapat kita sebut secara Independent. 
 Berbeda dengan asynchronous, synchronous programming memiliki pendekatan yang lebih old style. Task akan dieksekusi satu persatu sesuai dengan urutan dan prioritas task. Hal ini memiliki kekurangan pada lama waktu eksekusi karena masing-masing task harus menunggu task lain selesai untuk diproses terlebih dahulu.

 **2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
 Event-Driven Programming adalah paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya. Hal ini diterapkan ketika user mengklik tombol Add Task yang akan menyebabkan suatu event yaitu munculnya modal pada web.

 **3. Jelaskan penerapan asynchronous programming pada AJAX.**
 AJAX digunakan untuk mempermudah website dalam rangka mengupdate serta menampilkan data-data baru tanpa perlu melakukan reload dari server tersebut. Bisa dibilang, AJAX adalah sekumpulan teknis web development yang digunakan agar aplikasi web bekerja secara asynchronous (tidak langsung)

 **4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.
```shell
@login_required(login_url="/todolist/login")
def show_todolist_json(request):
    tasks = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', tasks), content_type='application/json')
```
Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.
```shell
path('json/', show_todolist_json, name="show_todolist_json"),
```
Lakukan pengambilan task menggunakan AJAX GET.
```shell

```
Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
```shell
<div class="text-center">
          <a>
            <input class="w-50 btn btn-lg btn-info" data-bs-toggle="modal" data-bs-target="#reg-modal" id="other-btn" type="button" value="Add Task" />
          </a>

<!-- Membuat modal -->
<div class="modal fade" id="reg-modal" tabindex="-1" aria-labelledby="modal-title" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content bg-warning">
      <div class="modal-header">
        <h5 class="modal-title" style="color: #000000;" id="modal-title">Create your new task</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="modal-title" style="color: #ffffff;" class="form-label">Title</label>
            <input type="text" class="form-control" id="modal title">
          </div>
          <div class="mb-3">
            <label for="modal-description" style="color: #ffffff;" class="form-label">Description</label>
            <input type="text" class="form-control" id="modal-description">
          </div>
        </div>
        <div class="modal-footer">
          <button type="submit" class="btn btn-info" id="add_button">Submit</button>
        </div>
        </form>
```
Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.
```shell
path('add/', add_task, name="add_task"),
```
Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add
```shell
def add_task(request):
    if request.method == "POST":
        x = request.POST.get('title')
        y = request.POST.get('description')
        new_item = Task.objects.create(user=request.user, date = str(datetime.datetime.now().date()), title= x, description = y)
        new_item.save()
    return HttpResponse('')
```


 