import shutil
from tkinter import filedialog
from os import path

def chose_path(ext='xlsx'):
    path = filedialog.asksaveasfilename()
    return path + ext


def creare_new_lifo(name="0", path="planilhas/"):
    shutil.copyfile(r"planilhas/bases/LIFO_base.xlsx", path + name)
    if 


def save_fig():
    print("saving the figure...")
    fig_name = r"images/" + "game_"
    save_num = 1

    # confere se o diretorio ja existe e cria um novo
    while True:
        fig_name = fig_name + str(save_num)
        if not path.exists(fig_name):
            path_name = fig_name
            break
        else:
            # print("this directory already exists!")
            cut = 0 - len(str(save_num))
            fig_name = fig_name[:cut]
            save_num += 1

    return fig_name
