#Mensagem de boas vindas
print('Bem vindo ao Recomendador de viagens LF!')
print('Vou te fazer algumas perguntas e com base nas respostas recomendarei o melhor lugar para você!')
print('Lembrando que nossas opções de respostas estarão entre parênteses, exemplo: (sim / não).')
print('Vamos Começar!')
print()
#escolhas do usuário
price = input('Qual o seu orçamento para esta viagem? (baixo / médio / alto) ')
temp = input('Qual o clima desejado? (quente / frio)' )
tipo = input('Qual seu tipo de viagem preferido? (aventura / descanso) ')
periodo = input('Qual a duração ideal para esta viagem? (curta / longa) ')
print()
#Viagem recomendada de acordo com as escolhas do usuário 
if price == 'baixo':
    if temp == 'quente':
        if tipo == 'aventura':
            if periodo == 'curta':
                lugar = 'Jericoacoara (CE)'
            else:
                lugar = 'Chapada dos Veadeiros (GO)'
        else:
            if periodo == 'curta':
                lugar = 'Porto de Galinhas (PE)'
            else:
                lugar = 'Maragogi (AL)'
    else:
        if tipo == 'aventura':
            if periodo == 'curta':
                lugar = 'Pico do Marumbi (PR)'
            else:
                lugar = 'Serra Catarinense (SC)'
        else:
            if periodo == 'curta':
                lugar = 'São Bento do Sapucaí (SP)'
            else:
                lugar = 'Cânions do Sul (RS/SC)'
elif price == 'médio':
    if temp == 'quente':
        if tipo == 'aventura':
            if periodo == 'curta':
                lugar = 'Capitólio (MG)'
            else:
                lugar = 'Chapada Diamantina (BA)'
        else:
            if periodo == 'curta':
                lugar = 'Ilhabela (SP)'
            else:
                lugar = 'Arraial d’Ajuda (BA)'
    else:
        if tipo == 'aventura':
            if periodo == 'curta':
                lugar = 'Campos do Jordão (SP)'
            else:
                lugar = 'Gramado + Canela (RS)'
        else:
            if periodo == 'curta':
                lugar = 'Monte Verde (MG)'
            else:
                lugar = 'Serra Gaúcha (tour completo)'
else:
    if temp == 'quente':
        if tipo == 'aventura':
            if periodo == 'curta':
                lugar = 'Fernando de Noronha (PE)'
            else:
                lugar = 'Jalapão (TO)'
        else:
            if periodo == 'curta':
                lugar = 'Resort All Inclusive – Bahia'
            else:
                lugar = 'Maldivas'
    else:
        if tipo == 'aventura':
            if periodo == 'curta':
                lugar = 'Bariloche (Argentina)'
            else:
                lugar = 'Patagônia (Chile/Argentina)'
        else:
            if periodo == 'curta':
                lugar = 'Campos do Jordão Premium (hotéis de luxo)'
            else:
                lugar = 'Suíça – Alpes (Zermatt)'
#Banco de dados equivalente ao preço de cada lugar
if lugar == 'Jericoacoara (CE)':
    price1 = 'R$1.200,00'
elif lugar == 'Chapada dos Veadeiros (GO)':
    price1 = 'R$1.800,00'
elif lugar == 'Porto de Galinhas (PE)':
    price1 = 'R$1.300,00'
elif lugar == 'Maragogi (AL)':
    price1 = 'R$1.900,00'
elif lugar == 'Pico do Marumbi (PR)':
    price1 = 'R$700,00'
elif lugar == 'Serra Catarinense (SC)':
    price1 = 'R$1.400,00'
elif lugar == 'São Bento do Sapucaí (SP)':
    price1 = 'R$650,00'
elif lugar == 'Cânions do Sul (RS/SC)':
    price1 = 'R$1.500,00'
elif lugar == 'Capitólio (MG)':
    price1 = 'R$1.700,00'
elif lugar == 'Chapada Diamantina (BA)':
    price1 = 'R$2.700,00'
elif lugar == 'Ilhabela (SP)':
    price1 = 'R$1.600,00'
elif lugar == 'Arraial d’Ajuda (BA)':
    price1 = 'R$2.800,00'
elif lugar == 'Campos do Jordão (SP)':
    price1 = 'R$1.900,00'
elif lugar == 'Gramado + Canela (RS)':
    price1 = 'R$3.500,00'
elif lugar == 'Monte Verde (MG)':
    price1 = 'R$1.500,00'
elif lugar == 'Serra Gaúcha (tour completo)':
    price1 = 'R$3.800,00'
elif lugar == 'Fernando de Noronha (PE)':
    price1 = 'R$6.000,00'
elif lugar == 'Jalapão (TO)':
    price1 = 'R$7.500,00'
elif lugar == 'Resort All Inclusive – Bahia':
    price1 = 'R$4.800,00'
elif lugar == 'Maldivas':
    price1 = 'R$22.000,00'
elif lugar == 'Bariloche (Argentina)':
    price1 = 'R$7.000,00'
elif lugar == 'Patagônia (Chile/Argentina)':
    price1 = 'R$14.000,00'
elif lugar == 'Campos do Jordão Premium (hotéis de luxo)':
    price1 = 'R$3.800,00'
else:
    price1 = 'R$26.000,00'
#Mensagem a ser exibida ao usuário
print()
print(f'De acordo com suas preferências, o local ideal para você viajar é para {lugar}!')
print(f'Sua viagem custará em média {price1}.')
input()
