#Leia uma temperatura em graus Farenheit e apresente-a convertida em graus Celsius. 
#A fórmula de conversão é: C = 5.0*(F-32.0)/9.0, sendo F a temperatura Farenheit e C a temperatura em Celcius.
tempF = float(input('Informe a temperatura em Farenheit: '))
tempC = 5.0*(tempF-32.0)/9.0
print('A temperatura convertida em Celcius é: ', tempC)