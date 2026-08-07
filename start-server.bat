@echo off
title HiFi Transmisi Local Server
echo ========================================================
echo   Menjalankan HiFi Transmisi Portal di Localhost:8000
echo ========================================================
echo.
echo Server aktif di: http://localhost:8000/
echo.
start http://localhost:8000/hifi-home/home.html
python -m http.server 8000
