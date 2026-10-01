# Spesifikasi Konsep Gamifikasi Power Inspect
**Lightweight Achievement, EXP Leveling & Grade System untuk Mobile & Web**

---

## 1. Pendahuluan & Filosofi Desain

Sistem gamifikasi pada aplikasi **Power Inspect** dirancang khusus untuk lingkungan operasional ketenagalistrikan (gardu induk, switchyard, transmisi) dengan prinsip dasar:
1. **Utilitarian & Kinerja Tinggi:** Menghindari beban rendering berlebih pada smartphone teknisi yang bekerja di lapangan di bawah terik matahari.
2. **Kualitas & Disiplin Riil:** Metrik EXP, level, grade, dan lencana (*badge*) berfokus pada akurasi data inspeksi, ketepatan waktu, dan deteksi anomali, bukan sekadar kecepatan mengisi form secara asal.
3. **Zero-Lag Policy:** Arsitektur meminimalkan konsumsi kuota data seluler dan baterai perangkat lapangan.
4. **Pemisahan Mode Operasional & Simulasi:** Memisahkan UI fitur utama operasional harian dengan modul simulasi/demo interaktif untuk QA, verifikasi logika, dan stakeholder showcase.

---

## 2. Sistem EXP, Leveling & Grade Kualifikasi

### 2.1 Matriks Grade & Tingkatan Level

Pengalaman teknisi diukur melalui akumulasi **Inspection EXP (iEXP)** yang mengkualifikasikan pengguna ke dalam **Grade** profesional dan tingkatan level:

| Grade | Rentang Level | Syarat Total iEXP | Gelar Kompetensi | Hak Akses & Privilese |
| :--- | :--- | :--- | :--- | :--- |
| **Grade E (Novice)** | Lv. 1 – 5 | 0 – 1.499 iEXP | *Junior Inspector Trainee* | Akses inspeksi rutin standar dengan supervisi. |
| **Grade D (Apprentice)** | Lv. 6 – 15 | 1.500 – 4.999 iEXP | *Certified Field Inspector* | Inspeksi mandiri gardu level tegangan 70/150 kV. |
| **Grade C (Specialist)** | Lv. 16 – 30 | 5.000 – 11.999 iEXP | *Senior Substation Inspector* | Validasi awal anomali kritis & rilis rekomendasi awal. |
| **Grade B (Expert)** | Lv. 31 – 50 | 12.000 – 24.999 iEXP | *Lead Diagnostic Specialist* | Inspeksi EHV 500 kV, investigasi anomali sistemik. |
| **Grade A (Master)** | Lv. 51+ | $\ge 25.000\text{ iEXP}$ | *Master Grid Assessor* | Peer-reviewer data inspeksi, mentor inspektur baru, badge eksklusif. |

### 2.2 Formula Perhitungan Level
Level dihitung secara deterministik di backend berdasarkan formula:
$$\text{Level} = \left\lfloor 1 + \sqrt{\frac{\text{iEXP}}{100}} \right\rfloor$$
Setiap kenaikan level memberikan bonus indikator visual, badge milestone, dan poin kontribusi regu/unit.

### 2.3 Aturan Perolehan EXP (Reward Actions)

| Kategori Aktivitas | Aksi Lapangan | Perolehan iEXP | Keterangan & Validasi |
| :--- | :--- | :--- | :--- |
| **Inspeksi Rutin** | Submit 1 Form Bay Komplit | +50 iEXP | Data lolos validasi isian lengkap & geotag valid |
| **Ketepatan Waktu** | Inspeksi Dini Hari (04.00 – 06.00) | +25 iEXP (Bonus) | Timestamp sinkron dengan GPS & server |
| | Inspeksi Beban Puncak (18.00 – 21.00) | +20 iEXP (Bonus) | Pengecekan termovisi/beban transmisi |
| **Awareness Anomali** | Temuan Anomali Mayor (Tervalidasi) | +100 iEXP | Disetujui supervisor/asman pemeliharaan |
| | Temuan Anomali Kritis (Emergency) | +200 iEXP | Disertai foto evidence tajam & deskripsi presisi |
| **Kualitas Data** | 100% Foto & Geotag Akurat | +15 iEXP (Bonus) | Tanpa reject / revisi oleh reviewer |
| **Misi / Quest** | Daily Inspection Streak (3 hari berturut-turut) | +75 iEXP | Konsistensi patroli harian |
| | Weekly Mission Clear (Selesai 1 Substation Bay) | +250 iEXP | Menyelesaikan seluruh aset dalam 1 gardu |

---

## 3. Matriks 4 Pilar Kategori Achievement (Badges)

| Pilar | Fokus Performa | Contoh Badge | Tier | Target & Kriteria |
| :--- | :--- | :--- | :--- | :--- |
| **Completeness** | Ragam jenis peralatan yang diinspeksi | **Prajurit All-Rounder** | Gold | Menginspeksi seluruh 8 grup aset utama gardu |
| | Kelengkapan unit dalam 1 bay | **Kolektor Bay** | Bronze/Silver/Gold | Selesai 5 / 25 / 50 Bay komplit |
| **Timeliness** | Disiplin jadwal dini hari | **Pejuang Subuh** | Silver | 10x inspeksi di jam 04.00 – 06.00 pagi |
| | Penuntasan administrasi harian | **Kejar Tayang** | Bronze/Silver/Gold | Submit di jam 21.00 – 23.59 (10x / 30x / 60x) |
| | Pengawasan jam beban puncak | **Patroli Beban Puncak** | Silver | 15x inspeksi di jam 18.00 – 21.00 |
| **Awareness** | Kejelian menemukan anomali lapangan | **Detektif Inspektur** | Gold/Platinum | Menemukan 50 / 100 anomali aset tervalidasi |
| | Kualitas evidence tanpa cacat | **Mata Elang** | Gold | 30 inspeksi beruntun dengan foto & geotag valid |
| **Readyness** | Adopsi aset baru & commissioning | **Prajurit Energizer** | Gold | 200 aset baru / selesai energize |
| | Kesiapan siaga tanggap darurat | **Kilat Respons** | Platinum | Inspeksi darurat dimulai $\le 30$ menit sejak tiket rilis |

---

## 4. Arsitektur Teknis & Model Data API

### 4.1 Zero-Lag Server Computing
Seluruh perhitungan penambahan EXP, kalkulasi kenaikan level/grade, serta pemenuhan target lencana dieksekusi di backend server saat form disubmit atau disetujui. Mobile client hanya menerima respons JSON ringkas ($\le 2\text{ KB}$).

### 4.2 Skema JSON Response (`/api/v1/inspector/gamification-profile`)
```json
{
  "user_id": "TECH-8821",
  "name": "Budi Santoso",
  "unit": "ULTG Surabaya Barat",
  "level": 18,
  "grade": {
    "code": "C",
    "name": "Specialist",
    "title": "Senior Substation Inspector"
  },
  "exp": {
    "current_exp": 6240,
    "next_level_exp": 6400,
    "current_level_min_exp": 5776,
    "progress_percentage": 74.3
  },
  "stats": {
    "total_inspections": 142,
    "total_anomalies_reported": 28,
    "current_streak_days": 5,
    "total_badges_unlocked": 9
  },
  "active_quest": {
    "quest_id": "daily_peak_patrol",
    "title": "Patroli Beban Puncak",
    "progress": 2,
    "target": 3,
    "reward_exp": 75
  },
  "recent_badges": [
    {
      "badge_id": "pejuang_subuh",
      "title": "Pejuang Subuh",
      "tier": "silver",
      "is_unlocked": true,
      "unlocked_at": "2026-09-15T05:32:00Z"
    }
  ]
}
```

---

## 5. Konsep Antarmuka (UI/UX) Berdasarkan Platform

### 5.1 Platform Mobile (Android / iOS untuk Teknisi Lapangan)
* **Karakter Desain:** Kompak, outdoor-ready, kontras tinggi (WCAG AA), ukuran touch target $\ge 44 \times 44\text{ pt}$.
* **Header Profil & EXP Bar:** Baris ringkas di tab akun/profil menampilkan Avatar, Badge Grade (contoh: *Grade C - Specialist*), Level Badge, dan Progress Bar EXP menuju level berikutnya.
* **Mini Widget Beranda:** 1 baris widget non-intrusif di atas daftar tugas inspeksi: progress misi harian aktif & streak hari berturut-turut.
* **Tab Pencapaian (Badges Showcase):** Filter kategori (Completeness, Timeliness, Awareness, Readyness), grid badge 3 kondisi visual (Locked, In-Progress, Unlocked).
* **Toast Notification Non-Blocking:** Notifikasi kecil di bagian atas layar pasca submit: `"+75 iEXP & +1 Progress: Pejuang Subuh"`.

### 5.2 Platform Web (Dashboard Supervisor & Manajemen)
* **Leaderboard & Ranking Unit:** Peringkat perorangan (Top Inspectors), regu kerja, ULTG, dan UPT berdasarkan akumulasi iEXP dan skor kepatuhan inspeksi.
* **Skill Tagging & Filter Penugasan:** Ikon badge keahlian mini muncul di samping nama personil pada tabel dispatching tugas (contoh: memfilter teknisi bersertifikasi *Detektif Inspektur* untuk gardu bermasalah).
* **Matriks Kompetensi Regu:** Grafik radar ringkasan 4 pilar kemampuan tim dalam satu unit kerja.
* **Audit & Export KPI:** Data perolehan iEXP, anomali valid, dan kepatuhan jadwal dapat diekspor langsung ke spreadsheet format evaluasi kinerja bulanan.

---

## 6. Pemisahan Struktur HiFi (Mockup & Prototype)

Untuk menjaga kejelasan antara sistem yang berjalan dalam aplikasi dan alat bantu pengujian/demonstrasi, desain HiFi dipisahkan menjadi dua modul utama:

### Modul A: Fitur Utama Operasional (Core Gamification Feature)
Halaman dan komponen UI yang digunakan langsung oleh user dalam alur produksi sehari-hari:
1. **Mobile - Profile & Gamification Hub:**
   - Ringkasan Level, Grade Badge, dan progress bar EXP.
   - Papan Misi Aktif (Daily & Weekly Quest).
   - Katalog Badge 4 Pilar dengan status progres real-time.
   - Papan Peringkat Mini (Leaderboard Regu).
2. **Web - Management & Leaderboard Dashboard:**
   - Tabel Klasemen Inspektur & Unit Kerja (Filter: Mingguan, Bulanan, All-Time).
   - Detail Kartu Profil Pegawai beserta rekam jejak badge, log iEXP, dan verifikasi anomali.
   - Matriks Sebaran Kompetensi Regu (4 Pilar).

### Modul B: Simulasi & Interactive Playground (Simulation Mode)
Modul mandiri yang difungsikan untuk testing logika, QA testing, dan presentasi stakeholder tanpa memerlukan input data riil gardu:
1. **Interactive Trigger Simulator:**
   - Panel kontrol pemilihan skenario inspeksi (contoh: *Simulasi Submit Subuh*, *Simulasi Temuan Anomali Kritis*, *Simulasi Weekly Streak Clear*).
   - Tombol eksekusi trigger event (`Trigger Action`).
2. **Visual Reward Feedback & Animation Showcase:**
   - **EXP Float Counter:** Animasi penambahan iEXP melayang (`+100 iEXP`).
   - **Level Up Modal:** Pop-up selebrasi kenaikan level beserta unlock hak ases baru.
   - **Grade Promotion Banner:** Animasi transisi grade (contoh: Promosi dari *Grade D* ke *Grade C - Specialist*).
   - **Badge Unlock Dialog:** Dialog detail lencana yang baru diperoleh lengkap dengan info timestamp dan syarat kelulusan.
3. **Log Event Real-Time Console:**
   - Menampilkan payload request/response JSON simulasi secara transparan untuk verifikasi dev/QA.