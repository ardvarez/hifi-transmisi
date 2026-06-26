# Screening Report: Dashboard Trend (Power Inspect)

## 1. Informasi Halaman
- **URL**: `http://10.1.48.26:7759/dashboard/trend`
- **Judul Halaman**: Dashboard Trend Hasil Inspeksi (Power Inspect)

## 2. Analisis UI & Layout
Berdasarkan hasil pemindaian (screening), halaman ini difungsikan sebagai form pencarian dan filter untuk melihat tren hasil inspeksi aset. Struktur utama dari halaman ini meliputi:

### A. Fitur Pencarian Cepat (Quick Search)
- Terdapat input teks dengan placeholder **"Masukkan Nama Gardu Induk"** untuk pencarian spesifik ke Gardu Induk.

### B. Filter Hierarki Berjenjang (Cascading Dropdowns)
Sistem menggunakan *dropdown* yang saling bergantung (berjenjang) dari level organisasi tertinggi hingga ke spesifikasi parameter inspeksi:
1. **Regional** (Contoh: TSJ)
2. **Kantor Induk** (Contoh: UITJBB)
3. **Unit Pelaksana** (Contoh: UPT CAWANG)
4. **ULTG** (Contoh: ULTG CAWANG)
5. **Gardu Induk** (Contoh: GI 150KV CAWANG LAMA)
6. **Jenis Aset** (Contoh: Over Current Relay)
7. **Aset** (Pemilihan item aset spesifik berdasarkan ID/merek, misal: *ALSTOM - 36050079 - RST*)
8. **Parameter Inspeksi** (Pemilihan jenis pengujian/inspeksi, misal: *Pengujian fungsi tripping sistem proteksi*)

*Catatan: Dropdown di-load secara dinamis dan baru bisa dipilih setelah dropdown di atasnya terisi.*

### C. Filter Waktu (Rentang Tanggal)
- **Tanggal Awal** (Start Date)
- **Tanggal Akhir** (End Date)
Pengguna dapat menentukan durasi inspeksi yang ingin dianalisis trennya.

### D. Aksi Utama
- Tombol **"CARI DATA"**: Digunakan untuk memicu eksekusi pencarian berdasarkan parameter yang telah dipilih di atas.

### E. Hasil Pencarian Data (Setelah "CARI DATA" di-klik)
Setelah melakukan pencarian, halaman menampilkan 2 section utama di bawah form pencarian:
1. **Section Chart**: Menampilkan diagram garis (*Line Chart*) yang memvisualisasikan tren parameter inspeksi terhadap waktu.
2. **Section Tabel Detail**: Menampilkan rincian data poin-poin dari grafik tersebut dalam bentuk tabel tabular di bawah chart.

## 3. Catatan Kendala Saat Screening
- Saat melakukan simulasi pencarian dengan mengklik tombol **"CARI DATA"**, sistem merespons dengan *popup error*: **"Terjadi Kesalahan. User Anda Sedang Login Pada Device Lain"**.
- Hal ini menyebabkan sesi *logout* otomatis dan kembali ke halaman login (kemungkinan karena sistem tidak mengizinkan *multi-login* atau *concurrent session* pada satu akun di waktu bersamaan).

## 4. Rencana Enhancement
Sesuai instruksi, dokumen ini akan menjadi dasar sebelum melanjutkan ke pembuatan atau perbaikan fitur (*enhancement*). Silakan sebutkan bagian mana yang ingin di-*enhance* (misal: perbaikan UI, optimalisasi pengambilan data dropdown, perubahan *flow* pencarian, penambahan chart/grafik setelah data dicari, dsb).
