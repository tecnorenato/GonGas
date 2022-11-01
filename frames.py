import tkinter as tk
from imagens import *
from tkinter import ttk
from cores import *
from placeHolders import *
from treeviews import *
from widgets import *
from janelas import *
from funções import *


class FramesControladores(WidgetsCompletos, TreeViews, Images, JanelasAcessórias, Funcs):
    def __init__(self):
        super().__init__()
        self.images_base64()
        self.frameTree_venda = None
        self.imagem_addUser = None
        self.imagem_editUser = None
        self.imagem_compras = None
        self.imagem_vendas = None
        self.imagem_estoque = None
        self.imagem_attDePreços = None
        self.imagem_todosClientes = None
        self.painel_deControle = None
        self.controleTreeClientes = None
        self.frame_treeViewCliente = None
        self.frameAdc_Cliente = None
        self.addClientes_frame = None
        self.editClientes_frame = None
        self.tarjEditClientes_frame = None
        self.listaDoSelecionado = None
        self.varDoCheck = None
        self.botãoEdiçãoDeCliente = None
        self.exibirPreços_frame = None
        self.addPreços_frame = None
        self.attPreços_frame = None
        self.entry_valor_novo = None
        self.entEstoque_frame = None
        self.venda_frame = None
        self.botãoComprasDeCliente = None
        self.frameTree_compraEfetuada = None

    def frame_dosBotõesMenu(self):  # Aqui inserimos os botões que observamos na janela principal!
        self.painel_deControle = tk.Frame(self.janela_doMenu, bg=preto_claro)
        self.painel_deControle.grid(sticky='w', row=0, column=0)
        self.imagem_addUser = tk.PhotoImage(data=base64.b64decode(self.addUser))
        tk.Button(self.painel_deControle, bg=preto_claro, image=self.imagem_addUser, activebackground=verde_médio,
                  command=self.janelaAddCliente).grid(padx=5, pady=5, row=0, column=0)
        self.imagem_editUser = tk.PhotoImage(data=base64.b64decode(self.editUser))
        self.botãoEdiçãoDeCliente = tk.Button(self.painel_deControle, bg=preto_claro, image=self.imagem_editUser, activebackground=verde_médio,
                                              command=self.janelaEditCliente)
        self.imagem_compras = tk.PhotoImage(data=base64.b64decode(self.compras))
        tk.Button(self.painel_deControle, bg=preto_claro, image=self.imagem_compras, activebackground=verde_médio, command=self.entradaNoEstoque).grid(
            padx=5, pady=5, row=1, column=0)
        self.imagem_vendas = tk.PhotoImage(data=base64.b64decode(self.vendas))
        self.botãoComprasDeCliente = tk.Button(self.painel_deControle, bg=preto_claro, image=self.imagem_vendas, activebackground=verde_médio, command=self.janelaMostrarCompras)

        self.imagem_estoque = tk.PhotoImage(data=base64.b64decode(self.estoque))
        tk.Button(self.painel_deControle, bg=preto_claro, image=self.imagem_estoque, activebackground=verde_médio).grid(
            padx=5, pady=5, row=2, column=0)
        self.imagem_attDePreços = tk.PhotoImage(data=base64.b64decode(self.att_de_preço))
        tk.Button(self.painel_deControle, bg=preto_claro, image=self.imagem_attDePreços,
                  activebackground=verde_médio, command=self.janela_preço).grid(padx=5, pady=5, row=2, column=1)
        self.imagem_todosClientes = tk.PhotoImage(data=base64.b64decode(self.todos_clientes))
        tk.Button(self.painel_deControle, bg=preto_claro, image=self.imagem_todosClientes,
                  activebackground=verde_médio).grid(padx=5, pady=5)

    def frame_controleTreeClientes(self):  # Conjunto de Entrys para controlar a treeview dos clientes
        self.controleTreeClientes = tk.Frame(self.janela_doMenu, bg=preto_claro)
        self.controleTreeClientes.grid(row=1, column=0)

        self.entrada_nome_filter(self.controleTreeClientes)
        self.entry_nome_filter.bind("<FocusIn>", self.formata_nome_filter)
        self.entry_nome_filter.bind("<FocusOut>", self.formata_nome_filter)
        self.entry_nome_filter.bind("<KeyRelease>", self.formata_nome_filter)

        self.entrada_telefone_filter(self.controleTreeClientes)
        self.entry_telefone_filter.bind("<FocusIn>", self.formata_telefone_filter)
        self.entry_telefone_filter.bind("<FocusOut>", self.formata_telefone_filter)
        self.entry_telefone_filter.bind("<KeyRelease>", self.formata_telefone_filter)

        self.entrada_endereço_filter(self.controleTreeClientes)
        self.entry_endereço_filter.bind("<FocusIn>", self.formata_endereço_filter)
        self.entry_endereço_filter.bind("<FocusOut>", self.formata_endereço_filter)
        self.entry_endereço_filter.bind("<KeyRelease>", self.formata_endereço_filter)

        self.entrada_observação_filter(self.controleTreeClientes)
        self.entry_observação_filter.bind("<FocusIn>", self.formata_observação_filter)
        self.entry_observação_filter.bind("<FocusOut>", self.formata_observação_filter)
        self.entry_observação_filter.bind("<KeyRelease>", self.formata_observação_filter)

    def frame_treeClientes(self):  # Frame para acolher a TreeView dos dados dos Clientes
        self.frame_treeViewCliente = tk.Frame(self.janela_doMenu, bg=preto_claro)
        self.frame_treeViewCliente.place(x=160, y=5, relwidth=0.85, relheight=0.9)

    def frame_addClientes(self):  # Conjunto de Entrys para adcionar clientes no BD
        self.addClientes_frame = tk.Frame(self.jan_adc_cliente, bg=preto_claro)
        self.addClientes_frame.grid(row=1, column=0, padx=5, pady=5)
        self.entrada_nome_edição(self.addClientes_frame)
        self.entry_nome_edição.bind("<FocusIn>", self.formata_nome_Novo)
        self.entry_nome_edição.bind("<FocusOut>", self.formata_nome_Novo)
        self.entry_nome_edição.bind("<KeyRelease>", self.formata_nome_Novo)

        self.entrada_telefone_edição(self.addClientes_frame)
        self.entry_telefone_edição.bind("<FocusIn>", self.formata_telefone_Novo)
        self.entry_telefone_edição.bind("<FocusOut>", self.formata_telefone_Novo)
        self.entry_telefone_edição.bind("<KeyRelease>", self.formata_telefone_Novo)

        self.entrada_endereço_edição(self.addClientes_frame)
        self.entry_endereço_edição.bind("<FocusIn>", self.formata_endereço_Novo)
        self.entry_endereço_edição.bind("<FocusOut>", self.formata_endereço_Novo)
        self.entry_endereço_edição.bind("<KeyRelease>", self.formata_endereço_Novo)

        self.entrada_observação_edição(self.addClientes_frame)
        self.entry_observação_edição.bind("<FocusIn>", self.formata_observação_Novo)
        self.entry_observação_edição.bind("<FocusOut>", self.formata_observação_Novo)
        self.entry_observação_edição.bind("<KeyRelease>", self.formata_observação_Novo)

        self.botão_addClilente(self.addClientes_frame)
        self.jan_adc_cliente.bind("<KeyRelease>", self.aparecerBotãoCadastrar)

    def frame_tarjetaDeEdição(self):
        self.tarjEditClientes_frame = tk.Frame(self.jan_edit_cliente, bg=preto_claro)
        self.tarjEditClientes_frame.grid(row=0, column=0)
        frase = f'Editando {self.dados_selec_tree_clientes()[2]}, {self.dados_selec_tree_clientes()[0]}º cliente,\nregistrado em {self.dados_selec_tree_clientes()[1]}.'
        tk.Label(self.tarjEditClientes_frame, text=frase, bg=preto_claro, fg='Yellow').grid(row=0, column=0)

    def frame_editClientes(self):  # Conjunto de Entrys para adcionar clientes no BD
        self.editClientes_frame = tk.Frame(self.jan_edit_cliente, bg=preto_claro)
        self.editClientes_frame.grid(row=1, column=0, padx=5, pady=5)
        self.entrada_nome_edição(self.editClientes_frame)
        self.entry_nome_edição.bind("<FocusIn>", self.formata_nome_Edição)
        self.entry_nome_edição.bind("<FocusOut>", self.formata_nome_Edição)
        self.entry_nome_edição.bind("<KeyRelease>", self.formata_nome_Edição)
        self.entry_nome_edição.delete(0, 'end')
        self.entry_nome_edição.insert(0, self.dados_selec_tree_clientes()[2])
        self.entry_nome_edição.config(bg=verde_médio)
        self.jan_edit_cliente.after(200, lambda: self.entry_nome_edição.focus())

        self.entrada_telefone_edição(self.editClientes_frame)
        self.entry_telefone_edição.bind("<FocusIn>", self.formata_telefone_Edição)
        self.entry_telefone_edição.bind("<FocusOut>", self.formata_telefone_Edição)
        self.entry_telefone_edição.bind("<KeyRelease>", self.formata_telefone_Edição)
        self.entry_telefone_edição.delete(0, 'end')
        self.entry_telefone_edição.insert(0, self.dados_selec_tree_clientes()[3])
        self.entry_telefone_edição.config(bg=verde_médio)

        self.entrada_endereço_edição(self.editClientes_frame)
        self.entry_endereço_edição.bind("<FocusIn>", self.formata_endereço_Novo)
        self.entry_endereço_edição.bind("<FocusOut>", self.formata_endereço_Novo)
        self.entry_endereço_edição.bind("<KeyRelease>", self.formata_endereço_Novo)
        self.entry_endereço_edição.delete(0, 'end')
        self.entry_endereço_edição.insert(0, self.dados_selec_tree_clientes()[4])
        self.entry_endereço_edição.config(bg=verde_médio)

        self.entrada_observação_edição(self.editClientes_frame)
        self.entry_observação_edição.bind("<FocusIn>", self.formata_observação_Novo)
        self.entry_observação_edição.bind("<FocusOut>", self.formata_observação_Novo)
        self.entry_observação_edição.bind("<KeyRelease>", self.formata_observação_Novo)
        self.entry_observação_edição.delete(0, 'end')
        self.entry_observação_edição.insert(0, self.dados_selec_tree_clientes()[5])
        self.entry_observação_edição.config(bg=verde_médio)

        self.varDoCheck = tk.StringVar(self.editClientes_frame, 'Sim')
        self.checkBox(self.editClientes_frame, 'Caloteiro')
        self.checkContinue.grid(columnspan=2)
        if self.dados_selec_tree_clientes()[6] == 'Sim':
            self.checkContinue.select()
        else:
            self.checkContinue.deselect()
        print(f'Var do check {self.varDoCheck.get()}')

        self.botão_editClilente(self.editClientes_frame)
        self.jan_edit_cliente.bind("<KeyRelease>", self.aparecerBotãoEditarJanEdição)
        self.jan_edit_cliente.bind("<FocusIn>", self.aparecerBotãoEditarJanEdição)
        seleção = self.listaCli_clientes.selection()
        print(self.dados_selec_tree_clientes())

        if len(seleção) == 0:
            self.jan_edit_cliente.title('Erro')
            frase = f'Por favor, selecione\nao menos um cliente\npara editarmos.'
            msg = tk.Label(janela, text=frase, bg=preto_claro, fg='yellow', font=('Verdana', 15))
            msg.place(x=0, rely=0.2, relwidth=1, relheight=0.5)

    def frame_janela_preços(self):
        self.exibirPreços_frame = tk.Frame(self.janelaPreço, bg=preto_claro, width=390, height=320)
        self.exibirPreços_frame.grid(row=1, column=0, padx=5, pady=5)
        self.treeView_Produtos()
        self.botão_addProduto(self.janelaPreço)
        self.bt_para_add_produto.grid(row=2, column=0)

    def frame_janela_addProduto(self):
        self.addPreços_frame = tk.Frame(self.janelaAddProduto, bg=preto_claro)
        self.addPreços_frame.grid(row=1, column=0, padx=5, pady=5)
        self.entrada_produto_novo(self.addPreços_frame)
        self.entry_produto_novo.bind("<FocusIn>", self.formata_produto_novo)
        self.entry_produto_novo.bind("<FocusOut>", self.formata_produto_novo)
        self.entry_produto_novo.bind("<KeyRelease>", self.formata_produto_novo)
        self.entry_qt_novo.bind("<FocusIn>", self.formata_preço_novo)
        self.entry_qt_novo.bind("<FocusOut>", self.formata_preço_novo)
        self.entry_qt_novo.bind("<KeyRelease>", self.formata_preço_novo)

    def frame_janela_attPreço(self):
        self.attPreços_frame = tk.Frame(self.janelaAttPreço, bg=preto_claro, width=400)
        # n, e, s, and/or w
        self.attPreços_frame.pack()
        try:
            produto1 = str(f'Nos primordios de {self.buscaPreçosAntigos()[2][1]} era vendido por R$ {self.buscaPreçosAntigos()[2][0]}')
            produto2 = str(f'Em {self.buscaPreçosAntigos()[1][1]} custava R$ {self.buscaPreçosAntigos()[1][0]}')
            tk.Label(self.attPreços_frame, text=produto1, bg=preto_claro, fg='Yellow').grid(row=1)
            tk.Label(self.attPreços_frame, text=produto2, bg=preto_claro, fg='Yellow').grid(row=2)
        except IndexError:
            pass
        finally:
            produto3 = str(f'Desde {self.buscaPreçosAntigos()[0][1]} o preço é de R$ {self.buscaPreçosAntigos()[0][0]}')
            tk.Label(self.attPreços_frame, text=produto3, bg=preto_claro, fg='Yellow', font=('Arial', 12)).grid(row=3)

        texto = f'Qual será o novo valor de {self.valoresSelecProduto[0]}?'
        tk.Label(self.attPreços_frame, text=texto, bg=preto_claro, fg='Yellow', font=('Arial', 12)).grid(row=4, pady=10)
        self.buscaPreçosAntigos()
        self.entry_valor_novo = tk.Entry(self.attPreços_frame, bg=preto_claro, fg='Gray', font=('verdana', 12), width=8)
        self.entry_valor_novo.grid(row=5)
        self.entry_valor_novo.insert(0, 'R$')
        self.entry_valor_novo.bind("<FocusIn>", self.formata_preço_edit)
        self.entry_valor_novo.bind("<FocusOut>", self.formata_preço_edit)
        self.entry_valor_novo.bind("<KeyRelease>", self.formata_preço_edit)
        self.botão_Edit_preço(self.attPreços_frame)
        self.btEditPreço.grid_forget()

    def frame_janelaEntradaEstoque(self):
        self.entEstoque_frame = tk.Frame(self.janelaEntEstoque, background=preto_claro)
        self.entEstoque_frame.pack(pady=10)
        self.comboEscolhaProduto()

    def frame_janelaVenda(self):
        # Empacotanto os frames na janela de Venda
        venda_frame = tk.Frame(self.janelaVenda, background=preto_claro)
        venda_frame.grid(row=0, column=0, pady=10)

        # Chamando espaço para digitar nome do cliente
        frameNome = tk.Frame(venda_frame)
        frameNome.grid(row=0, column=0)
        self.nome_DeCliente(frameNome, self.bindDoNomeCliente, 'Consultando')
        self.entry_nome.delete(0, 'end')

        # Chamando espaço para colocar forma de pagamento
        framePagamento = tk.Frame(venda_frame)
        framePagamento.grid(row=0, column=1, padx=5, sticky='w')
        self.forma_dePagamento(framePagamento)
        self.comboxFormaPGTO.config(width=15)
        self.comboxFormaPGTO.bind('<<ComboboxSelected>>', self.verdeComboPgto)

        # Chamando espaço para digitar telefone do cliente
        frameTelefone = tk.Frame(venda_frame)
        frameTelefone.grid(row=1, column=0)
        self.telefone_DeCliente(frameTelefone, self.bindDoTelefoneCliente, 'Consultando')
        self.entry_telefone.delete(0, 'end')

        # Chamando espaço para digitar endereço do cliente
        frameEndereço = tk.Frame(venda_frame)
        frameEndereço.grid(row=1, column=1, padx=5)
        self.endereço_DeCliente(frameEndereço, self.bindDoEndereçoCliente, 'Consultando')
        self.entry_endereço.config(width=16)
        self.entry_endereço.delete(0, 'end')

        # Chamando espaço para digitar observação do cliente
        frameObservação = tk.Frame(venda_frame)
        frameObservação.grid(row=2, column=0, columnspan=2, sticky='w', padx=5)
        self.observação_DeCliente(frameObservação, self.bindDaObservaçãoCliente, 'Consultando')
        self.entry_observação.config(width=40)
        self.entry_observação.delete(0, 'end')

        # Criando o frame para os botões de produto
        frameBotõesDeProdutos = tk.Frame(venda_frame)
        frameBotõesDeProdutos.grid(row=3, column=0, columnspan=2, pady=10, sticky='n')
        self.botõesDeAddProduto(frameBotõesDeProdutos)

        # Chamando espaço para digitar quantidade de produtos
        frameQtdeProduto = tk.Frame(venda_frame)
        frameQtdeProduto.grid(row=4, column=0, padx=15, sticky='w', columnspan=2)
        self.quantidade_DeProduto(frameQtdeProduto, self.bindDaQuantidadeProduto)
        self.entry_qt.config(width=4)

        # Chamando espaço para escolher qual produto add
        frameComboProdutos = tk.Frame(venda_frame)
        frameComboProdutos.grid(row=4, column=0, padx=10, sticky='n', columnspan=2)
        self.escolha_deProduto(frameComboProdutos)
        self.comboxProduto.config(width=20)
        self.comboxProduto.bind('<<ComboboxSelected>>', self.verdeComboProduto)

        # Chamando o botão verde sem comando
        frameBotãoVerdinho = tk.Frame(venda_frame)
        frameBotãoVerdinho.grid(row=4, column=0, padx=50, sticky='e', columnspan=2)
        self.botãoVerde(frameBotãoVerdinho)
        self.btVerdinho.grid_forget()
        self.btVerdinho.config(command=self.colocaItemNaTreeDeComprasComBotão)

        # Chamando TreeView
        self.frameTree_venda = tk.Frame(venda_frame, width=400, height=200)
        self.frameTree_venda.grid(row=5, column=0, columnspan=2, pady=10)
        self.treeView_venda(self.frameTree_venda)

        # Chamando Total da Compra
        frameTotalDaVenda = tk.Frame(venda_frame, width=400, height=200)
        frameTotalDaVenda.grid(row=6, column=0, columnspan=2, sticky='e', padx=20)
        self.totalDaCompra(frameTotalDaVenda)

        # Botão Aperto de Mão
        frameBtApertoDeMão = tk.Frame(venda_frame, width=400, height=200)
        frameBtApertoDeMão.grid(row=7, column=0, columnspan=2, pady=10)
        self.botãoApertodeMão(frameBtApertoDeMão)
        self.btApertodeMão.config(command=self.vendaRealizada)
        self.btApertodeMão.grid_forget()

    def frame_janelaComprasEfetuada(self):
        # Empacotanto os frames na janela de Venda
        todoFrame = tk.Frame(self.janelaVenda, background=preto_claro)
        todoFrame.grid(row=0, column=0, pady=10)

        outrosDados = tk.Frame(todoFrame, width=600, height=70, bg=preto_claro)
        outrosDados.grid(row=1, column=0)

        self.dadosDaJanelaCompra(outrosDados)

        self.frameTree_compraEfetuada = tk.Frame(todoFrame, width=600, height=400)
        self.frameTree_compraEfetuada.grid(row=2, column=0, pady=10)
        self.treeView_ComprasEfetuadas(self.frameTree_compraEfetuada)
