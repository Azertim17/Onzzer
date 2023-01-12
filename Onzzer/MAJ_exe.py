import os

# This program is used to create a new version of the Onzzer.exe App

command = 'pyinstaller --noconfirm --onefile --windowed --icon "C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/Icones/app.ico" --add-data "C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/Icones;Icones/" --add-data "C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/request_albums.py;." --add-data "C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/request_artistes.py;." --add-data "C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/request_pistes.py;." --add-data "C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/youtube_search.py;." --hidden-import "json" --hidden-import "requests" --hidden-import "PyQt5" --hidden-import "os" --hidden-import "sys" --hidden-import "webbrowser"  "C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/Onzzer.py"'
os.system(command)
