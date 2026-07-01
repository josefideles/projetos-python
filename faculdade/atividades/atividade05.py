'''Crie um programa que peça ao usuário para inserir sua nota em uma prova
e imprima se ele foi aprovado ou reprovado
(considerando que a nota mínima para aprovação é 7)'''

#1 passo: Irei pedir a nota da prova ao usuário
#2 passo: Criar a condição de ser aprovado ou reprovado
#3 passo: Comparar a condição com a nota dele
#4 passo: Imprimir o status de sua nota
#5 passo: Fazer esse mesmo código na interface do PySimpleGUI

points = float(input('Insira a sua nota da prova para saber o seu status: '))
if points%1 == 0:       #criei uma condição para não ter casas decimais em inteiro
    points = int(points)
media = 7
if points < media:
    print('A sua nota foi inferior a média, que é de {}, e a sua nota foi de {}.\nInfelizmente você foi reprovado, mas utilize essa nota como aprendizado para poder fechar a próxima prova. Você tem muito esforço!!!'.format(media, points))
elif points > 10:
    print('O limite da prova é de 10 pontos, e você não pode exceder a pontuação máxima para calcular a sua média!')
else:
    print('Ótimo, a sua nota foi maior que a média, que é de {}.\nVocê está aprovado, o seu resultado vem de todo o seu esforço para estudar para a prova. Continue assim!!!'.format(media))