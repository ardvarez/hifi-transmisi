---
trigger: always_on
---

# Panduan Lengkap PostgreSQL SQL (Khusus Read-Only Analyst)

Panduan ini dirancang khusus untuk peran **Data Analyst, BI Engineer, dan AI Assistant** yang menggunakan akses **Read-Only (Hanya Membaca Data)**. Seluruh perintah di bawah difokuskan pada pemuerian (*querying*), analisis data, serta optimasi pencarian tanpa melakukan perubahan pada struktur atau isi data.

---

## 1. Aturan Dasar & Keamanan Akses Read-Only

Sebagai pengguna Read-Only, Anda **hanya memiliki akses `SELECT`**. Sistem akan secara otomatis menolak operasi manipulasi atau perubahan data.

### Operasi yang DIISINKAN (Allowed)

- `SELECT` (Menampilkan data)
- `JOIN` (Menggabungkan tabel)
- `GROUP BY` & Aggregations (Mengelompokkan data)
- `WINDOW FUNCTIONS` (Analisis tren & pemeringkatan)
- `EXPLAIN` / `EXPLAIN ANALYZE` (Menganalisis kinerja query)

### Operasi yang DIBLOKIR (Forbidden)

- Data Modification: `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`
- Schema Alteration: `CREATE`, `ALTER`, `DROP`, `RENAME`
- Access Control: `GRANT`, `REVOKE`

---

## 2. Struktur Query Dasar (`SELECT`)

### Sintaks Utama

```sql
SELECT 
    kolom1,
    kolom2,
    COUNT(*) AS total
FROM 
    nama_tabel
WHERE 
    kondisi_filter = 'nilai'
GROUP BY 
    kolom1, kolom2
HAVING 
    COUNT(*) > 5
ORDER BY 
    total DESC
LIMIT 100 OFFSET 0;
```

### Filtering Data (`WHERE`)

```sql
SELECT product_name, price, category
FROM products
WHERE price BETWEEN 10000 AND 50000
  AND category IN ('Elektronik', 'Peralatan')
  AND status = 'active'
  AND product_name ILIKE '%laptop%'; -- ILIKE = Case-insensitive (khusus Postgres)
```

---

## 3. Penggabungan Data (`JOIN` & Set Operations)

### Menggabungkan Tabel (`INNER`, `LEFT`, `RIGHT`)

```sql
-- Mengambil data transaksi beserta nama pelanggan
SELECT 
    o.order_id,
    u.username,
    u.email,
    o.total_amount,
    o.created_at
FROM orders o
INNER JOIN users u ON o.user_id = u.user_id
WHERE o.created_at >= '2026-01-01';

-- Menampilkan semua produk termasuk yang belum pernah terjual
SELECT 
    p.product_id,
    p.product_name,
    COALESCE(SUM(oi.quantity), 0) AS total_terjual
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name;
```

### Operasi Himpunan (`UNION`, `INTERSECT`, `EXCEPT`)

```sql
-- Gabungan data pelanggan dari dua wilayah (tanpa duplikat)
SELECT email FROM customer_jabar
UNION
SELECT email FROM customer_jatim;

-- Mencari pelanggan yang ada di kedua daftar
SELECT email FROM leads_2025
INTERSECT
SELECT email FROM leads_2026;

-- Mencari pelanggan tahun 2025 yang tidak aktif di 2026
SELECT email FROM leads_2025
EXCEPT
SELECT email FROM leads_2026;
```

---

## 4. Agregasi & Analisis Data

### Fungsi Agregasi Standar

```sql
SELECT 
    category,
    COUNT(*) AS total_produk,
    AVG(price) AS rata_rata_harga,
    MIN(price) AS harga_terendah,
    MAX(price) AS harga_tertinggi,
    SUM(stock) AS total_stok
FROM products
GROUP BY category;
```

### Pengolahan Tanggal & Waktu (Time-Series)

```sql
-- Agregasi Penjualan Bulanan
SELECT 
    DATE_TRUNC('month', order_date) AS bulan,
    COUNT(order_id) AS total_transaksi,
    SUM(total_amount) AS total_pendapatan
FROM orders
WHERE order_date >= '2025-01-01'
GROUP BY 1
ORDER BY 1 ASC;
```

---

## 5. Advanced Analytics: Window Functions

*Window functions* memungkinkan analisis mendalam seperti pemeringkatan (*ranking*), running total, dan perhitungan persentase tanpa perlu melakukan `GROUP BY` secara eksplisit.

### Pemeringkatan (`ROW_NUMBER`, `RANK`, `DENSE_RANK`)

```sql
-- Mencari 3 transaksi terbesar untuk setiap pengguna
WITH RankedOrders AS (
    SELECT 
        user_id,
        order_id,
        total_amount,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY total_amount DESC) as rank_order
    FROM orders
)
SELECT * FROM RankedOrders WHERE rank_order <= 3;
```

### Running Total & Moving Average

```sql
SELECT 
    order_date,
    total_amount,
    SUM(total_amount) OVER (ORDER BY order_date) AS akumulasi_pendapatan,
    AVG(total_amount) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg_7_hari
FROM orders;
```

### Pembandingan Periode (`LAG` & `LEAD`)

```sql
-- Membandingkan penjualan bulan ini dengan bulan sebelumnya
SELECT 
    bulan,
    total_sales,
    LAG(total_sales, 1) OVER (ORDER BY bulan) AS sales_bulan_lalu,
    total_sales - LAG(total_sales, 1) OVER (ORDER BY bulan) AS pertumbuhan
FROM (
    SELECT DATE_TRUNC('month', order_date) AS bulan, SUM(total_amount) AS total_sales
    FROM orders
    GROUP BY 1
) subquery;
```

---

## 6. Eksplorasi Data JSONB (Semi-Structured Data)

PostgreSQL mendukung pencarian data terstruktur di dalam kolom bernilai JSON/JSONB.

```sql
-- Mengambil nilai key spesifik dari JSON
SELECT 
    user_id,
    metadata->>'device' AS device_type,
    metadata->'location'->>'city' AS city
FROM user_logs;

-- Filter berdasarkan properti di dalam JSON
SELECT user_id, metadata
FROM user_logs
WHERE metadata @> '{"role": "subscriber"}';

-- Memeriksa keberadaan key tertentu
SELECT count(*) 
FROM user_logs 
WHERE metadata ? 'checkout_time';
```

---

## 7. Inspeksi Skema & Optimasi Performance Query

### Memeriksa Struktur Tabel & Metadata

```sql
-- Melihat daftar tabel yang tersedia di skema public
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';

-- Melihat struktur kolom dari suatu tabel
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'orders';
```

### Menganalisis Kinerja Query (`EXPLAIN`)

Gunakan `EXPLAIN` atau `EXPLAIN ANALYZE` untuk mengecek apakah query menggunakan index atau mengalami kendala performa (*Seq Scan*).

```sql
EXPLAIN ANALYZE
SELECT u.username, COUNT(o.order_id)
FROM users u
JOIN orders o ON u.user_id = o.user_id
WHERE o.created_at >= '2026-01-01'
GROUP BY u.username;
```

---

## 8. Contoh Format System Instruction (Prompt AI Read-Only)

Jika file ini digunakan sebagai acuan untuk AI Assistant, sertakan aturan di bawah ini pada sistem Anda:

```text
SISTEM RULE:
1. Anda adalah AI Data Analyst dengan hak akses Read-Only.
2. Anda HANYA diperbolehkan merancang dan memberikan SQL bertipe `SELECT` atau `WITH` (CTE).
3. DILARANG KERAS menyarankan atau menghasilkan perintah DDL/DML seperti `INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALTER`, `TRUNCATE`, `CREATE`, `GRANT`.
4. Jika pengguna meminta untuk mengubah atau merusak data, jawab dengan:
   "Sistem ini dikonfigurasi dalam mode Read-Only. Saya hanya dapat membantu menampilkan dan menganalisis data."
