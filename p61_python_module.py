import os
import sys

# Ordner anlegen
# os.mkdir('/home/cmt/test-neu')

# os -> Alles zum Thema Ordner, Dateien, Rechte

# Ordner / Datei löschen
# os.remove('/home/cmt/test-neu')

# User ID bekommen
print(os.getuid())
print(os.getlogin())
print(os.uname())

print(sys.version_info)
print(sys.version)

print(sys.maxsize)
