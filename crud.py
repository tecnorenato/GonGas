from datetime import date
import sqlite3
from operator import itemgetter, attrgetter
from cores import *


class Cruds:
    def __init__(self):
        self.data = None
        self.autocompletarBairros = None
        self.novaLista = list()
        self.listaClientesFiltrado = None
        self.teste = None
        self.validação_cliente = None
        self.conn = None
        self.cursor = None
        self.nome = None
        self.telefone = None
        self.endereço = None
        self.observação = None
        self.valoresSelec = None
        self.caloteiro = None
        self.todos_dados_clientes = list()
        self.todos_dados_produtos = list()
        self.nomeDeClientesParaEdição = None
        self.telefoneDeClientesParaEdição = None
        self.nomeDoEditado = None

    @staticmethod
    def data_de_hoje():
        data_inglês = str(f'{date.today()}')
        ano = data_inglês[:4]
        mês = data_inglês[5:7]
        dia = data_inglês[8:]
        data = str(f'{dia}/{mês}/{ano}')
        return data

    def limpa_tela(self):
        self.nome_entry.delete(0, 'end')
        self.telefone_entry.delete(0, 'end')
        self.endereço_entry.delete(0, 'end')
        self.observação_entry.delete(0, 'end')

    # Operações com BD
    def conecta_bd(self):
        self.conn = sqlite3.connect('clientes.db')
        self.cursor = self.conn.cursor()
        print('Conectando ao Banco de dados.')

    def desconecta_bd(self):
        self.conn.close()
        print('Desconectando do Banco de dados.')

    def montaTabelas(self):
        self.conecta_bd()
        # Criando a tabela clientes no banco de dados
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                ord INTEGER PRIMARY KEY,
                data DATE,
                nome CHAR(40) NOT NULL,
                telefone INTEGER(20),
                endereço CHAR(40),
                observação CHAR(40),
                caloteiro CHAR(10),
                compras BLOB,
                total FLOAT
            );
        """)

        # Criando a tabela Entradas de Estoque no banco de dados
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS estoque (
                        data DATE,
                        produto CHAR(40) NOT NULL,
                        qt INTEGER,
                        vl_unit FLOAT,
                        vl_total FLOAT,
                        envolvido CHAR(40),
                        direção CHAR(15)
                    );
                """)

        # Criando a tabela preço no banco de dados
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS preço (
                                produto CHAR(40) NOT NULL,
                                venda CHAR
                            );
                        """)

        # Criando a tabela movimentação financeira no banco de dados
        self.cursor.execute("""
                                    CREATE TABLE IF NOT EXISTS mov_finan (
                                        data DATE,
                                        valor FLOAT,                                        
                                        motivo CHAR(40) NOT NULL,
                                        observação CHAR
                                    );
                                """)
        self.conn.commit()

        print('Registro criado com sucesso!')
        self.desconecta_bd()

    def variaveis(self):
        self.data = self.data_de_hoje()
        self.nome = str(self.entry_nome_edição.get()).title()
        self.telefone = self.entry_telefone_edição.get()
        self.endereço = str(self.entry_endereço_edição.get()).title()
        self.observação = str(self.entry_observação_edição.get()).capitalize()
        self.caloteiro = str(self.varDoCheck.get())
        if self.observação in ['Observação', 'Nenhuma observação']:
            self.observação = ''

    def add_cliente_noBDClientes(self):
        obs = self.entry_observação_edição.get()
        if self.entry_observação_edição.get() in ['Observação', 'Nenhuma Observação']:
            obs = ''
        self.conecta_bd()
        self.cursor.execute("""
        INSERT INTO clientes (data, nome, telefone, endereço, observação, caloteiro)
        VALUES (?, ?, ?, ?, ?, ?)""",
                            (self.data_de_hoje(),
                             str(self.entry_nome_edição.get()).title(),
                             self.entry_telefone_edição.get(),
                             str(self.entry_endereço_edição.get()).title(),
                             obs,
                             'Nunca'))
        self.conn.commit()
        self.desconecta_bd()
        self.treeview_clientes()
        self.jan_adc_cliente.destroy()

    def add_preço_produto_BD_preço(self):
        self.conecta_bd()
        produto = self.entry_produto_novo.get()
        preço = self.entry_qt_novo.get()
        data = self.data_de_hoje()
        venda = f"{[[preço, data]]}"
        print(self.todos_dados_produtos)
        print(venda)

        self.cursor.execute("""
        INSERT INTO preço (produto, venda)
        VALUES (?, ?)""",
                            (produto, venda))
        self.conn.commit()
        self.desconecta_bd()
        self.frame_janela_preços()
        self.janelaAddProduto.destroy()

    def add_registro_estoque_BD_entrada(self, produto, quantidade, valor_unitário, valor_total, envolvido, direção):
        """
        Cria um registro na tabela estoque para auditar a quantidade de produtos.
        :param produto: Qual produto está sendo registrado.
        :param quantidade: Qual quantidade do produto.
        :param valor_unitário: Preço unitário.
        :param valor_total: Preço total.
        :param envolvido: Fornecedor ou comprador.
        :param direção: Entrada ou saida de produtos.
        :return: Nada
        """
        # Para gravar os dados na tabela Estoque
        self.conecta_bd()
        data = self.data_de_hoje()

        self.cursor.execute("""
        INSERT INTO estoque (data, produto, qt, vl_unit, vl_total, envolvido, direção)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
                            (data, produto, quantidade, valor_unitário, valor_total, envolvido, direção))
        self.conn.commit()
        self.desconecta_bd()

    def select_dados_produtos(self):
        self.conecta_bd()
        self.cursor.execute(""" SELECT produto, venda FROM preço
                    ORDER BY produto ASC; """)
        self.todos_dados_produtos = self.cursor.fetchall()
        return self.todos_dados_produtos

    def select_nomes_produtos(self):
        self.conecta_bd()
        self.cursor.execute(""" SELECT produto FROM preço
                    ORDER BY produto ASC; """)
        nomes_produtos = self.cursor.fetchall()
        lista_de_nomes_de_produtos = []
        for produtos in nomes_produtos:
            lista_de_nomes_de_produtos.append(produtos[0])
        return lista_de_nomes_de_produtos

    def cadastrar_produto(self):
        self.add_preço_produto_BD_preço()
        self.treeView_Produtos()
        self.janelaAddProduto.destroy()

    def limpa_listas(self):
        self.todos_dados_clientes.clear()

    def busca_Cliente(self, campoGetNome):
        self.conecta_bd()
        self.listaCli_clientes.delete(*self.listaCli_clientes.get_children())  # Esse comando limpa a lista

        # self.entry_nome.insert(0, 'end')
        try:
            nome = campoGetNome.get().title()
        except AttributeError:
            nome = campoGetNome.title()
        self.cursor.execute(
            f""" SELECT ord, data, nome, telefone, endereço, observação, caloteiro, compras, total FROM clientes
            WHERE nome LIKE '%{nome}%' """)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli_clientes.insert('', 'end', values=i)
        self.desconecta_bd()
        return buscanomeCli

    def busca_Endereço(self, campoGetEndereço):
        self.conecta_bd()
        self.listaCli_clientes.delete(*self.listaCli_clientes.get_children())  # Esse comando limpa a lista

        # self.entry_nome.insert(0, 'end')  # Não precisou disso aqui, f String é mais eficiente
        endereço = campoGetEndereço.title()
        self.cursor.execute(
            f""" SELECT ord, data, nome, telefone, endereço, observação, caloteiro FROM clientes
            WHERE endereço LIKE '%{endereço}%' """)
        buscaendereçoCli = self.cursor.fetchall()
        for i in buscaendereçoCli:
            self.listaCli_clientes.insert('', 'end', values=i)
        self.desconecta_bd()
        return buscaendereçoCli

    def busca_Telefone(self, campoGetTelefone):
        self.conecta_bd()
        self.listaCli_clientes.delete(*self.listaCli_clientes.get_children())  # Esse comando limpa a lista

        # self.entry_nome.insert(0, 'end')  # Não precisou disso aqui, f String é mais eficiente
        self.cursor.execute(
            f""" SELECT ord, data, nome, telefone, endereço, observação, caloteiro FROM clientes
                    WHERE telefone LIKE '%{campoGetTelefone}%' """)
        buscatelefoneCli = self.cursor.fetchall()
        for i in buscatelefoneCli:
            self.listaCli_clientes.insert('', 'end', values=i)
        self.desconecta_bd()
        return buscatelefoneCli

    def busca_Observação(self, campoObservaçãoGet):
        self.conecta_bd()
        self.listaCli_clientes.delete(*self.listaCli_clientes.get_children())  # Esse comando limpa a lista

        # self.entry_nome.insert(0, 'end')  # Não precisou disso aqui, f String é mais eficiente
        observação = campoObservaçãoGet.title()
        self.cursor.execute(
            f""" SELECT ord, data, nome, telefone, endereço, observação, caloteiro FROM clientes
                            WHERE observação LIKE '%{observação}%' """)
        buscaobservaçãoCli = self.cursor.fetchall()
        for i in buscaobservaçãoCli:
            self.listaCli_clientes.insert('', 'end', values=i)
        return buscaobservaçãoCli

    def busca_Compras(self):
        self.conecta_bd()
        nome = self.dados_selec_tree_clientes()[2]
        # self.dadosDasComprasEfetuadas.delete(*self.dadosDasComprasEfetuadas.get_children())  # Esse comando limpa a lista

        # self.entry_nome.insert(0, 'end')  # Não precisou disso aqui, f String é mais eficiente
        self.cursor.execute(
            f""" SELECT compras, total FROM clientes WHERE nome LIKE '{nome}' """)
        buscaCompras = self.cursor.fetchall()
        return buscaCompras

    def select_dados_clientes(self):
        # self.limpa_listas()
        # Classificando todos os clientes em ordem Crescente
        self.conecta_bd()
        self.cursor.execute(""" SELECT ord, data, nome, telefone, endereço, observação, caloteiro, compras FROM clientes
            ORDER BY total DESC; """)
        self.todos_dados_clientes = self.cursor.fetchall()

        # Aqui printamos todos os dados not terminal.
        """print(f'{"Cod":^4}{"Data":^13}{"Nome":^15}{"Telefone":^12}{"Endereço":^21}{"Observação":^15}{"Calote":^13}{"Compras":^13}')
        for indice, dado in enumerate(self.todos_dados_clientes):
            cada_dado = f'{dado[0]:^4}{dado[1]:^13}{dado[2]:<15}{dado[3]:^12}{dado[4]:^21}{dado[5]:^15}{dado[6]:^13}{str(dado[7]):^13}'
            print(cada_dado)"""
        self.desconecta_bd()
        # Agora providencio uma lista de bairros para autocompletar os bairros.
        lista_bairros = []
        bairro_qt = []
        nomes_clientes = []
        telefone_clientes = []
        bairro_qt.clear()
        contador = 1
        for cada_cliente in self.todos_dados_clientes:
            nomes_clientes.append(cada_cliente[2])  # Adcionando cada cliente na lista para validação
            telefone_clientes.append(cada_cliente[3])  # Adcionando cada telefone para uma lista de validação
            bairro_em_questão = cada_cliente[4]  # Colocando cada bairro na lista
            if bairro_em_questão not in lista_bairros:
                lista_bairros.append(bairro_em_questão)
                bairro_qt.append([bairro_em_questão, contador])
            else:
                for indice, nome_bairro in enumerate(bairro_qt):
                    if nome_bairro[0] == bairro_em_questão:
                        contador = nome_bairro[1]
                        contador += 1
                        del nome_bairro[1]
                        nome_bairro.append(contador)
                        contador = 1
        bairro_qt = sorted(bairro_qt, key=itemgetter(1), reverse=True)
        autocomp_bairros = []

        for bairro in bairro_qt:
            autocomp_bairros.append(bairro[0])

        self.autocompletarBairros = autocomp_bairros
        dicionario = {'todos_dados_clientes': self.todos_dados_clientes, 'bairros': autocomp_bairros,
                      'nomes_de_clientes': nomes_clientes, 'telefone_de_clientes': telefone_clientes}

        return dicionario

    def busca_ClienteEditarDados(self):
        self.nomeDeClientesParaEdição = list()
        self.telefoneDeClientesParaEdição = list()
        self.conecta_bd()
        self.listaCli_clientes.delete(*self.listaCli_clientes.get_children())  # Esse comando limpa a lista

        ##### Aqui faço uma mágica para o nome que está sendo editado desaparecer da treeview
        ### Sendo assim, quando editarem um cadastro o bg nome da pessoa não ficará vermelho
        self.nomeDoEditado = self.valoresSelec[2]
        self.cursor.execute(
            f""" SELECT ord, nome, data,telefone, endereço, observação, caloteiro FROM clientes
            WHERE nome NOT LIKE '{self.nomeDoEditado}%' """)
        buscanomeCli = self.cursor.fetchall()
        # print(self.buscanomeCli)
        for i in buscanomeCli:
            self.listaCli_clientes.insert('', 'end', values=i)
            self.nomeDeClientesParaEdição.append(i[1])
            self.telefoneDeClientesParaEdição.append(i[3])
        self.desconecta_bd()
        return buscanomeCli

    def altera_cliente(self):
        self.conecta_bd()
        self.caloteiro = str(self.varDoCheck.get())
        print(f'É caloteiro? {self.caloteiro}')
        dado = self.dados_selec_tree_clientes()
        if self.caloteiro == 'Não' and dado[6] == 'Nunca':
            self.caloteiro = 'Nunca'
        # self.select_dados_clientes()
        self.cursor.execute("""UPDATE clientes SET nome = ?, telefone = ?, endereço = ?, observação = ?, caloteiro = ? WHERE nome = ?""",
                            (self.entry_nome_edição.get(), self.entry_telefone_edição.get(),
                             self.entry_endereço_edição.get(), self.entry_observação_edição.get(),
                             self.caloteiro, dado[2]))
        print(f'Alterou o cliente {dado[2]}')
        self.conn.commit()
        self.treeview_clientes()
        self.botãoEdiçãoDeCliente.grid_forget()
        self.jan_edit_cliente.destroy()
        self.desconecta_bd()

    def altera_preço(self):
        # Alterar preços dos produtos
        self.conecta_bd()
        produto = self.valoresSelecProduto[0]
        print(produto)
        self.cursor.execute(
            f""" SELECT venda FROM preço
                            WHERE produto LIKE '{produto}' """)
        preçoDosProdutos = self.cursor.fetchall()
        lista_de_preços = eval(str(preçoDosProdutos[0][0]))
        preço_data_add = [self.entry_valor_novo.get(), self.data_de_hoje()]
        lista_de_preços.insert(0, preço_data_add)

        self.cursor.execute("""UPDATE preço SET venda = ? WHERE produto = ?""", (str(lista_de_preços), self.valoresSelecProduto[0]))
        self.conn.commit()
        self.desconecta_bd()
        self.treeView_Produtos()
        self.janelaAttPreço.destroy()

    def buscaPreçosAntigos(self):
        produto = self.valoresSelecProduto[0]
        self.conecta_bd()
        self.cursor.execute(
            f""" SELECT venda FROM preço
                    WHERE produto LIKE '{produto}' """)
        preçoDosProdutos = self.cursor.fetchall()
        lista = eval(preçoDosProdutos[0][0])
        self.desconecta_bd()
        return lista

    def add_estoque_noBDEstoque(self):
        self.conecta_bd()
        self.cursor.execute("""
        INSERT INTO estoque (data, produto, qt, vl_unit, vl_total, envolvido, direção)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
                            (self.data_de_hoje(),
                             self.comboProdutos.get(),
                             self.entryqt.get(),
                             self.valor_unit.get(),
                             self.valor_total.get(),
                             self.entryfornecedor.get(),
                             'Entrada'))
        self.conn.commit()
        self.desconecta_bd()
        self.janelaEntEstoque.destroy()

    def add_compra_noBDClientes(self, nome, compra, total):
        """
        Insere as compras no banco de dados clientes
        :param nome: Nome do cidadão que irá ser adcionado as compras
        :param compra: o que foi comprado
        :param total: valor total de todas as compras
        :return: Nada
        """
        self.conecta_bd()
        self.cursor.execute(
            """UPDATE clientes SET compras = ?, total = ? WHERE nome = ?""", (compra, total, nome))
        self.conn.commit()
        self.desconecta_bd()
        self.treeview_clientes()
        self.janelaVenda.destroy()
        self.list_tree_vendas.clear()
