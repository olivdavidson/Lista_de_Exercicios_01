sal_base = float(input('Insira o salário base: '))
acresc = sal_base + (sal_base*(5/100))
desc = sal_base - (sal_base*(7/100))
aux = acresc - desc
liquido = sal_base + aux
print('O salário líquido é de R$ %.2f'%liquido)
