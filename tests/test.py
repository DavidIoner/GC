base = "planilhas/bases/LIFO_base.xlsx"
ext = "." + base.split(".")[-1]
path = base[: 0 - len(ext)]
print(path)
print(ext)
