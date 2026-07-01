'''Uma loja de calçados está em liquidação. Com isso, para cada compra à vista, 
a loja concede 8% de desconto no preço da peça.
Crie um programa que leia o preço de uma peça 
e imprima tela o novo preço já com o desconto aplicado.'''

valor_produto = float(input('Insira o valor do produto para calcular o desconto:'))

valor_promocional = valor_produto*(92/100)
desconto = valor_produto-valor_promocional

'''print('Você terá um desconto de  R$', desconto, 
      'reais. E o valor a ser pago é:  R$', valor_promocional)'''

print('Você terá um desconto de  R${:.2f}'.format(desconto),    
      # As {} sao mascaras e server para receber um valor, e o '.format()' define qual o valor que a mascara ira receber
      # o codigo dentro da mascara {} que e ":.2f" quer dizer que "para depois do ponto, ou virgula, tera apenas duas casas decimais"
      'reais. E o valor a ser pago é:  R${:.2f}'.format(valor_promocional))