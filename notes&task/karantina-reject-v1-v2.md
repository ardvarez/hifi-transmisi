# Dokumentasi Alur Simulasi Data Reject (Karantina Ulang) V1 & V2

## 1. Ringkasan Fitur
Fitur simulasi penanganan **Data Reject (Karantina Ulang)** diimplementasikan seragam di **Mobile V1** dan **Mobile V2**, dengan pemisahan identitas permohonan (*Permit ID*) khusus untuk kasus ditolak:
- **Kasus Normal / Baru**: `RTR20250000001` (atau ID permit dinamis lainnya dari URL)
- **Kasus Ditolak / Reject**: `RTR20250000004` (dengan mode `karantina_ulang`)

---

## 2. Perubahan Alur Bisnis Data Reject
1. **Pemisahan Nomor RTR**:
   - Data normal memakai `RTR20250000001` (atau ID masing-masing).
   - Data reject diverifikasi menggunakan `RTR20250000004`.
2. **Bypass Tahap Kedatangan**:
   - Pada data reject (`RTR20250000004`), material sudah tercatat tiba di gudang sejak `29 Okt 2025, 14:15 WIB (Sudah Diterima)`.
   - Form/tombol konfirmasi kedatangan di-bypass secara otomatis.
3. **Status Detail & Catatan Verifikator (1 Layer Terpadu di V1)**:
   - Status verifikasi: `Ditolak Verifikator (Karantina Ulang)`.
   - Banner digabung menjadi 1 layer informasi terpadu (tidak bertumpuk 2 box terpisah):
     - Memuat teks operasional kedatangan sekaligus catatan penolakan Verifikator Asman.
     - Dibatasi maksimal **3 baris** dengan CSS line-clamp dan tombol interaktif **"Lihat Selengkapnya" (View More)**.
   - Aksi **"Lihat Komponen Ditolak"** disematkan di dalam banner sebagai tombol pemicu **Bottom Sheet Modal**.
    - Bottom sheet modal (V1) & Section Card (V2) menampilkan:
      - Informasi kuantitas status: Normal : N, Rusak : N, Tidak Tersedia : N.
      - Tombol **Revisi Section** diposisikan tepat di bawah informasi kuantitas dengan tampilan memanjang (*full-width*) agar area klik lebih luas.
4. **Tindakan Revisi & Pre-filled Nilai**:
   - Tombol per-section di `karantina-action.html` aktif langsung sebagai `Revisi Section`.
   - Pada `check-sheet.html`, input kuantitas otomatis terisi berdasarkan inputan sebelumnya.
   - Tombol sticky footer langsung siap untuk `Kirim Ulang Hasil Karantina` ke Verifikator.

---

## 3. Perbaikan Bug "Lihat Detail Selalu ke 001"
- **Penyebab**: Fungsi `setKarantinaCase('baru')` sebelumnya menimpa variabel `currentRtrCode` menjadi hardcoded `'RTR20250000001'`. Selain itu, tautan kartu reject di list masih merujuk ke `-05` bukan `004`.
- **Solusi**:
  1. `currentRtrCode` kini mempertahankan permit ID dari URL (misal: `RTR20250000002`, `RTR20250000003`, dll.).
  2. Kartu reject di list/home dikaitkan langsung ke `RTR20250000004` dengan parameter `&mode=karantina_ulang`.
  3. Modal detail di home mobile V2 menyediakan tombol aksi langsung menuju halaman aksi karantina sesuai ID yang diklik.

---

## 4. Daftar File yang Diperbarui
- `hifi-mobile/ers/Karantina & Pengembalian/karantina-action.html` (V1)
- `hifi-mobile/ers/Karantina & Pengembalian/list-karantina.html` (V1)
- `hifi-mobile/ers/Karantina & Pengembalian/check-sheet.html` (V1)
- `hifi-mobile/ers/Karantina & Pengembalian/home-mobile.html` (V1)
- `hifi-mobile/ers-v2/Karantina & Pengembalian/karantina-action.html` (V2)
- `hifi-mobile/ers-v2/Karantina & Pengembalian/list-karantina.html` (V2)
- `hifi-mobile/ers-v2/Karantina & Pengembalian/home-mobile.html` (V2)
- `hifi-ers/Perencanaan/Karantina & Tindak Lanjut/verifikasi-karantina.html` (Web ERS - Input Reject Per-Komponen)
- `hifi-home/home.html` (Menu Navigasi Portal)

---

## 5. Input Alasan / Catatan Reject Per Komponen (Web ERS)
- Modal penolakan di `verifikasi-karantina.html` menampilkan card input teks alasan per baris komponen yang diceklis.
- Terdapat validasi wajib isi seluruh catatan komponen yang ditolak sebelum submit.
- Placeholder dan informasi komponen (Nama, Merk, Kode Material, Satuan, Kuantitas Rusak/Selisih) ditampilkan otomatis secara kontekstual.

- Pada kartu reject per komponen kini menampilkan baris badge kondisi & quantity: Normal (Stock Standby), Rusak, Tidak Tersedia, Selisih (jika ada), dan Total Stock.
- **Slide Up Expandable Bottom Sheet (V1 & V2)**: Bottom sheet modal / drawer dapat di-slide / drag ke atas atau disentuh pada handle untuk memperluas area scroll hingga 96vh.

---

## 6. Pembersihan UI Redundan & Chip Status Komponen (V1 & V2)
- **Status Spesifikasi Redundan Dihapus**: Menghapus baris "Status Verifikasi: Ditolak Verifikator (Karantina Ulang)" / "Status Permit" dari kartu spesifikasi umum di `karantina-action.html` (V1 & V2).
- **Label Tanggal Tiba**: Teks `(Sudah Diterima)` dihapus, format tanggal tiba bersih: `29 Okt 2025, 14:15 WIB`.
- **Notice Banner Takeout**: Banner `Revisi Karantina Ulang (Ditolak Verifikator)` / `Catatan Verifikator Asman` di atas check sheet dihapus.
- **Chip Status Karantina Ulang**: Chip status berlabel `Karantina Ulang` digeser ke ujung paling kanan kartu grup komponen (V1 & V2) agar layout seimbang dan tidak kosong.
- **Catatan Reject Verifikator pada Komponen**: Ditambahkan card catatan reject verifikator tepat di bawah header komponen pada `check-sheet.html` (V1 & V2) sebagai panduan/gambaran teknisi saat melakukan perbaikan fisik.
- **Section Lolos QC Dihilangkan saat Karantina Ulang**: Pada `karantina-action.html` (V1 & V2), kartu Guy Wire Section (yang sebelumnya berstatus "Sesuai / Lolos QC") otomatis disembunyikan saat mode karantina ulang aktif, sehingga hanya section yang bermasalah dan memerlukan revisi (`Column Section` & `Foundation Section`) yang tampil.
- **Nama Komponen Check Sheet Dipertahankan**: Pada `check-sheet.html` (V1 & V2), nama komponen header tidak ditimpa/diubah (tetap menggunakan template asli seperti `Plate Column` / `Plate Column & Mast Modul`).
- **Hanya Komponen Karantina Ulang yang Tampil**: Pada `check-sheet.html` (V1 & V2), seluruh grup komponen lain yang tidak bermasalah disembunyikan saat mode karantina ulang aktif, sehingga hanya komponen yang perlu direvisi yang tampil. Input pada komponen yang disembunyikan tidak dihitung dalam total stok.
- **Perapihan List Section (V1 & V2)**:
  - Pada V2, tombol aksi pengecekan (`btnCheckColumn`, `btnCheckFoundation`) dipindahkan ke luar kotak `komponen-ulang-box` agar posisi tombol selalu seragam di bagian bawah kartu section (baik pada mode permohonan baru maupun karantina ulang).
  - Pada V1, layout kartu section diseragamkan dengan V2: dilengkapi icon section, sub-judul item aksesoris, dan chip status pill (`Belum Dicek`, `Revisi Karantina`, `Selesai Dicek`) di sudut kanan atas kartu.
  - Teks tombol pengecekan diseragamkan menjadi `Check Section` / `Revisi Section` / `Selesai Dicek`.

---

## Update Drawer Overlay Kanan & Reposisi Chip Check Sheet (15 Okt 2026)

### 1. Right Slide-Over Drawer Overlay di [verifikasi-karantina.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-ers/Perencanaan/Karantina%20&%20Tindak%20Lanjut/verifikasi-karantina.html)
- Tombol **Detail Pemasangan** dan **Detail Pembongkaran** sekarang membuka slide-over overlay drawer kanan (`.drawer-card-right`, lebar 620px).
- **Detail Pemasangan**:
  - Diambil dari data [pemasangan-action.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers/Pemasangan/pemasangan-action.html).
  - Berisi identitas permit `INST202500091`, kode mobile `ASM20250000001`, lokasi tapak `TOWER SUTT 150kV UNGARAN-WELERI #0085`, koordinat `-7.2575, 109.1866`, waktu pasang `10 Mei - 20 Mei 2025`, PIC `Luis Andreas BGS`, spesifikasi tower Lindsay 150kV Suspension Guyed Mast, seksi modul terpasang, dan galeri 4 foto proses pemasangan lengkap dengan modal lightbox zoom preview.
- **Detail Pembongkaran**:
  - Diambil dari data [pembongkaran-action.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers/Pembongkaran/pembongkaran-action.html).
  - Berisi permit `DIS20250012`, lokasi tapak, jadwal `18 - 20 Mar 2025`, PIC `Budi Santoso`, Safety Officer `Ahmad Fauzi`, catatan penurunan komponen, dan galeri 4 foto proses pelepasan konduktor, mast modul, sling guy wire, hingga loading truk transit.

### 2. Reposisi Chip Status Karantina Ulang di Check Sheet
- File: [ers/check-sheet.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers/Karantina%20&%20Pengembalian/check-sheet.html) & [ers-v2/check-sheet.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Karantina%20&%20Pengembalian/check-sheet.html)
- Chip `Karantina Ulang` dipindahkan langsung bersanding di sebelah kanan nama komponen (h2 / title block) sehingga baris judul padat terisi dan tidak menyisakan ruang kosong.

### 3. Penyesuaian List Section di [ers/karantina-action.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers/Karantina%20&%20Pengembalian/karantina-action.html)
- Tampilan kartu list section V1 disesuaikan 100% seperti gambar referensi:
  - Judul section bold di baris atas (`Column Section`, `Foundation Section`, `Guy Wire Section`).
  - Baris label `Status Data` dengan nilai `Belum Pengecekan` (warna teks merah polos `#ef4444` tanpa background pill).
  - Baris label `Total Aksesoris` dengan kuantitas bold di sebelah kanan (`20` untuk Column & Foundation, `12` untuk Guy Wire).
  - Tombol aksi berlabel `Check` lengkap dengan icon checklist clipboard.

### 4. Perbedaan Karakteristik Desain (Gap Enhancement V1 vs V2)
- **V1 ([ers/karantina-action.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers/Karantina%20&%20Pengembalian/karantina-action.html))**:
  - Mengikuti UI klasik/sederhana (tampilan list section flat dengan metadata Status Data & Total Aksesoris + tombol `Check`).
  - Detail komponen yang ditolak diakses melalui bottom sheet trigger.
- **V2 ([ers-v2/karantina-action.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Karantina%20&%20Pengembalian/karantina-action.html))**:
  - Sengaja **dibiarkan dan dipertahankan** sebagai versi enhancement modern untuk memperlihatkan gap kemajuan UI/UX.
  - Memiliki icon box per-seksi, subtitle item rincian, status badge pill, serta `komponen-ulang-box` terintegrasi langsung di dalam kartu (menampilkan nama komponen reject, catatan verifikator inline, dan breakdown kuantitas Normal/Rusak/Tidak Tersedia).