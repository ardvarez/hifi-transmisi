# Dokumentasi Konversi Dashboard ERS (Power Inspect Style)

## 1. Ringkasan
Dashboard ERS pada path `c:\KERJAAN\Project\hifi-transmisi\hifi-ers\Dashboard\dashboard-ERS (Non-Detail).html` telah dikonversi mengikuti tampilan resmi **Power Inspect PLN** (`https://powerinspect.pln.co.id/dashboard/emergency-restoration-system`).

## 2. Fitur & Komponen yang Diimplementasikan
- **System Topbar**: Kontak helpdesk (`helpdesk.pi@iconpln.co.id`), Security issue (`soc@pln.co.id`), dan status online.
- **Left Rail Sidebar (80px)**: Logo PLN petir dan menu navigasi terintegrasi ke seluruh modul (Portal, ERS, Peta PI, Tower, Mutasi, Perencanaan, Perizinan).
- **Header & Breadcrumbs**: `Dashboard ERS / Ketersediaan ERS` dengan tombol Filter.
- **KPI Summary Cards (3 Cards)**:
  - Total ERS Terpasang (Set) (nilai dinamis sesuai filter data)
  - Total ERS Set ERS Lengkap
  - Total ERS Set ERS Tidak Lengkap
- **Peta Interaktif (Leaflet)**:
  - Tab 1: **Set ERS** dengan pin marker gudang/lokasi dan popup detail.
  - Tab 2: **Tower Operasi**:
    - Titik tower beroperasi menggunakan icon transmisi tower (biru primary circle dengan transmisi tower putih dan outer halo translucent).
    - Legend peta disederhanakan menjadi 1 item representatif (**Tower Operasi** warna biru primary).
    - Cluster bulat biru dengan angka agregasi titik (misal cluster 2).
    - Popup card mengusung **Modern Card Grid**:
      - Accent top bar gradient (Navy).
      - Header Penghantar & Unit Pelaksana.
      - **Multi-Tower Pill Switcher** (`[ 1. T.03 ] [ 2. T.02 ] [ 3. T.01 ]`): user dapat memilih tower secara instan tanpa menambah tinggi popup.
      - Box detail tower aktif (Nama Tower & Functloc).
      - 2x2 Spec Box: Merk ERS, Jumlah Set, Total Tower, dan Status.
      - Timeline progress bar visual tanggal pasang s/d rencana bongkar.
      - Tombol aksi cepat: `Lihat di Tabel ↓`.
  - Tab 3: **Tower Operasi Terpasang** (Data Acuan Perencanaan & Perizinan Pemasangan ERS):
    - Titik tower operasional yang telah disetujui izin pemasangannya (badge emerald hijau `Terpasang (Izin Lengkap)`).
    - Marker icon transmisi tower warna biru primary dengan animasi outer halo.
    - Legend peta 1 item representatif (**Tower Operasi Terpasang** warna biru primary).
    - Popup card mengusung **Modern Card Grid + Multi-Tower Switcher**:
      - Accent top bar gradient (Emerald).
      - Header Penghantar & Unit Pelaksana.
      - **Dual Reference Chips**: Tag biru `ASM2026...` (Izin) & Tag teal `PTE2026...` (Perencanaan).
      - **Multi-Tower Pill Switcher** (`[ 1. T.03 ] [ 2. T.02 ] [ 3. T.01 ]`).
      - Box detail tower aktif (Nama Tower & Functloc).
      - 2x2 Spec Box: Merk & Tipe, Jumlah Set, Klasifikasi, Total Tower.
      - Timeline progress bar visual tanggal pasang s/d rencana bongkar.
      - Footer PIC Pemasangan & Tombol pintas `Lihat di Tabel ↓`.
    - Tabel 15 kolom dan KPI cards otomatis tersinkronisasi menampilkan data tower operasional terpasang saat tab ini aktif.
  - Tombol **Buka Semua Detail / Tutup Semua Detail**.
  - **Tinggi Peta Ditingkatkan (560px)**: Seluruh peta kepulauan Indonesia langsung terlihat utuh tanpa terpotong.
  - **Tooltip / Popup Diperbesar (345px width & typography ramah lansia/senior)**: Font title (13.5px), spek nilai (12px), chip/dates/button (10.5-11px), padding lebih lega.
  - Legend peta interaktif (Set ERS, Tower Operasi, Tower Terpasang).
- **Grafik Analitik ERS (3 Chart Card di Atas Tabel)**:
  1. **ERS Operasi Per Unit**: Horizontal Bar Chart menampilkan jumlah ERS Terpasang (biru) dan Selesai (hijau) per Unit Induk (P3BS, P3BSUL, UIT JBT, NTB, P3BKAL, UIT JBM, dsb.).
  2. **Set ERS Lengkap & Tidak Lengkap**: Grouped Column Bar Chart dengan data perbandingan status Set ERS Lengkap vs Tidak Lengkap per Unit Induk (dilengkapi dummy data representatif).
  3. **Durasi ERS Operasi**: Doughnut Chart dengan ringkasan stat di tengah (`63 Total Data`) dan breakdown durasi: `< 1 Tahun` (biru), `1 - 3 Tahun` (kuning), dan `> 3 Tahun` (merah).
- **Tabel Data (15 Kolom Standar Power Inspect)**:
  1. No.
  2. Unit Induk
  3. Unit Pelaksana
  4. Penghantar
  5. Tower (dengan tombol `View More` jika teks panjang)
  6. ID Functloc
  7. Latitude
  8. Longitude
  9. Jumlah Set Terpasang
  10. Merk Terpasang
  11. Penyebab Pemasangan
  12. Tanggal Pemasangan
  13. Rencana Tanggal Pembongkaran
  14. Keterangan (dengan tombol `View More`)
  15. Status (`Terpasang`)
- **Pencarian & Sorting**: Filter pencarian real-time dan pengurutan (A-Z, Z-A, angka) pada tiap kolom header tabel.
- **Paginasi Interaktif**: Pilihan 5, 10, 25, 50 baris per halaman, navigasi halaman pintar (`1, 2, 3...`).
- **Modal Filter (Sesuai Aturan Standar Input UI PLN)**:
  - Unit Induk (Combo Box Default)
  - Unit Pelaksana (Cascading Combo Box)
  - Merk ERS (Segmented Pill tanpa icon: Semua, Lindsey, SBB)
  - Status (Segmented Pill: Semua, Terpasang, Tersedia)
  - Rentang Tanggal Pemasangan
- **Floating Notes FAB**: Catatan dan info Hifi tersimpan otomatis di localStorage.
- **Preview & Komparasi Tooltip/Popup**: Telah dibuat simulasi 3 opsi desain popup di `hifi-ers/Dashboard/preview-tooltip-options.html` lengkap dengan opsi multi-tower.
- **Implementasi Tooltip Peta Terpilih (Opsi 1 Modern Card Grid + Multi-Tower Switcher)**:
  - Header bergradien dengan tombol close circular modern (`×`).
  - Dual Reference Chip (No. Permit & No. Rencana) dengan micro-icon dan monospace font.
  - Multi-Tower Pill Bar tersegmentasi untuk navigasi tower instan jika titik memiliki >1 tower.
  - Active Tower Box lengkap dengan tag indeks tower aktif (`Tower 1 dari 3`) dan Functloc code.
  - Grid Spesifikasi 2x2 berlabel icon (`Merk ERS`, `Jumlah Set`, `Klasifikasi / Status`, `Total Tower`).
  - Visual Timeline Bar progress durasi terpasang (Tanggal Pasang s/d Rencana Bongkar).
  - Footer PIC pelaksana + tombol aksi pintas `Lihat di Tabel ↓` (filter & auto-scroll ke baris tabel).
- **Integrasi Home Portal**: Menu pada `hifi-home/home.html` telah diperbarui mengarah ke file ini.

