'''Victor Gabriel Cunha Rodrigues e Lorrana Evelyn de Araújo Pereira'''

from random import randint
class Celular():
    def __init__(self,numero,cor):
        self.__numero = numero
        self.__cor = cor
        self.__bateria = randint(0,100)
        self.__sinal = False
        self.__ligado = False
        self.__estado = None
        self.__credito = 0
        self.__aparelho_conectado = None
        self.__caixa_sms = []


    @property
    def cor (self):
        return self.__cor
    
    @cor.setter
    def cor (self,valor):
        print('nao e possivel alterar a cor ')
    
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self,valor):
        print('nao pode alterar o numero')

    @property
    def bateria(self):
        return self.__bateria
    @bateria.setter
    def bateria(self,valor):
        print("Não é possível alterar a bateria")

    @property
    def sinal(self):
        return self.__sinal
    @sinal.setter
    def sinal(self,valor):
        print("Não é possível alterar o sinal")

    @property
    def ligado(self):
        return self.__ligado
    @ligado.setter
    def ligado(self,valor):
        print("Não é possível alterar")

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado (self , valor):
        print("Não é possível alterar")

    @property
    def credito(self):
        return self.__credito
    @credito.setter
    def credito (self,valor):
        print("Não é possível alterar")

    @property
    def aparelho_conectado(self):
        return self.__aparelho_conectado
    @aparelho_conectado.setter
    def aparelho_conectado(self,valor):
        print("Não é possível alterar")
    
    @property
    def caixa_sms(self):
        return self.__caixa_sms

    @caixa_sms.setter
    def caixa_sms(self,valor):
        print("Não é possível alterar")



    def ligar (self):
        self.__sinal = True
        self.__ligado = True
        self.__estado = 0
        print('o celular esta ligado')

    def desligar(self):
        self.__sinal = False
        self.__ligado = False
        self.__estado = None
        print('o celular está desligado')

    def colocar_creditos(self,valor=None):
        if valor == None:
            self.__credito = self.__credito + 1
        else:
            self.__credito = valor
    
    def carregar_bateria(self):
        self.__bateria = 100

    def fazer_ligacao(self,aparelho):
        if type(aparelho)== Celular and self.__sinal ==True and aparelho.__sinal ==True and self.__estado==0 and self.__credito >= 1:
            self.__estado = 1
            self.__aparelho_conectado =True
            print(f'o aparelho está em ligacao')

        elif type(aparelho)== Celular and self.__sinal ==False and self.__estado==0 and self.__credito >= 1:
            print('o sinal está desligado')

        elif type(aparelho)== Celular and self.__sinal ==True and self.__estado==1 and self.__credito >= 1:
            print('esta em outra chamada')
        
        elif type(aparelho)== Celular  and self.__sinal ==True and self.__estado== None and self.__credito >= 1:
            print('o celular está desligado')
        
        elif type(aparelho)== Celular  and self.__sinal ==True and self.__estado== 0 and self.__credito <1:
            print('o celular está sem credito')
        
        else:
            print('o celular está desligado')

    def encerrar_ligacao(self,tempo):
        if self.__estado == 1 and self.__bateria > 0:
            self.__estado = 0
            tempo = self.__bateria - tempo
            print(f'bateria final: {tempo}%')
        elif self.__bateria < 0:
            self.__bateria = 0
        else:
            print('a chamada ja foi encerrada')
    

    def enviar_sms(self,mensagem,ap_destino):
        if self.__sinal == True and self.__ligado == True and self.__credito >=0.5:
            self.__credito = self.__credito - 0.5
            ap_destino.__caixa_sms.append(mensagem)
            ap_destino = mensagem


        elif self.__sinal == True and self.__ligado == True and self.__credito <0.5:
            print('voce nao tem creditos suficiente')
    
    def ver_sms(self,ap_destino):
        print(self.__caixa_sms)
    
    def esvaziar_caixa(self):
        self.__caixa_sms = None
    

print('==========celular 1==========')
cell1 = Celular(9999,'cinza')

cell1.ligar()
print(cell1.bateria)
cell1.carregar_bateria()
print(cell1.bateria)
print(cell1.credito)
cell1.colocar_creditos(15)
print(cell1.credito)
cell1.cor =  'verde'
cell1.numero = 97537



print('===========celular 2=======================')
cell2 = Celular(8888,'azul')
cell2.ligar()
print(cell2.bateria)
cell2.colocar_creditos(5)
print(cell2.credito)
cell2.enviar_sms('ola',cell1)
print(cell1.caixa_sms[0])
print(cell1.caixa_sms)
cell1.esvaziar_caixa()
print(cell1.caixa_sms)
#cell2.desligar()
cell2.fazer_ligacao(cell1)
cell2.encerrar_ligacao(12)


print('============celular 3==============')
cell3 = Celular(1357,'vermelho')
cell3.ligar()
print(cell3.bateria)
cell3.colocar_creditos(45)
cell3.carregar_bateria()
print(f'{cell3.bateria}%')
cell3.enviar_sms('some da minha vida',cell2)
print(cell2.caixa_sms[0])


print('========celular 4============')
cell4 = Celular(2678,'preto')
cell4.ligar()
#cell4.colocar_creditos()
cell4.fazer_ligacao(cell1)
cell4.desligar()