---
trigger: always_on
---

## Note for Hifi

- Pada saat hifi baru dibuat tolong setup juga menunya pada @home.html supaya mudah navigasinya
- Jangan lupa pastikan kepada user apakah ada hirarki unit atau tidak
- Tanyakan ke user apakah membutuhkan notes, jika ada tanyakan apa notesnya
- Tanyakan Validasi yang perlu diperhatikan
- Tanyakan user creatornya
- Buat 1 Tampilan yang seragam untuk semua Hifi
- Kalo mau cek tampilan jangan buka localhost langsung ke path file aja bukanya dari home.html
- Dom digunakan hanya ketika ada perintah saja, jangan terlalu inisiatif scanning page
- **Standard Input UI**:
  - **Radio Button (Single Select <= 3 opsi)**: Pakai konsep Button biasa tanpa icon (Segmented Pill / Toggle Button group text only).
  - **Combo Box Default (Single Select > 3 opsi)**: Pakai dropdown select / combobox standar.
  - **Checkbox (Multi Select)**: Pakai konsep dropdown combobox dengan opsi multi-check (Multi-Select Checklist Dropdown).
  - **Number**: Sesuaikan tipe data (Integer tanpa desimal atau Double/Float dengan desimal dan step).
  - **Text Input & Text Area**: Mengikuti styling input PLN yang seragam.
- Pastikan pengecekan tag sebelum trigger selesai ke user, biar ga ada bug ataupun error dari FE
