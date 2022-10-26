class Operacao():
    def __init__(self, quantidade, valor_unitario, taxa_corretagem,ativo):
        self.ativo = ativo
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.taxa_corretagem = taxa_corretagem

    #quantidade x valor unitario
    def calcular_operacao(self):
        self.produto = self.valor_unitario * self.quantidade
        print(f'valor da operacão(sem taxas): {self.produto:.2f}')

    #0.3% sobre a açao
    def calcular_taxas_b3(self):
        self.taxa_b3 = self.valor_unitario * 0.0300
        print(f'taxa B3: {self.taxa_b3:.2f}')

    #somar B3 + taxa corretagem + valor total(compra)
    def calcular_valor_total(self):
        self.taxa_total = self.taxa_b3 + self.taxa_corretagem + self.produto
        print(f'taxa total(compra): {self.taxa_total:.2f}')
        
    
    # B3 - taxa de corretagem - valor sem taxas
    def calcular_valor_venda(self):
        self.taxa_venda = self.produto - self.taxa_corretagem - self.taxa_b3
        print(f'taxa total(venda): {self.taxa_venda:.2f}')


    #preço medio (compra)
    def preco_medio_compra(self):
        ativo = self.ativo.get()
        precoMedio = (self.taxa_total / self.quantidade) * ativo
        print(f'o preço médio é: {round(precoMedio,2)}')
            
    

''''
print('===============OPERAÇAÕ DE COMPRA===================')
op1 = Operacao(100,9.5, 2.5)
op1.calcular_operacao()
op1.calcular_taxas_b3()
op1.calcular_valor_total()

#Segunda Operação
print('===================SEGUNDA OPERAÇÃO COMPRA====================')
op2 = Operacao(100,9.1,2.5)
op2.calcular_operacao()
op2.calcular_taxas_b3()
op2.calcular_valor_total()

print('===================TERCEIRA OPERAÇÃO VENDA====================')
op3 = Operacao(100,20,2.5)
op3.calcular_operacao()
op3.calcular_taxas_b3()
op3.calcular_valor_venda()'''

print('============TESTE MEDIA=================')
op99 = Operacao(100,9.5, 2.5)
op99.calcular_operacao()
op99.calcular_taxas_b3()
op99.calcular_valor_total()
op99.preco_medio_compra()