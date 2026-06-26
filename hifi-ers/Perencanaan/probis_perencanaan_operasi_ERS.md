*Ini akan saya gunakan untuk acuan proses bisnisnya menu Perencanaan Operasi ERS. 
nb: 
[] = Flow Probis
() = Action User

Ini probis yang digunakan untuk membuat perencanaan pembangunan Tower ERS

1. (Create Data) User akan membuat rencana pembangunan Tower ERS dengan memilih tower yang akan digantikan dengan Tower ERS, user juga akan mendesign kebutuhan tower yang beroperasi.
2. (Approve or Reject) Approval dilakukan oleh Manager UPT, jika ditolak maka data akan dikembalikan ke Creator untuk diperbaiki. Jika disetujui maka data akan dikirim ke MSB Pengelola untuk pengecekan kembali.
3. A (Submit, Disposisi or Reject) Pengajuan akan masuk ke MSB Fashar Unit Induk apakah menyetujui pembangunan Tower ERS atau tidak, jika ditolak maka data akan dikembalikan ke Creator untuk diperbaiki. Jika disetujui maka data akan dikirim ke MSB Pengelola untuk pengecekan kembali. Dan MSB Fashar akan memetakan detail dari perencanaannya, dengan mengalokasikan komponen yang akan digunakan. Selain itu juga akan menentukan jika perlu peminjaman komponen atau Set ERS.
3. B (Draft or Reject) Data yang sudah diarahkan Disposisi oleh MSB Fashar akan diterima oleh Staff Unit Induk untuk mengecek kelengkapan dan kebutuhan perencanaan tersebut. dan jika sudah sesuai dapat dikirimkan kembali ke MSB Fashar. Dan MSB Fashar bisa melakukan flow 3. A lagi
4. (Approve or Reject)Approval selanjutnya akan dilakukan oleh SRM Hartrans Unit Induk, jika ditolak maka data akan dikembalikan ke MSB Fashar untuk diperiksa. Dan jika disetujui maka akan dilihat terlebih dahulu apakah peminjaman komponen dilakukan antar Unit Induk atau Antar Unit Induk dan Unit Pengelola. Atau tidak dilakukan sama sekali. Jika perlu peminjaman maka akan masuk ke flow mutasi.
5. (Create Data) User ASMAN RenEv membuat perizinan pemasangan base on perencanaan yang sudah dibuat.
6. (Entry Data) User UPT akan menginput realisasi keberangkatan, tiba, mulai pemasangan dan selesai pemasangan dengan perangkat mobile. Setelah itu tower ERS tercatat operasi
7. (Create Data) User ASMAN RenEv membuat perizinan pembongkaran base on Perencanaan yang sudah siap dibongkar. ini juga bisa langsung diajukan untuk perizinan pengembalian.
8. (Entry Data) User UPT akan menginput realisasi mulai pembongkaran dan selesai pembongkaran dengan perangkat mobile. Setelah itu tower ERS tidak tercatat operasi dan Siap dilakukan pengembalian
9. (Create Data) User ASMAN Kons membuat pengajuan pengembalian base on Perizinan Pengembalian.
10. (Entry Data) User ASMAN PDKB akan menginput realisasi keberangkatan dan tibanya komponen digudang transit dengan perangkat mobile. Lalu setelah itu mengisi karantina hasil operasi dengan melihat kelengkapan dan kondisi komponen yang sudah datang.
11. (Verifikasi & Reject) ASMAN Kons akan memverifikasi hasil pengecekan dan kondisi komponen yang sudah datang. Jika sudah sesuai maka akan dilanjutkan ke proses pengembalian. 

