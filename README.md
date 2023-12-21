Deseja-se implementar um sistema para realizar o pagamento de vendedores (corretores) de uma
imobiliária. A imobiliária possui dois tipos de vendedores, os contratados e os comissionados. Os
vendedores contratados são funcionários da imobiliária e, portanto, recebem um salário fixo mensal. Além
disso, recebem uma porcentagem fixa de 1% sobre o valor de cada imóvel vendido. Já os vendedores
comissionados recebem apenas a comissão sobre as vendas efetuadas, a qual varia entre 1 e 5%. Este
percentual é negociado entre o dono da imobiliária e cada vendedor comissionado, assim, o valor deste
percentual varia entre os vendedores comissionados.
Você deve seguir a modelagem anexa de modo a implementar um sistema capaz de calcular o valor mensal
devido a cada vendedor. Note que cada vendedor deve possuir uma lista de objetos Venda. Utilizando os
objetos dessa lista é possível calcular a renda dos vendedores comissionados. Já para os vendedores
contratados, é necessário calcular o valor obtido com as comissões e juntar a ele o salário mensal. Assim, o
método calculaRenda deve receber como entrada o mês e o ano e obter a renda do vendedor naquele mês
do ano.
O método getDados deve imprimir o nome e o número da carteira de trabalho para os vendedores
contratados. Já para os vendedores comissionados, este método deve imprimir o nome e o número do CPF
do vendedor.
Após implementar as classes do modelo, o código a seguir deve executar sem erros (Não é permitido
modificar este código):
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
A saída produzida pelo programa deve ser a seguinte:
Nome: João da Silva - Nro Carteira: 1234
Renda no mês 3 de 2022:
7000.0
Nome: José Santos - Nro CPF: 4321
Renda no mês 3 de 2022:
30000.0
