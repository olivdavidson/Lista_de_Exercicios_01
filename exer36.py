import math
alt = float(input('Informe a altura do cilindro: '))
raio = float(input('Informe o raio do cilindro: '))
volume = math.pi * raio**2 * alt
print('O volume do cilindro é de: %.2f'%volume)