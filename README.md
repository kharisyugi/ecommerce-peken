# PEKEN 4.0 Frontend

### Mulai

Kita di sini pakai framework vuejs versi 2, dengan vue-cli beserta dependencies lainnya, bisa lihat **package.json** pada projek ini.

Untuk memulai setting harus memakai yarn, kalau belum install, silahkan install dahulu, caranya bisa lihat di [sini](https://classic.yarnpkg.com/en/docs/install/#debian-stable)

Karena menggunakan cli, **versi node** yang diinstall minimal harus **10.xx** dan paling tinggi **14.xx**

### Pengaturan Baru

Pertama clone dulu dari gitlab, kemudian masuk folder peken-4.0-fe,

Kemudian atur **enviroment** untuk host/url api yang nanti dipakai,

cari file **.env.example**, ganti menjadi **.env**, dalam file **.env** ganti isi dari **VUE_APP_API_URL**,

misal **VUE_APP_API_URL=localhost:3000**, isi ini tergantung pada server yang digunakan

Jalankan perintah,

```bash
yarn install
```

tujuannya untuk menginstall semua paket yang ada di **package.json**, kalau sudah diinstall langsung jalankan projek saja

### Menjalankan projek (development)

```bash
yarn run dev
```

Kalau sudah, bisa ikuti petunjuk di terminal masing-masing os, biasanya akses [localhost:8080](https://classic.yarnpkg.com/en/docs/install/#debian-stable) di browser

### Membuild untuk deploy ke server

Jika mau menjalankan di server projek harus di build dahulu, bisa jalankan perintah

```bash
yarn run build
```
