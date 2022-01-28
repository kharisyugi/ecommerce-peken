# PEKEN 4.0 Backend

### Mulai

Pertama clone dulu dari github, kemudian masuk folder peken-4.0,

Kemudian atur **setting** untuk host/url api,pengaturan database yang akan digunakan,

Kemudian Install **requierements.text** agar packages yang dibutuhkan ter-install

jalankan perintah **python manage.py migrate** && **python manage.py makemigrations**,( perintah untuk build Model,Apss,dan Database)

Jalankan perintah,


### Menjalankan projek (development)

```bash
python manage.py runserver
```

Kalau sudah, bisa ikuti petunjuk di terminal masing-masing os, biasanya akses [localhost:8080]di browser

### Membuild untuk deploy ke server (HEROKU)

Jika mau menjalankan di server projek harus di build dahulu, bisa jalankan perintah

### MAC OS

```bash
brew install heroku/brew/heroku
```
### UBUNTU

```bash
sudo snap install heroku --classic
```

Selanjutya ikuti link berikut--[sini](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)


