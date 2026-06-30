## Note kebutuhan MANTAPS
- bikin menu baru Master OSL
- bikin master sistem inputnya:
	- Nama Sistem
	- UNIT INDUK P2B
	- Pembangkit terbesar (Parent 1, Pembangkit)
	- Kapasitas
	
- bikin master sub-sistem relasi dengan sistem berikut inputnya
    - Pilih Sistem
    - Pilih UP2B Base on data sistem (cek dari data unit hierarki dan tampilkan data UPTnya)
    - Input nama sub-sistem
	- Jenis Kriteria N-1 = TRAFO, PEMBANGKIT dan PENGHANTAR
	- Kriteria N-1 = 	- Kalo Trafo GI, Bay TRAFO
						- Kalo pembangkit 1 parent diatas, nama pembangkit
						- Kalo PENGHANTAR GI, Bay Line
	- Kapasitas N-1 = 
	
	- Jenis Kriteria N-1-1 = TRAFO, PEMBANGKIT dan PENGHANTAR
	- Kriteria N-1-1 = 	- Kalo Trafo GI, Bay TRAFO
						- Kalo pembangkit 1 parent diatas, nama pembangkit
						- Kalo PENGHANTAR GI, Bay Line
	- Kapasitas N-1-1 =
	
	- Jenis Kriteria N-2= TRAFO, PEMBANGKIT dan PENGHANTAR
	- Kriteria N-2 = 	- Kalo Trafo GI, Bay TRAFO
						- Kalo pembangkit 1 parent diatas, nama pembangkit
						- Kalo PENGHANTAR GI, Bay Line
	- Kapasitas N-2 =	
- Unit Level 4 ditambah combobox Sistem dan relasi ke Sub-sistem

## Mekanisme
- Pengaturannya dibuat tab supaya lebih mudah dalam proses pembuatannya 
- Menu baru untuk Sistem dan Sub sistem