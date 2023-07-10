import os

while True:

    print()
    Porcentagens = ('Sair', '5%', '7%', '10%', '15%')

    for i, valor in enumerate(Porcentagens):
        print(i, valor)
    print()

    opcao = input('Selecione a porcentagem desejada: ')
    print()

    if opcao == '1':  # 5% porcento selecionado
        take_rate = 5
        print('TAKE RATE PRICING SELECIONADO 5%')
        print()
        Take_Rate_refera = float(
            input('Informe o valor de TAKE RATE DA REFERA EM %: '))
        # convertendo para % valor inserido
        print()
        Valor_prestador = float(input('Informe o VALOR PRESTADOR: '))
        print()
        Take_Rate_imobiliaria = float(
            input('Informe o valor de TAKE RATE DA IMOBILIÁRIA EM %: '))
        print()
        valor_refera = Valor_prestador*(Take_Rate_refera / 100)
        texto_valor_refera = f'Valor Refera R${valor_refera:.2f}'
        print(texto_valor_refera)
        valor_imobiliaria = Valor_prestador*(Take_Rate_imobiliaria / 100)
        texto_valor_imbobiliaria = f'Valor Imobiliária R$ {valor_imobiliaria:.2f}'
        print(texto_valor_imbobiliaria)
        valor_total = valor_refera+valor_imobiliaria+Valor_prestador
        texto_valor_total = f'Valor Total R$ {valor_total:.2f}'
        print(texto_valor_total)
        print()

        # Alterações baseado % definida de revenue

        valor_pricing = Valor_prestador*(take_rate / 100)
        texto_valor_pricing = f'Valor PRICING R$ {valor_pricing:.2f}'
        print(texto_valor_pricing)
        novo_valor_refera = valor_pricing+valor_refera
        texto_novo_valor_refera = f'Novo Valor REFERA R$ {novo_valor_refera:.2f}'
        print(texto_novo_valor_refera)
        print()

        # Informações de alteração no BO

        novo_valor_prestador = Valor_prestador-valor_pricing
        texto_novo_valor_prestador = f'Novo Valor do PRESTADOR: R$ {novo_valor_prestador:.2f}'
        print(texto_novo_valor_prestador)
        novo_take_rate_refera = (novo_valor_refera/novo_valor_prestador) * 100
        novo_take_rate_refera_porcentagem = "{:.2f}%".format(
            novo_take_rate_refera)
        texto_novo_take_rate_refera = f'Novo Take Rate Refera é : {novo_take_rate_refera_porcentagem}'
        print(texto_novo_take_rate_refera)
        novo_take_rate_imobiliaria = (
            valor_imobiliaria/novo_valor_prestador) * 100
        novo_take_rate_imobiliaria_porcentagem = "{:.2f}%".format(
            novo_take_rate_imobiliaria)
        texto_novo_take_rate_imobiliaria = f'Novo Take Rate Imobiliária é : {novo_take_rate_imobiliaria_porcentagem}'
        print(texto_novo_take_rate_imobiliaria)
        desconto_pricing = Valor_prestador-novo_valor_prestador
        texto_desconto_pricing = f'Desconto Pricing é: RS {desconto_pricing:.2f}'
        print(texto_desconto_pricing)

    if opcao == '2':  # 7% porcento selecionado
        take_rate = 7
        print('TAKE RATE PRICING SELECIONADO 7%')
        print()
        Take_Rate_refera = float(
            input('Informe o valor de TAKE RATE DA REFERA EM %: '))
        # convertendo para % valor inserido
        print()
        Valor_prestador = float(input('Informe o VALOR PRESTADOR: '))
        print()
        Take_Rate_imobiliaria = float(
            input('Informe o valor de TAKE RATE DA IMOBILIÁRIA EM %: '))
        print()
        valor_refera = Valor_prestador*(Take_Rate_refera / 100)
        texto_valor_refera = f'Valor Refera R${valor_refera:.2f}'
        print(texto_valor_refera)
        valor_imobiliaria = Valor_prestador*(Take_Rate_imobiliaria / 100)
        texto_valor_imbobiliaria = f'Valor Imobiliária R$ {valor_imobiliaria:.2f}'
        print(texto_valor_imbobiliaria)
        valor_total = valor_refera+valor_imobiliaria+Valor_prestador
        texto_valor_total = f'Valor Total R$ {valor_total:.2f}'
        print(texto_valor_total)
        print()

        # Alterações baseado % definida de revenue

        valor_pricing = Valor_prestador*(take_rate / 100)
        texto_valor_pricing = f'Valor PRICING R$ {valor_pricing:.2f}'
        print(texto_valor_pricing)
        novo_valor_refera = valor_pricing+valor_refera
        texto_novo_valor_refera = f'Novo Valor REFERA R$ {novo_valor_refera:.2f}'
        print(texto_novo_valor_refera)
        print()

        # Informações de alteração no BO

        novo_valor_prestador = Valor_prestador-valor_pricing
        texto_novo_valor_prestador = f'Novo Valor do PRESTADOR: R$ {novo_valor_prestador:.2f}'
        print(texto_novo_valor_prestador)
        novo_take_rate_refera = (novo_valor_refera/novo_valor_prestador) * 100
        novo_take_rate_refera_porcentagem = "{:.2f}%".format(
            novo_take_rate_refera)
        texto_novo_take_rate_refera = f'Novo Take Rate Refera é : {novo_take_rate_refera_porcentagem}'
        print(texto_novo_take_rate_refera)
        novo_take_rate_imobiliaria = (
            valor_imobiliaria/novo_valor_prestador) * 100
        novo_take_rate_imobiliaria_porcentagem = "{:.2f}%".format(
            novo_take_rate_imobiliaria)
        texto_novo_take_rate_imobiliaria = f'Novo Take Rate Imobiliária é : {novo_take_rate_imobiliaria_porcentagem}'
        print(texto_novo_take_rate_imobiliaria)
        desconto_pricing = Valor_prestador-novo_valor_prestador
        texto_desconto_pricing = f'Desconto Pricing é: RS {desconto_pricing:.2f}'
        print(texto_desconto_pricing)

    if opcao == '3':  # 10% porcento selecionado
        take_rate = 10
        print('TAKE RATE PRICING SELECIONADO 10%')
        print()
        Take_Rate_refera = float(
            input('Informe o valor de TAKE RATE DA REFERA EM %: '))
        # convertendo para % valor inserido
        print()
        Valor_prestador = float(input('Informe o VALOR PRESTADOR: '))
        print()
        Take_Rate_imobiliaria = float(
            input('Informe o valor de TAKE RATE DA IMOBILIÁRIA EM %: '))
        print()
        valor_refera = Valor_prestador*(Take_Rate_refera / 100)
        texto_valor_refera = f'Valor Refera R${valor_refera:.2f}'
        print(texto_valor_refera)
        valor_imobiliaria = Valor_prestador*(Take_Rate_imobiliaria / 100)
        texto_valor_imbobiliaria = f'Valor Imobiliária R$ {valor_imobiliaria:.2f}'
        print(texto_valor_imbobiliaria)
        valor_total = valor_refera+valor_imobiliaria+Valor_prestador
        texto_valor_total = f'Valor Total R$ {valor_total:.2f}'
        print(texto_valor_total)
        print()

        # Alterações baseado % definida de revenue

        valor_pricing = Valor_prestador*(take_rate / 100)
        texto_valor_pricing = f'Valor PRICING R$ {valor_pricing:.2f}'
        print(texto_valor_pricing)
        novo_valor_refera = valor_pricing+valor_refera
        texto_novo_valor_refera = f'Novo Valor REFERA R$ {novo_valor_refera:.2f}'
        print(texto_novo_valor_refera)
        print()

        # Informações de alteração no BO

        novo_valor_prestador = Valor_prestador-valor_pricing
        texto_novo_valor_prestador = f'Novo Valor do PRESTADOR: R$ {novo_valor_prestador:.2f}'
        print(texto_novo_valor_prestador)
        novo_take_rate_refera = (novo_valor_refera/novo_valor_prestador) * 100
        novo_take_rate_refera_porcentagem = "{:.2f}%".format(
            novo_take_rate_refera)
        texto_novo_take_rate_refera = f'Novo Take Rate Refera é : {novo_take_rate_refera_porcentagem}'
        print(texto_novo_take_rate_refera)
        novo_take_rate_imobiliaria = (
            valor_imobiliaria/novo_valor_prestador) * 100
        novo_take_rate_imobiliaria_porcentagem = "{:.2f}%".format(
            novo_take_rate_imobiliaria)
        texto_novo_take_rate_imobiliaria = f'Novo Take Rate Imobiliária é : {novo_take_rate_imobiliaria_porcentagem}'
        print(texto_novo_take_rate_imobiliaria)
        desconto_pricing = Valor_prestador-novo_valor_prestador
        texto_desconto_pricing = f'Desconto Pricing é: RS {desconto_pricing:.2f}'
        print(texto_desconto_pricing)

    if opcao == '4':  # 15% porcento selecionado
        take_rate = 15
        print('TAKE RATE PRICING SELECIONADO 15%')
        print()
        Take_Rate_refera = float(
            input('Informe o valor de TAKE RATE DA REFERA EM %: '))
        # convertendo para % valor inserido
        print()
        Valor_prestador = float(input('Informe o VALOR PRESTADOR: '))
        print()
        Take_Rate_imobiliaria = float(
            input('Informe o valor de TAKE RATE DA IMOBILIÁRIA EM %: '))
        print()
        valor_refera = Valor_prestador*(Take_Rate_refera / 100)
        texto_valor_refera = f'Valor Refera R${valor_refera:.2f}'
        print(texto_valor_refera)
        valor_imobiliaria = Valor_prestador*(Take_Rate_imobiliaria / 100)
        texto_valor_imbobiliaria = f'Valor Imobiliária R$ {valor_imobiliaria:.2f}'
        print(texto_valor_imbobiliaria)
        valor_total = valor_refera+valor_imobiliaria+Valor_prestador
        texto_valor_total = f'Valor Total R$ {valor_total:.2f}'
        print(texto_valor_total)
        print()

        # Alterações baseado % definida de revenue

        valor_pricing = Valor_prestador*(take_rate / 100)
        texto_valor_pricing = f'Valor PRICING R$ {valor_pricing:.2f}'
        print(texto_valor_pricing)
        novo_valor_refera = valor_pricing+valor_refera
        texto_novo_valor_refera = f'Novo Valor REFERA R$ {novo_valor_refera:.2f}'
        print(texto_novo_valor_refera)
        print()

        # Informações de alteração no BO

        novo_valor_prestador = Valor_prestador-valor_pricing
        texto_novo_valor_prestador = f'Novo Valor do PRESTADOR: R$ {novo_valor_prestador:.2f}'
        print(texto_novo_valor_prestador)
        novo_take_rate_refera = (novo_valor_refera/novo_valor_prestador) * 100
        novo_take_rate_refera_porcentagem = "{:.2f}%".format(
            novo_take_rate_refera)
        texto_novo_take_rate_refera = f'Novo Take Rate Refera é : {novo_take_rate_refera_porcentagem}'
        print(texto_novo_take_rate_refera)
        novo_take_rate_imobiliaria = (
            valor_imobiliaria/novo_valor_prestador) * 100
        novo_take_rate_imobiliaria_porcentagem = "{:.2f}%".format(
            novo_take_rate_imobiliaria)
        texto_novo_take_rate_imobiliaria = f'Novo Take Rate Imobiliária é : {novo_take_rate_imobiliaria_porcentagem}'
        print(texto_novo_take_rate_imobiliaria)
        desconto_pricing = Valor_prestador-novo_valor_prestador
        texto_desconto_pricing = f'Desconto Pricing é: RS {desconto_pricing:.2f}'
        print(texto_desconto_pricing)

    elif opcao == '0':
        os.system('cls')
        print('OBRIGADO POR USAR NOSSOS SERVICOS!!')
        print()
        break

    else:
        print('selecione uma opcao valida')
