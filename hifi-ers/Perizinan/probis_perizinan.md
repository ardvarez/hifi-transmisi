##---
nama: probis_perizinan
deskripsi: fitur aplikasi dalam ERS untuk melanjutkan proses perencanaan pemasangan ERS.
---

## Klasifikasi (Tipe Permit/Perizinan)
- Secara detail fitur dapat melakukan pengajuan perizinan dalam proses operasi Tower ERS
- Klasifikasinya ada Pemasangan, Pembongkaran dan Pengembalian & Karantina
- Dapat dilakukan dengan dasar nomor Perencanaan yang sudah selesai atau sudah terpenuhi kebutuhannya
- Klasifikasi akan menjadi input dan akan menentukan field isian dibawahnya

## Alur permit pemasangan
- Permit pemasangan dapat diajukan oleh ASMAN RENEV dari Unit Pelaksana (UPT)
- User perlu menentukan nomor perencanaan yang sudah siap untuk dipasang (dampaknya lalu menampilkan detail data pada tablenya. isi tablenya ada kolom )
- Lalu tergenerate nomor perizinan dengan insial (ASMYYYY) YYYY adalah tahun
- Lalu user perlu menentukan PIC Pemasangan berdasarkan user UPT yang tersedia
- Lalu melampirkan file lampiran berupa perizinan pemasangan 
- Setelah itu user akan menentukan Estimasi tanggal pemasangan dam tanggal selesai. Hal ini perlu diisi berdasarkan jumlah tower yang perlu dipasang
- Setelah itu tekan Action submit (Fix pelaksanaan) atau draft (Membuat draft rencana pemasangan)

## Alur permit pembongkaran
- Permit pembongkaran dapat diajukan oleh ASMAN RENEV dari Unit Pelaksana (UPT)
- User perlu menentukan nomor perencanaan yang sudah terpasang
- Lalu tergenerate nomor perizinan dengan insial (DISYYYY) YYYY adalah tahun
- Lalu user perlu menentukan PIC Pembongkaran berdasarkan user UPT yang tersedia
- Lalu melampirkan file lampiran berupa perizinan Pembongkaran 
- Terdapat Checkbox pengembalian, jika ingin sekaligus diajukan pengembaliannya
- Jika diceklis, perlu mengisi Gudang Tujuan (Ini isinya unit UPT sampai GI sesuai pembuatnya)
- Lalu mengisi PIC Pengecekan berdasarkan user UPT 
- Lalu mengisi estimasi tanggal keberangkatan dan tanggal estimasi tiba
- Setelah itu tekan Action submit (Fix pelaksanaan) atau draft (Membuat draft rencana pemasangan)
- Pada Table user dapat memilih tower yang akan dibongkar (dan dikembalikan jika diceklis pengembaliannya), setelah itu user perlu mengisi estimasi tanggal mulai dan selesai bongkar.
- Lalu ada aksi hapus jika ingin menghapus data
- Setelah itu tekan Action submit (Fix pelaksanaan) atau draft (Membuat draft rencana pembongkaran)

## Alur permit pengembalian
- Permit pengembalian dapat diajukan oleh ASMAN Logistik dari Unit Pelaksana (UPT)
- User perlu menentukan nomor perencanaan yang sudah terbongkar
- Lalu tergenerate nomor perizinan dengan insial (RTRYYYY) YYYY adalah tahun
- Lalu user perlu menentukan PIC Pengembalian berdasarkan user UPT yang tersedia
- Lalu melampirkan file lampiran berupa perizinan Pengembalian
- Lalu memilih Nomor Permit Bongkar
- Pilih tanggal estimasi berangkat
- Pilih tanggal estimasi tiba
- Pilih gudang tujuan sesuai UPT Terkait
- Lalu pilih PIC Pengecekan berdasarkan user UPT 
- Pada Table user dapat memilih tower yang akan dikembalikan
- Setelah itu tekan Action submit (Fix pelaksanaan) atau draft (Membuat draft rencana pemasangan)

## Notes
- Secara alur data akan mengalir dari pemasangan, pembongkaran lalu pengembalian
- tanggal digunakan sebagai acuan saja belum menjadi target penyelesaian atau action
- tanggal bisa backdate