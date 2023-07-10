import re
import sys

print('Bem vindo(a) ao verificador de CPF')

name = input('Digite seu Nome: ')
cpf = input('Digite seu cpf :')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    cpf
)

entrada_sequencial = cpf == cpf[0] * len(cpf)

if entrada_sequencial:
    print('Você enviou dados sequenciais. ')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
(digito_1)

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
(digito_2)

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'Olá {name}.')
    print(f'Seu CPF {cpf_enviado_usuario}')
    print(f' é um CPF válido!')
else:
    print('Não é um cpf válido')
