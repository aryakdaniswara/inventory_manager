# inventory_manager

### Membuat sebuah proyek Django baru
<details>
<summary> Membuat proyek Django baru </summary>
  
1. Buat sebuah direktori (_folder_) baru di tempat yang ada inginkan dengan nama `inventory_manager`
2. Klik kanan pada folder yang telah Anda buat dan pilih `Copy as path`
3. Tekan Win + X dan pilih 'Terminal (Admin)'
4. Pada Terminal ketik 'cd' dan tekan Ctrl + V untuk _paste_ alamat dari direktori yang sudah kita buat. Tampilan dari kode Anda harusnya terlihat sepeti ini:
```
cd "C:\Users\direktoriAnda\inventory_manager"
```
- Tekan enter untuk pindah ke direktori `inventory_manager` pada Terminal.
5. Buat virtual environment baru dengan perintah berikut
```
 python -m venv env
```
6. Aktivasi virtual environment dengan perintah berikut
```
 env\Scripts\activate.bat
```
<p align="center"> atau </p>

```
 env\Scripts\activate
```
- Jika virtual environment sudah menyala akan ditandai dengan `(env)` pada Terminal
7. Dalam direktori yang sama buat sebuah file `requirements.txt` yang berisi dependencies:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
8. Pastikan virtual environment menyala dan install dependencies dengan perintah berikut:
  ```
    pip install -r requirements.txt
  ```
9. Buat proyek Django baru dengan nama `inventory_manager` dengan perintah berikut:
  ```
    django-admin startproject invenetory .
  ```
10. Tambahkan `*` ke `ALLOWED_HOST` di `settings.py` untuk keperluan deployment dengan perintah berikut
 ```
 ...
 ALLOWED_HOSTS = ["*"]
 ...

 ```
</details>
<details>
<summary> Memeriksa proyek Django yang sudah dibuat </summary>

1. Jalankan server untuk mengecek apakah proyek Django sudah berjalan. 
```
python manage.py runserver
```
2. Buka `http://localhost:8000` di peramban Anda. Jika ada animasi roket maka proyek Django Anda sudah berjalan.

</details>

---
### Membuat aplikasi dengan nama main dan routing untuk menjalankannya.
<details>
<summary> Membuat aplikasi main pada proyek Anda </summary>
  
  1. Buka terminal di direktori proyek Django Anda dan jalakan virtual environment
  
  ```
  cd "C:\Users\direktoriAnda\inventory_manager"
  env\Scripts\activate.bat
  ```

2. Buat aplikasi main dengan perintah berikut.
  ```
  python manage.py startapp main
  ```
3. Tambahkan aplikasi main ke INSTALLED_APPS di settings.py inventory_manager agar aplikasi tersebut dapat diakses

```python
INSTALLED_APPS = [
...,
'main',
...
]    
```
</details>
<details>
<summary> Membuat templates dan mengisinya </summary>
  
1. Buat direktori baru bernama `templates` pada direktori `main`
2. Buat sebuah file baru bernama `main.html` yang berisi
  
```
<h1>Inventory Manager 00</h1>

<h5>Nama: </h5>
<p>{{ myName }}<p>
<h5>Kelas: </h5>
<p>{{ class }}<p>
<h5>Nama Aplikasi: </h5>
<p>{{ appName }}<p>

<h5>Nama Produk: </h5>
<p>{{ name }}<p>
<h5>Jumlah: </h5>
<p>{{ amount }}<p>
<h5>Deskripsi: </h5>
<p>{{ description }}<p>
```

- Sesuaikan isi `main.html` dengan preferensi Anda
</details>

---
### Melakukan routing pada urls.py.
<details>
<summary> Konfigurasi untuk menjalankan aplikasi main </summary>

1. Buat file baru bernama `urls.py` pada direktori `main`
```
from django.urls import path #Definisi pola URL
from main.views import show_main #Fungsi dari views.py untuk tampilan

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
2. Buka direktori `inventory_manager` dan cari file `urls.py` (berbeda dari file di direktori `main`)
3. Tambahkan fungsi `include` dengan perintah
```
...
from django.urls import path, include 
...
```

4. Tambahkan rute url yang akan mengarahkan tampilan ke `main `
```
urlpatterns = [
...
path('main/', include('main.urls')),
...
]
```
</details>

---
### Membuat model pada aplikasi main dan migrasi
<details>
<summary> Konfigurasi model pada aplikasi </summary>

1. Buat model dengan cara membuka direktori aplikasi main di `models.py`
```
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField(default=0)
```

2. Lakukan migrasi agar perubahan model dapat tersimpan
```
python manage.py makemigrations
python manage.py migrate
```
</details>

---
### Membuat fungsi pada views.py
<details>
<summary> Konfigurasi views.py</summary>

1. Buka file `views.py` di direktori `main` dan tambahkan kode beikut
```
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'myName' : 'Arya Kusuma Daniswara',
        'class' : 'PBP B',
        'appName' : 'inventory00',
        'name': 'Botol',
        'amount': '2',
        'description' : 'Botol 500 ml yang sangat bagus'
    }

    return render(request, "main.html", context)
```
- File `views.py` akan melengkapi template `main.html` yang sudah dibuat
</details>

---
### Melakukan deployment ke Adaptable 
<details>
<summary> Konfigurasi Github</summary>

1. Buat repositori baru dengan nama `inventory_manager`
2. Tambahkan file `.gitignore`
 ```
  # Django
  *.log
  *.pot
  *.pyc
  __pycache__
  db.sqlite3
  media

  # Backup files
  *.bak 

  # If you are using PyCharm
  # User-specific stuff
  .idea/**/workspace.xml
  .idea/**/tasks.xml
  .idea/**/usage.statistics.xml
  .idea/**/dictionaries
  .idea/**/shelf

  # AWS User-specific
  .idea/**/aws.xml

  # Generated files
  .idea/**/contentModel.xml

  # Sensitive or high-churn files
  .idea/**/dataSources/
  .idea/**/dataSources.ids
  .idea/**/dataSources.local.xml
  .idea/**/sqlDataSources.xml
  .idea/**/dynamic.xml
  .idea/**/uiDesigner.xml
  .idea/**/dbnavigator.xml

  # Gradle
  .idea/**/gradle.xml
  .idea/**/libraries

  # File-based project format
  *.iws

  # IntelliJ
  out/

  # JIRA plugin
  atlassian-ide-plugin.xml

  # Python
  *.py[cod] 
  *$py.class 

  # Distribution / packaging 
  .Python build/ 
  develop-eggs/ 
  dist/ 
  downloads/ 
  eggs/ 
  .eggs/ 
  lib/ 
  lib64/ 
  parts/ 
  sdist/ 
  var/ 
  wheels/ 
  *.egg-info/ 
  .installed.cfg 
  *.egg 
  *.manifest 
  *.spec 

  # Installer logs 
  pip-log.txt 
  pip-delete-this-directory.txt 

  # Unit test / coverage reports 
  htmlcov/ 
  .tox/ 
  .coverage 
  .coverage.* 
  .cache 
  .pytest_cache/ 
  nosetests.xml 
  coverage.xml 
  *.cover 
  .hypothesis/ 

  # Jupyter Notebook 
  .ipynb_checkpoints 

  # pyenv 
  .python-version 

  # celery 
  celerybeat-schedule.* 

  # SageMath parsed files 
  *.sage.py 

  # Environments 
  .env 
  .venv 
  env/ 
  venv/ 
  ENV/ 
  env.bak/ 
  venv.bak/ 

  # mkdocs documentation 
  /site 

  # mypy 
  .mypy_cache/ 

  # Sublime Text
  *.tmlanguage.cache 
  *.tmPreferences.cache 
  *.stTheme.cache 
  *.sublime-workspace 
  *.sublime-project 

  # sftp configuration file 
  sftp-config.json 

  # Package control specific files Package 
  Control.last-run 
  Control.ca-list 
  Control.ca-bundle 
  Control.system-ca-bundle 
  GitHub.sublime-settings 

  # Visual Studio Code
  .vscode/* 
  !.vscode/settings.json 
  !.vscode/tasks.json 
  !.vscode/launch.json 
  !.vscode/extensions.json 
  .history
  ```

3. Inisiasi git directory, tambahkan perubahan, _push_, dan _commit_
    ```
    git init
    git remote add origin https://github.com/aryakdaniswara/inventory_manager.git
    git branch -M main
    git add .
    git commit -m "<pesan>"
    git push origin main

    ```
</details>
<details>
<summary> Membuat test unit </summary>

1. Buat test unit dengan membuka file `tests.py` di direktori main
```
  from django.test import TestCase, Client

  class mainTest(TestCase):
      def test_main_url_is_exist(self):
          response = Client().get('/main/')
          self.assertEqual(response.status_code, 200)

      def test_main_using_main_template(self):
          response = Client().get('/main/')
          self.assertTemplateUsed(response, 'main.html')
  ```
2. Jalankan tes dengan perintah
  ```
  python manage.py test
  ```
</details>
<details>
<summary> Konfigurasi Adaptable </summary>

1. Buka situs https://adaptable.io/ dan login menggunakan github Anda
2. Klik `New app` dan pilih `Connect an Existing Repository`
3. Pilih repositori github `inventotry_manager` yang telah Anda buat
4. Pilih branch `main`
5. Pilih `python app template`
6. Pilih `PostgeSQL`
7. Pilih versi python yang Anda gunakan misal `3.11`
8. Isi start command dengan `start command sebagai berikut `python manage.py migrate && gunicorn inventory_manager.wsgi`
9. Pilih nama domain yang Anda inginkan
10. Centang `HTTP Listener Port
</details>

---
### Bagan Relasi
<img src=img/bagan.png>

- urls.py <div>
  File urls.py akan menerima request yang dilakukan User. Pencarian url akan dilakukan urlpatterns untuk menemukan url yang sesuai dengan request yang diberikan.
- views.py <div>
  File views.py akan menjalakan fungsi show_main yang akan memberikan context yang nantinya akan menjadi acuan dari isi website tersebut. Context yang diberikan akan diteruskan ke main.html untuk memberikan response yang sesuai
- models.py <div>
  models.py akan berisikan data yang kita inginkan pada aplikasi. Model dapat berisikan atribut yang memiliki field masing-masing seperti, text, integer, atau char
- html <div>
  html atau file main.html pada template akan menunjukan tampilan kepada User. Tampilan ini akan berisi informasi berdasarkan data yang diterima dari views.py yang akan disesuaikan dengan fieldnya masing-masing
---

### Mengapa menggunakan virtual environtment
Virtual environment digunakan agar tidak terjadi konflik antar dependencies yang ada pada proyek lain atau pada versi lain yang ada. Virtual environment menyediakan lingkungan yang tertutup di mana dependencies yang ada hanya akan sesuai dengan yang diinstall pada virtual enviroment itu

Pengembangan aplikasi web berbasis Django masih dapat digunakan tanpa menggunakan virtual environment. Akan tetapi, semakin kita sering membuat dan 'otak-otik' dengan dependency atau proyek-proyek yang kita punya, konflik akan semakin rentan untuk terjadi dan akan menggangu proses pengembangan aplikasi kita.

---

### MVC, MVT, dan MVVM
1. MVC (Model View Controller)
   Sistem pengembangan aplikasi dengan cara pemisahan kode menjadi 3 bagian, Model, View, dan Controller.
   - Model: Bagian yang mengelola data dan logika dari aplikasi
   - View: Bagian yang menampilkan hasil response dari request yang diberikan User dan mengatur tampilan dan logika tampilan
   - Controller: Bagian yang mengatur hubungan antara Model dan View
  
2. MVT (Model View Template)
   Sistem pengembangan aplikasi yang mirip dengan MVC, tapi bagian Controller digantikan dengan Template
    - Model: Bagian yang mengelola data dan logika dari aplikasi
   - View: Bagian yang menampilkan hasil response dari request yang diberikan User, namun tanpa mengatur logika tampilan
   - Template: Bagian yang mengatur struktur tampilan dari data yang diperoleh

3. MVVM (Model View ViewModel)
   Sistem pengembangan aplikasi dengan pemisahan pada 3 bagian, yaitu, Model, View, dan ViewModel. Struktur ViewModel berbeda dengan Controller, di mana ViewModel memiliki keterikatan (binding) yang lebih ketat.
   - Model: Bagian yang mengelola data dan logika dari aplikasi
   - View: Bagian yang mengatur tampilan dari aplikasi dan menampilkan data. Action dari input pengguna akan diteruskan ke ViewModel
   - ViewModel: Bagian perantara antara Model dan View. ViewModel menjadi penghubung antara logika dan tampilan aplikasi
---

### Membuat input form untuk menambahkan objek model pada aplikasi main
Untuk membuat suatu input form, kita perlu membuat file baru bernama `forms.py` pada direktori aplikasi `main`. File ini akan digunakan untuk membuat kerangka form yang akan menerima input dari pengguna. Dalam file tersebut kita akan menambahkan field yang ingin kita dapatkan dari pengguna. Jika pada model yang kita punya tidak ada nilai _default_, maka semua field harus dimasukkan ke dalam form berikut. 

```
from django.forms import ModelForm
from main.models import Item

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "amount", "description"]
```
pada file `forms.py` akan diambil field _name_, _price_, _amount_, dan _description_ dari models yang kita buat, dalam file ini adalah `Item`. Sebenarnya ada satu field yang diambil secara otomatis, yaitu field `date_added`.

---
### Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
Untuk mengimplementasikan fungsi yang ingin kita gunakan pada aplikasi ini, kita perlu menerapkan fungsi tersebut ke dalam file `views.py` yang berada pada direktori `main`. Terdapat 5 fungsi yang ingin kita tambahkan pada aplikasi ini:
1. Fungsi create_product <br>
   fungsi ini digunakan untuk membuat product baru sesuai dengan form HTML yang sebelumnya diisi oleh pengguna.
3. Fungsi show_xml <br>
   fungsi ini akan menampilkan data dari semua produk yang sudah dibuat dalam format xml.
5. Fungsi show_json <br>
   fungsi ini digunakan untuk menampilkan data dari semua produk yang sudah dibuat dalam format JSON.
7. Fungsi show_xml_by_id <br>
   fungsi ini akan menampilkan data produk yang ada berdasarkan dengan id yang diinginkan dalam format xml.
9. Fungsi show_json_by_id <br>
   fungsi ini akan menampilkan data produk yang ada berdasarkan dengan id yang diinginkan dalam format JSON.
   
Implementasi dari fungsi tersebut dapat dilihat dari kode berikut: 
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

---
### Membuat routing URL untuk masing-masing fungsi views 
Routing URL akan dilakukan agar fungsi yang telah kita buat di `views.py` agar pengguna dapat menggunakan fungsi tersebut sesuai dengan tujuannya.  Routing URL diterapkan pada file `urls.py` yang ada pada folder `main`. Pada file ini, kita akan mengimpor fungsi yang telah kita buat dari `views.py` dan menambahkan _path url_-nya agar fungsi tersebut dapat diakses. Fungsi yang telah kita buat akan berkorespondensi dengan url nya masing-masing, yang ditunjukkan pada kode berikut:

```
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```

---
### Mengakses URL menggunakan Postman
- main HTML
  <img src=img/HTML.jpg>
- create-form HTML
  <img src=img/create-form.jpg>
- XML
   <img src=img/XML.jpg>
- JSON
   <img src=img/JSON.jpg>
- XML by ID
  <img src=img/XMLbyID.jpg>
- JSON by ID
- <img src=img/JSONbyID.jpg>

---
### Tambahan
- Memperbaiki `tests.py` yang berada pada direktori `main`
  Unit testing diperbaiku agar dapat berjalan dengan memberikan suatu nilai default kepada parameter yang dibutuhkan walaupun parameter tersebut tidak diujikan dalam unit test tersebut. Dengan menambahkan nilai default pada paramaeter model yang ada, unit test dapat berjalan tanpa adanya error.
- Menambahkan penghitung item
  Untuk menambahkan penghitung item yang ada, dapat dibuat dengan mengecek len dari item. Dengan kata lain, ketika kita mengetahui berapa banyak item yang sudah dibuat sesuai dengan `item = Item.objects.all()` dan mencari tau dengan `len(item)`, kita bisa mengetahui sudah berapa banyak item yang sudah dibuat. Implementasi dari metode ini dapat dilihat dari kode berikut di file `views.py` dalam direktori `main`.

```
def show_main(request):
    item = Item.objects.all()

    context = {
        'name' : 'Arya Kusuma Daniswara',
        'class' : 'PBP B',
        'appName' : 'inventory00',
        'products': item,
        'products_count' : len(item),
    }

    return render(request, "main.html", context)
```

---
### Perbedaan antara form POST dan GET dalam Django
- Metode POST digunakan untuk mengirimkan _request_ untuk membuat, memperbarui, atau menghapus data. Pada metode POST, nilai variabel tidak akan ditambilkan di url sehingga lebih aman. Metode POST biasa digunakan untuk _request_ yang akan mengubah data seperti mengirim formulir atau mengirim komentar.
- Metode GET adalah _request_ yang umumnya digunakan untuk mengambil suatu data dari server. Pada metode GET, nilai variabel biasanya akan dapat dilihat melalui url sehingga menjadi lebih tidak aman. Metode GET digunakan untuk mengakses/navigasi halaman atau mencari informasi.

---
 ### Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data
 - XML biasanya digunakan untuk pertukaran data antar aplikasi yang berbeda atau untuk konfigurasi data. XML menyimpan daya dalam struktur pohon sehingga digunakan untuk menggambar atau menyusun data dalam bentuk hierarki. XML juga memiliki sintaks yang lebih kompleks, tidak terlalu mudah dibaca, dan cenderung lebih _redundant_ karena harus mengulang referensi yang ada.
 - JSON adalah format pertukaran data yang ringan dengan sintaks yang lebih padat dan lebih mudah dibaca oleh manusia. JSON menggunakan struktur seperti peta dengan data yang direpresentasikan dalam bentuk pasangan kunci-nilai. JSON biasa digunakan untuk pertukaran data terstruktur seperti pada pertukaran data antar server.
 - HTML biasanya digunakan untuk membuat konten dari halaman web yang ada untuk diterjemahkan oleh _browser_. HTML memiliki sintaks yang cenderung ditargetkan kepada pembuatan tampilan web dan mendefinisikan elemen yang ada dalam web tersebut.
---
### Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern
Format JSON sering digunakan dalam pertukaran data antara aplikasi web modern dikarenakan beberapa hal, antara lain:
1. JSON merupakan format yang lebih ringan dan efisien dibandingkan dengan format lain seperti XML. Dengan beban yang lebih ringan, server dapat bekerja dengan lebih cepat dan efisien.
2. JSON memiliki sintaks yang sederhana dan mudah dibaca oleh manusia sehingga dapat memudahkan pengembang untuk memahaminya ketika menghadapi dengan masalah pada format JSON
3. JSON mendungkung berbagai macam struktur data. Dengan menggunakan JSON, pengembang dapat membuat berbagai macam data yang lebih kompleks dengan mudah.
4. JSON dapat diproses oleh sebagian besar browser modern menggunakan JavaScript. Dengan adanya dukungan ini, pertukaran data dapat dilakukan dengan lebih mudah dan efisien.
---
#### Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm adalah sistem autentikasi pengguna dari Django yang digunakan untuk mendaftarkan pengguna baru ke situs web yang kita inginkan. Sistem ini akan menyimpan data hasil registrasi dan akan memberifikasi username dan password yang dimasukkan oleh pengguna secara otomatis

##### Kelebihan
UserCreationForm akan membuat proses pembuatan akun user baru menjadi lebih cepat dan sederhana, tanpa perlu membuat seluruh sistem sendiri dengan manual. Kita hanya perlu menggunakan framework yang sudah ada di Django. UserCreationForm juga sudah menyimpan data secara otomatis dan aman, serta sudah memvalidasi password yang digunakan user sehingga akun yang dibuat sudah memiliki keamanan yang cukup.

##### Kekurangan
Pada UserCreationForm form pembuatan akun yang diberikan hanya berbentuk tampilan dasar dan sederhana. Beberapa fitur juga tidak ada dalam tampilannya, fitur seperti verifikasi email dan lainnya tidak ada. UserCreationForm hanya memberika form pembuatan user dengan fields yang sederhana, hanya fields seperti username, password, dan nama.

### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- Autentifikasi adalah proses verifikasi identitas pengguna ketika pengguna tersebut berusaha untuk mengakses aplikasi web. Validasi data antara username dan password yang dilaukan ketika pengguna login. Autentifikasi penting untuk memastikan bahwa yang mengakses aplikasi web memang benar pengguna dengan data dan kredensial yang sesuai.
- Otorisasi adalah proses yang menentukan izin yang dimiliki suatu user ketika sudah login. Otorisasi akan mengatur hal apa saja yang bisa diakses atau dimiliki oleh pengguna tersebut. Otorisasi penting untuk memastikan batasan izin dan akses bagi user yang Anda. Jangan sampai user dapat mengakses atau mengubah informasi yang penting.

### Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies merupakan suatu data yang disimpan dalam browser user dan digunakan untuk menyimpan informasi yang diperlukan daro suatu aplikasi web. Cokkies dapat membantu aplikasi web untuk mengingat dan mengidentifikasi sesi user ketika sedang berinteraksi. Cookies dapat digunakan untuk beberapa keperluan seperti mengingat preferensi user atau melakukan otentikasi seperti ketika login. Django menggunakan salah satunya untuk login juga, jadi kita tidak perlu login lagi di setiap berpindah lama. Cookies pada Django digunakan dengan cara menyisipkan session id yang unik untuk menghubungkan cookies sehingga dapat mengakses session id yang ada. Dengan session id tersebut, Django dapat menghubungkan user dengan sesi yang tepat ketika kita mengakses website.

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Dalam pengembangan penggunaan cookies secara default 'sebenarnya' aman karena cookies umumnya digunakan untuk mempermudah dan mempercepat akses kita ke siatu web. Akan tetapi, belakangan ini terdapat banyak kasus di mana dengan adanya penggunaan cookies dapat terjadi penggunaan data aktivitas kita yang kemudian digunakan untuk iklan, atau bahkan tindakan kriminal. Penggunaan cookies yang tidak sesuai tersebut dapat melanggar privasi kita atau bahkan tanpa implementasi yang benar bisa jadi digunakan untuk memalsukan session kita sehingga terjadi session hijacking di mana orang pura-pura menjadi kita dengan menggunakan data sesi yang ada.

### Implementasi checklist
1. Membuat file register.html sebagai template dari form untuk registrasi user
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
2. Membuat fungsi register, login, dan logout di views.py dan menambahkan path url ke urls.py
```
ddef register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
- Hubungkan dengan urls.py
```
from main.views import register, login_user, logout_user
...
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
```
3. Membuat login dibutuhkan untuk mengakses menu inventory, menambahkan last login dan cookies, serta menghubungkan data inventory dengan user yang login
```
@login_required(login_url='/login')
def show_main(request):
    item = Item.objects.filter(user=request.user)

    context = {
        'name' : request.user.username,
        'class' : 'PBP B',
        'appName' : 'inventory00',
        'products': item,
        'products_count' : len(item),
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```
- Sesuaikan model untuk menghubungkan Item dengan user
```
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
```
4. Melakukan pengecekan dan membuat user
```
env\Scripts\activate
python manage.py runserver
```
Ketika sudah dapat mengakses secara lokal, buat user dengan menekan register dan melengkapi form yang ada.

5. Membuat dan mengetes fitur tambahan
- Terdapat beberapa fitur tambahan dalam aplikasi web ini, yaitu tombol '+', '-' dan 'Delete'.
- Tombol '+' digunakan untuk menambahkan amount suatu barang (increment), tombol '-' untuk mengurangi amount suatu barang (decrement), dan tombol 'Delete' untuk menghapus suatu barang.
Fungsi pada views.py ada pada kode berikut:
```
def increment_amount(request, product_id):
    item = get_object_or_404(Item, id=product_id)
    item.amount += 1
    item.save()
    return redirect('main:show_main')

def decrement_amount(request, product_id):
    item = get_object_or_404(Item, id=product_id)
    if item.amount > 0:
        item.amount -= 1
        item.save()
    return redirect('main:show_main')

def delete_product(request, product_id):
    item = get_object_or_404(Item, id=product_id)
    item.delete()
    return redirect('main:show_main')
```
untuk menambahkan tombol pada tabel yang kita punya bisa menggunakan kode berikut:
```
...
 <tr>
            <td>{{product.name}}</td>
            <td> 
                <a href="{% url 'main:increment_amount' product.id%}">
                    <button>+</button> 
                </a>
            {{product.amount}} 
                <a href="{% url 'main:decrement_amount' product.id%}">
                    <button>-</button> 
                </a> 
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
            <td> 
                <a href="{% url 'main:delete_product' product.id%}">
                    <button> Delete </button>
                </a>
            </td>
        </tr>
...
```
- Jangan lupa untuk menambahkan path url ke urls.py
```
from main.views import increment_amount, decrement_amount, delete_product
...
path('increment_amount/<int:product_id>/', increment_amount, name='increment_amount'),
path('decrement_amount/<int:product_id>/', decrement_amount, name='decrement_amount'),
path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
...
```
- Coba tambahkan dan kurangi amount, coba delete suatu item
  
6. Membuat dan mengetes dummy data pada 2 user
  
Tambahkan beberapa item dengan mengisi form 'Add Item' di kedua user
- Berikut tampilan di user 1: ABA
<img src=img/user_1_ABA.jpg>

- Berikut tampilan di user 2: Ari
<img src=img/user_2_Ari.jpg>

Dapat dilihat bahwa isi dari user 1 dan user 2 berbeda. user 1 hanya akan mengakses item yang ada di user 1, begitu juga dengan user 2

---
###  Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya
1. Selector Universal `(*)`: Selector ini digunakan untuk memilih semua elemen dalam halaman web. Selector ini biasa digunakan untuk memberikan gaya dasar. Perlu berhati-hati dalam menggunakan selector ini karena dapat mempengaruhi semua elemen.
2. Selector Tag `(<p>, <h1>, <div>, dll.)`: Selector ini memilih semua elemen dengan tag HTML tertentu. Selector ini berguna untuk mengatur gaya dasar elemen-elemen HTML seperti paragraf, judul, atau div, dan sering digunakan dalam pembuatan tata letak halaman.
3. Selector Class (.classname): Selector ini digunakan untuk memilih elemen-elemen yang memiliki kelas tertentu. Selector ini digunakan ketika menggabungkan elemen-elemen yang ingin diatur dengan gaya yang sama atau papa penerapan gaya pada suatu kelas.
4. Selector ID (#idname): Selector ini digunakan untuk memilih elemen dengan ID tertentu. Selector ini biasa digunakan untuk mengatur gaya atau perilaku khusus untuk elemen dengan ID tertentu.
5. Selector Pseudo-class (:pseudo-class): Selector ini memilih elemen berdasarkan keadaan atau interaksi pengguna, seperti elemen yang sedang dihover oleh mouse (:hover), elemen yang sedang aktif (:active), atau elemen yang sedang difokuskan (:focus). Selector inidigunakan untuk memberikan efek interaktif pada element.
6. Selector Pseudo-element (::pseudo-element): Selector ini digunakan untuk memilih bagian khusus dari elemen, seperti bagian sebelum (:before) atau sesudah (:after) elemen, atau bahkan baris pertama (:first-line) dalam elemen teks. Selector ini dapat digunakan untuk mengatur gaya khusus untuk bagian-bagian elemen tertentu.
7. Selector Kombinasi: Selector ini memungkinkan untuk memilih elemen berdasarkan hubungan atau konteks mereka dalam dokumen, seperti elemen yang berada dalam elemen lain (element1 element2), elemen yang langsung berikutnya (element1 + element2), atau elemen yang berada di bawah elemen lain (element1 > element2). Selector ini digunakan untuk elemen yang memiliki hubungan tertentu
8. Selector Atribut ([attribute], [attribute=value], [attribute~=value]) Selector ini memilih elemen berdasarkan atribut HTML mereka. Selector ini digunakan ketika ingin menargetkan elemen yang memiliki atribut tertentu atau nilai atribut tertentu.

---
### Tag HTML5
1. `<main>`: Digunakan untuk mengelompokkan konten utama dalam halaman web. Biasanya, satu halaman web hanya memiliki satu elemen `<main>`, dan akan berguna dalam membantu mesin pencari dan aksesibilitas untuk mengidentifikasi konten utama.

2. `<aside>`: Untuk konten sampingan yang terkait dengan konten utama, seperti sidebar dengan widget atau iklan. Ini membantu memisahkan konten utama dari informasi tambahan.

3. `<figure>`: Untuk menandai konten media, seperti gambar atau video, beserta elemen yang terkait seperti keterangan menggunakan tag `<figcaption>`.

4. `<time>`: Digunakan untuk menandai waktu atau tanggal dalam teks. Tag ini akan membantu mesin pencari dan pembaca layar memahami konteks waktu dalam konten.

5. `<mark>`: Untuk menyorot atau menandai teks dalam sebuah paragraf. Tag ini berguna untuk menyoroti kata-kata penting atau mencari teks yang relevan.

6. `<details>` dan `<summary>`: Digunakan untuk membuat elemen yang bisa diperluas dan disusutkan. Biasanya digunakan untuk informasi tambahan yang bisa diakses dengan mengklik atau menekan tombol "Details".

7. `<section>`: Tag ini digunakan untuk mengelompokkan konten terkait, tag `<section>` juga dapat digunakan untuk memberikan struktur berlapis pada halaman web.

8. `<header>`: Tag ini digunakan untuk bagian atas halaman web, tag `<header>` juga dapat digunakan untuk mengelompokkan elemen-elemen header dalam bagian tertentu dari halaman.

9. `<nav>`: Untuk menu navigasi utama, Anda juga bisa menggunakan tag `<nav>` untuk sub-menu atau menu navigasi lainnya dalam halaman.

10. `<footer>`: Tag ini akan berisi informasi kontak atau hak cipta, tag `<footer>` juga bisa berisi tautan-tautan terkait atau informasi penting lainnya.

---
### Perbedaan antara Margin dan Padding
- Margin adalah ruang di luar batas elemen. Margin akan mempengaruhi jarak antara suatu elemen dengan elemen lain di sekitarnya. Margin digunakan untuk mengatur jarak antara elemen-elemen, membuat elemen tersebut akan terpisah dari elemen lain, atau mengontrol tata letak secara keseluruhan.
- Padding adalah ruang di dalam batas elemen. Padding akan mempengaruhi jarak antara isi elemen dan batas elemen itu sendiri. Padding digunakan untuk mengatur jarak antara suatu konten elemen dan batas elemen tersebut.

---
### Perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
- Bootstrap adalah frame work CSS open source yang digunakan untuk membuat situs web dan aplikasi responsif. Bootstrap adalah framework front end berbasis mobile pertama yang berisi template HTML, CSS, dan JavaScript untuk berbagai komponen. Bootstrap menyediakan komponen siap pakai dengan gaya bawaan. Anda menggabungkan kelas-kelas Bootstrap ke dalam elemen HTML.  Dalam Bootstrap, kustomisasi tema dan gaya bisa dilakukan tetapi terkadang memerlukan penyesuaian yang lebih rumit. Bootstrap juga memiliki berkas yang lebih besar karena menyertakan banyak komponen dan gaya bawaan. Bootstrap digunakan jika ingin mengembangkan situs web atau aplikasi dengan cepat, tidak ingin menulis banyak CSS kustom, dan memerlukan komponen-komponen siap pakai.
  
-  Tailwind CSS adalah framework CSS berbasis utilitas dan low-level framework dari CSS. Tailwind menawarkan kelas-kelas dengan satu fungsi yang dapat langsung digunakan dalam halaman web untuk styling elemen. Tailwind CSS memungkinkan pengembangan dengan cepat dengan interface pengguna yang custom. Tailwind juga merupakan salah satu library CSS berbasis utilitas paling populer. Tailwind CSS menggunakan pendekatan utilitas, yang berarti perku membangun gaya elemen secara eksplisit dengan menambahkan kelas-kelas ke elemen HTML. Tailwind memungkinkan pengguna untuk dengan mudah menyesuaikan setiap aspek tampilan dengan mengedit file konfigurasi. Tailwind juga memungkinkan pengguna untuk dengan mudah menyesuaikan setiap aspek tampilan dengan mengedit file konfigurasi. Tailwind digunakan ketika ingin memiliki kendali yang lebih besar atas tampilan, ingin menghindari overhead CSS yang tidak perlu, atau jika ingin membuat desain yang sangat kustom sesuai kebutuhan yang diperlukan.

---
1. Tambahkan Bootstrap dan JSke `base.html` yang merupakan dasar dari halaman html yang lain. Anda dapat menggunakan kode berikut
- Bootstrap
```
<head>
    {% block meta %}
        ...
    {% endblock meta %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
```

- JS
```
<head>
    ...
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
</head>
```

3. Pada tugas ini pertama saya menambahkan navbar ke halaman `base.html` agar navbar dapat terlihat di seluruh halaman yang lain. Pilihan penggunaan navbar dapat dilihat di [link berikut](https://getbootstrap.com/docs/5.3/components/navbar/)
  
4. Selanjutnya saya menambahkan fungsi edit untuk mengubah produk yang dibuat
```
def edit_product(request, id):
    product = Item.objects.get(pk = id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
    
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```

Tambahkan kode tersebut di views.py pada aplikasi Anda dan hubungkan dengan urls.py

5. Memperbaiki layout halaman. Selanjutnya saya memperbaiki layout halaman dengan dasar kode berikut
```
<div class="container mt-5">
    <div class="login" style="padding-left: 20px; padding-right: 20px;">
```
- Kode tersebut dapat digunakan agar tiap halaman yang ada memiliki jarak dan tidak terlalu menempel ke kiri atau kanan
  
6. Kustomisasi button, saya mengubah button saya agar menjadi lebih indah dengan kode berikut
```
<a href="{% url 'main:edit_product' product.pk %}" class="btn btn-warning btn-sm me-2">
```
- Sesuaikan kebutuhan button Anda dan tambahkan sesuai dengan letak button tersebut. Cek [link ini](https://getbootstrap.com/docs/5.3/components/buttons/) untuk informasi tentang button

### Tambahan
Untuk mengimplentasi bonus, saya menggunakan kode berikut agar dapat mendeteksi bahwa produk yang ditampilkan merupakan produk terakhir
```
 <tr{% if forloop.last %} class="last-row"{% endif %}>
```
- kemudian kode tersebut akan memanggil kode yang mengubah warna produk menjadi merah
  
```
 <style>
        .last-row td {
            color: red; /* Set the text color for the last row */
        }
    </style>
```
---
### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Synchronous Programming: <br>
Dalam synchronous programming, operasi atau tugas akan dieksekusi satu per satu secara berurutan. Setiap operasi harus menunggu operasi sebelumnya selesai sebelum dapat dimulai. Oleh karena itu, keseluruhan proses dapat memakan waktu yang lama karena tugas berikutnya tidak dapat dijalankan sebelum tugas sebelumnya telah selesai. Tipe ini cocok untuk tugas yang cepat dan tidak memerlukan waktu yang lama untuk menyelesaikan.
- Asynchronous Programming: <br>
Dalam asynchronous programming operasi atau tugas dapat dieksekusi secara bersamaan tanpa harus menunggu operasi sebelumnya selesai. Asynchronous programming memungkinkan aplikasi untuk tetap responsif, karena tidak menghentikan operasi lain selama operasi yang memakan waktu sedang berjalan. Tipe ini sangat berguna saat ada tugas yang memerlukan waktu lama karena dapat menjalankan tugas lain tanpa menghentikan tugas yang lama tersebut.

###  Penerapan paradigma event-driven programming dalam JavaScript dan AJAX
Paradigma event-driven programming adalah cara untuk merespons peristiwa atau events yang terjadi dalam aplikasi. Paradigma event-driven programming ini sangat umum dalam JavaScript dan digunakan secara luas dalam pengembangan web, terutama dalam kombinasi dengan teknologi seperti AJAX untuk membuat aplikasi web responsif. Salah satu contoh penggunaan paradigma ini adalah pada  tombol Add Product di berkas main.html. Dengan mengklik tombol tersebut, suatu event terjadi, yaitu pembukaan form yang dapat diisi dengan produk baru

### Penerapan asynchronous programming pada AJAX
AJAX (Asynchronous JavaScript and XML) adalah teknologi yang menggunakan programming asynchronous untuk berkomunikasi antara browser dan server tanpa harus merefresh halaman web secara keseluruhan. Saat browser melakukan permintaan AJAX, seperti permintaan GET atau POST, browser dapat menjalankan kode JavaScript lainnya tanpa harus menunggu respons dari server. Dengan AJAX, request JavaScript tidak perlu menunggu respons untuk melanjutkan proses sehingga aplikasi web dapat menjadi lebih responsif.

### Bandingkan Fetch API dan jQuery untuk Penerapan AJAX
- Fetch API <br>
Fetch API adalah bagian dari standar web modern, yang berarti itu adalah API bawaan yang terintegrasi dalam browser web utama. Fetch API lebih ringan dan modern daripada jQuery, dan ini merupakan pilihan yang baik untuk pengembangan web yang lebih baru. Fetch API menggunakan konsep promise, sehingga memungkinkan untuk mengelola permintaan dan respons secara lebih jelas dan dapat diandalkan.
- jQuery <br>
jQuery adalah sebuah library JavaScript yang menyederhanakan banyak tugas di dalam pengembangan web. Selain AJAX, jQuery memiliki berbagai fitur lain yang memudahkan manipulasi DOM dan efek visual. jQuery diciptakan untuk memastikan kompatibilitas lintas browser yang baik, sehingga Anda dapat yakin bahwa kode Anda akan berjalan dengan baik di berbagai browser. Namun, jQuery memiliki ukuran yang lebih besar dan bisa jadi berlebijan jika hanya ingin menggunakan fitur-fitur AJAX

### Implementasi Checklist
- AJAX GET <br>
Pada berkas views.py, saya membuat fungsi get_item_json untuk menerima barang-barang yang dimiliki oleh pengguna dalam bentuk format JSON.  Fungsi tersebut kemudian dihubungkan di urls.py dan diterapkan dalam main.html untuk membuat fungsi getItems() yang bersifat asinkronus menggunakan async. Fungsi tersebut akan mengembalikan JSON file menggunakan fetch API. Selanjutnya ada fungsi refreshProducts() yang akan mereload halaman secara asinkronus untuk memperbarui data yang ada.
- AJAX POST <br>
Implementasi AJAX POST digunakan untuk membuat sebuah produk baru secara asinkronus. Sebelumnya saya membuat halaman modal yang akan muncul ketika saya menekan button add product by AJAX. Pada modal tersebut berisi form seperti ketika kita sebelumnya ingin membuat produk dengan field nama, amount, price, dan description. Pada modal tersebut terdapat button Close yang akan mentrigger action untuk menambahkan produk ke dalam tabel. Pada views.py daya membuat fungsi add_item_ajax yang akan menambahkan item jika form valid. Kemudian saya menambahkan pathnya di urls,py. Pada main.html, saya menambahkan fungsi addproduct untuk membuat barang terbaru tersebut, setelah itu akan terjadi reload secara asinkronus menggunakan refreshProducts()
- collectstatic <br>
Sebelum saya menjalankan perintah python manage.py collectstatic yang akan mengambil semua berkas static, saya mengubah STATIC_ROOT di settings.py. Tujuannya adalah untuk mengumpulkan berkas static di suatu direktori tertentu, dalam hal ini staticfiles.
