from abc import ABC, abstractmethod

class Vendedor(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__vendas = []
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def vendas(self):
        return self.__vendas
    
    def adicionaVenda(self, CodImovel, Mes, Ano, Valor):
        venda = Venda(CodImovel, Mes, Ano, Valor)#venda é uma isntância da classe venda
        self.vendas.append(venda)#cada objeto da lista vendas é um objeto da classe Venda


    @abstractmethod
    def getDados(self):
        pass

    @abstractmethod
    def calculaRenda(self, Mes, Ano):
        pass

class Venda:
    def __init__(self, CodImovel, MesVenda, AnoVenda, ValorVenda):
        self.__CodImovel = CodImovel
        self.__MesVenda = MesVenda
        self.__AnoVenda = AnoVenda
        self.__ValorVenda = ValorVenda

    @property
    def CodImovel(self):
        return self.__CodImovel
    
    @property
    def MesVenda(self):
        return self.__MesVenda
    
    @property
    def AnoVenda(self):
        return self.__AnoVenda
    
    @property 
    def ValorVenda(self):
        return self.__ValorVenda
    
class Contratado(Vendedor):
    def __init__(self, codigo, nome, salario, nroCartTrabalho):
        super().__init__(codigo, nome)
        self.__salario = salario
        self.__nroCartTrabalho = nroCartTrabalho

    @property
    def salario(self):
        return self.__salario
    
    @property
    def nroCartTrabalho(self):
        return self.__nroCartTrabalho
    
    def getDados(self):
        return f"Nome: {self.nome} - Nro Carteira: {self.nroCartTrabalho}"
    
    def calculaRenda(self, Mes, Ano):
        comissao = 0
        for venda in self.vendas:#verificar cada venda individualmente na lista de vendas
            if venda.MesVenda == Mes and venda.AnoVenda == Ano:
                comissao += venda.ValorVenda * 0.01
        return self.salario 
    
class Comissionado(Vendedor):
    def __init__(self, codigo, nome, nroCPF, comissao):
        super().__init__(codigo, nome)
        self.__nroCPF = nroCPF
        self.__comissao = comissao

    @property
    def nroCPF(self):
        return self.__nroCPF
    
    @property
    def comissao(self):
        return self.__comissao
    
    def getDados(self):
        return f"Nome: {self.nome} - Nro CPF: {self.nroCPF}"
    
    def calculaRenda(self, Mes, Ano):
        comissao = 0
        for venda in self.vendas:
            if venda.MesVenda == Mes and venda.AnoVenda == Ano:
                comissao += venda.ValorVenda * (self.comissao / 100)
        return comissao
    
if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print (func.getDados())
        print ("Renda no mês 3 de 2022: ")
        print (func.calculaRenda(3, 2022))