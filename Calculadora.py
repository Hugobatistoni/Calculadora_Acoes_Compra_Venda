#MENSAGEM DE BOAS VINDAS
print('Bem Vindo a Calculadora de Ações, informe a mesma quantidade de compra e venda')

#INFORMAR O PREÇO DA COMPRA E QUANTIDADE

precodecompra = float(input('Qual o preço de compra ?'))
quantidadecompra = float(input('qual a quantidade de ações ?'))
resultado_compra = precodecompra * quantidadecompra
print('O Valor total de compra é de',resultado_compra)

#INFORMAR O PREÇO DA VENDA E QUANTIDADE

precodevenda = float(input('Qual o preço de venda ?'))
quantidadevenda = float(input('qual a quantidade de ações ?'))
resultado_venda = precodevenda * quantidadevenda
print('O Valor total de compra é de',resultado_venda)

#CALCULA O VALOR DE COMPRA MENOS O VALOR DE VENDA

resultado =  resultado_venda - resultado_compra

#RETORNA A MENSAGEM

if resultado > 0:
    print('Seu lucro foi de',resultado,'real')
else :
    print('Você não obteve lucro na operação, perda de',resultado,'reais ')
