import math
cat_a = float(input('Informe o valor do primeiro cateto: '))
cat_b = float(input('Informe o valor do segundo cateto: '))
hipo = math.sqrt(cat_a**2 + cat_b**2)
print('O valor da Hipotenusa é: %.2f'%hipo)