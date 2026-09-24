# Prompt: Pusat Notifikasi Multi-Modul (Mobile-First)

## Role & Objective

Bertindaklah sebagai Senior UI/UX Designer & Lead Frontend Engineer. Buatkan desain antarmuka mobile-first beserta kode komponen yang modular, bersih, dan production-ready (React + Tailwind CSS) untuk **Pusat Notifikasi Multi-Modul Aplikasi Enterprise Manajemen Aset & Operasional Ketenagalistrikan**.

---

## 1. Mekanisme Akses Kontekstual (Contextual Navigation & Deep Linking)

Komponen ini menggunakan **1 sistem notifikasi terpadu (single shared component/page)** yang dapat dipanggil secara fleksibel:

- **Akses Global:** Jika dibuka dari menu utama/global navigasi, tab modul otomatis terpilih ke `Semua` dengan header umum *"Pusat Notifikasi"*.
- **Akses Kontekstual per Modul:** Jika activity/layar notifikasi ini dipicu dari dalam modul tertentu (misal: tombol notifikasi di halaman *NEW PST*, *Power Inspect*, atau *Power Swift*):
  - Komponen menerima prop/parameter (contoh: `initialModule="new_pst"` atau query parameter `?module=new_pst`).
  - **Auto-Filter:** Tab modul langsung terkunci/terpilih secara otomatis pada modul pemanggil, dan feed langsung menampilkan notifikasi modul tersebut.
  - **Dynamic Header:** Judul header serta sub-teks langsung berganti merefleksikan modul terkait (contoh: *"Notifikasi NEW PST"* dengan sub-teks *"Master Data, Persetujuan & Mutasi Aset"*).
  - Pengguna tetap dapat menggeser/mengganti filter tab ke modul lain jika diperlukan (*switchable tab*).

---

## 2. Lingkup Modul & Taksonomi Notifikasi

### A. NEW PST (Master Data, Persetujuan & Mutasi Aset)

1. **Penambahan Aset Baru** (Tipe: Info)
2. **Permintaan Persetujuan Penambahan Aset** (Tipe: Action Required / Approval)
3. **Permintaan Persetujuan Perubahan Aset** (Tipe: Action Required / Approval)
4. **Permintaan Persetujuan Mutasi Aset** (Tipe: Action Required / Approval)

### B. Power Inspect (Inspeksi & Work Order Aset)

1. **Inspeksi Ulang WO** (Menampilkan counter: *jumlah aset yang diinspeksi ulang*)
2. **WO Baru dari Tindak Lanjut** (Tipe: Task Assignment)
3. **WO Baru dari Perencanaan Jadwal** (Tipe: Scheduled Task)
4. **WO Baru Kondisional** (Tipe: Urgent / Unscheduled Task)
5. **Aset Anomali dari Inspeksi Terbaru** (Tipe: Alert / Warning)

### C. Power Swift - ERS (Emergency Restoration System & Logistik)

1. **Permit Baru Pemasangan** (Tipe: Permit Request / Approval)
2. **Permit Baru Pembongkaran** (Tipe: Permit Request / Approval)
3. **Permit Baru Pengembalian & Karantina** (Tipe: Material Tracking)
4. **Stock Opname Baru** (Tipe: Inventory Audit)
5. **Stock Opname Ulang** (Tipe: Inventory Verification)

---

## 3. Layout & Architectural Requirements

### A. Dynamic Header & Search Bar

- **App Bar**:
  - Tombol kembali (navigasi balik ke modul pemanggil).
  - Judul dinamis sesuai modul aktif (contoh: *"Pusat Notifikasi"* saat `all`, atau *"Notifikasi Power Inspect"* saat modul aktif).
  - Sub-teks dinamis sesuai deskripsi fungsi modul.
  - Aksi cepat *Tandai Semua Dibaca* (berlaku untuk modul yang sedang aktif difilter) dan tombol setting/filter lanjutan.
- **Search Bar**: Input pencarian terpadu dengan placeholder kontekstual: `"Cari notifikasi, GI, nomor WO/Permit, atau anomali..."`.

### B. Dual-Tier Filtering

- **Level 1 (Scope Modul)**: Horizontal scroll tab pills dengan badge angka unread:
  - `Semua`
  - `NEW PST`
  - `Power Inspect`
  - `Power Swift (ERS)`
  *(State aktif ditandai kontras warna solid primary/dark).*
- **Level 2 (Status & Urgensi)**: Quick filter pills:
  - `Semua Status`
  - `Belum Dibaca`
  - `Perlu Persetujuan`
  - `Prioritas / Anomali`
  - `Hari Ini`

### C. Timeline Feed

- Pengelompokan daftar notifikasi berdasarkan rentang waktu dengan heading informatif (contoh: `HARI INI • 3 Notifikasi`).

---

## 4. Notification Card Anatomy (Data-Dense & Scannable)

Setiap kartu notifikasi memiliki hierarki visual:

1. **Visual Anchor & Unread State**:
   - Ikon visual kategori/modul di kiri dalam lingkaran berlatar lembut (*soft rounded background*).
   - Indikator unread berupa titik biru solid (*blue dot*) di pojok kanan atas kartu.
2. **Header Badge Row (Single-Line Alignment)**:
   - Deretan chip horizontal rapi:
     - Badge Modul (`NEW PST` / `Power Inspect` / `Power Swift`).
     - Badge Urgensi jika ada (`Perhatian`, `Urgent`, `Persetujuan`).
     - Badge Kategori Aktivitas (`Mutasi Aset`, `WO Kondisional`, `Permit Pemasangan`, dll).
3. **Konten Utama**:
   - **Judul**: Bold, jelas, menyertakan nomor referensi dokumen/aset (contoh: *Permintaan Persetujuan Penambahan Aset #REQ-ADD-2026-089* atau *Inspeksi Ulang WO #WO-882 (5 Aset)*).
   - **Deskripsi Ringkas**: Maksimal 2 baris (*line-clamp-2*).
4. **Structured Metadata Box**:
   - Cardlet/container abu-abu terang (*subtle cardlet*) berformat *key-value*, memuat parameter spesifik operasional (misal: *Peralatan*, *Lokasi GI*, *Pemohon*, *Status Register*, atau *Jumlah Aset Terdampak*).
5. **Card Footer**:
   - Timestamp relatif di kiri bawah (contoh: *15 menit yang lalu*).
   - Tombol Aksi (CTA) kontekstual di kanan bawah:
     - **Approval/Urgent**: Tombol solid primary kontras (contoh: *Review & Setujui*, *Proses WO*).
     - **Informational/Detail**: Tombol outline/ghost subtle (contoh: *Lihat Aset Register →*, *Cek Detail Anomali →*).

---

## 5. Deliverables Output

1. Sediakan **Mock Data JSON** representatif berisi notifikasi dari ketiga modul di atas beserta metadata dinamisnya.
2. Buatkan komponen **React (Tailwind CSS)** yang menerima prop `initialModule` (default: `'all'`), menangani pemfilteran data secara otomatis, mengupdate header dinamis, dan mendukung toggle unread/read.
