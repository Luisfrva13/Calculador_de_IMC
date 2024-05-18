nome = (input('Digite seu nome:'))
peso = str(input('Digite seu peso:')).replace(',' , '.')
altura = str(input('Digite sua altura:')).replace(',' , '.')

peso = float(peso)
altura = float(altura)

imc = peso / altura **2

print(f'O valor do IMC de {nome} é {imc:,.2f}.')

if imc < 18.5:
    print(f'Baixo Peso')

elif imc < 24.9:
    print(f'Peso Ideal')

elif imc < 29.9:
    print(f'Sorbepeso')

elif imc < 34.9:
    print(f'Obesidade I')

elif imc < 39.9:
    print(f'Obesidade II')

else:
    print(f'Obesidade III')




















               




