# Original User Request

## Initial Request — 2026-06-11T16:28:34+07:00

# Teamwork Project Prompt — Draft

> Status: Launched
> Goal: Craft prompt → get user approval → delegate to teamwork_preview

Membangun Dashboard Asset Management untuk PLN (Sub-bidang Transmisi). Sistem mencatat siklus hidup aset mulai dari fase aset siap beroperasi (mengabaikan fase perencanaan). Aset yang baru dicatat langsung dianggap sebagai aset baru yang siap beroperasi dengan Serial ID / Nomor Teknis. Tim agen (PM, IT BA, UI/UX, FE) akan berkolaborasi mewujudkan dashboard ini.

Working directory: C:/KERJAAN/Project/hifi-ers/hifi-new-pst/dashboard
Integrity mode: development

## Requirements

### R1. Dashboard Frontend
Membangun frontend aplikasi web menggunakan framework Vue atau Nuxt.js. Harus memiliki antarmuka yang modern, responsif, dan mudah digunakan (fokus pada UI/UX yang premium sesuai praktik terbaik). 

### R2. Pencatatan Aset Baru (Siap Operasi)
Sistem harus memiliki form pencatatan aset transmisi baru. Pencatatan ini langsung menandai aset sebagai "siap beroperasi" dengan membutuhkan input mandatory seperti "Serial ID" atau "Nomor Teknis". Fase perencanaan diabaikan sepenuhnya dalam alur kerja ini.

### R3. Visualisasi Data Aset
Dashboard utama harus menampilkan daftar aset yang sudah tercatat dan beroperasi, serta ringkasan metrik (misal: jumlah aset aktif). Tim dibebaskan untuk menentukan struktur data mock (tiruan) yang sesuai.

### R4. Penanganan Valuasi Aset
Sistem harus mengakomodasi pencatatan valuasi aset. Karena informasi rinci atau anggaran dari masa perencanaan seringkali tidak ada, sistem harus menyediakan field fleksibel untuk memasukkan estimasi valuasi aset saat ini atau menandainya jika belum diketahui.

### R5. Indikator Kesehatan Aset (Asset Health)
Dashboard harus menampilkan metrik atau indikator "Kesehatan Aset" (misalnya dalam bentuk persentase, skor, atau status warna) untuk setiap aset. Indikator ini akan digunakan sebagai alat bantu analisis untuk merencanakan anggaran pengadaan aset baru di masa depan.

## Acceptance Criteria

### Verifikasi Frontend & Fungsionalitas
- [ ] Proyek Vue/Nuxt berhasil diinisialisasi dan dapat berjalan secara lokal (`npm run dev` tanpa error).
- [ ] Terdapat form input aset yang memvalidasi keberadaan Serial ID/Nomor Teknis dan menetapkan status awal aset sebagai "Siap Operasi".
- [ ] Tidak ada langkah, field, atau referensi UI yang menyinggung fase "Perencanaan" (Planning) aset.
- [ ] Terdapat field khusus pada form untuk mencatat "Estimasi Valuasi Aset" yang fleksibel.
- [ ] Indikator "Kesehatan Aset" (Asset Health) divisualisasikan dengan jelas pada tabel/daftar aset di dashboard.
- [ ] Aset yang ditambahkan lewat form dapat terlihat langsung pada daftar/tabel aset di halaman dashboard.
