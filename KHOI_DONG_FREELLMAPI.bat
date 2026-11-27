@echo off
chcp 65001 > nul
title FreeLLMAPI Gateway - AI Free Token Station
color 0B

echo ==============================================================================
echo       FREELLMAPI - TRẠM CHUYỂN TIẾP AI & KHO TOKEN MIỄN PHÍ TỔNG HỢP
echo                      DỰ ÁN: E18_APIKEY_Free (KHO SỐ 2)
echo ==============================================================================
echo.
echo [1/3] Kiểm tra môi trường Node.js...
node -v
echo.
echo [2/3] Cấu hình thông số trạm phát:
echo * Cổng kết nối (Port): http://localhost:3001
echo * OpenAI Endpoint: http://localhost:3001/v1
echo * Unified API Key: freellmapi-8aa2aa9beea85ea2f4eea4c21ae0b97e4fb460521fa7fd77
echo * Dashboard URL: http://localhost:3001
echo * Tài khoản đăng nhập Dashboard: admin@example.com / HegoAdminPassword2026!
echo.
echo [3/3] Đang khởi động Server FreeLLMAPI...
echo (Nhấn Ctrl+C để dừng server khi không sử dụng)
echo ------------------------------------------------------------------------------
cd /d "%~dp0"
node server/dist/index.js
pause
