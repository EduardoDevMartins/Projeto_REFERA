
# Exercicio calculo  IMC
# IMC = peso / (altura x altura)
print('Bem vindo ao cálculo de IMC, por favor preencha os dados a seguir como mostrado nos exemplos.')
name = input('Insira seu nome: ')
altura1 = input('Insira sua altura (exemplo: 1.73): ')
peso1 = input('Insira seu peso (exemplo: 102.5): ')
altura = float(altura1)
peso = float(peso1)
imc = peso/(altura * altura)

texto = f'{name} tem {altura:.2f} de altura, e de peso {peso:.2f} quilos'
texto2 = f'O seu IMC é: {imc:.2f}'
print(texto)
print(texto2)


entrada1 = input('digite o valor do seu IMC (exemplo: 33.45): ')
entrada = float(entrada1)

if entrada <= 18.5:
    print('Seu IMC está classificado como magreza.')

    print('Procurar um Nutricionista e um profissional de Educação física')

elif entrada <= 24.9:
    print('Seu IMC está classificado como normal')
    print('Parabéns!!!!')

elif entrada <= 29.9:
    print('Seu IMC indica Sobrepeso')
    print(' Cuidado, é necessário algum ajuste em sua alimentação')

elif entrada <= 39.9:
    print('Seu IMC indica Obesidade grau II')
    print('Você precisa de um especialista')

elif entrada >= 40:
    print('Seu IMC indica Obesidade grave tipo III')
    print('Você pode enfartar a qualquer momento, procure um médico')

...
