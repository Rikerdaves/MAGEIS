'Victor Gabriel Cunha Rodrigues e Lorrana Evelyn de Araujo Pereira'



class BombaCombustivel():
    def __init__(self,identificador,tipo,ValorLitro,capacidade,
    quantidade):
         
        self.__identificador= identificador
        self.__tipo = tipo
        self.__ValorLitro = ValorLitro
        self.__capacidade = capacidade
        self.__quantidade = quantidade
        self.__valor_faturado = 0
        self.__quant_venda = 0

    #ENCAPSULAMENTO
    @property
    def identificador(self):
        return self.__identificador
    @identificador.setter
    def identificador(self,valor):
        print('impossivel alterar o identificador')

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self,tipo=None):
        if tipo == None:
            tipo = 1
        else:
            tipo = tipo

    @property
    def ValorLitro(self):
        return self.__ValorLitro
    @ValorLitro.setter
    def ValorLitro(self,valor):
        print('impossivel alterar o valor')
    
    @property
    def capacidade(self):
        return self.__capacidade
    @capacidade.setter
    def capacidade(self,valor):
        print('impossivel alterar a capacidade')
    
    @property
    def quantidade(self):
        return self.__quantidade
    @quantidade.setter
    def quantidade(self,valor):
        print('impossível alterar a quantidade')

    @property
    def valor_faturado(self):
        return self.__valor_faturado
    
    
    @property
    def quant_venda(self):
        return self.__quant_venda
    @quant_venda.setter
    def quant_venda(self,valor):
        print('impossivel alterar')



    #MÉTODOS
    def AbastecerBomba(self):
        if self.__quantidade < self.__capacidade:
            self.__quantidade = self.__capacidade 
        else:
            print('a capacidade máxima ja foi atingida')


    
    def AbastecerPorValor(self,valor):
        if self.__quantidade > 0 :
            self.__valor_faturado = self.__valor_faturado + valor
            QuantAdicionado = valor/self.__ValorLitro
            self.__quant_venda = self.__quant_venda + QuantAdicionado
            valor = QuantAdicionado
            self.__quantidade = self.__quantidade - QuantAdicionado
            print(f'{QuantAdicionado:.1f} litros foi adicionado ao veiculo')

        elif valor < 0:
            print('valor nao pode ser menor que 0')
        else:
            print('bomba sem litros suficiente para abastecer')
    

    def AbastecerPorLitro(self,litro):
        if  self.__quantidade > 0:
            self.__quant_venda = self.__quant_venda + litro
            self.__quantidade = self.__quantidade - litro
            QuantAdicionado2 = litro * self.__ValorLitro
            self.__valor_faturado = self.__valor_faturado +QuantAdicionado2
            print(f'voce ira pagar {QuantAdicionado2:.2f}')
        
        elif litro < 0:
            print('valor nao pode ser menor que 0')

        else:
            print('bomba sem litros suficiente para abastecer')



    def __str__(self):
        return f'quantidade:{self.__quantidade:.1f}'+ f'\n quantidade de litros vendidos:{self.__quant_venda:.1f}'+f'\n valor arrecadado:{self.__valor_faturado:.1f} '


print('=========bomba 1 ===========')
bomba1 = BombaCombustivel(123,1,7,440,100)
bomba1.AbastecerBomba()
print(bomba1.quantidade)
bomba1.AbastecerPorValor(84)
print(f'quantidade apos abastecer por valor: {bomba1.quantidade}')
bomba1.AbastecerPorLitro(12)
print(f'quantidade apos abastecer por litros:{bomba1.quantidade}')
print(bomba1)


print('============bomba 2==============')
bomba2 = BombaCombustivel(234,2,4.5,500,290)
bomba2.AbastecerBomba()
print(bomba2.quantidade)
bomba2.AbastecerPorLitro(28)
bomba2.quantidade = 234 # encapsulamento
bomba2.AbastecerPorValor(46)
print(bomba2)

print('============bomba 3==============')
bomba3 = BombaCombustivel(274,4,6,800,300)
bomba3.AbastecerPorValor(35)
bomba3.AbastecerPorLitro(200)
bomba3.AbastecerPorValor(167)
bomba3.capacidade = 1233 #mensagem de erro devido ao encapsulamento
print(bomba3)



print('============bomba 4==============')
bomba4 = BombaCombustivel(23433,3,8,760,178)
bomba4.AbastecerPorValor(25)
print(bomba4.tipo)
bomba4.AbastecerPorValor(100)
print(bomba4.quantidade)
bomba4.AbastecerPorValor(100)
print(bomba4.quantidade)
print(bomba4)
print(bomba4)
