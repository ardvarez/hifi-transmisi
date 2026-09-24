# Perubahan & Penyelarasan Modul ERS V2

## Ringkasan Penyelarasan
1. **Penyelarasan Alur Status Retur & Logistik Karantina (`home-mobile.html`)**:
   - **Status 1 (Mulai / Siap Dikirim)**: Menampilkan tombol *Lihat Detail* (outline) dan *Keberangkatan* (solid blue). Menekan *Keberangkatan* membuka modal input waktu pengiriman dimulai & data armada, lalu mengubah status menjadi *Sedang Dikirim*.
   - **Status 2 (Sedang Dikirim)**: Menampilkan tombol *Lihat Detail* (outline) dan *Kedatangan* (solid blue). Menekan *Kedatangan* membuka modal konfirmasi barang tiba di gudang transit/karantina dengan input waktu sampai, lalu mengubah status menjadi *Sedang Dikarantina*.
   - **Status 3 (Sedang Dikarantina)**: Menampilkan tombol *Lihat Detail* (full-width solid blue) menuju `karantina-action.html` untuk memproses verifikasi section & check sheet.
2. **Daftar Item Tower Karantina (`list-karantina.html`)**:
   - Menyelaraskan daftar batch tower template (*Template Tower A*, *Template Tower B*) dengan status *Sedang Dikirim*, *Siap Karantina*, *Sedang Karantina*, *Selesai*, dan *Rejected*.
   - Menyertakan data tanggal lengkap (*Selesai Bongkar*, *Est. Berangkat*, *Est. Tiba*, *Total Set*), filter drawer terpadu, dan wadah log error.
   - **Serah Terima BAST ditiadakan** sesuai instruksi.
3. **Lembar Kendali Batch Karantina (`karantina-action.html`)**:
   - Menampilkan spesifikasi batch tower, tanggal diterima di gudang transit, tab riwayat pembongkaran & pemasangan dari site, serta daftar section (*Column*, *Foundation*, *Guy Wire*).
   - Tombol *Check Section* membuka `check-sheet.html`.
4. **Pengisian Lembar Uji (`check-sheet.html`)**:
   - Input lengkap per grup aksesoris: Jumlah Normal, Jumlah Tidak Tersedia, Jumlah Rusak, Waktu Karantina, Keterangan Kendala, serta upload foto evidence cacat fisik.
   - Total stock live counter dan simpan hasil pengecekan.
5. **In-App Alert & Toast Feedback**:
   - Seluruh `alert()` browser digantikan oleh **In-App Toast Notification Banner** (animasi slide-down, status icon, dark theme floating badge, auto-wrap text) dan **Interactive Feedback Modals** (konfirmasi pengiriman, kedatangan, penyimpanan check sheet, penerbitan Berita Acara Karantina).
6. **Wadah Log Error & Exception Backend (BE) / Mobile Hit**:
   - Khusus menyimpan jejak error teknis saat hit API ke backend atau runtime mobile (misal: `500 Server Error - Deadlock Detected`, `422 Payload Mismatch`, `408 Request Timeout`, `502 Bad Gateway`).
   - Card yang **memiliki error hit BE/mobile** akan menampilkan badge & kotak error merah untuk bahan trace dan debugging. Card yang **bersih (0 error)** otomatis disembunyikan.
   - Mengklik kotak error membuka **Bottom Sheet Drawer (`#errorDetailDrawer`)** dengan jejak monospace trace error, endpoint API, status code, tombol `Salin Text` ke clipboard, serta form simulasi pencatatan error baru.
7. **Actionable Cards Interaction**:
   - Seluruh area card kini dapat diklik langsung (`cursor: pointer`, micro-interaction active scale).
   - Mengklik card pada status *Mulai / Dikirim* otomatis membuka **Modal Detail Permit**, sedangkan pada status *Sedang Dikarantina* langsung membuka halaman verifikasi `karantina-action.html`.
   - Sub-aksi di dalam card (*Keberangkatan*, *Kedatangan*, *Wadah Error*) menggunakan `stopPropagation` sehingga tidak terjadi konflik klik ganda.
8. **Pembersihan Navbar**:
   - Bottom navbar ditiadakan di seluruh ERS V2.
9. **Validasi Tag**:
   - Pengecekan 111 file HTML dengan `node script/check_tags.js` menghasilkan 0 error/mismatch.

## Modul yang Disesuaikan (ERS V2)
- [home-mobile.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/home-mobile.html)
- [Pemasangan/home-mobile.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Pemasangan/home-mobile.html)
- [Pemasangan/list-pemasangan.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Pemasangan/list-pemasangan.html)
- [Pemasangan/pemasangan-action.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Pemasangan/pemasangan-action.html)
- [Pembongkaran/home-mobile.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Pembongkaran/home-mobile.html)
- [Pembongkaran/list-pembongkaran.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Pembongkaran/list-pembongkaran.html)
- [Pembongkaran/pembongkaran-action.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Pembongkaran/pembongkaran-action.html)
- [Karantina & Pengembalian/home-mobile.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Karantina%20&%20Pengembalian/home-mobile.html)
- [Karantina & Pengembalian/list-karantina.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Karantina%20&%20Pengembalian/list-karantina.html)
- [Karantina & Pengembalian/karantina-action.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Karantina%20&%20Pengembalian/karantina-action.html)
- [Karantina & Pengembalian/check-sheet.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Karantina%20&%20Pengembalian/check-sheet.html)
- [Stock Opname/home-mobile.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Stock%20Opname/home-mobile.html)
- [Stock Opname/stock-opname-action.html](file:///c:/KERJAAN/Project/hifi-transmisi/hifi-mobile/ers-v2/Stock%20Opname/stock-opname-action.html)
