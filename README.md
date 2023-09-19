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
<img src=bagan.png>

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
  <img src=HTML.jpg>
- create-form HTML
  <img src=create-form.jpg>
- XML
   <img src=XML.jpg>
- JSON
   <img src=JSON.jpg>
- XML by ID
  <img src=XMLbyID.jpg>
- JSON by ID
- <img src=JSONbyID.jpg>

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








