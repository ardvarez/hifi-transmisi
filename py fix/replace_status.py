import sys

files = [
    r"c:\KERJAAN\Project\hifi-ers\hifi-ers\Mutasi\pengecekan-pengembalian-peminjam.html",
    r"c:\KERJAAN\Project\hifi-ers\hifi-ers\Mutasi\pengajuan-pengembalian-peminjaman.html"
]

target = '<td style="color:#D97706;font-weight:600">Menunggu Pengembalian</td>'
replacement = '<td><div class="chip chip-tunggu"><div class="chip-dot"></div>Menunggu Pengembalian</div></td>'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace(target, replacement)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Done replacing text")
