horas_trab = float(input('Informe o valor da hora de trabalho: '))
val_horas = float(input('Informe a quantidade de horas trabalhadas: '))
pgto = horas_trab * val_horas
acresc = pgto + (pgto*(10/100))
print('O valor do pagamento com o acréscimo de 10 porcento é de R$ %.2F'%acresc)