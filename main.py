import threading
from tkinter import *
from tkinter import filedialog as fd

from main_pack import parser


def insertText():
    file_name = fd.askopenfilename(filetypes=(("Excel файлы", "*.xlsx"),))
    threading.Thread(target=parser.read_xlsx, args=(file_name, )).start()


root = Tk()
b1 = Button(text="Открыть", command=insertText)
b1.grid(row=1, sticky=E)
root.mainloop()
