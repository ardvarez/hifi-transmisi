# Dokumentasi Lengkap Modul ERS Mobile V1 (Emergency Restoration System)

Dokumen ini memuat seluruh informasi teknis, alur operasional (*business flow*), struktur data, komponen antarmuka, serta interaksi fitur pada seluruh modul **ERS Mobile Versi 1**.

---

## 1. Ikhtisar & Arsitektur Modul ERS Mobile V1

Sistem **Emergency Restoration System (ERS)** pada aplikasi mobile PLN Transmisi berfungsi untuk mengelola dan memonitor seluruh siklus operasional tower darurat mulai dari ketersediaan stok, mobilisasi, instalasi/ereksi, pembongkaran, hingga inspeksi mutu karantina sebelum kembali ke gudang induk.

### Siklus Hidup Operasional Tower ERS
```
[ Stock Opname / Gudang ] 
           │
           ▼
[ 1. Pemasangan (Erection) ] ──────────► [ 2. Operasi Bertegangan ]
                                                    │
                                                    ▼
[ 4. Pengembalian ke Gudang ] ◄───── [ 3. Karantina & Inspeksi ] ◄───── [ 2. Pembongkaran ]
```

---

## 2. Modul Dashboard / Home ERS (`home-mobile.html`)

Halaman utama dashboard ERS memberikan visibilitas komprehensif terkait inventaris, sebaran geografis, status permit, serta pintasan cepat ke 4 modul operasional.

### 2.1 Komponen & Fitur Tampilan
1. **Header & Status Bar**:
   - Status bar iOS clean concept (Jam, Indikator Sinyal, Wi-Fi, Baterai).
   - Tombol *Back* menuju Katalog Utama (`../catalog-mobile.html`).
   - Badge status server development & judul modul.
   - Tombol Notifikasi ERS (`../notifikasi-catalog-mobile.html?app=ers`).
   - Tombol Drawer Filter Wilayah & Parameter Data.
2. **Katalog Fitur ERS (Quick Navigation Grid)**:
   - **Pemasangan** (`Pemasangan/home-mobile.html`): Ikon Wrench biru.
   - **Pembongkaran** (`Pembongkaran/home-mobile.html`): Ikon Truck Ramp Box oranye.
   - **Pengembalian & Karantina** (`Karantina & Pengembalian/home-mobile.html`): Ikon Box Archive ungu.
   - **Stock Opname** (`Stock Opname/home-mobile.html`): Ikon Boxes Stacked hijau.
   - Tombol trigger modal drawer katalog lengkap (*4 Modul*).
3. **KPI Cards Grid (Ringkasan Ketersediaan & Pemasangan)**:
   - **Total ERS Terpasang (Set)**: Nilai total set yang saat ini berdiri dan beroperasi di lapangan.
   - **Set ERS Lengkap**: Total set ERS yang seluruh komponen modularnya lengkap 100%.
   - **Set ERS Tidak Lengkap**: Total set ERS yang mengalami kehilangan/kerusakan komponen aksesoris.
4. **Peta Sebaran Interaktif (Leaflet.js Map)**:
   - Tab switch: **Set ERS** vs **Tower Operasi**.
   - Marker cluster / custom pin unit sebaran di seluruh unit PLN (Jawa, Bali, Sumatera, dll).
   - Fitur *Reset Zoom* / *Detail Sebaran*.
5. **Grafik & Visualisasi Operasional (Chart.js)**:
   - **ERS Operasi Per Unit** (Bar Chart): Jumlah tower ERS yang beroperasi di masing-masing Unit Induk Transmisi (UIT).
   - **Set ERS Lengkap & Tidak Lengkap** (Stacked Bar Chart): Rasio kelengkapan komponen per unit.
   - **Durasi ERS Operasi** (Donut Chart dengan counter nilai tengah): Distribusi lama masa pakai pemasangan (< 1 bulan, 1–3 bulan, 3–6 bulan, > 6 bulan).
6. **Detail ERS (Data Table & List Cards)**:
   - Search bar live search (pencarian nama unit, nomor penghantar, merk tower).
   - Filter tombol drawer: Unit Pengelola, Jalur Penghantar, Status Kelengkapan, Rentang Tanggal.
   - Card informasi unit, pelaksana, jalur SUTT/SUTET, merk tipe tower, dan durasi operasi.
   - Kontrol paginasi data.

---

## 3. Pusat Notifikasi (`notifikasi-mobile.html`)

Pusat notifikasi mengelola pemberitahuan darurat, perubahan status permit, instruksi pembongkaran, pengingat jadwal, dan hasil inspeksi karantina.

### 3.1 Kategori Filter Notifikasi (Chips Filter)
- **Semua**: Seluruh histori pemberitahuan.
- **Belum Dibaca**: Menampilkan notifikasi dengan status *unread* (badge dot merah/ungu).
- **Pemasangan**: Khusus instruksi kerja, approval permit, dan penugasan pemasangan baru.
- **Pembongkaran**: Notifikasi jadwal pelepasan/pembongkaran tower darurat.
- **Karantina**: Konfirmasi kedatangan material rilis dan status check sheet.

### 3.2 Interaksi & Fitur
- **Tandai Semua Sudah Dibaca**: Membersihkan semua indikator titik merah/badge belum dibaca.
- **Klik Item Notifikasi**: Navigasi langsung menuju halaman detail permit atau form tindakan yang bersangkutan.
- **Badge Prioritas**: Label *Urgent*, *Info*, *Warning*, dan *Success*.

---

## 4. Modul Pemasangan ERS (`/Pemasangan/`)

Modul ini memfasilitasi teknisi lapangan dan supervisor dalam proses survei, pendirian tower ERS, validasi koordinat, serta pengunggahan bukti penyelesaian perakitan.

### 4.1 Struktur Halaman
| File | Deskripsi |
| :--- | :--- |
| `home-mobile.html` | Daftar permit pemasangan, search box, quick filter status (Semua, Menunggu, Proses, Selesai), dan drawer filter parameter. |
| `list-pemasangan.html` | Rincian permit tower dalam satu jalur transmisi, progres ereksi per tower, dan daftar item komponen. |
| `pemasangan-action.html` | Lembar kerja utama pemasangan, peta perbandingan titik rencana vs aktual, dan form submit status pelaksanaan. |

### 4.2 Alur Kerja & Form Tindakan Pemasangan (`pemasangan-action.html`)
1. **Informasi Awal & Unduh File Rencana**:
   - Menampilkan alert sisa hari pelaksanaan permit.
   - Ringkasan lokasi: Nama tower (cth: `TOWER SUTT 150kV UNGARAN-WELERI#0085`), koordinat, unit induk, dan pelaksana.
   - Tombol **Lihat Lokasi**: Modal ringkasan kondisi tapak tower.
   - Tombol **File Rencana**: Bottom sheet untuk mengunduh dokumen PDF SOP/Rencana Erection.
2. **Peta Interaktif (Titik Rencana vs Titik Aktual)**:
   - **Pin Biru**: Titik rencana lokasi tower berdasarkan data perizinan awal.
   - **Pin Hijau**: Titik aktual posisi pendirian tower di lapangan.
   - Garis offset jarak (contoh selisih ~45 meter) dan tombol navigasi langsung ke Google Maps.
3. **Tab Aksesoris & Konfigurasi**:
   - Menampilkan daftar komponen struktural: *Column Section*, *Foundation Base*, *Guy Wire System*, *Insulator String*, dan aksesoris penghantar.
4. **Tahap 1: Submit Mulai Pemasangan**:
   - Tekan tombol **Mulai Pemasangan** di bagian bawah.
   - Muncul modal drawer input:
     - **Waktu Mulai Pemasangan** (Input tanggal & jam sistem).
     - **Evidence Foto Lapangan** (Upload foto kondisi tapak / mobilisasi alat).
     - **Catatan Mulai** (Opsional).
   - Setelah konfirmasi: Status permit berubah menjadi **Sedang Dipasang**, tab **Informasi** terbuka.
5. **Tahap 2: Submit Selesai Pemasangan**:
   - Tombol bawah berganti menjadi **Selesai Pemasangan**.
   - Input modal verifikasi penyelesaian:
     - **Waktu Selesai Pemasangan**.
     - **Evidence Foto Penyelesaian** (Foto tower ERS berdiri tegak & siap tarik konduktor).
     - **Catatan Akhir**.
   - Output: Status tower berubah menjadi **Selesai Pemasangan**, kartu evidence selesai tampil di tab Informasi.

---

## 5. Modul Pembongkaran ERS (`/Pembongkaran/`)

Digunakan saat jalur transmisi permanen telah pulih dan tower darurat ERS harus dibongkar secara aman untuk pengembalian komponen.

### 5.1 Struktur Halaman
| File | Deskripsi |
| :--- | :--- |
| `home-mobile.html` | Daftar permit pembongkaran dengan status *Siap Bongkar*, *Sedang Dibongkar*, dan *Selesai*. |
| `list-pembongkaran.html` | Daftar tower dalam permit yang siap diturunkan. |
| `pembongkaran-action.html` | Lembar kendali pembongkaran, verifikasi *mixed komponen*, upload bukti pelepasan, dan monitoring durasi dismantling. |

### 5.2 Alur Kerja Pembongkaran
1. **Pemeriksaan Spesifikasi Tower**:
   - Memeriksa apakah tower menggunakan komponen campuran (*Mixed Component: Ya/Tidak*).
   - Verifikasi data permit, tanggal mulai operasi, dan batas waktu dismantling.
2. **Tahap 1: Mulai Pembongkaran**:
   - Tekan tombol **Mulai Pembongkaran**.
   - Form modal: Waktu mulai pelepasan + Foto evidence awal pembongkaran.
   - Status berubah menjadi **Sedang Dibongkar**.
3. **Pelepasan Komponen Bertahap**:
   - Penurunan konduktor & travers.
   - Pelepasan guy wire dan pemilahan baut/jointing.
   - Pembongkaran kolom mast dan fondasi darurat.
4. **Tahap 2: Selesai Pembongkaran**:
   - Unggah foto evidence material rilis yang sudah ditata di atas truk/palet.
   - Submit laporan selesai pembongkaran.
   - Material otomatis dialihkan statusnya ke batch **Karantina & Pengembalian**.

---

## 6. Modul Pengembalian & Karantina (`/Karantina & Pengembalian/`)

Modul pengelolaan logistik retur material ERS dari site pembongkaran menuju gudang transit/induk, serta kontrol mutu (*Quality Assurance*) untuk memastikan seluruh komponen ERS diperiksa kondisinya (normal/layak, kurang/hilang, rusak/perlu repair) sebelum masuk kembali ke rak penyimpanan gudang.

### 6.1 Struktur Halaman & Komponen
| File | Deskripsi |
| :--- | :--- |
| `home-mobile.html` | Monitoring daftar permit retur (`RTR...`) dengan tahapan status: *Mulai / Siap Dikirim*, *Sedang Dikirim*, *Sedang Dikarantina*, dan *Selesai*. Dilengkapi tombol aksi *Keberangkatan*, *Kedatangan*, dan *Lihat Detail*. |
| `list-karantina.html` | Rincian batch material retur dan ringkasan item komponen yang diterima di gudang. |
| `karantina-action.html` | Lembar kendali batch karantina tower ERS, spesifikasi teknis, verifikasi per-section (*Column Section*, *Foundation Section*, *Guy Wire Section*), serta riwayat data & foto evidence pembongkaran dari site. |
| `check-sheet.html` | Lembar uji pemeriksaan fisik detail per grup aksesoris (Plate Column, Erection Tools, Foundation, Guy Wire) dengan input jumlah normal, hilang, rusak, serta foto evidence. |

### 6.2 Alur Operasional Pengembalian & Karantina (End-to-End)

```
[ 1. Status: Mulai / Siap Dikirim ]
               │
               ▼  Action: User tekan tombol "Keberangkatan" (Input Waktu Keberangkatan & Armada)
[ 2. Status: Sedang Dikirim ]
               │
               ▼  Action: Armada sampai di site/gudang transit -> User tekan "Kedatangan" (Input Waktu Tiba)
[ 3. Status: Sedang Dikarantina ]
               │
               ▼  Action: User tekan "Lihat Detail" / "Proses Karantina"
[ 4. Verifikasi Section (karantina-action.html) ]
               │
               ├──> Pengecekan Column Section ─────► Form check-sheet.html
               ├──> Pengecekan Foundation Section ──► Form check-sheet.html
               └──> Pengecekan Guy Wire Section ───► Form check-sheet.html
               │
               ▼  Seluruh section berstatus "Sudah Dicek"
[ 5. Selesai Karantina & Penerbitan Berita Acara ]
```

#### Tahap 1: Keberangkatan dari Site (Status: *Mulai / Siap Dikirim*)
- Data permit retur (contoh: `RTR20250000001`) tampil dengan informasi: Estimasi Berangkat, Estimasi Tiba, Jumlah Tower Emergency (TE), dan Merk.
- User menekan tombol **Keberangkatan**.
- Muncul modal pengisian: **Waktu Pengiriman Dimulai (Waktu Keberangkatan)**, Armada Pengangkut, Driver/PIC, dan Foto Armada Berangkat.
- Setelah submit, status permit berubah menjadi **Sedang Dikirim**.

#### Tahap 2: Kedatangan di Gudang Transit (Status: *Sedang Dikirim*)
- Saat armada logistik tiba di gudang tujuan/transit, user pada data permit (contoh: `RTR20250000002`) menekan tombol **Kedatangan**.
- Muncul modal konfirmasi: **Waktu Sampai / Kedatangan Material**, Petugas Penerima Gudang, dan Foto Kedatangan Muatan.
- Setelah konfirmasi, status permit berubah menjadi **Sedang Dikarantina**.

#### Tahap 3: Pelaksanaan Karantina & Check Sheet (Status: *Sedang Dikarantina*)
- User membuka halaman **karantina-action.html** melalui tombol **Lihat Detail**.
- Halaman menampilkan spesifikasi tower ERS, tanggal diterima gudang, tab riwayat pembongkaran dari site, serta daftar section material:
  - **Column Section** (Mast modul, flange, baut sambung)
  - **Foundation Section** (Base plate, gimbal pin, anchor pad)
  - **Guy Wire Section** (Sling kawat baja, turnbuckle, guy grip)
- User menekan tombol **Check Section** untuk membuka formulir uji teknis di **check-sheet.html**.

#### Tahap 4: Pengisian Check Sheet QC (`check-sheet.html`)
- Pada setiap grup aksesoris, petugas menginput:
  1. **Jumlah Peralatan Normal (Layak)** + Upload Evidence Foto
  2. **Jumlah Peralatan Tidak Tersedia (Hilang)** + Upload Evidence Foto
  3. **Jumlah Peralatan Rusak (Afkir/Repair)** + Upload Evidence Foto
  4. **Waktu Pemeriksaan Karantina**
  5. **Keterangan / Catatan Teknis Cacat Fisik**
- Sistem secara otomatis menghitung **Total Item Terhitung** di sticky summary bar bawah.
- User menekan **Simpan Pengecekan** -> Status section di `karantina-action.html` terbarui menjadi **Sudah Dicek** (Hijau).

#### Tahap 5: Penyelesaian Karantina & BAST
- Ketika seluruh section telah diverifikasi, tombol **Selesaikan Karantina** otomatis aktif di bagian bawah.
- Sistem mencatat waktu selesai karantina, menerbitkan Berita Acara Karantina, dan mengarahkan material normal kembali ke rak siap pakai.

---

## 7. Modul Stock Opname (`/Stock Opname/`)

Berfungsi untuk audit inventaris fisik berkala di gudang unit penyimpanan ERS.

### Fitur Utama:
- Pencocokan jumlah fisik modul ERS di rak penyimpanan dengan catatan di database sistem.
- Filter batch berdasarkan Gudang Induk, Pelaksana Stock Opname, dan Periode Audit.
- Pembuatan Berita Acara Stock Opname (BASO) fisik ERS.

---

## 8. Ringkasan Status & Navigasi Antar Halaman

```
[ Dashboard Utama: ers/home-mobile.html ]
   ├──> Notifikasi: ers/notifikasi-mobile.html
   │
   ├──> [Pemasangan]
   │     ├── home-mobile.html (List Permit Pasang)
   │     ├── list-pemasangan.html (Detail Tower Pasang)
   │     └── pemasangan-action.html (Mulai -> Selesai Erection)
   │
   ├──> [Pembongkaran]
   │     ├── home-mobile.html (List Permit Bongkar)
   │     ├── list-pembongkaran.html (Detail Tower Bongkar)
   │     └── pembongkaran-action.html (Mulai -> Selesai Bongkar)
   │
   ├──> [Karantina & Pengembalian]
   │     ├── home-mobile.html (List Batch Karantina)
   │     ├── list-karantina.html (Daftar Item Karantina)
   │     ├── karantina-action.html (Konfirmasi Tiba -> Verifikasi Section)
   │     └── check-sheet.html (Checklist Teknis & Bukti Cacat)
   │
   └──> [Stock Opname]
         └── home-mobile.html (Audit Stok Gudang ERS)
```
