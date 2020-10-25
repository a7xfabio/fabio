from pathlib import Path

archivo = Path("lab2par2PF / palabras_ingles.txt")

print(archivo.name)

if not archivo.exists():
    print("file does not exist")
else:
    print("file exist")