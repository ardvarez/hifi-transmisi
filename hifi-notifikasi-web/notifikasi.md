# Dokumentasi & Standar Konten Notifikasi Terpadu (Web & Mobile Transmisi)

Dokumen ini adalah spesifikasi arsitektur data, format konten (Title & Body), dan panduan integrasi sistem notifikasi terpadu untuk ekosistem aplikasi Web dan Mobile (HiFi ERS / Power Swift, HiFi New PST, Power Inspect, Mantaps, dan FFE).

---

## 1. Mekanisme Integrasi Kontekstual (Web & Mobile)

Sistem notifikasi dirancang sebagai **Single Shared Notification System** yang mendukung navigasi global maupun pemanggilan kontekstual dari dalam modul tertentu:

1. **Akses Global (Semua Modul)**
   - Parameter: `?module=all` (Default).
   - Judul Header: *"Pusat Notifikasi Transmisi"*.
   - Filter Tab Modul: Terpilih `Semua`.

2. **Akses Kontekstual per Modul (Deep Linking)**
   - Parameter URL / Query:
     - `?module=new_pst` &rarr; Header: *"Notifikasi NEW PST"* (*Master Data, Persetujuan & Mutasi Aset*).
     - `?module=power_inspect` &rarr; Header: *"Notifikasi Power Inspect"* (*Inspeksi, Work Order & Anomali Aset*).
     - `?module=ers` &rarr; Header: *"Notifikasi Power Swift (ERS)"* (*Permit Pemasangan, Karantina & Stock Opname*).
     - `?module=ffe` &rarr; Header: *"Notifikasi FFE"* (*Peralatan Proteksi & Pemadam Kebakaran*).
     - `?module=mantaps` &rarr; Header: *"Notifikasi Mantaps"* (*Parameter & Monitoring Operasional*).
   - **Auto-Filter**: Tab modul otomatis terkunci/terpilih ke modul pemanggil. Pengguna tetap bisa berpindah filter tab kapan saja.

---

## 2. Format Konten Notifikasi (Cukup Title & Body)

Setiap notifikasi diformat ringkas dan lugas, hanya terdiri dari **Title (Judul)** dan **Body (Pesan Deskripsi)**:

### A. NEW PST (Master Data, Persetujuan & Mutasi Aset)

| Jenis Notifikasi | Tipe / Priority | Title (Judul) | Body (Pesan Deskripsi) | Action CTA |
| :--- | :--- | :--- | :--- | :--- |
| **Penambahan Aset Baru** | `INFO` | **Penambahan Aset Baru Selesai Diproses** | Aset PMT 150kV ABB Bay Trafo 1 GI Cawang telah berhasil didaftarkan dalam Master Asset Register Level 5. | *Lihat Aset &rarr;* |
| **Persetujuan Penambahan Aset** | `APPROVAL` | **Permintaan Persetujuan Penambahan Aset #REQ-ADD-2026-089** | Registrasi aset baru Bay Trafo 2 GI Gandul telah diajukan oleh Spv. Pemeliharaan dan menunggu persetujuan otorisasi. | *Review & Setujui* |
| **Persetujuan Perubahan Aset** | `APPROVAL` | **Permintaan Persetujuan Perubahan Data #REV-2026-112** | Pembaruan kapasitas & rating arus Trafo GI Bandung Selatan menunggu persetujuan verifikator. | *Review Perubahan* |
| **Persetujuan Mutasi Aset** | `APPROVAL` | **Permintaan Persetujuan Mutasi Aset #MUT-PST-9021** | Permohonan mutasi Trafo 150/20kV 60MVA dari UPT Cawang ke UPT Bandung membutuhkan otorisasi Manager. | *Otorisasi Mutasi* |

---

### B. Power Inspect (Inspeksi, Work Order & Anomali Aset)

#### Standar Format Prefix Nomor WO & Tindak Lanjut:
- **WO Rutin**: `INS` + `YYYY` + `xxxxxxxx` (8 digit sequence) &rarr; Contoh: `INS202601875357`
- **WO Kondisional**: `CDT` + `YYYY` + `xxxxxxxx` &rarr; Contoh: `CDT202601875357`
- **WO Inspeksi Tindak Lanjut**: `TLI` + `YYYY` + `xxxxxxxx` &rarr; Contoh: `TLI202601875357`
- **Nomor Tindak Lanjut**: `TL` + `YYYY` + `xxxxxxxx` &rarr; Contoh: `TL202601875357`

| No | Tipe Notifikasi | Priority | Title Template | Message / Body Template | Contoh Nyata |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Inspeksi Ulang WO + Jumlah Aset** | `WARNING` | `Inspeksi Ulang {{nomor_wo}}` | `Yth. Petugas, WO {{nomor_wo}} dengan {{jumlah_aset}} aset memerlukan inspeksi ulang oleh {{user_verifikator}}. Mohon segera lakukan verifikasi dan tindak lanjut melalui aplikasi mobile. Terima kasih.` | **Title**: `Inspeksi Ulang INS202601875357`<br>**Message**: `Yth. Petugas, WO INS202601875357 dengan 5 aset memerlukan inspeksi ulang oleh Spv. Pemeliharaan (Budi Santoso). Mohon segera lakukan verifikasi dan tindak lanjut melalui aplikasi mobile. Terima kasih.` |
| 2 | **WO Baru dari Tindak Lanjut** | `WARNING` | `Penugasan WO Baru: {{nomor_wo}} (Tindak Lanjut)` | `Yth. Petugas, WO tindak lanjut {{nomor_wo}} telah diterbitkan berdasarkan temuan pada WO {{nomor_wo_referensi}}. Silakan cek rincian pekerjaan dan jadwalkan penanganan pada aplikasi mobile. Terima kasih.` | **Title**: `Penugasan WO Baru: TLI202601875357 (Tindak Lanjut)`<br>**Message**: `Yth. Petugas, WO tindak lanjut TLI202601875357 telah diterbitkan berdasarkan temuan pada WO TL202601875312. Silakan cek rincian pekerjaan dan jadwalkan penanganan pada aplikasi mobile. Terima kasih.` |
| 3 | **WO Baru dari Perencanaan Jadwal** | `INFO` | `Penugasan WO Terjadwal: {{nomor_wo}}` | `Yth. Petugas, WO rutin {{nomor_wo}} untuk periode {{periode_jadwal}} di lokasi {{lokasi_aset}} telah ditugaskan kepada Anda. Mohon laksanakan inspeksi sesuai jadwal yang ditentukan. Terima kasih.` | **Title**: `Penugasan WO Terjadwal: INS202601875389`<br>**Message**: `Yth. Petugas, WO rutin INS202601875389 untuk periode Triwulan IV 2026 di lokasi Bay Trafo GI Ungaran telah ditugaskan kepada Anda. Mohon laksanakan inspeksi sesuai jadwal yang ditentukan. Terima kasih.` |
| 4 | **WO Baru Kondisional** | `CRITICAL` | `Penugasan WO Kondisional: {{nomor_wo}}` | `Yth. Petugas, WO kondisional {{nomor_wo}} diterbitkan atas trigger {{kondisi_pemicu}} pada aset {{nama_aset}}. Mohon segera lakukan pengecekan kondisi lapangan melalui aplikasi mobile. Terima kasih.` | **Title**: `Penugasan WO Kondisional: CDT202601875357`<br>**Message**: `Yth. Petugas, WO kondisional CDT202601875357 diterbitkan atas trigger Sambaran Petir & Anomali Suhu pada aset Tower #120 SUTET 500kV Ungaran-Mandirancan. Mohon segera lakukan pengecekan kondisi lapangan melalui aplikasi mobile. Terima kasih.` |
| 5 | **Aset Anomali dari Inspeksi Terbaru** | `CRITICAL` | `Peringatan Aset Anomali: {{nomor_wo}} {{techidentno}}` | `Perhatian: Ditemukan {{jumlah_anomali}} aset berstatus anomali pada WO {{nomor_wo}} di lokasi {{lokasi_aset}}. Segera tinjau hasil inspeksi untuk mitigasi risiko lebih lanjut. Terima kasih.` | **Title**: `Peringatan Aset Anomali: INS202601875390 T1-CT-GI-BDS-01`<br>**Message**: `Perhatian: Ditemukan 1 aset berstatus anomali pada WO INS202601875390 di lokasi Bay Trafo 1 GI Bandung Selatan. Segera tinjau hasil inspeksi untuk mitigasi risiko lebih lanjut. Terima kasih.` |

---

### C. Power Swift - ERS (Emergency Restoration System & Logistik)

| Jenis Notifikasi | Tipe / Priority | Title (Judul) | Body (Pesan Deskripsi) | Action CTA |
| :--- | :--- | :--- | :--- | :--- |
| **Permit Baru Pemasangan** | `APPROVAL` | **Permit Baru Pemasangan Tower ERS #PMT-INS-2026-01** | Pengajuan permit pemasangan tower darurat ERS di SUTET 500kV Ungaran-Mandirancan butuh persetujuan Manager UPT. | *Review & Setujui* |
| **Permit Baru Pembongkaran** | `APPROVAL` | **Permit Baru Pembongkaran ERS #PMT-DIS-2026-19** | Pekerjaan perbaikan darurat selesai, pengajuan pembongkaran Tower ERS di GI Ungaran siap diverifikasi. | *Setujui Pembongkaran* |
| **Pengembalian & Karantina** | `WARNING` | **Peralatan Masuk Karantina ERS #RET-ERS-880** | Pengembalian material tower ERS darurat memiliki 3 unit komponen abnormal (Guy Wire & Insulator) dan perlu karantina teknis. | *Verifikasi Karantina* |
| **Stock Opname Baru** | `INFO` | **Jadwal Stock Opname ERS #SO-ERS-2026-Q3** | Penghitungan fisik inventaris Basecamp Gudang Transmisi Cawang periode Triwulan III telah dibuka. | *Buka Stock Opname* |
| **Stock Opname Ulang** | `WARNING` | **Stock Opname Ulang Basecamp Cawang #SO-ERS-Q3-REV** | Verifikasi selisih stock opname material Guy Grip Dead End (-2 Unit) memerlukan pencocokan fisik ulang. | *Verifikasi Ulang* |

---

### D. FFE & Mantaps

| Modul | Tipe / Priority | Title (Judul) | Body (Pesan Deskripsi) | Action CTA |
| :--- | :--- | :--- | :--- | :--- |
| **FFE** | `SUCCESS` | **Inspeksi Berkala FFE Hydrant & APAR** | Pengecekan 12 unit APAR & 2 Hydrant UPT Bandung telah selesai dengan status 100% laik operasi. | *Buka Laporan* |
| **Mantaps** | `INFO` | **Arsip Otomatis Log Parameter Mantaps** | Sinkronisasi 14.280 baris data parameter operasi dan telemetri transmisi bulanan telah berhasil diarsipkan di cloud. | *Arsip Log* |

---

## 3. Struktur Data Schema JSON Ringkas

```json
{
  "id": "NTF-2026-0491",
  "title": "Inspeksi Ulang WO #WO-PI-2026-882",
  "body": "Terdeteksi 5 aset peralatan di jalur SUTT 150kV Cawang - Bekasi memerlukan inspeksi ulang hasil evaluasi QC Base AHI.",
  "module": "POWER_INSPECT",
  "module_label": "Power Inspect",
  "category": "INSPECTION",
  "priority": "WARNING",
  "is_read": false,
  "created_at": "2026-09-29T10:45:00+07:00",
  "time_relative": "15 menit lalu",
  "action_url": "../hifi-power-inspect/validasi-inspeksi/validasi-inspeksi-mainpage.html",
  "action_label": "Proses Inspeksi Ulang"
}
```

---

## 4. Standar UI/UX & Design Tokens PLN (Corporate Theme)

### A. Design Tokens & Color Palette

| Token Variabel | Nilai Warna Hex | Penggunaan |
| :--- | :--- | :--- |
| `--pln-blue` | `#0A58CA` | Warna utama, tombol primer, header aktif, badge tab |
| `--pln-blue-dark` | `#003B8E` | Background sidebar web, hover button primer, logo contrast |
| `--pln-blue-light` | `#E7F1FF` | Background kartu unread, hover item, soft chip |
| `--pln-yellow` | `#F7A800` | Aksen logo PLN, badge log/peringatan, active icon state |
| `--pln-yellow-light` | `#FEF3C7` | Background pill warning & approval |
| `--danger` | `#DC2626` | Notifikasi kritis, anomali AHI, badge dot unread |
| `--danger-light` | `#FEE2E2` | Soft background pill kritis & urgent |
| `--success` | `#16A34A` | Notifikasi status sukses, verifikasi selesai |
| `--success-light` | `#DCFCE7` | Soft background pill sukses |
| `--card` | `#FFFFFF` | Background kartu notifikasi & modal |
| `--surface` | `#F1F5F9` / `#F8FAFC` | Background halaman & container filter |
| `--border` | `#E2E8F0` | Borderline kartu, pembatas tabel & form |

### B. Standar Tipografi & Input UI
- **Tipografi**: Heading menggunakan **Outfit** (font-weight 600–800), Body/Text menggunakan **Inter** (font-weight 400–600).
- **Segmented Button (<= 3 opsi)**: Tombol pill horizontal tanpa icon (contoh: *Semua*, *Belum Dibaca*, *Sudah Dibaca*).
- **Dropdown Combobox (> 3 opsi)**: Standar select styling PLN (contoh: Filter Modul, Filter Urgensi, Filter Kategori).
- **Sidebar Web**: Lebar 60px warna Dark Navy (`#003B8E`) dengan Logo PLN Kuning Emas (`#F7A800`) dan navigasi vertikal.

---

## 5. Pemetaan Aset Visual Proyek

- **Logo PLN Corporate**: `assets/logo-pln.svg`
- **Power Swift / ERS**: `assets/logo-transmission-one.svg`
- **New PST**: `assets/logo-new-pst.svg` / `assets/FA_New_PST_Logo.svg`
- **Power Inspect**: `assets/logo-power-inspect.svg`
- **FFE (Fire Fighting)**: `assets/logo-ffe.svg`
- **Mantaps**: `assets/logo-mantaps.svg`
- **Dashboard Global**: `assets/logo-dashboard.svg`

---

## 6. Panduan Integrasi Sidebar & Topbar Web Modul

Untuk menghubungkan tombol notifikasi pada sidebar atau topbar setiap modul web ke Pusat Notifikasi:

1. **HiFi ERS / Power Swift**:
   ```html
   <a href="../../hifi-notifikasi-web/notifikasi-center.html?module=ers" class="nav-icon" title="Notifikasi ERS">
       <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
       <span style="position:absolute; top:4px; right:4px; width:8px; height:8px; background:#ef4444; border-radius:50%; border:1.5px solid var(--pln-blue);"></span>
   </a>
   ```

2. **HiFi New PST**:
   ```html
   <a href="../../hifi-notifikasi-web/notifikasi-center.html?module=new_pst" class="nav-item" title="Notifikasi NEW PST">
       <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
       <span style="position:absolute; top:4px; right:4px; width:8px; height:8px; background:#ef4444; border-radius:50%; border:1.5px solid rgba(10,30,60,0.95);"></span>
   </a>
   ```

3. **HiFi Power Inspect**:
   ```html
   <a href="../../hifi-notifikasi-web/notifikasi-center.html?module=power_inspect" class="menu-item" title="Notifikasi Power Inspect">
       <i class="ri-notification-3-line"></i>
       <span style="position:absolute; top:8px; right:8px; width:7px; height:7px; background:#ef4444; border-radius:50%;"></span>
   </a>
   ```

4. **HiFi Portal Home (`home.html`)**:
   - Menu Sidebar: `HiFi Notifikasi Web` &rarr; Submenu kontekstual (Semua, New PST, Power Inspect, ERS).
   - Topbar Action: Tombol Lonceng Notifikasi langsung me-load `notifikasi-center.html` di dalam `contentFrame`.
