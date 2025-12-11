#Coleta de dados
SB = float(input('Digite seu Salário Bruto mensal: R$'))
VRD = float(input('Digite o valor diário do seu VR: R$'))
VTD = float(input('Digite o valor diário do seu VT: R$'))
DU = int(input('Digite a quantidade de dias trabalhados da sua folha: '))
print()
#Regime  de Contratação do Usuário
RC = input('Digite o seu Regime de Contratação com:\n"0" para Jovem Aprendiz\n"1" para estagiário e\n"2" para Efetivo CLT\n\nDigite aqui: ')
print()
#INSS
if RC == '0':
    inss = SB * (7.5/100)
else:
    if SB >= 8157.41:
        inss = 951.63
    elif SB >= 4190.84:
        inss = ((SB - 4190.83) * (14/100)) + (113.85 + 114.83 + 167.63)
    elif SB >= 2793.89:
        inss = ((SB - 2793.88) * (12/100)) + (113.85 + 114.83)
    elif SB >= 1518.01:
        inss = ((SB - 1518.00) * (9/100)) + (113.85)
    else:
        inss = SB * (7.5/100)
#IRRF
BC = (SB - inss)
if BC >= 4664.69:
    irrf = (BC * (27.5/100)) - 913.49
elif BC >= 3751.06:
    irrf = (BC * (22.5/100)) - 675.49
elif BC >= 2826.66:
    irrf = (BC * (15/100)) - 394.16
elif BC >= 2428.81:
    irrf = (BC * (7.5/100)) - 182.16
else:
    irrf = 0
#Condição de IRRF negativo
if irrf >= 0:   
    irrf =irrf
else:
    irrf = 0
#Cálculo do valor mensal
VRM = VRD * DU
VTM = VTD * DU
#Cálculo de descontos
DVR = VRM * (20/100)
DVT = SB * (6/100)
#Condição de Estagiário
if RC == '1':
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
SL = SB - DVT - DVR - inss - irrf
VRL = VRM
VTL = VTM
#Mensagem ao usuário
print('----- Valores Considerados -----')
print()
print(f'De acordo com o seu salário bruto (R${SB:.2f})\nSeu VR (R${VRD:.2f} por dia) e\nSeu VT (R${VTD:.2f} por dia)')
print()
print('----- Descontos -----')
print()
print(f'O valor a ser descontado devido ao VR é igual a R${DVR:.2f}')
print(f'O valor a ser descontado devido ao VT é igual a R${DVT:.2f}')
print(f'O valor a ser descontado devido ao INSS é igual a R${inss:.2f}')
print(f'O valor a ser descontado devido ao IRRF é igual a R${irrf:.2f}')
print()
print(f'A soma de seus descontos é igual a R${DVR + DVT + inss + irrf:.2f}')
print()
print('----- Benefícios -----')
print()
print(f'O valor a ser recebido de VR será de R${VRM:.2f}')
print(f'O valor a ser recebido de VT será de R${VTM:.2f}')
print()
print(f'A soma de seus benefícios é igual a R${VRM + VTM:.2f}')
print()
print('----- Valor Líquido Final -----')
print()
print(f'Somando seu Salário Líquido (R${SL:.2f}) e a soma entre seus benefícios (R${VRM + VTM:.2f})\nO total que receberá no dia do pagamento será: R${SL + VRL + VTL:.2f}')
input()
