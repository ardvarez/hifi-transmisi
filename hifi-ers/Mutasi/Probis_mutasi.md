*Ini akan saya gunakan untuk acuan proses bisnisnya pada Mutasi atau Peminjaman Komponen ataupun Set ERS. 
nb: 
[] = Flow Probis
() = Action User
~ = Stock Movement

1. [Antar UIT & UPT] Create data peminjaman bisa dengan jenis peminjaman satuan dan 1 Set. (Createornya adalah MSB Fashar Unit Peminjam) 
~Belum ada stock Movement

2. [Antar UIT & UPT] (Approve or Reject) Approval oleh peminjam dilakukan oleh SRM Hartrans Peminjam, jika ditolak datanya akan kembali ke Creator 
~Belum ada stock Movement

3. [Antar UIT & UPT] (Approve or Reject) Jika sudah disetujui data akan dibroadcast ke Unit Pengelola untuk melihat apakah tersedia atau bersedia meminjamkan komponen ataupun set ERS yang dimiliki. 
~Belum ada stock Movement [UIT] 
~Setelah approve SRM Hartrans Ada pengurangan stock Movement dari STOCK STANDBY ke IN TRANSIT [UPT] (-STOCK STANDBY & +IN TRANSIT)

4. [Antar UIT] (Approve or Reject) Approval selanjutnya akan dilakukan oleh MSB Fashar Pengelola, jika disetujui maka akan dikirim ke MSB Pengelola untuk penyiapan atau alokasi komponen sesuai jenis peminjamannya. Jika ditolak akan kembali ke Creator
~Setelah approve SRM Hartrans Ada pengurangan stock Movement dari STOCK STANDBY ke IN TRANSIT

5. [Antar UIT] (Approve or Reject) Setelah asset disiapkan dan disetujui akan dilakukan Approval oleh SRM Hartrans Pengelola untuk mengetahui peminjaman yang terjadi. Jika ditolak akan kembali ke MSB Fashar Pengelola untuk disesuaikan
~Jika direject ada roleback dari IN TRANSIT kembali ke STOCK STANDBY (-IN TRANSIT & +STOCK STANDBY)

6. [Antar UIT & UPT] (Approve or Reject) Setelah disetujui akan masuk ke Approval Manager UPT untuk mengetahui 
~Jika direject ada roleback dari IN TRANSIT kembali ke STOCK STANDBY (-IN TRANSIT & +STOCK STANDBY)

7. [Antar UIT & UPT] (Approve or Reject) menugaskan Asman Logistik untuk menyiapkan dan mengirimkan Komponen yang akan dipinjamkan. Jika ditolak akan kembali ke Approval MSB Fashar untuk pengecekan kembali.
~Jika direject ada roleback dari IN TRANSIT kembali ke STOCK STANDBY (-IN TRANSIT & +STOCK STANDBY)
~Jika dikirim tidak ada stock movement

8. [Antar UIT & UPT] (Approve or Reject) Lalu jika sudah disetujui akan masuk ke Pengecekan Asman Kons Pengelola untuk dicek dan dikirim ke peminjam.
~Jika direject ada roleback dari IN TRANSIT kembali ke STOCK STANDBY (-IN TRANSIT & +STOCK STANDBY)

9. [Antar UIT & UPT] (Approve or Reject) Lalu jika sudah dikirim akan masuk ke Pengecekan Asman Kons Peminjam untuk konfirmasi penerimaan barang dan dilakukan pengecekan barang.
~Jika direject ada roleback dari IN TRANSIT kembali ke STOCK STANDBY  (-IN TRANSIT & +STOCK STANDBY)
~Jika diterima akan ada stock movement dari IN TRANSIT UPT Pengelola ke IN TRANSIT Gudang Transit UPT Peminjam lalu masuk ke Stock Stand by Pinjam
(-IN TRANSIT UPT Pengelola & +IN TRANSIT UPT Peminjam)
(-IN TRANSIT Gudang Transit & +STANDBY PINJAM Gudang Transit)

10. [Antar UIT & UPT] Setelah semuanya selesai data akan masuk ke Pengajuan Pengembalian Pengelola. User pengaju adalah Asman PDKB Peminjam, 
~Setelah Disubmit ada stock movement dari Stock Standby Pinjam ke In Transit (-Standby Pinjam & +In Transit)

11. [Antar UIT & UPT] (Approve or Reject) Lalu disetujui oleh Manager UPT Peminjam.
~Jika direject ada roleback dari IN TRANSIT kembali ke STOCK STANDBY PINJAM (-In Transit & +Stock Standby Pinjam)
~Jika diapprove tidak ada stock movement

12. [Antar UIT & UPT] (Approve or Reject) Setelah itu dilakukan pengecekan oleh Asman Kons Peminjam untuk proses pengiriman dan penyiapan Komponen.
~Jika direject ada roleback dari IN TRANSIT kembali ke STOCK STANDBY PINJAM (-In Transit & +Stock Standby Pinjam)
~Jika dikirim tidak ada stock movement

13. [Antar UIT & UPT] Lalu jika sudah dikirim, data akan masuk ke Asman Kons Pengelola untuk diterima dan dilakukan pengecekan berupa karantina terhadap kondisi komponen yang masuk.
~Jika diterima ada stock movement dari IN TRANSIT Gudang Transit Peminjam ke IN TRANSIT UPT Pengelola lalu masuk ke Stock Stand by jika tidak terjadi kendala. (-In Transit Gudang Transit Peminjam & +In Transit UPT Pengelola)
~Jika diterima ada stock movement dari IN TRANSIT Gudang Transit Peminjam ke IN TRANSIT UPT Pengelola lalu masuk ke Stock Stand by jika terjadi kendala. (-In Transit Gudang Transit Peminjam & +In Transit UPT Pengelola, namun untuk Komponen yang terkendala (Ada defisit atau selisih) akan tetap di In Transit)


*Actor Antar UIT
1. Unit Induk - MSB FASHAR Peminjam
2. Unit Induk - SRM HARTRANS Peminjam
3. System
4. Unit Pengelola - MSB Fashar Pengelola
5. Unit Pengelola - SRM HARTRANS Pengelola
6. Unit Pengelola - Manager UPT Pengelola
7. Unit Pengelola - Asman Logistik Pengelola
8. Unit Pengelola - Asman Kons Pengelola
9. Unit Pengelola - Asman Kons Peminjam
10. Unit Pengelola - Asman PDKB Peminjam
11. Unit Pengelola - Manager UPT Peminjam
12. Unit Pengelola - Asman Kons Peminjam
13. Unit Pengelola - Asman Kons Pengelola

*Actor Antar UPT
1. Unit Induk - MSB FASHAR Peminjam
2. Unit Induk - SRM HARTRANS Peminjam
3. System
4. Unit Pengelola - Manager UPT Pengelola
5. Unit Pengelola - Asman Logistik Pengelola
6. Unit Pengelola - Asman Kons Pengelola
7. Unit Pengelola - Asman Kons Peminjam
8. Unit Pengelola - Asman PDKB Peminjam
9. Unit Pengelola - Manager UPT Peminjam
10. Unit Pengelola - Asman Kons Peminjam
11. Unit Pengelola - Asman Kons Pengelola