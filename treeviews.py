from tkinter import ttk
from cores import *
from crud import *


class TreeViews(Cruds):
    def __init__(self):
        super().__init__()
        self.list_tree_vendas = list()
        self.nomes_de_produtos_cadastrados = list()
        self.listaComTodasCompras = list()
        self.listaCli_clientes = None
        self.scrooLista = None
        self.dados_cli = None
        self.listaCli_preços = None
        self.seleçãoDosPreços = None
        self.dados_da_venda = None
        self.dadosDasComprasEfetuadas = None

    def treeview_clientes(self):
        # Construindo a treeview
        style = ttk.Style()
        style.theme_use("default")
        # Estilizando a Treeview
        style.configure("Treeview", background=preto_claro, fieldbackground=preto_claro, foreground='white',
                        font='arial, 15', rowheight=30,)
        style.map('Treeview', background=[('selected', 'green')])

        # Estilizando os Cabeçalhos
        style.configure('Heading', font='arial, 15', background=preto_claro, foreground='white')

        self.listaCli_clientes = ttk.Treeview(self.frame_treeViewCliente, height=3, columns=('col0', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7'))
        self.listaCli_clientes.heading("#0", text="")
        self.listaCli_clientes.heading("#1", text="Ord")
        self.listaCli_clientes.heading("#2", text="Data")
        self.listaCli_clientes.heading("#3", text="Nome")
        self.listaCli_clientes.heading("#4", text="Telefone")
        self.listaCli_clientes.heading("#5", text="Endereço")
        self.listaCli_clientes.heading("#6", text="Observação")
        self.listaCli_clientes.heading("#7", text="Caloteiro")
        self.listaCli_clientes.heading("#8", text="Compras")

        # Definindo tamanho das Colunas
        self.listaCli_clientes.column("#0", width=1, stretch=False)
        self.listaCli_clientes.column("#1", width=50, anchor='c', stretch=False)
        self.listaCli_clientes.column("#2", width=150, anchor='c', stretch=False)
        self.listaCli_clientes.column("#3", width=200, anchor='c', stretch=False)
        self.listaCli_clientes.column("#4", width=165, anchor='c', stretch=False)
        self.listaCli_clientes.column("#5", width=180, anchor='c', stretch=False)
        self.listaCli_clientes.column("#6", width=125)
        self.listaCli_clientes.column("#7", width=100, anchor='w', stretch=False)
        self.listaCli_clientes.column("#8", width=1, stretch=False)

        self.listaCli_clientes.place(relwidth=1, relheight=1)

        # O bind é para avisar que a qualquer momento que tiver interação com a lista chama uma função
        # self.listaCli_clientes.bind("<Double-1>", self.OnDoubleClick) ##################

        # Inserindo dados na tree
        self.dados_cli = Cruds().select_dados_clientes()['todos_dados_clientes']
        for cada_dado in self.dados_cli:
            self.listaCli_clientes.insert('', 'end', values=cada_dado)

        self.scrooLista = ttk.Scrollbar(self.frame_treeViewCliente)
        self.scrooLista.place(relx=0.985, y=31, relheight=0.95, width=20)
        self.listaCli_clientes.configure(yscrollcommand=self.scrooLista.set)
        self.scrooLista.config(command=self.listaCli_clientes.yview)
        self.listaCli_clientes.bind("<ButtonRelease-1>", lambda evento: [self.aparecerBotãoEditarJanPrincipal("<ButtonRelease-1>"),
                                                                         self.aparecerBotãoComprasJanPrincipal("<ButtonRelease-1>")])
        self.listaCli_clientes.bind("<Double-Button-1>", lambda evento: self.venda())

        # Sumindo com os botões de add cliente e mostra as vendas
        self.botãoEdiçãoDeCliente.grid_forget()
        self.botãoComprasDeCliente.grid_forget()

    def treeView_Produtos(self):
        # Construindo a treeview
        style = ttk.Style()
        style.theme_use("default")
        # Estilizando a Treeview
        style.configure("Treeview", background=preto_claro, fieldbackground=preto_claro, foreground='white',
                        font='arial, 15', rowheight=30, )
        style.map('Treeview', background=[('selected', 'green')])

        # Estilizando os Cabeçalhos
        style.configure('Heading', font='arial, 15', background=preto_claro, foreground='white')

        self.listaCli_preços = ttk.Treeview(self.exibirPreços_frame, height=3, columns=('Produto', 'Preço', 'Data'))
        self.listaCli_preços.heading("#0", text="")
        self.listaCli_preços.heading("#1", text="Produto")
        self.listaCli_preços.heading("#2", text="Preço")
        self.listaCli_preços.heading("#3", text="Data")

        # Definindo tamanho das Colunas
        self.listaCli_preços.column("#0", width=0, stretch=False)
        self.listaCli_preços.column("#1", width=168, anchor='c', stretch=True)
        self.listaCli_preços.column("#2", width=90, anchor='c', stretch=False)
        self.listaCli_preços.column("#3", width=118, anchor='c', stretch=False)

        # listaCli_clientes.bind("<ButtonRelease-1>", self.printar)
        self.seleçãoDosPreços = self.listaCli_preços.selection()
        self.listaCli_preços.bind("<Double-Button-1>", self.chamarJanelaAttPreço)
        self.listaCli_preços.place(relwidth=1, relheight=1)

        # Inserindo dados na tree
        self.select_dados_produtos()
        dados = self.todos_dados_produtos
        for cada_dado in dados:
            lista = cada_dado[1]
            saida = eval(lista)
            produto = cada_dado[0]
            preço = saida[0][0]
            data = saida[0][1]
            linha = [produto, preço, data]
            self.listaCli_preços.insert('', 'end', values=linha)
            self.nomes_de_produtos_cadastrados.append(produto)

    def treeView_venda(self, janela):
        # Construindo a treeview

        self.dados_da_venda = ttk.Treeview(master=janela, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.dados_da_venda.heading("#0", text="")
        self.dados_da_venda.heading("#1", text="Qt")
        self.dados_da_venda.heading("#2", text="Produto")
        self.dados_da_venda.heading("#3", text="Unidade")
        self.dados_da_venda.heading("#4", text="Total")

        # Definindo tamanho das Colunas
        self.dados_da_venda.column("#0", width=0, stretch=False)
        self.dados_da_venda.column("#1", width=45, anchor='c', stretch=False)
        self.dados_da_venda.column("#2", width=172, anchor='c')
        self.dados_da_venda.column("#3", width=80, anchor='c', stretch=False)
        self.dados_da_venda.column("#4", width=100, anchor='c', stretch=False)

        self.dados_da_venda.place(relwidth=1, relheight=1)
        self.dados_da_venda.bind("<Delete>", self.selecionadoNaTreeVenda)

        # Inserindo dados na tree
        for cada_dado in self.list_tree_vendas:
            linha = cada_dado
            self.dados_da_venda.insert('', 'end', values=linha)

    def treeView_ComprasEfetuadas(self, janela):
        # Construindo a treeview
        self.dadosDasComprasEfetuadas = ttk.Treeview(master=janela, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.dadosDasComprasEfetuadas.heading("#0", text="")
        self.dadosDasComprasEfetuadas.heading("#1", text="Data")
        self.dadosDasComprasEfetuadas.heading("#2", text="Valor")
        self.dadosDasComprasEfetuadas.heading("#3", text="Pgto")
        self.dadosDasComprasEfetuadas.heading("#4", text="Baixa")
        self.dadosDasComprasEfetuadas.heading("#5", text="Observação")

        # Definindo tamanho das Colunas
        self.dadosDasComprasEfetuadas.column("#0", width=0, stretch=False)
        self.dadosDasComprasEfetuadas.column("#1", width=110, anchor='c', stretch=False)
        self.dadosDasComprasEfetuadas.column("#2", width=90, anchor='c', stretch=False)
        self.dadosDasComprasEfetuadas.column("#3", width=80, anchor='c', stretch=False)
        self.dadosDasComprasEfetuadas.column("#4", width=110, anchor='c', stretch=False)
        self.dadosDasComprasEfetuadas.column("#5", width=100, anchor='w')

        self.dadosDasComprasEfetuadas.place(relwidth=1, relheight=1)

        # Inserindo dados na tree
        for cada_dado in self.comprasDoClienteSelecionado()[0]:
            linha = cada_dado
            self.dadosDasComprasEfetuadas.insert('', 'end', values=linha)
