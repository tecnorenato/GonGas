import tkinter

from imagens import *
from cores import *
from widgets import *
from imagens import *
from tkinter import *


class JanelasAcessórias:
    def __init__(self):
        super().__init__()
        self.images_base64()
        self.janelaVenda = None
        self.jan_adc_cliente = None
        self.jan_edit_cliente = None
        self.janelaPreço = None
        self.janelaAddProduto = None
        self.janelaAttPreço = None
        self.janelaEntEstoque = None

    def janelaAddCliente(self):
        self.jan_adc_cliente = tk.Toplevel()
        janela = self.jan_adc_cliente
        janela.resizable(False, False)
        janela.configure(bg=preto_claro)
        janela.iconphoto(False, tk.PhotoImage(data=base64.b64decode(self.iconeAddUser)))
        janela.geometry('200x180+800+200')
        janela.title('Add')
        self.frame_addClientes()
        janela.focus_force()
        janela.grab_set()
        janela.mainloop()

    def janelaEditCliente(self):
        self.jan_edit_cliente = tk.Toplevel()
        janela = self.jan_edit_cliente
        janela.resizable(False, False)
        janela.configure(bg=preto_claro)
        janela.iconphoto(False, tk.PhotoImage(data=base64.b64decode(self.iconeEditUser)))
        janela.geometry('200x220+800+200')
        janela.title('Edit')
        self.frame_tarjetaDeEdição()
        self.frame_editClientes()
        janela.focus_force()
        janela.grab_set()
        janela.mainloop()

    def janela_preço(self):
        self.janelaPreço = tk.Toplevel()
        janela = self.janelaPreço
        janela.resizable(False, False)
        janela.configure(bg=preto_claro)
        janela.geometry('400x400+800+200')
        janela.title('Gestor de Preços')
        janela.iconphoto(False, tk.PhotoImage(data=base64.b64decode(self.iconePreço)))
        janela.focus_force()
        janela.grab_set()
        self.frame_janela_preços()

        janela.mainloop()

    def adcionarProduto(self):
        self.janelaAddProduto = tk.Toplevel()
        janela = self.janelaAddProduto
        janela.resizable(False, False)
        janela.configure(bg=preto_claro)
        janela.geometry('400x50+800+560')
        janela.title('Adcionar Produto')
        janela.iconphoto(False, tk.PhotoImage(data=base64.b64decode(self.iconePreço)))
        janela.focus_force()
        janela.grab_set()
        self.frame_janela_addProduto()

        janela.mainloop()

    def attPreço(self):
        self.janelaAttPreço = tk.Toplevel()
        janela = self.janelaAttPreço
        janela.focus_force()
        janela.grab_set()
        janela.resizable(False, False)
        janela.configure(bg=preto_claro)
        janela.geometry('400x200+800+230')
        janela.title('Att Preços')
        janela.iconphoto(False, tk.PhotoImage(data=base64.b64decode(self.iconePreço)))
        self.frame_janela_attPreço()

        janela.mainloop()

    def entradaNoEstoque(self):
        self.janelaEntEstoque = tk.Toplevel()
        janela = self.janelaEntEstoque
        janela.focus_force()
        janela.grab_set()
        janela.resizable(False, False)
        janela.configure(bg=preto_claro)
        janela.geometry('400x160+800+230')
        janela.title('Entradas Estoque')
        janela.iconphoto(False, tk.PhotoImage(data=base64.b64decode(self.iconeCestinhaVerde)))
        self.frame_janelaEntradaEstoque()

        janela.mainloop()

    def venda(self):
        self.janelaVenda = tk.Toplevel()
        janela = self.janelaVenda
        janela.focus_force()
        janela.grab_set()
        janela.resizable(False, False)
        janela.configure(bg=preto_claro)
        janela.geometry('400x530+800+150')
        janela.title('Efetuar Venda')
        janela.iconphoto(False, tk.PhotoImage(data=base64.b64decode(self.iconeDinheiroNaMão)))
        dados = self.dados_selec_tree_clientes()
        self.frame_janelaVenda()
        self.entry_nome.insert(0, dados[2])
        self.entry_telefone.insert(0, dados[3])
        self.entry_endereço.insert(0, dados[4])
        self.entry_observação.insert(0, dados[5])
        self.entry_nome.config(state='readonly', readonlybackground=verde_médio, fg=preto_claro)
        self.entry_telefone.config(state='readonly', readonlybackground=verde_médio, fg=preto_claro)
        self.entry_endereço.config(state='readonly', readonlybackground=verde_médio, fg=preto_claro)
        self.entry_observação.config(fg=preto_claro, bg=verde_médio)
        self.comboxFormaPGTO.focus()
        janela.bind('<Button>', self.mostrarBotãoApertoDeMãos)
        janela.bind('<Return>', self.mostrarBotãoApertoDeMãos)

        janela.mainloop()

    def janelaMostrarCompras(self):

        self.janelaVenda = Toplevel()
        dados = self.dados_selec_tree_clientes()
        janela = self.janelaVenda
        janela.focus_force()
        janela.grab_set()
        janela.resizable(False, False)
        janela.configure(bg=preto_claro)
        janela.geometry('600x530+700+150')
        janela.title(f'Compras de {dados[2]}')
        # janela.iconphoto(False, self.PhotoImage(data=base64.b64decode(self.iconeDinheiroNaMão)))
        self.frame_janelaComprasEfetuada()
        self.dadosDasComprasEfetuadas.bind("<Double-Button-1>", lambda evento: self.janelaItensComprados())
        janela.mainloop()

    def janelaItensComprados(self):
        # top level
        top = Toplevel()
        top.title('Novo formulário')
        top.geometry('200x100')
        lb1 = Label(top, text='Label na nova janela')
        lb1.pack()

        def btn_exit():
            top.destroy()
            top.update()

        leb2 = Button(top, text='Fechar', command=btn_exit)
        leb2.pack()

# JanelasAcessórias().janelaAddCliente()
