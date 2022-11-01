from cores import *
from crud import *


class PlaceTudo(Cruds):
    def __init__(self):
        super().__init__()
        self.dados_cli = None

    def formata_nome_filter(self, evento):
        ação = str(evento).split()[0]
        match ação:
            case '<FocusIn':
                if self.entry_nome_filter.get() in ['', 'Nome']:
                    self.entry_nome_filter.delete(0, 'end')
                    self.entry_nome_filter.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entry_nome_filter.get() in ['', 'Nome']:
                    self.entry_nome_filter.config(bg=preto_claro, fg='Gray')
                    self.entry_nome_filter.insert(0, 'Nome')
            case '<KeyRelease':
                if evento.keysym in ['Left', 'Right']:
                    return
                else:
                    digitado = str(self.entry_nome_filter.get()).title()
                    self.entry_nome_filter.delete(0, 'end')
                    self.entry_nome_filter.insert(0, digitado)
                    self.dados_cli = self.busca_Cliente(self.entry_nome_filter)

        print(evento)

    def formata_telefone_filter(self, evento):
        ação = str(evento).split()[0]
        match ação:
            case '<FocusIn':
                if self.entry_telefone_filter.get() in ['', 'Telefone']:
                    self.entry_telefone_filter.delete(0, 'end')
                    self.entry_telefone_filter.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entry_telefone_filter.get() in ['', 'Telefone']:
                    self.entry_telefone_filter.config(bg=preto_claro, fg='Gray')
                    self.entry_telefone_filter.insert(0, 'Telefone')
            case '<KeyRelease':
                numtel = self.entry_telefone_filter.get().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")[
                         :11]
                telformat = ""

                if evento.keysym.lower() in ["left", "right", "backspace"]:
                    self.dados_cli = self.busca_Telefone(self.entry_telefone_filter.get())
                    return
                if len(numtel) == 11:
                    self.entry_telefone_filter.config(bg=branco_gelo, fg=preto_claro)
                elif len(numtel) < 11:
                    self.entry_telefone_filter.config(bg='white', fg=preto_claro)

                for index in range(len(numtel)):

                    if not numtel[index] in "0123456789":
                        continue
                    if index == 0:
                        telformat += "(" + numtel[index]
                    elif index == 1:
                        telformat += numtel[index] + ") "

                    elif index == 6:
                        telformat += numtel[index] + "-"
                    else:
                        telformat += numtel[index]

                self.entry_telefone_filter.delete(0, "end")
                self.entry_telefone_filter.insert(0, telformat)
                self.dados_cli = self.busca_Telefone(self.entry_telefone_filter.get())
        print(evento)

    def formata_endereço_filter(self, evento):
        ação = str(evento).split()[0]
        match ação:
            case '<FocusIn':
                if self.entry_endereço_filter.get() in ['', 'Endereço']:
                    self.entry_endereço_filter.delete(0, 'end')
                    self.entry_endereço_filter.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entry_endereço_filter.get() in ['', 'Endereço']:
                    self.entry_endereço_filter.config(bg=preto_claro, fg='Gray')
                    self.entry_endereço_filter.insert(0, 'Endereço')
            case '<KeyRelease':
                if evento.keysym in ['Left', 'Right', "Multi_key"]:
                    return
                else:
                    digitado = str(self.entry_endereço_filter.get()).title()
                    self.entry_endereço_filter.delete(0, 'end')
                    self.entry_endereço_filter.insert(0, digitado)
                    self.autocompBairros(evento, self.entry_endereço_filter)
                    self.dados_cli = self.busca_Endereço(self.entry_endereço_filter.get())
        print(evento)

    @staticmethod
    def autocompBairros(evento, campoEndereço):
        end_procurado = str(campoEndereço.get()).title()
        qt_caracteres = len(end_procurado)
        opções = list()
        if not str(evento.char).isalpha():
            pass
        else:
            try:
                endereços = Cruds().select_dados_clientes()['bairros']
                for bairro in endereços:
                    if bairro.title().startswith(end_procurado):
                        opções.append(bairro)
            finally:
                if len(opções) > 0:
                    campoEndereço.delete(0, 'end')
                    campoEndereço.insert(0, opções[0])
                    campoEndereço.select_range(qt_caracteres, 'end')
                else:
                    campoEndereço.delete(0, 'end')
                    campoEndereço.insert(0, end_procurado)

    def formata_observação_filter(self, evento):
        ação = str(evento).split()[0]
        match ação:
            case '<FocusIn':
                if self.entry_observação_filter.get() in ['', 'Observação']:
                    self.entry_observação_filter.delete(0, 'end')
                    self.entry_observação_filter.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entry_observação_filter.get() in ['', 'Observação']:
                    self.entry_observação_filter.config(bg=preto_claro, fg='Gray')
                    self.entry_observação_filter.insert(0, 'Observação')
            case '<KeyRelease':
                if evento.keysym in ['Left', 'Right']:
                    return
                else:
                    digitado = str(self.entry_observação_filter.get()).capitalize()
                    self.entry_observação_filter.delete(0, 'end')
                    self.entry_observação_filter.insert(0, digitado)
                    self.dados_cli = self.busca_Observação(self.entry_observação_filter.get())
        print(evento)

    def formata_nome_Novo(self, evento):
        ação = str(evento).split()[0]
        match ação:
            case '<FocusIn':
                if self.entry_nome_edição.get() in ['', 'Nome']:
                    self.entry_nome_edição.delete(0, 'end')
                    self.entry_nome_edição.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entry_nome_edição.get() in ['', 'Nome']:
                    self.entry_nome_edição.config(bg=preto_claro, fg='Gray')
                    self.entry_nome_edição.insert(0, 'Nome')
            case '<KeyRelease':
                if evento.keysym in ['Left', 'Right']:
                    return
                else:
                    self.dados_cli = self.busca_Cliente(self.entry_nome_edição)
                    lista_de_clientes = self.select_dados_clientes()['nomes_de_clientes']
                    digitado = str(self.entry_nome_edição.get()).title()
                    self.entry_nome_edição.delete(0, 'end')
                    self.entry_nome_edição.insert(0, digitado)
                    if len(digitado) < 3:
                        self.entry_nome_edição.config(bg=branco_gelo, fg=preto_claro)
                    elif digitado in lista_de_clientes:
                        self.entry_nome_edição.config(bg=vermelho_salmão, fg=preto_claro)
                    else:
                        self.entry_nome_edição.config(bg=verde_médio, fg=preto_claro)

        print(evento)

    def formata_telefone_Novo(self, evento):
        ação = str(evento).split()[0]
        numtel = self.entry_telefone_edição.get().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")[:11]
        match ação:
            case '<FocusIn':
                if self.entry_telefone_edição.get() in ['', 'Telefone']:
                    self.entry_telefone_edição.delete(0, 'end')
                    self.entry_telefone_edição.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entry_telefone_edição.get() in ['', 'Telefone']:
                    self.entry_telefone_edição.config(bg=preto_claro, fg='Gray')
                    self.entry_telefone_edição.insert(0, 'Telefone')
                elif len(numtel) != 11:
                    self.entry_telefone_edição.config(bg=vermelho_salmão, fg='Gray')
            case '<KeyRelease':
                telformat = ""
                self.dados_cli = self.busca_Telefone(self.entry_telefone_edição.get())

                if evento.keysym.lower() in ["backspace"]:
                    self.entry_telefone_edição.config(bg=vermelho_salmão, fg='Gray')
                    return
                elif evento.keysym.lower() in ["left", "right"]:
                    return
                elif self.entry_telefone_edição.get() in self.select_dados_clientes()['telefone_de_clientes']:
                    self.entry_telefone_edição.config(bg=vermelho_salmão, fg='Gray')
                elif len(numtel) == 11:
                    self.entry_telefone_edição.config(bg=verde_médio, fg=preto_claro)
                elif len(numtel) < 11:
                    self.entry_telefone_edição.config(bg='white', fg=preto_claro)

                for index in range(len(numtel)):

                    if not numtel[index] in "0123456789":
                        continue
                    if index == 0:
                        telformat += "(" + numtel[index]
                    elif index == 1:
                        telformat += numtel[index] + ") "

                    elif index == 6:
                        telformat += numtel[index] + "-"
                    else:
                        telformat += numtel[index]

                self.entry_telefone_edição.delete(0, "end")
                self.entry_telefone_edição.insert(0, telformat)
        print(evento)

    def formata_endereço_Novo(self, evento):
        ação = str(evento).split()[0]
        match ação:
            case '<FocusIn':
                if self.entry_endereço_edição.get() in ['', 'Endereço']:
                    self.entry_endereço_edição.delete(0, 'end')
                    self.entry_endereço_edição.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entry_endereço_edição.get() in ['', 'Endereço']:
                    self.entry_endereço_edição.config(bg=preto_claro, fg='Gray')
                    self.entry_endereço_edição.insert(0, 'Endereço')
            case '<KeyRelease':
                if evento.keysym in ['Left', 'Right', "Multi_key"]:
                    return
                else:
                    digitado = str(self.entry_endereço_edição.get()).title()
                    self.entry_endereço_edição.delete(0, 'end')
                    self.entry_endereço_edição.insert(0, digitado)
                    self.autocompBairros(evento, self.entry_endereço_edição)
                    self.dados_cli = self.busca_Endereço(self.entry_endereço_edição.get())
                    if len(self.entry_endereço_edição.get()) > 3:
                        self.entry_endereço_edição.config(bg=verde_médio, fg=preto_claro)
                    else:
                        self.entry_endereço_edição.config(bg=branco_gelo, fg=preto_claro)

        print(evento)

    def formata_observação_Novo(self, evento):
        ação = str(evento).split()[0]
        match ação:
            case '<FocusIn':
                if self.entry_observação_edição.get() in ['', 'Observação', 'Nenhuma Observação']:
                    self.entry_observação_edição.delete(0, 'end')
                    self.entry_observação_edição.config(bg=verde_médio, fg=preto_claro)
            case '<FocusOut':
                if self.entry_observação_edição.get() in ['', 'Observação']:
                    self.entry_observação_edição.config(bg=verde_médio, fg=preto_claro)
                    self.entry_observação_edição.insert(0, 'Nenhuma Observação')
            case '<KeyRelease':
                if evento.keysym in ['Left', 'Right']:
                    return
                else:
                    digitado = str(self.entry_observação_edição.get()).capitalize()
                    self.entry_observação_edição.delete(0, 'end')
                    self.entry_observação_edição.insert(0, digitado)
                    self.dados_cli = self.busca_Observação(self.entry_observação_edição.get())
                    self.entry_observação_edição.config(bg=verde_médio, fg=preto_claro)
        print(evento)

    def formata_nome_Edição(self, evento):
        ação = str(evento).split()[0]
        match ação:
            case '<FocusIn':
                if self.entry_nome_edição.get() in ['', 'Nome']:
                    self.entry_nome_edição.delete(0, 'end')
                    self.entry_nome_edição.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entry_nome_edição.get() in ['', 'Nome']:
                    self.entry_nome_edição.config(bg=preto_claro, fg='Gray')
                    self.entry_nome_edição.insert(0, 'Nome')
            case '<KeyRelease':
                if evento.keysym in ['Left', 'Right']:
                    return
                else:
                    self.dados_cli = self.busca_ClienteEditarDados()
                    digitado = str(self.entry_nome_edição.get()).title()
                    self.entry_nome_edição.delete(0, 'end')
                    self.entry_nome_edição.insert(0, digitado)
                    if len(digitado) < 3:
                        self.entry_nome_edição.config(bg=branco_gelo, fg=preto_claro)
                    elif digitado in self.nomeDeClientesParaEdição:
                        self.entry_nome_edição.config(bg=vermelho_salmão, fg=preto_claro)
                    else:
                        self.entry_nome_edição.config(bg=verde_médio, fg=preto_claro)

        print(evento)

    def formata_telefone_Edição(self, evento):
        self.busca_ClienteEditarDados()
        ação = str(evento).split()[0]
        numtel = self.entry_telefone_edição.get().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")[:11]
        match ação:
            case '<FocusIn':
                if self.entry_telefone_edição.get() in ['', 'Telefone']:
                    self.entry_telefone_edição.delete(0, 'end')
                    self.entry_telefone_edição.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entry_telefone_edição.get() in ['', 'Telefone']:
                    self.entry_telefone_edição.config(bg=preto_claro, fg='Gray')
                    self.entry_telefone_edição.insert(0, 'Telefone')
                elif len(numtel) != 11:
                    self.entry_telefone_edição.config(bg=vermelho_salmão, fg='Gray')
            case '<KeyRelease':
                telformat = ""
                self.dados_cli = self.busca_Telefone(self.entry_telefone_edição.get())

                if evento.keysym.lower() in ["backspace"]:
                    self.entry_telefone_edição.config(bg=vermelho_salmão, fg='Gray')
                    return
                elif evento.keysym.lower() in ["left", "right"]:
                    return
                elif self.entry_telefone_edição.get() in self.telefoneDeClientesParaEdição:
                    self.entry_telefone_edição.config(bg=vermelho_salmão, fg='Gray')
                elif len(numtel) == 11:
                    self.entry_telefone_edição.config(bg=verde_médio, fg=preto_claro)
                elif len(numtel) < 11:
                    self.entry_telefone_edição.config(bg='white', fg=preto_claro)

                for index in range(len(numtel)):

                    if not numtel[index] in "0123456789":
                        continue
                    if index == 0:
                        telformat += "(" + numtel[index]
                    elif index == 1:
                        telformat += numtel[index] + ") "

                    elif index == 6:
                        telformat += numtel[index] + "-"
                    else:
                        telformat += numtel[index]

                self.entry_telefone_edição.delete(0, "end")
                self.entry_telefone_edição.insert(0, telformat)
        print(evento)

    def formata_produto_novo(self, evento):
        ação = str(evento).split()[0]
        match ação:
            case '<FocusIn':
                if self.entry_produto_novo.get() in ['', 'Produto']:
                    self.entry_produto_novo.delete(0, 'end')
                    self.entry_produto_novo.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entry_produto_novo.get() in ['', 'Produto']:
                    self.entry_produto_novo.config(bg=preto_claro, fg='Gray')
                    self.entry_produto_novo.insert(0, 'Produto')
            case '<KeyRelease':
                if evento.keysym in ['Left', 'Right']:
                    return
                else:
                    digitado = str(self.entry_produto_novo.get()).title()
                    self.entry_produto_novo.delete(0, 'end')
                    self.entry_produto_novo.insert(0, digitado)
                    if len(digitado) < 3:
                        self.entry_produto_novo.config(bg=branco_gelo, fg=preto_claro)
                    elif digitado in self.nomes_de_produtos_cadastrados:
                        self.entry_produto_novo.config(bg=vermelho_salmão, fg=preto_claro)
                    else:
                        self.entry_produto_novo.config(bg=verde_médio, fg=preto_claro)
        self.aparecerBotãoAddProduto()
        print(evento)

    def formata_preço_novo(self, evento):
        ação = str(evento).split()[0]
        preço = self.entry_qt_novo.get()
        qtCaracteresPreço = len(preço)
        match ação:
            case '<FocusIn':
                if self.entry_qt_novo.get() in ['', 'R$']:
                    self.entry_qt_novo.delete(0, 'end')
                    self.entry_qt_novo.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entry_qt_novo.get() in ['', 'R$']:
                    self.entry_qt_novo.config(bg=preto_claro, fg='Gray')
                    self.entry_qt_novo.insert(0, 'R$')
                elif qtCaracteresPreço < 3:
                    self.entry_qt_novo.config(bg=vermelho_salmão, fg='Gray')
            case '<KeyRelease':
                telformat = ""
                if evento.keysym.lower() in ["backspace"]:
                    self.entry_qt_novo.config(bg=vermelho_salmão, fg='Gray')
                    return
                elif evento.keysym.lower() in ["left", "right"]:
                    return
                elif len(str(preço).replace('.', '')) > 2:
                    self.entry_qt_novo.config(bg=verde_médio, fg=preto_claro)
                elif len(str(preço).replace('.', '')) < 3:
                    self.entry_qt_novo.config(bg='white', fg=preto_claro)

                for index in range(qtCaracteresPreço):

                    if not preço[index] in "0123456789":
                        continue

                    if index == qtCaracteresPreço-2:
                        telformat += "." + preço[index]

                    else:
                        telformat += preço[index]

                self.entry_qt_novo.delete(0, "end")
                self.entry_qt_novo.insert(0, telformat)
                self.aparecerBotãoAddProduto()
        print(evento)

    def formata_preço_edit(self, evento):
        ação = str(evento).split()[0]
        preço = self.entry_valor_novo.get()
        qtCaracteresPreço = len(preço)
        match ação:
            case '<FocusIn':
                if self.entry_valor_novo.get() in ['', 'R$']:
                    self.entry_valor_novo.delete(0, 'end')
                    self.entry_valor_novo.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entry_valor_novo.get() in ['', 'R$']:
                    self.entry_valor_novo.config(bg=preto_claro, fg='Gray')
                    self.entry_valor_novo.insert(0, 'R$')
                elif qtCaracteresPreço < 3:
                    self.entry_valor_novo.config(bg=vermelho_salmão, fg='Gray')
            case '<KeyRelease':
                telformat = ""
                if evento.keysym.lower() in ["backspace"]:
                    self.entry_valor_novo.config(bg=vermelho_salmão, fg='Gray')
                    return
                elif evento.keysym.lower() in ["left", "right"]:
                    return
                elif len(str(preço).replace('.', '')) > 2:
                    self.entry_valor_novo.config(bg=verde_médio, fg=preto_claro)
                elif len(str(preço).replace('.', '')) < 3:
                    self.entry_valor_novo.config(bg='white', fg=preto_claro)

                for index in range(qtCaracteresPreço):

                    if not preço[index] in "0123456789":
                        continue

                    if index == qtCaracteresPreço-2:
                        telformat += "." + preço[index]

                    else:
                        telformat += preço[index]

                self.entry_valor_novo.delete(0, "end")
                self.entry_valor_novo.insert(0, telformat)
        self.aparecerBotãoEditPreçoProduto()
        print(evento)

    def formata_preço_entrada_produto(self, evento):
        ação = str(evento).split()[0]
        preço = self.valor_unit.get()
        qtCaracteresPreço = len(preço)
        match ação:
            case '<FocusIn':
                if self.valor_unit.get() in ['', 'Unitário']:
                    self.valor_unit.delete(0, 'end')
                    self.valor_unit.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.valor_unit.get() in ['', 'Unitário']:
                    self.valor_unit.config(bg=preto_claro, fg='Gray')
                    self.valor_unit.insert(0, 'Unitário')
                elif qtCaracteresPreço < 3:
                    self.valor_unit.config(bg=vermelho_salmão, fg='Gray')
            case '<KeyRelease':
                telformat = ""
                if evento.keysym.lower() in ["backspace"]:
                    self.valor_unit.config(bg=vermelho_salmão, fg='Gray')
                    return
                elif evento.keysym.lower() in ["left", "right"]:
                    return
                elif len(str(preço).replace('.', '')) > 2:
                    self.valor_unit.config(bg=verde_médio, fg=preto_claro)
                elif len(str(preço).replace('.', '')) < 3:
                    self.valor_unit.config(bg='white', fg=preto_claro)

                for index in range(qtCaracteresPreço):

                    if not preço[index] in "0123456789":
                        continue

                    if index == qtCaracteresPreço - 2:
                        telformat += "." + preço[index]

                    else:
                        telformat += preço[index]

                self.valor_unit.delete(0, "end")
                self.valor_unit.insert(0, telformat)
                if qtCaracteresPreço > 2:
                    total = float(self.valor_unit.get()) * int(self.entryqt.get())
                    self.valor_total.delete(0, 'end')
                    self.valor_total.insert(0, f'{total:.2f}')
                    self.aparecerBotãoAddEstoque()
        print(evento)

    def formata_quantidade_entrada_produto(self, evento):
        ação = str(evento).split()[0]
        preço = self.entryqt.get()
        qtCaracteresPreço = len(preço)
        match ação:
            case '<FocusIn':
                if self.entryqt.get() in ['', 'Qt']:
                    self.entryqt.delete(0, 'end')
                    self.entryqt.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entryqt.get() in ['', 'Qt']:
                    self.entryqt.config(bg=preto_claro, fg='Gray')
                    self.entryqt.insert(0, 'Qt')
                elif qtCaracteresPreço < 1:
                    self.entryqt.config(bg=vermelho_salmão, fg='Gray')
            case '<KeyRelease':
                if evento.keysym.lower() in ["backspace"]:
                    self.entryqt.config(bg=vermelho_salmão, fg='Gray')
                    return
                elif evento.keysym.lower() in ["left", "right"]:
                    return

                for index in range(qtCaracteresPreço):

                    if not preço[index] in "0123456789":
                        continue
                    if qtCaracteresPreço > 0:
                        self.entryqt.config(bg=verde_médio, fg='Gray')
                    self.aparecerBotãoAddEstoque()
        print(evento)

    def formata_fornecedor_entrada_produto(self, evento):
        ação = str(evento).split()[0]
        match ação:
            case '<FocusIn':
                if self.entryfornecedor.get() in ['', 'Fornecedor']:
                    self.entryfornecedor.delete(0, 'end')
                    self.entryfornecedor.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if self.entryfornecedor.get() in ['', 'Fornecedor']:
                    self.entryfornecedor.config(bg=preto_claro, fg='Gray')
                    self.entryfornecedor.insert(0, 'Fornecedor')
            case '<KeyRelease':
                if evento.keysym in ['Left', 'Right']:
                    return
                else:
                    digitado = str(self.entryfornecedor.get()).title()
                    self.entryfornecedor.delete(0, 'end')
                    self.entryfornecedor.insert(0, digitado)
                if len(self.entryfornecedor.get()) > 2:
                    self.entryfornecedor.config(bg=verde_médio, fg=preto_claro)
                self.aparecerBotãoAddEstoque()
        print(evento)

    def bindDoNomeCliente(self, evento):
        """
        PlaceHolder para nomes de clientes, independente se está inserindo ou consultando
        :param evento: Qual evento do bind está acontecendo
        :return: Não retorna nada
        """
        ação = str(evento).split()[0]
        nome = self.entry_nome
        match ação:
            case '<FocusIn':
                if nome.get() in ['', 'Nome']:
                    nome.delete(0, 'end')
                    nome.config(bg=branco_gelo, fg=preto_claro)
                    print(evento)
                if self.motivo_nome == 'Consultando':
                    if str(nome.get()).strip() in self.select_dados_clientes()['nomes_de_clientes']:
                        nome.config(bg=verde_médio, fg=preto_claro)
                elif self.motivo_nome == 'Inserindo':
                    if str(nome.get()).strip() in self.select_dados_clientes()['nomes_de_clientes']:
                        nome.config(bg=vermelho_salmão, fg=preto_claro)
            case '<FocusOut':
                if nome.get() in ['', 'Nome']:
                    nome.config(bg=preto_claro, fg='Gray')
                    nome.insert(0, 'Nome')
                if self.motivo_nome == 'Consultando':
                    if str(nome.get()).strip() in self.select_dados_clientes()['nomes_de_clientes']:
                        nome.config(bg=verde_médio, fg=preto_claro)
                    else:
                        nome.config(bg=vermelho_salmão, fg=preto_claro)
                elif self.motivo_nome == 'Inserindo':
                    if str(nome.get()).strip() in self.select_dados_clientes()['nomes_de_clientes']:
                        nome.config(bg=vermelho_salmão, fg=preto_claro)
            case '<KeyRelease':
                if evento.keysym in ['Left', 'Right']:
                    return
                else:
                    digitado = str(nome.get()).title()
                    nome.delete(0, 'end')
                    nome.insert(0, digitado)
                    if self.motivo_nome == 'Consultando':
                        if str(nome.get()).strip() in self.select_dados_clientes()['nomes_de_clientes']:
                            nome.config(bg=verde_médio, fg=preto_claro)
                        else:
                            nome.config(bg=branco_gelo, fg=preto_claro)
                    elif self.motivo_nome == 'Inserindo':
                        if str(nome.get()).strip() in self.select_dados_clientes()['nomes_de_clientes']:
                            nome.config(bg=vermelho_salmão, fg=preto_claro)
                        else:
                            if len(nome.get()) > 2:
                                nome.config(bg=verde_médio, fg=preto_claro)
                            else:
                                nome.config(bg=branco_gelo, fg=preto_claro)
                                print(self.motivo_nome)

    def verdeComboPgto(self, evento):
        self.comboxFormaPGTO .configure(style='T2.TCombobox')
        self.style.map('T2.TCombobox', fieldbackground=[('readonly', verde_médio)],
                       selectbackground=[('readonly', verde_médio)],
                       selectforeground=[('readonly', preto_claro)])
        self.mostrarBotãoApertoDeMãos('<Button>')
        str(evento)

    def bindDoTelefoneCliente(self, evento):
        """
        PlaceHolder para nomes de clientes, independente se está inserindo ou consultando
        :param evento: Qual evento do bind está acontecendo
        :return: Não retorna nada
        """
        ação = str(evento).split()[0]
        telefone = self.entry_telefone
        match ação:
            case '<FocusIn':
                if telefone.get() in ['', 'Telefone']:
                    telefone.delete(0, 'end')
                    telefone.config(bg=branco_gelo, fg=preto_claro)
                    print(evento)
            case '<FocusOut':
                if len(telefone.get()) != 15:
                    telefone.config(bg=vermelho_salmão, fg=preto_claro)
                if telefone.get() in ['', 'Telefone']:
                    telefone.config(bg=preto_claro, fg='Gray')
                    telefone.insert(0, 'Telefone')
            case '<KeyRelease':
                numtel = telefone.get().replace("(", "").replace(")", "").replace("-", "").replace(
                    " ", "")[
                         :11]
                telformat = ""

                if evento.keysym.lower() in ["left", "right", "backspace"]:
                    telefone.config(bg=branco_gelo, fg=preto_claro)
                    return
                if len(numtel) == 11:
                    telefone.config(bg=branco_gelo, fg=preto_claro)
                elif len(numtel) < 11:
                    telefone.config(bg='white', fg=preto_claro)

                for index in range(len(numtel)):

                    if not numtel[index] in "0123456789":
                        continue
                    if index == 0:
                        telformat += "(" + numtel[index]
                    elif index == 1:
                        telformat += numtel[index] + ") "

                    elif index == 6:
                        telformat += numtel[index] + "-"
                    else:
                        telformat += numtel[index]
                if len(telefone.get()) == 15:
                    if self.motivo_telefone == 'Consultando':
                        if telefone.get() in self.select_dados_clientes()['telefone_de_clientes']:
                            telefone.config(bg=verde_médio, fg=preto_claro)
                        else:
                            telefone.config(bg=vermelho_salmão, fg=preto_claro)
                    elif self.motivo_telefone == 'Consultando':
                        if telefone.get() in self.select_dados_clientes()['telefone_de_clientes']:
                            telefone.config(bg=vermelho_salmão, fg=preto_claro)
                        else:
                            telefone.config(bg=verde_médio, fg=preto_claro)

                telefone.delete(0, "end")
                telefone.insert(0, telformat)

    def bindDoEndereçoCliente(self, evento):
        ação = str(evento).split()[0]
        endereço = self.entry_endereço
        match ação:
            case '<FocusIn':
                if endereço.get() in ['', 'Endereço']:
                    endereço.delete(0, 'end')
                    endereço.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if endereço['bg'] == branco_gelo:
                    endereço.config(bg=vermelho_salmão, fg=preto_claro)
                if endereço.get() in ['', 'Endereço']:
                    endereço.config(bg=preto_claro, fg='Gray')
                    endereço.insert(0, 'Endereço')
            case '<KeyRelease':
                if evento.keysym in ['Left', 'Right', "Multi_key"]:
                    return
                else:
                    digitado = str(endereço.get()).title()
                    endereço.delete(0, 'end')
                    endereço.insert(0, digitado)
                    self.autocompBairros(evento, endereço)
                    if len(endereço.get()) > 2:
                        if self.motivo_endereço == 'Consultando':
                            if endereço.get() in self.select_dados_clientes()['bairros']:
                                endereço.config(bg=verde_médio, fg=preto_claro)
                            else:
                                endereço.config(bg=vermelho_salmão, fg=preto_claro)
                        if self.motivo_endereço == 'Inserindo':
                            if endereço.get() in self.select_dados_clientes()['bairros']:
                                endereço.config(bg=vermelho_salmão, fg=preto_claro)
                            else:
                                endereço.config(bg=verde_médio, fg=preto_claro)
                    if len(endereço.get()) < 3:
                        endereço.config(bg=branco_gelo, fg=preto_claro)

    def bindDaObservaçãoCliente(self, evento):
        ação = str(evento).split()[0]
        observação = self.entry_observação
        match ação:
            case '<FocusIn':
                if observação.get() in ['', 'Observação']:
                    observação.delete(0, 'end')
                    observação.config(bg=branco_gelo, fg=preto_claro)
            case '<FocusOut':
                if observação.get() in ['', 'Observação']:
                    observação.config(bg=preto_claro, fg='Gray')
                    observação.insert(0, 'Observação')
            case '<KeyRelease':
                if evento.keysym in ['Left', 'Right']:
                    return
                else:
                    digitado = str(observação.get()).capitalize()
                    observação.delete(0, 'end')
                    observação.insert(0, digitado)
                    if len(observação.get()) > 2:
                        observação.config(bg=verde_médio, fg=preto_claro)
        print(evento)

    def bindDaQuantidadeProduto(self, evento):
        ação = str(evento).split()[0]
        quantidade = self.entry_qt
        match ação:
            case '<FocusIn':
                if quantidade.get() in ['', 'Qtde']:
                    quantidade.delete(0, 'end')
                    quantidade.config(bg=branco_gelo, fg=preto_claro)
                    print(evento)
            case '<FocusOut':
                if len(quantidade.get()) > 0:
                    quantidade.config(bg=verde_médio, fg=preto_claro)
                if quantidade.get() in ['', 'Qtde']:
                    quantidade.config(bg=preto_claro, fg='Gray')
                    quantidade.insert(0, 'Qtde')
            case '<KeyRelease':
                if evento.keysym.lower() in ["left", "right", "backspace"]:
                    quantidade.config(bg=branco_gelo, fg=preto_claro)
                    return
                if len(quantidade.get()) > 0:
                    quantidade.config(bg=verde_médio, fg=preto_claro)

                for index in range(len(quantidade.get())):
                    if quantidade.get()[index] in "0123456789":
                        pass
                    else:
                        quantidade.delete(len(quantidade.get())-1, len(quantidade.get()))

    def verdeComboProduto(self, evento):
        # self.style.map('TCombobox', fieldbackground=[('readonly', verde_médio)])
        # self.style.map('TCombobox', selectbackground=[('readonly', verde_médio)])
        # self.style.map('TCombobox', selectforeground=[('readonly', preto_claro)])
        # self.style.map('TCombobox', foreground=[('readonly', preto_claro)])
        self.comboxProduto.configure(style='T2.TCombobox')
        self.style.map('T2.TCombobox', fieldbackground=[('readonly', verde_médio)], selectbackground=[('readonly', verde_médio)],
                       selectforeground=[('readonly', preto_claro)])
        self.btVerdinho.grid(row=0, column=0)
        self.mostrarBotãoApertoDeMãos('<Button>')
        str(evento)
