#Coleta de dados
SB = float(input('Digite seu Salário Bruto mensal: R$'))
VRD = float(input('Digite o valor diário do seu VR: R$'))
VTD = float(input('Digite o valor diário do seu VT: R$'))
DU = int(input('Digite a quantidade de dias trabalhados da sua folha: '))
print()
#Regime  de Contratação do Usuário
RC = input('Digite o seu Regime de Contratação com:\n"j" para Jovem Aprendiz\n"e" para estagiário e\n"c" para Efetivo CLT\n\nDigite aqui: ')
print()
#Verificar valor do INSS
if RC == 'j':
    inss = SB * (7.5/100)
else:
    if SB >= 7507.49:
        inss = 876.98
    elif SB >= 3856.95:
        inss = ((SB - 3856.94) * (14/100)) + (99 + 112.62 + 154.28)
    elif SB >= 2571.30:
        inss = ((SB - 2571.29) * (12/100)) + (99 + 112.62)
    elif SB >= 1320.01:
        inss = ((SB - 1320.00) * (9/100)) + (99)
    else:
        inss = SB * (7.5/100)
#IRRF
BC = (SB - inss)
if BC >= 4664.69:
    irrf = (BC * (27.5/100)) - 869.36
elif BC >= 3751.06:
    irrf = (BC * (22.5/100)) - 636.13
elif BC >= 2826.66:
    irrf = (BC * (15/100)) - 354.80
elif BC >= 1903.99:
    irrf = (BC * (7.5/100)) - 142.80
else:
    irrf = 0
#Cálculo do valor mensal
VRM = VRD * DU
VTM = VTD * DU
#Cálculo de descontos
DVR = VRM * (20/100)
DVT = SB * (6/100)
#Condição de Estagiário
if RC == 'e':
    DVR = 0
    DVT = 0
    irrf = 0
    inss = 0
else:
    DVR = DVR
    DVT = DVT
    irrf = irrf
    inss = inss
#Valor líquido a ser recebido
SL = SB - DVT - inss - irrf
VRL = VRM - DVR
VTL = VTM
#Mensagem ao usuário
print('----- Salário Líquido -----')
print()
print(f'De acordo com os dados fornecidos, o valor líquido do seu salário a ser recebido será de {SL:.2f}')
print()
print('----- Descontos -----')
print()
print(f'O valor a ser descontado devido ao VR é igual a R${DVR:.2f}')
print(f'O valor a ser descontado devido ao VT é igual a R${DVT:.2f}')
print(f'O valor a ser descontado devido ao INSS é igual a R${inss:.2f}')
print(f'O valor a ser descontado devido ao IRRF é igual a R${irrf:.2f}')
print()
print('----- Banefícios -----')
print()
print(f'O valor a ser recebido de VR será de R${VRM:.2f}')
print(f'O valor a ser recebido de VT será de R${VTM:.2f}')
print()
print('----- Valor Líquido Final -----')
print()
print(f'Somando todos os seus valores líquidos, o total que receberá no dia do pagamento será: R${SL + VRL + VTL:.2f}')
input()
