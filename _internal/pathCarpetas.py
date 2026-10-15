import os;

pathCarpetas = [
    os.path.join("C:\\","Users", f"{os.getenv("USERNAME")}", "AppData"),
    os.path.join("C:\\"),
    os.path.join("C:\\","Program Files (x86)", "Microsoft"),
    os.path.join("C:\\","Program Files"),
    os.path.join("C:\\","Users", "Default", "AppData"),
]

pathDirectorio = [
    os.path.join("C:\\","Users", f"{os.getenv("USERNAME")}", "Desktop"),
    os.path.join("C:\\","Users", f"{os.getenv("USERNAME")}", "Pictures"),
    os.path.join("C:\\","Users", f"{os.getenv("USERNAME")}", "Downloads"),
    os.path.join("C:\\","Users", f"{os.getenv("USERNAME")}", "Documents"),
]

#BK_MALWARE_ATACK

for ruta in pathDirectorio:
    if os.path.exists(ruta) == True:
        print(f"Ruta: {ruta}: [EXISTE]")
    else:
        print(f"Ruta: {ruta}: [ERROR]")
