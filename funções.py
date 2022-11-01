import tkinter
from cores import *
from widgets import WidgetsCompletos


class Funcs:
    def __init__(self):
        self.testee = WidgetsCompletos().entry_nome()
        self.valoresSelec = None
        self.valoresSelecProduto = None
        self.dict_venda = None

    def aparecerBotãoCadastrar(self, evento):
        nome = self.entry_nome_edição["bg"]
        telefone = self.entry_telefone_edição["bg"]
        endereço = self.entry_endereço_edição["bg"]
        if nome == verde_médio and telefone == verde_médio and endereço == verde_médio:
            self.bt_para_cadastrar.grid(columnspan=2, pady=15)
        else:
            self.bt_para_cadastrar.grid_forget()
        str(evento).title()

    def aparecerBotãoEditarJanEdição(self, evento):
        nome = self.entry_nome_edição["bg"]
        telefone = self.entry_telefone_edição["bg"]
        endereço = self.entry_endereço_edição["bg"]
        if nome == verde_médio and telefone == verde_médio and endereço == verde_médio:
            self.bt_para_editar.grid(columnspan=2, pady=5)
        else:
            self.bt_para_editar.grid_forget()
        str(evento).title()

    def aparecerBotãoEditarJanPrincipal(self, evento):
        try:
            if len(self.dados_selec_tree_clientes()) > 0:
                self.botãoEdiçãoDeCliente.grid(padx=5, pady=5, row=0, column=1)
            else:
                self.botãoEdiçãoDeCliente.grid_forget()
        except AttributeError:
            pass
        str(evento).title()

    def aparecerBotãoComprasJanPrincipal(self, evento):
        try:
            if len(self.dados_selec_tree_clientes()) > 0:
                self.botãoComprasDeCliente.grid(padx=5, pady=5, row=1, column=1)
            else:
                self.botãoComprasDeCliente.grid_forget()
        except AttributeError:
            pass
        str(evento).title()

    def aparecerBotãoAddProduto(self):
        produto = self.entry_produto_novo["bg"]
        quantidade = self.entry_qt_novo["bg"]
        if produto == verde_médio and quantidade == verde_médio:
            self.btAdcProduto.grid(row=2, column=3, padx=15)
        else:
            self.btAdcProduto.grid_forget()

    def dados_selec_tree_clientes(self):
        self.listaCli_clientes.selection()
        # Aqui é para selecionar os dados da tabela que der duplo clique e colocar na memória
        for n in self.listaCli_clientes.selection():
            valoresSelecTree = self.listaCli_clientes.item(n, 'values')
            ordem = valoresSelecTree[0]
            data = valoresSelecTree[1]
            nome = valoresSelecTree[2]
            telefone = valoresSelecTree[3]
            endereço = valoresSelecTree[4]
            observação = valoresSelecTree[5]
            caloteiro = valoresSelecTree[6]
            self.valoresSelec = [ordem, data, nome, telefone, endereço, observação, caloteiro]
        return self.valoresSelec

    def dados_selec_tree_produtos(self):
        self.listaCli_preços.selection()
        # Aqui é para selecionar os dados da tabela que der duplo clique e colocar na memória
        for n in self.listaCli_preços.selection():
            valoresSelecTree = self.listaCli_preços.item(n, 'values')
            produto = valoresSelecTree[0]
            preço = valoresSelecTree[1]
            data = valoresSelecTree[2]
            self.valoresSelecProduto = [produto, preço, data]
            print(self.valoresSelecProduto)
        return self.valoresSelecProduto

    def chamarJanelaAttPreço(self, evento):
        self.dados_selec_tree_produtos()
        self.attPreço()
        str(evento).title()

    def aparecerBotãoEditPreçoProduto(self):
        preço = self.entry_valor_novo["bg"]
        if preço == verde_médio:
            self.btEditPreço.grid(row=6, pady=10)
        else:
            self.btEditPreço.grid_forget()

    def aparecerBotãoAddEstoque(self):
        if fornecedor == verde_médio and quantidade == verde_médio and valor_unit == verde_médio:
            self.btAddEstoque.grid(row=3, columnspan=3, pady=15)
        else:
            self.btAddEstoque.grid_forget()

    def colocaItemNaTreeDeCompras(self, item):
        """
        Add item e quantidade na Treeveiew de vendas.
        :param item: Qual item que tem que ser add.
        :return: Nada!
        """
        preçoUnit = 0
        for valorUnit in self.select_dados_produtos():
            if valorUnit[0] == item:
                preçoUnit = f'{float(eval(valorUnit[1])[0][0]):.2f}'
        if item not in self.produtosJáComprados:
            self.list_tree_vendas.append([1, item, preçoUnit, preçoUnit])
            self.produtosJáComprados.append(item)
        elif item in self.produtosJáComprados:
            for produtos in self.list_tree_vendas:
                if produtos[1] == item:
                    qt = produtos[0]
                    del (produtos[0])
                    produtos.insert(0, qt + 1)
                    del (produtos[3])
                    preçoTotal = f'{int(qt + 1) * float(preçoUnit):.2f}'
                    produtos.insert(3, preçoTotal)
        self.treeView_venda(self.frameTree_venda)
        self.calculaTotal()
        self.mostrarBotãoApertoDeMãos('<Button>')

    def colocaItemNaTreeDeComprasComBotão(self):
        """
        Add item e quantidade na Treeveiew de vendas digitando.
        :return: Nada!
        """
        item = self.comboxProduto.get()
        try:
            quant = int(self.entry_qt.get())
        except ValueError:
            quant = 1
        preçoUnit = 0
        for valorUnit in self.select_dados_produtos():
            if valorUnit[0] == item:
                preçoUnit = f'{float(eval(valorUnit[1])[0][0]):.2f}'
        if item not in self.produtosJáComprados:
            self.list_tree_vendas.append([quant, item, preçoUnit, f'{float(preçoUnit)*int(quant):.2f}'])
            self.produtosJáComprados.append(item)
        elif item in self.produtosJáComprados:
            for produtos in self.list_tree_vendas:
                if produtos[1] == item:
                    qt = produtos[0]
                    del (produtos[0])
                    produtos.insert(0, qt + quant)
                    del (produtos[3])
                    preçoTotal = f'{int(qt + quant) * float(preçoUnit):.2f}'
                    produtos.insert(3, preçoTotal)
        self.treeView_venda(self.frameTree_venda)
        self.calculaTotal()
        self.btVerdinho.grid_forget()
        self.entry_qt.config(bg=preto_claro, fg='Gray')
        self.entry_qt.delete(0, 'end')
        self.entry_qt.insert(0, 'Qtde')
        self.comboxProduto.configure(style='T3.TCombobox')
        self.style.map('T3.TCombobox', fieldbackground=[('readonly', preto_claro)])
        self.comboxProduto['state'] = 'normal'
        self.comboxProduto.delete(0, 'end')
        self.comboxProduto.insert(0, 'Produto')
        self.comboxProduto['state'] = 'readonly'
        self.mostrarBotãoApertoDeMãos('<Button>')

    def tiraItemNaTreeDeCompras(self, item, botão):
        """
        Exclui item e quantidade na Treeveiew de vendas.
        :param botão: Não lembro o que é, mas aqui é sem efeito.
        :param item: Qual item que tem que ser add.
        :return: Nada!
        """
        preçoUnit = 0
        for valorUnit in self.select_dados_produtos():
            if valorUnit[0] == item:
                preçoUnit = f'{float(eval(valorUnit[1])[0][0]):.2f}'
        if item not in self.produtosJáComprados:
            pass
        elif item in self.produtosJáComprados:
            self.piscarVermelho(evento='<Button-3>', botão=botão)
            for produtos in self.list_tree_vendas:
                if produtos[1] == item:
                    qt = produtos[0]
                    del (produtos[0])
                    produtos.insert(0, qt - 1)
                    del (produtos[3])
                    preçoTotal = f'{int(qt - 1) * float(preçoUnit):.2f}'
                    produtos.insert(3, preçoTotal)
        for indice, venda in enumerate(self.list_tree_vendas):
            if venda[0] == 0:
                self.list_tree_vendas.pop(indice)
                self.produtosJáComprados.remove(venda[1])
                self.calculaTotal()
            if len(self.list_tree_vendas) == 0:
                self.labelTotalDaCompra.config(text=f'Total: 0.00')
        self.calculaTotal()
        self.treeView_venda(self.frameTree_venda)

    def calculaTotal(self):
        """
        Funçao para calcular o valor total de toda compra.
        :return: Valor total da compra
        """
        total = 0
        for valorTotal in self.list_tree_vendas:
            tot = float(valorTotal[3])
            total += tot
            self.labelTotalDaCompra.config(text=f'Total: {total:.2f}')
        return f'{total:.2f}'

    def selecionadoNaTreeVenda(self, evento):
        """
        Captura os dados selecionados na TreeView de Venda.
        :param evento: Simplesmente o evento que o acionou
        :return: Nada
        """
        produto = ''
        for n in self.dados_da_venda.selection():
            valoresSelecTree = self.dados_da_venda.item(n, 'values')
            produto = valoresSelecTree[1]
        for indice, linhas in enumerate(self.list_tree_vendas):
            if linhas[1] == produto:
                self.produtosJáComprados.remove(produto)
                del (self.list_tree_vendas[indice])
        self.treeView_venda(self.frameTree_venda)
        self.calculaTotal()
        self.mostrarBotãoApertoDeMãos('<Button>')
        str(evento).title()

    def piscarVermelho(self, evento, botão):
        """
        Faz o botão piscar vermelho quando clica com algum botão.
        :param evento: evento que chamou a função.
        :param botão: qual botão chamou a função.
        :return: NADA!
        """
        botão.configure(background=vermelho_salmão)
        self.janelaVenda.after(100, lambda: botão.configure(background=preto_claro))
        # Blink red when right click
        str(evento).title()

    def mostrarBotãoApertoDeMãos(self, evento):
        if self.comboxFormaPGTO.get() != 'Pagamento' and len(self.list_tree_vendas) > 0:
            self.btApertodeMão.grid(row=0, column=0)
        else:
            self.btApertodeMão.grid_forget()
        str(evento).title()

    def vendaRealizada(self):
        # Armazenando a compras no BD Clientes.
        totalGeral = 0
        try:
            compras = eval(self.busca_Cliente(self.dados_selec_tree_clientes()[2])[0][7])
        except TypeError:
            compras = []
        except SyntaxError:
            compras = []
        if self.comboxFormaPGTO.get() == 'Fiado':
            dataDoPagamento = 'Aberto'
        else:
            dataDoPagamento = self.data_de_hoje()
        self.dict_venda = {'data da compra': self.data_de_hoje(), 'lista de compras': self.list_tree_vendas, 'pagamento': self.comboxFormaPGTO.get(),
                           'total': self.calculaTotal(), 'observação': self.entry_observação.get(), 'data do pagamento': dataDoPagamento}
        print(f'Dict Venda: {self.dict_venda}')
        print(f'Nome: {self.dados_selec_tree_clientes()[2]}')
        compras.insert(0, self.dict_venda)
        print(f'{"=-"*30}')
        for cada_compra in compras:
            totalGeral += float(cada_compra['total'])
        self.add_compra_noBDClientes(self.dados_selec_tree_clientes()[2], str(compras), f'{totalGeral:.2f}')

        # Enviando as informaçãoes para tabela de estoque para controlar quantidade.
        print(f'{"=-"*30}')
        tudo = eval(self.busca_Cliente(self.dados_selec_tree_clientes()[2])[0][7])
        itens_comprados_agora = tudo[0]['lista de compras']
        print(itens_comprados_agora)
        for item in itens_comprados_agora:
            qt = item[0]
            produto = item[1]
            vl_unit = item[2]
            vl_total = item[3]
            envolvido = self.dados_selec_tree_clientes()[2]
            direção = 'Saída'
            self.add_registro_estoque_BD_entrada(produto, qt, vl_unit, vl_total, envolvido, direção)
        self.treeview_clientes()

    def comprasDoClienteSelecionado(self):
        compras = eval(str(self.busca_Compras()))[0][0]
        total = eval(str(self.busca_Compras()))[0][1]
        todasCompras = eval(compras)
        listaComTodasCompras = []
        for cadaRegistro in todasCompras:
            dataCompra = cadaRegistro['data da compra']
            listaDeCompras = cadaRegistro['lista de compras']
            pagamento = cadaRegistro['pagamento']
            valor = cadaRegistro['total']
            obs = cadaRegistro['observação']
            dataPagamento = cadaRegistro['data do pagamento']
            linha = [dataCompra, valor, pagamento, dataPagamento, obs]
            listaComTodasCompras.append(linha)
        return listaComTodasCompras, total

