# Cáculos enegéticos para o fim do mês
# Autor: Eduardo Campos

# Entrada de Dados
eletrodoméstico = input("Por favor, insira o nome do eletrodomético para calcularmos seu gasto elétrico: ")
potência = float(input("Informe a potência em Watts (W): "))
tempo = float(input("Você diria que usa quantas horas por dia?: "))

# Cálculo de dados
consumo_elétrico_mensal = (potência * tempo * 30) / 1000 #kWh
cálculo_monetário = (consumo_elétrico_mensal * 0.80) #reais (R$)

# Saída
print (f"O {eletrodoméstico} tem um consumo de, aproximadamente,{consumo_elétrico_mensal: .0f} kWh/mês, custanto cerca de{cálculo_monetário: .2f} R$ mensais.")