#Leia uma temperatura em graus Celsiuse e apresente-a convertida em graus Farenheit. 
#A fórmula de conversão é: F = C*(9.0/5.0)+32.0, sendo F a temperatura Farenheit e C a temperatura em Celcius.
tempC = float(input('Informe a temperatura em Celcius: '))
tempF = tempC*(9.0/5.0)+32.0
print('A temperatura convertida em Farenheit é de: %.2f'%tempF,'F°')