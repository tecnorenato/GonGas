import tkinter as tk
from imagens import *
from widgets import *
from cores import *
from frames import *


class JanPrincipal(FramesControladores, WidgetsCompletos):
    def __init__(self):
        super().__init__()
        self.janela_doMenu = None
        self.janela_menu()

    def janela_menu(self):
        self.janela_doMenu = tk.Tk()
        janela = self.janela_doMenu
        janela.state('zoomed')
        janela.title('Disk Gás Gonçalves')
        janela.configure(background=preto_claro)
        janela.geometry("%dx%d" % (janela.winfo_screenwidth(), janela.winfo_screenheight()))
        janela.minsize(1200, 640)

        self.frame_dosBotõesMenu()
        self.frame_controleTreeClientes()
        self.frame_treeClientes()
        self.treeview_clientes()

        janela.mainloop()


JanPrincipal()
