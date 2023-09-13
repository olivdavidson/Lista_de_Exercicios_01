diaria = int(input('Informe os dias trabalhados: '))
val_dias = diaria * 30
pgto = val_dias - (val_dias*(8/100))
print('O valor que você irá receber já com os 8 porcento descontados é R$ %.2f'%pgto)