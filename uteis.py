import os
import shutil
from datetime import datetime
from tkinter import filedialog


def get_save_path(ext="xlsx"):
    caminho = filedialog.asksaveasfilename()
    return caminho + ext


def create_spsh(caminho="planilhas/savedspreadsheet_", save_as=False):

    base = r"planilhas/bases/LIFO_base.xlsx"
    ext = "." + base.split(".")[-1]
    if save_as:
        caminho = get_save_path()
    else:
        caminho = default_file_name(caminho)
    path_name = caminho + ext
    shutil.copyfile(base, path_name)
    return path_name


def default_file_name(caminho, date=False):
    """
    check the caminho if the dir name exists and create a new one with a sequence number
    caminho: the caminho name of the saving file
    date: inset the date time in the name
    """
    print("saving the file...")
    save_num = 1

    # confere se o diretorio ja existe e cria um novo
    while True:
        ext = "." + caminho.split(".")[-1]
        caminho = (caminho[: 0 - len(ext)]) + str(save_num)

        if not os.path.exists(caminho):
            print(caminho + "J")
            print(ext)
            path_name = caminho
            break
        else:
            # print("this directory already exists!")
            print(caminho + "jota")
            cut = 0 - (len(str(save_num)))
            caminho = caminho[:cut]
            save_num += 1

    if date:
        now = datetime.today().strftime("%Y-%m-%d-%H:%M")
        path_name = f"{path_name} - {now}"

    return path_name


# pega os dados necessários para fazer os calculos

# fazer auto complete inserindo os dados faltantes nas cedulas corretas
#
create_spsh()
