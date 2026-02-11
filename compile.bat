@echo off

pyinstaller ^
--onefile ^
--noconsole ^
--icon=icon.ico ^
--distpath Compiled ^
--workpath Compiled\BuildTemp ^
"SniperElite_4 - Priority Setter.py"

rmdir /s /q Compiled\BuildTemp

echo.
echo Build selesai. Tekan tombol apa saja untuk keluar...
pause