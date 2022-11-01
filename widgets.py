import tkinter as tk
from imagens import *
from tkinter import ttk
from cores import *
from placeHolders import *
from treeviews import*


class WidgetsCompletos(Images, PlaceTudo):
    def __init__(self):
        super().__init__()
        self.images_base64()
        self.produtosJáComprados = []
        self.img_icoendereço_filter = None
        self.img_p13liqui = None
        self.btÁguaGás510 = None
        self.bt_para_editar = None
        self.btÁguaNat510 = None
        self.entry_endereço_edição = None
        self.btP45Liquigás = None
        self.rotulo_observação_edição = None
        self.btÁgua1500 = None
        self.entry_qt_novo = None
        self.rotulo_observação_filter = None
        self.btÁgua1500 = None
        self.img_icoNome_dinheiro = None
        self.entryqt = None
        self.img_icoTelefone_edição = None
        self.checkContinue = None
        self.motivo_nome = None
        self.bt_para_cadastrar = None
        self.bt_para_add_produto = None
        self.btAddEstoque = None
        self.entry_produto_novo = None
        self.imgConfirmar = None
        self.btAdcProduto = None
        self.motivo_telefone = None
        self.entryfornecedor = None
        self.motivo_endereço = None
        self.btEditPreço = None
        self.valor_unit = None
        self.style = None
        self.valor_total = None
        self.entry_qt = None
        self.img_addPreço = None
        self.img_icoNom = None
        self.comboxFormaPGTO = None
        self.entry_nome = None
        self.img_agua1500 = None
        self.img_icoTelefone = None
        self.img_agua510Gaseficada = None
        self.entry_telefone = None
        self.entry_observação = None
        self.entry_endereço = None
        self.img_icoEndereço = None
        self.img_icoObservação = None
        self.img_icoVerdin = None
        self.motivo_observação = None
        self.btApertodeMão = None
        self.img_agua20L = None
        self.img_icoQuantidade = None
        self.labelTotalDaCompra = None
        self.img_icoProduto = None
        self.comboxProduto = None
        self.btVerdinho = None
        self.img_p13ultra = None
        self.img_p45liqui = None
        self.img_apertoDeMão = None
        self.btP13Liquigás = None
        self.img_p45ultra = None
        self.btP45Ultragaz = None
        self.img_agua510Natural = None
        self.btÁgua20L = None
        self.btP13Ultragaz = None
        self.img_addProduto = None
        self.img_icoobservação_filter = None
        self.rotulo_endereço_filter = None
        self.entry_observação_edição = None
        self.img_icoobservação_edição = None
        self.img_icoendereço_edição = None
        self.rotulo_telefone_edição = None
        self.rotulo_endereço_edição = None
        self.entry_telefone_edição = None
        self.img_icoNome_edição = None
        self.rotulo_nome_edição = None
        self.entry_nome_edição = None
        self.entry_observação_filter = None
        self.rotulo_telefone_filter = None
        self.entry_endereço_filter = None
        self.entry_telefone_filter = None
        self.img_icoTelefone_filter = None
        self.entry_nome_filter = None
        self.rotulo_nome_filter = None
        self.img_icoNome_filter = None

    def entrada_nome_filter(self, janela):
        self.img_icoNome_filter = tk.PhotoImage(data=base64.b64decode(self.nome))
        self.rotulo_nome_filter = tk.Label(master=janela, bg=preto_claro, image=self.img_icoNome_filter)
        self.rotulo_nome_filter.grid(row=0, column=0)
        self.entry_nome_filter = tk.Entry(master=janela, bg=preto_claro, fg='Gray', font=('verdana', 10), width=20)
        self.entry_nome_filter.grid(row=0, column=1)
        self.entry_nome_filter.insert(0, 'Nome')

    def entrada_telefone_filter(self, janela):
        self.img_icoTelefone_filter = tk.PhotoImage(data=base64.b64decode(self.telefone))
        self.rotulo_telefone_filter = tk.Label(master=janela, bg=preto_claro, image=self.img_icoTelefone_filter)
        self.rotulo_telefone_filter.grid(row=1, column=0)
        self.entry_telefone_filter = tk.Entry(janela, bg=preto_claro, fg='Gray', font=('verdana', 10), width=20)
        self.entry_telefone_filter.grid(row=1, column=1)
        self.entry_telefone_filter.insert(0, 'Telefone')

    def entrada_endereço_filter(self, janela):
        self.img_icoendereço_filter = tk.PhotoImage(data=base64.b64decode(self.endereço))
        self.rotulo_endereço_filter = tk.Label(master=janela, bg=preto_claro, image=self.img_icoendereço_filter)
        self.rotulo_endereço_filter.grid(row=2, column=0)
        self.entry_endereço_filter = tk.Entry(janela, bg=preto_claro, fg='Gray', font=('verdana', 10), width=20)
        self.entry_endereço_filter.grid(row=2, column=1)
        self.entry_endereço_filter.insert(0, 'Endereço')

    def entrada_observação_filter(self, janela):
        self.img_icoobservação_filter = tk.PhotoImage(data=base64.b64decode(self.observação))
        self.rotulo_observação_filter = tk.Label(master=janela, bg=preto_claro, image=self.img_icoobservação_filter)
        self.rotulo_observação_filter.grid(row=3, column=0)
        self.entry_observação_filter = tk.Entry(janela, bg=preto_claro, fg='Gray', font=('verdana', 10), width=20)
        self.entry_observação_filter.grid(row=3, column=1)
        self.entry_observação_filter.insert(0, 'Observação')

    def entrada_nome_edição(self, janela):
        self.img_icoNome_edição = tk.PhotoImage(data=base64.b64decode(self.nome))
        self.rotulo_nome_edição = tk.Label(master=janela, bg=preto_claro, image=self.img_icoNome_edição)
        self.rotulo_nome_edição.grid(row=0, column=0)
        self.entry_nome_edição = tk.Entry(master=janela, bg=preto_claro, fg='Gray', font=('verdana', 12), width=16)
        self.entry_nome_edição.grid(row=0, column=1)
        self.entry_nome_edição.insert(0, 'Nome')

    def entrada_telefone_edição(self, janela):
        self.img_icoTelefone_edição = tk.PhotoImage(data=base64.b64decode(self.telefone))
        self.rotulo_telefone_edição = tk.Label(master=janela, bg=preto_claro, image=self.img_icoTelefone_edição)
        self.rotulo_telefone_edição.grid(row=1, column=0)
        self.entry_telefone_edição = tk.Entry(janela, bg=preto_claro, fg='Gray', font=('verdana', 12), width=16)
        self.entry_telefone_edição.grid(row=1, column=1)
        self.entry_telefone_edição.insert(0, 'Telefone')

    def entrada_endereço_edição(self, janela):
        self.img_icoendereço_edição = tk.PhotoImage(data=base64.b64decode(self.endereço))
        self.rotulo_endereço_edição = tk.Label(master=janela, bg=preto_claro, image=self.img_icoendereço_edição)
        self.rotulo_endereço_edição.grid(row=2, column=0)
        self.entry_endereço_edição = tk.Entry(janela, bg=preto_claro, fg='Gray', font=('verdana', 12), width=16)
        self.entry_endereço_edição.grid(row=2, column=1)
        self.entry_endereço_edição.insert(0, 'Endereço')

    def entrada_observação_edição(self, janela):
        self.img_icoobservação_edição = tk.PhotoImage(data=base64.b64decode(self.observação))
        self.rotulo_observação_edição = tk.Label(master=janela, bg=preto_claro, image=self.img_icoobservação_edição)
        self.rotulo_observação_edição.grid(row=3, column=0)
        self.entry_observação_edição = tk.Entry(janela, bg=preto_claro, fg='Gray', font=('verdana', 10), width=20)
        self.entry_observação_edição.grid(row=3, column=1)
        self.entry_observação_edição.insert(0, 'Observação')

    def botão_addClilente(self, janela):
        self.bt_para_cadastrar = tk.Button(janela, image=self.imagem_addUser,
                                           bg=preto_claro, activebackground=verde_médio, width=100,
                                           height=45, command=self.add_cliente_noBDClientes)

    def botão_editClilente(self, janela):
        self.bt_para_editar = tk.Button(janela, image=self.imagem_editUser,
                                           bg=preto_claro, activebackground=verde_médio, width=100,
                                           height=45, command=self.altera_cliente)

    def checkBox(self, janela, msg):
        self.checkContinue = tk.Checkbutton(janela, text=msg, variable=self.varDoCheck,
                                            onvalue='Sim', offvalue='Não', activebackground=preto_claro,
                                            bg=preto_claro, selectcolor=preto_claro)

    def botão_addProduto(self, janela):
        self.img_addProduto = tk.PhotoImage(data=base64.b64decode(self.botãoMais))
        self.bt_para_add_produto = tk.Button(janela, image=self.img_addProduto,
                                             bg=preto_claro, activebackground=verde_médio, width=100,
                                             height=45, command=self.adcionarProduto)

    def entrada_produto_novo(self, janela):
        self.entry_produto_novo = tk.Entry(janela, bg=preto_claro, fg='Gray', font=('verdana', 12), width=16)
        self.entry_produto_novo.grid(row=2, column=1, padx=15)
        self.entry_produto_novo.insert(0, 'Produto')
        self.entry_qt_novo = tk.Entry(janela, bg=preto_claro, fg='Gray', font=('verdana', 12), width=8)
        self.entry_qt_novo.grid(row=2, column=2, sticky='E', padx=15)
        self.entry_qt_novo.insert(0, 'R$')
        self.img_addPreço = tk.PhotoImage(data=base64.b64decode(self.botãoVerdinho))
        self.btAdcProduto = tk.Button(janela, bg=preto_claro, image=self.img_addPreço, activebackground=verde_médio, command=self.add_preço_produto_BD_preço)
        # self.btAdcProduto.grid(row=2, column=3, padx=15)

    def botão_Edit_preço(self, janela):
        self.imgConfirmar = tk.PhotoImage(data=base64.b64decode(self.botãoVerdinho))
        self.btEditPreço = tk.Button(janela, image=self.imgConfirmar, activebackground=verde_médio, bg=preto_claro, command=self.altera_preço)
        self.btEditPreço.grid(row=6)

    def qtDeProduto(self):
        self.entryqt = tk.Entry(self.entEstoque_frame, bg=preto_claro, fg='Gray', font=('verdana', 12), width=5)
        self.entryqt.insert(0, 'Qt')
        self.entryqt.grid(column=0, row=1, pady=5)
        self.valor_unit = tk.Entry(self.entEstoque_frame, bg=preto_claro, fg='Gray', font=('verdana', 12), width=8)
        self.valor_unit.insert(0, 'Unitário')
        self.valor_unit.grid(column=1, row=1, pady=5)
        self.valor_total = tk.Entry(self.entEstoque_frame, bg=preto_claro, fg='Gray', font=('verdana', 12), width=8)
        self.valor_total.insert(0, 'Total')
        self.valor_total.grid(column=2, row=1, pady=5)
        self.entryfornecedor = tk.Entry(self.entEstoque_frame, bg=preto_claro, fg='Gray', font=('verdana', 12), width=36)
        self.entryfornecedor.insert(0, 'Fornecedor')
        self.entryfornecedor.grid(column=0, row=2, columnspan=3, sticky='E')
        self.img_addPreço = tk.PhotoImage(data=base64.b64decode(self.botãoVerdinho))
        self.btAddEstoque = tk.Button(self.entEstoque_frame, image=self.img_addPreço, activebackground=verde_médio, bg=preto_claro, width=80, height=25,
                                      command=self.add_estoque_noBDEstoque)

        self.valor_unit.bind('<KeyRelease>', self.formata_preço_entrada_produto)
        self.valor_unit.bind('<FocusIn>', self.formata_preço_entrada_produto)
        self.valor_unit.bind('<FocusOut>', self.formata_preço_entrada_produto)
        self.entryqt.bind('<KeyRelease>', self.formata_quantidade_entrada_produto)
        self.entryqt.bind('<FocusIn>', self.formata_quantidade_entrada_produto)
        self.entryqt.bind('<FocusOut>', self.formata_quantidade_entrada_produto)
        self.entryfornecedor.bind('<KeyRelease>', self.formata_fornecedor_entrada_produto)
        self.entryfornecedor.bind('<FocusIn>', self.formata_fornecedor_entrada_produto)
        self.entryfornecedor.bind('<FocusOut>', self.formata_fornecedor_entrada_produto)

    def nome_DeCliente(self, janela, funçãoDoBind, motivo=None):
        """
        Monta com imagem e entrada o campo para colher o nome do cliente além de agir com o placeHolder.
        :param janela: Frame ou janela que acomodará a entrada.
        :param funçãoDoBind: Função a ser chamada para o bind.
        :param motivo: Consultando ou Inserindo? Muda a cor na validação de acordo com motivo. Em ambos os casos
        verificam se o nome já existe no BD.
        """
        frame = tk.Frame(janela, bg=preto_claro, width=100)
        frame.grid(row=0, column=0)
        self.img_icoNom = tk.PhotoImage(data=base64.b64decode(self.nome))
        foto = tk.Label(master=frame, image=self.img_icoNom, bg=preto_claro)
        foto.grid(column=0, row=0)
        self.entry_nome = tk.Entry(frame, bg=preto_claro, font=('Arial', 12), fg='Gray')
        self.entry_nome.insert(0, 'Nome')
        self.entry_nome.grid(column=1, row=0)
        self.entry_nome.bind('<KeyRelease>', funçãoDoBind)
        self.entry_nome.bind('<FocusIn>', funçãoDoBind)
        self.entry_nome.bind('<FocusOut>', funçãoDoBind)
        self.motivo_nome = motivo

    def forma_dePagamento(self, janela=None):
        frame = tk.Frame(janela, bg=preto_claro)
        frame.grid(row=1, column=0)
        self.img_icoNome_dinheiro = tk.PhotoImage(data=base64.b64decode(self.iconeDinheiroNaMão))
        foto = tk.Label(frame, image=self.img_icoNome_dinheiro, bg=preto_claro)
        foto.grid(column=0, row=0)
        self.style = ttk.Style()
        self.style.map('TCombobox', fieldbackground=[('readonly', preto_claro)])
        self.style.map('TCombobox', selectforeground=[('readonly', 'White')])
        self.style.map('TCombobox', foreground=[('readonly', 'Gray')])
        self.style.configure("TCombobox", background=preto_claro)
        self.comboxFormaPGTO = ttk.Combobox(frame, values=['Dinheiro', 'Fiado', 'Débito', 'Crédito'], width=10, font=('Arial', 12))
        self.comboxFormaPGTO.grid(column=1, row=0)
        self.comboxFormaPGTO.insert(0, 'Pagamento')
        self.comboxFormaPGTO['state'] = 'readonly'
        self.comboxFormaPGTO.option_add("*TCombobox*Listbox*Background", preto_claro)
        self.comboxFormaPGTO.option_add("*TCombobox*Listbox*Foreground", 'Yellow')

    def telefone_DeCliente(self, janela, funçãoDoBind, motivo=None):
        """
        Monta com imagem e entrada o campo para colher o telefone do cliente além de agir com o placeHolder.
        :param janela: Frame ou janela que acomodará a entrada.
        :param funçãoDoBind: Função a ser chamada para o bind.
        :param motivo: Consultando ou Inserindo? Muda a cor na validação de acordo com motivo. Em ambos os casos
        verificam se o telefone já existe no BD.
        """
        frame = tk.Frame(janela, bg=preto_claro, width=100)
        frame.grid(row=0, column=0)
        self.img_icoTelefone = tk.PhotoImage(data=base64.b64decode(self.telefone))
        foto = tk.Label(frame, image=self.img_icoTelefone, bg=preto_claro)
        foto.grid(column=0, row=0)
        self.entry_telefone = tk.Entry(frame, bg=preto_claro, font=('Arial', 12), fg='Gray')
        self.entry_telefone.insert(0, 'Telefone')
        self.entry_telefone.grid(column=1, row=0)
        self.entry_telefone.bind('<KeyRelease>', funçãoDoBind)
        self.entry_telefone.bind('<FocusIn>', funçãoDoBind)
        self.entry_telefone.bind('<FocusOut>', funçãoDoBind)
        self.motivo_telefone = motivo

    def endereço_DeCliente(self, janela, funçãoDoBind, motivo=None):
        """
        Monta com imagem e entrada o campo para colher endereço do cliente além de agir com o placeHolder.
        :param janela: Frame ou janela que acomodará a entrada.
        :param funçãoDoBind: Função a ser chamada para o bind.
        :param motivo: Consultando ou Inserindo? Muda a cor na validação de acordo com motivo. Em ambos os casos
        verificam se endereço já existe no BD.
        """
        frame = tk.Frame(janela, bg=preto_claro, width=100)
        frame.grid(row=0, column=0)
        self.img_icoEndereço = tk.PhotoImage(data=base64.b64decode(self.endereço))
        foto = tk.Label(frame, image=self.img_icoEndereço, bg=preto_claro)
        foto.grid(column=0, row=0)
        self.entry_endereço = tk.Entry(frame, bg=preto_claro, font=('Arial', 12), fg='Gray')
        self.entry_endereço.insert(0, 'Endereço')
        self.entry_endereço.grid(column=1, row=0)
        self.entry_endereço.bind('<KeyRelease>', funçãoDoBind)
        self.entry_endereço.bind('<FocusIn>', funçãoDoBind)
        self.entry_endereço.bind('<FocusOut>', funçãoDoBind)
        self.motivo_endereço = motivo

    def observação_DeCliente(self, janela, funçãoDoBind, motivo=None):
        """
        Monta com imagem e entrada o campo para colher a observação do cliente além de agir com o placeHolder.
        :param janela: Frame ou janela que acomodará a entrada.
        :param funçãoDoBind: Função a ser chamada para o bind.
        :param motivo: Consultando ou Inserindo? Muda a cor na validação de acordo com motivo. Em ambos os casos
        verificam se a observação já existe no BD.
        """
        frame = tk.Frame(janela, bg=preto_claro, width=100)
        frame.grid(row=0, column=0)
        self.img_icoObservação = tk.PhotoImage(data=base64.b64decode(self.observação))
        foto = tk.Label(frame, image=self.img_icoObservação, bg=preto_claro)
        foto.grid(column=0, row=0)
        self.entry_observação = tk.Entry(frame, bg=preto_claro, font=('Arial', 12), fg='Gray')
        self.entry_observação.insert(0, 'Observação')
        self.entry_observação.grid(column=1, row=0)
        self.entry_observação.bind('<KeyRelease>', funçãoDoBind)
        self.entry_observação.bind('<FocusIn>', funçãoDoBind)
        self.entry_observação.bind('<FocusOut>', funçãoDoBind)
        self.motivo_observação = motivo

    def quantidade_DeProduto(self, janela, funçãoDoBind):
        """
        Monta com imagem e entrada o campo para colher a quantidade de produto além de agir com o placeHolder.
        :param janela: Frame ou janela que acomodará a entrada.
        :param funçãoDoBind: Função a ser chamada para o bind.
        """
        frame = tk.Frame(janela, bg=preto_claro, width=100)
        frame.grid(row=0, column=0)
        self.img_icoQuantidade = tk.PhotoImage(data=base64.b64decode(self.iconeQuantidade))
        foto = tk.Label(frame, image=self.img_icoQuantidade, bg=preto_claro)
        foto.grid(column=0, row=0)
        self.entry_qt = tk.Entry(frame, bg=preto_claro, font=('Arial', 12), fg='Gray')
        self.entry_qt.insert(0, 'Qtde')
        self.entry_qt.grid(column=1, row=0)
        self.entry_qt.bind('<KeyRelease>', funçãoDoBind)
        self.entry_qt.bind('<FocusIn>', funçãoDoBind)
        self.entry_qt.bind('<FocusOut>', funçãoDoBind)

    def escolha_deProduto(self, janela=None):
        """
        Funcão para colocar o combobox de produtos.
        :param janela: Janela em que será alocado o Widget.
        :return: NADA
        """
        frame = tk.Frame(janela, bg=preto_claro)
        frame.grid(row=1, column=0)
        self.img_icoProduto = tk.PhotoImage(data=base64.b64decode(self.iconeProduto))
        foto = tk.Label(frame, image=self.img_icoProduto, bg=preto_claro)
        foto.grid(column=0, row=0)
        self.comboxProduto = ttk.Combobox(frame, values=self.select_nomes_produtos(), width=10, font=('Arial', 12))
        self.comboxProduto.grid(column=1, row=0)
        self.comboxProduto.insert(0, 'Produto')
        self.comboxProduto['state'] = 'readonly'
        self.comboxProduto.option_add("*TCombobox*Listbox*Background", preto_claro)
        self.comboxProduto.option_add("*TCombobox*Listbox*Foreground", 'Yellow')
        self.comboxProduto.bind('<<ComboboxSelected>>', self.verdeComboProduto)

    def botãoVerde(self, janela):
        frame = tk.Frame(janela, bg=preto_claro)
        frame.grid(row=0, column=0)
        self.img_icoVerdin = tk.PhotoImage(data=base64.b64decode(self.botãoVerdinho))
        self.btVerdinho = tk.Button(frame, image=self.img_icoVerdin, bg=preto_claro, activebackground=verde_médio)
        self.btVerdinho.grid(row=0, column=0)

    def botãoApertodeMão(self, janela):
        frame = tk.Frame(janela, bg=preto_claro)
        frame.grid(row=0, column=0)
        self.img_apertoDeMão = tk.PhotoImage(data=base64.b64decode(self.apertoDeMão))
        self.btApertodeMão = tk.Button(frame, image=self.img_apertoDeMão, bg=preto_claro, activebackground=verde_médio, width=80, height=40)
        self.btApertodeMão.grid(row=0, column=0)

    def totalDaCompra(self, janela):
        frame = tk.Frame(janela, bg=preto_claro)
        frame.grid(row=0, column=0)
        self.labelTotalDaCompra = tk.Label(janela, text='Total: 0.00', bg=preto_claro, fg='yellow')
        self.labelTotalDaCompra.grid(row=0, column=0)

    def botõesDeAddProduto(self, janela=None):
        self.img_p13ultra = tk.PhotoImage(data=base64.b64decode(self.p13ulltragaz))
        self.img_p13liqui = tk.PhotoImage(data=base64.b64decode(self.p13liquigás))
        self.img_p45ultra = tk.PhotoImage(data=base64.b64decode(self.p45ulltragaz))
        self.img_p45liqui = tk.PhotoImage(data=base64.b64decode(self.p45liquigás))
        self.img_agua20L = tk.PhotoImage(data=base64.b64decode(self.agua20L))
        self.img_agua1500 = tk.PhotoImage(data=base64.b64decode(self.agua1500))
        self.img_agua510Natural = tk.PhotoImage(data=base64.b64decode(self.agua510natural))
        self.img_agua510Gaseficada = tk.PhotoImage(data=base64.b64decode(self.agua510gaseficada))

        self.btP13Ultragaz = tk.Button(janela, bg=preto_claro, height=90, width=45, activebackground=verde_médio, image=self.img_p13ultra,
                                       command=lambda: self.colocaItemNaTreeDeCompras('P13 Ultragaz'))
        self.btP13Ultragaz.bind('<Button-3>', lambda evento, item='P13 Ultragaz', botão=self.btP13Ultragaz: self.tiraItemNaTreeDeCompras(item, botão))
        self.btP13Ultragaz.grid(column=0, row=0)

        self.btP13Liquigás = tk.Button(janela, bg=preto_claro, height=90, width=45, activebackground=verde_médio, image=self.img_p13liqui,
                                       command=lambda: self.colocaItemNaTreeDeCompras('P13 Liquigás'))
        self.btP13Liquigás.bind('<Button-3>', lambda evento, item='P13 Liquigás', botão=self.btP13Liquigás: self.tiraItemNaTreeDeCompras(item, botão))
        self.btP13Liquigás.grid(column=1, row=0)

        self.btP45Ultragaz = tk.Button(janela, bg=preto_claro, height=90, width=45, activebackground=verde_médio, image=self.img_p45ultra,
                                       command=lambda: self.colocaItemNaTreeDeCompras('P45 Ultragaz'))
        self.btP45Ultragaz.bind('<Button-3>', lambda evento, item='P45 Ultragaz', botão=self.btP45Ultragaz: self.tiraItemNaTreeDeCompras(item, botão))
        self.btP45Ultragaz.grid(column=2, row=0)

        self.btP45Liquigás = tk.Button(janela, bg=preto_claro, height=90, width=45, activebackground=verde_médio, image=self.img_p45liqui,
                                       command=lambda: self.colocaItemNaTreeDeCompras('P45 Liquigás'))
        self.btP45Liquigás.bind('<Button-3>', lambda evento, item='P45 Liquigás', botão=self.btP45Liquigás: self.tiraItemNaTreeDeCompras(item, botão))
        self.btP45Liquigás.grid(column=3, row=0)

        self.btÁgua20L = tk.Button(janela, bg=preto_claro, height=90, width=45, activebackground=verde_médio, image=self.img_agua20L,
                                   command=lambda: self.colocaItemNaTreeDeCompras('Água 20L'))
        self.btÁgua20L.bind('<Button-3>', lambda evento, item='Água 20L', botão=self.btÁgua20L: self.tiraItemNaTreeDeCompras(item, botão))
        self.btÁgua20L.grid(column=4, row=0)

        self.btÁgua1500 = tk.Button(janela, bg=preto_claro, height=90, width=45, activebackground=verde_médio, image=self.img_agua1500,
                                    command=lambda: self.colocaItemNaTreeDeCompras('Água 1500'))
        self.btÁgua1500.bind('<Button-3>', lambda evento, item='Água 1500', botão=self.btÁgua1500: self.tiraItemNaTreeDeCompras(item, botão))
        self.btÁgua1500.grid(column=5, row=0)

        self.btÁguaNat510 = tk.Button(janela, bg=preto_claro, height=90, width=25, activebackground=verde_médio, image=self.img_agua510Natural,
                                      command=lambda: self.colocaItemNaTreeDeCompras('Água Nat 510'))
        self.btÁguaNat510.bind('<Button-3>', lambda evento, item='Água Nat 510', botão=self.btÁguaNat510: self.tiraItemNaTreeDeCompras(item, botão))
        self.btÁguaNat510.grid(column=6, row=0)

        self.btÁguaGás510 = tk.Button(janela, bg=preto_claro, height=90, width=25, activebackground=verde_médio, image=self.img_agua510Gaseficada,
                                      command=lambda: self.colocaItemNaTreeDeCompras('Água Gás 510'))
        self.btÁguaGás510.bind('<Button-3>', lambda evento, item='Água Gás 510', botão=self.btÁguaGás510: self.tiraItemNaTreeDeCompras(item, botão))
        self.btÁguaGás510.grid(column=7, row=0)

    def dadosDaJanelaCompra(self, janela):
        nome = tk.Label(janela, text=f'Nome: {self.dados_selec_tree_clientes()[2]}', font=('Arial', 12), bg=preto_claro, fg='Yellow', anchor="w")
        nome.place(x=5, y=0)
        telefone = tk.Label(janela, text=f'Telefone: {self.dados_selec_tree_clientes()[3]}', font=('Arial', 12), bg=preto_claro, fg='Yellow', anchor="e")
        telefone.place(x=300, y=0)
        endereço = tk.Label(janela, text=f'Endereço: {self.dados_selec_tree_clientes()[4]}', font=('Arial', 12), bg=preto_claro, fg='Yellow', anchor="e")
        endereço.place(x=5, y=20)
        observação = tk.Label(janela, text=f'Observação: {self.dados_selec_tree_clientes()[5]}', font=('Arial', 12), bg=preto_claro, fg='Yellow', anchor="e")
        observação.place(x=300, y=20)
        total = tk.Label(janela, text=f'Total: {self.comprasDoClienteSelecionado()[1]:.2f}', font=('Arial', 12), bg=preto_claro, fg='Yellow', anchor="e")
        total.place(x=5, y=40)
