const fs = require('fs');
const path = require('path');
const { Client } = require('pg');

async function runCheck() {
    console.log(`[${new Date().toISOString()}] Starting query 'Pengecekan nilai AHI tidak sesuai'...`);
    const client = new Client({
        connectionString: "postgresql://sigatra_apps:uU31Zc%5E6iZs9@10.99.8.128:5444/sigatra_dbprod",
        statement_timeout: 0,
        connectionTimeoutMillis: 60000
    });

    try {
        await client.connect();
        const sql = `WITH DetailPengecekan AS (
            SELECT 
                tar.id, 
                tar.techidentno, 
                tar.ahi_v3,
                tara.health_index AS ahi_asset_index,
                tip.health_index AS inspeksi_parameter_index,
                MAX(tara.health_index) OVER(PARTITION BY tar.id) AS max_health_index
            FROM t_assets_register tar 
            INNER JOIN t_assets_register_ahi tara ON tara.id_asset = tar.id
            INNER JOIN t_inspeksi_parameter tip ON tip.id = tara.id_inspeksi_parameter 
            WHERE tar.ahi_v3 IS NOT NULL 
              AND tara.is_ahi IS true
        )
        SELECT 
            id,
            techidentno,
            ahi_v3,
            max_health_index,
            CASE 
                WHEN ahi_v3 = max_health_index THEN 'Sesuai'
                ELSE 'Tidak Sesuai' 
            END AS status_kesesuaian_ahi,
            ahi_asset_index,
            inspeksi_parameter_index,
            'Ada Selisih' AS status_sinkron_tip
        FROM DetailPengecekan
        WHERE ahi_asset_index != inspeksi_parameter_index;`;

        const startTime = Date.now();
        const res = await client.query(sql);
        const durationMin = ((Date.now() - startTime) / 60000).toFixed(2);

        console.log(`[${new Date().toISOString()}] Query selesai dalam ${durationMin} menit. Total baris selisih: ${res.rowCount}`);

        const reportsDir = path.join(__dirname, '..', 'reports');
        if (!fs.existsSync(reportsDir)) {
            fs.mkdirSync(reportsDir, { recursive: true });
        }

        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
        const reportPath = path.join(reportsDir, `pengecekan_ahi_${timestamp}.json`);
        fs.writeFileSync(reportPath, JSON.stringify(res.rows, null, 2));

        console.log(`[${new Date().toISOString()}] Hasil laporan tersimpan di: ${reportPath}`);
    } catch (err) {
        console.error(`[${new Date().toISOString()}] Error eksekusi query:`, err.message);
    } finally {
        await client.end();
    }
}

runCheck();
