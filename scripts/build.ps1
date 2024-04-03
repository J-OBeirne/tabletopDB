.\venv\Scripts\pyinstaller.exe --clean --noconfirm --onefile --console --add-data "./data;data/" --add-data "./static;static/" --add-data "./templates;templates/" --paths "./venv/Lib/site-packages" "./server.py"
Remove-Item .\build -Recurse -Force -Confirm:$false
Remove-Item .\server.spec -Force -Confirm:$false