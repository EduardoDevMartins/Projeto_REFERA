import os


while True:

    print()
    categorias = ('Sair', 'vazamento', 'ar-condicionado',
                  'Eletrica', 'caca-vazamento')

    for i, valor in enumerate(categorias):
        print(i, valor)
    print()

    opcao = input('Selecione a categoria desejada: ')

    if opcao == '1':  # VAZAMENTO
        tipo_residencia = input('[1] CASA OU [2] APARTAMENTO : ')
        if tipo_residencia != '1':
            print()
            print('ACIONAR CACA VAZAMENTO')
            print()
        if tipo_residencia == '1':
            status_registro = input(
                'o relogio continua girando com o registro desligado? [1] SIM [2] NAO : ')
            if status_registro == '1':
                print(
                    'verificar possivel erro da concessionaria, caso negativo, instalar valvula para supressao de ar')
                print()
            if status_registro != '1':
                verificar_vazamento = input(
                    'Voce encontrou algum vazamento aparente? [1] SIM [2] NAO : ')
                if verificar_vazamento == '1':
                    print('REPARAR O VAZAMENTO')
                    print()
                if verificar_vazamento != '1':
                    print('ACIONAR CACA VAZAMENTO')
                    print()

    elif opcao == '2':  # AR CONDICIONADO
        qual_problema = input(
            '[1]Nao resfria e nao ventila [2] Nao resfria e so ventila [3] Nao liga [4] Vazamento [5] Risco de queda')
        if qual_problema == '1':
            print('Visita/realizar teste capacitor Evaporador')
            teste_capacitor = input('Teste funcionou? [1]SIM [2]NAO : ')
            if teste_capacitor == '1':
                print('Teste motor do ventilador/Regulagem da turbina')
                resultado_teste_motor_turbina = input(
                    'O teste Funcionou? [1]SIM [2]NAO : ')
                if resultado_teste_motor_turbina == '1':
                    print('INDEFINIDO')
                if resultado_teste_motor_turbina == '2':
                    print('NECESSARIO TROCA DO MOTOR DO VENTILADOR')
            if teste_capacitor == '2':
                print('NECESSARIO TROCA DO CAPACITOR')

        if qual_problema == '2':
            ...
        if qual_problema == '3':
            ...
        if qual_problema == '4':
            ...
        if qual_problema == '5':
            ...

    elif opcao == '3':  # ELETRICA
        ...

    elif opcao == '4':  # CACA VAZAMENTO
        tipo_problema = input(
            'Qual tipo de problema? [1] INFILTRACAO OU [2] VAZAMENTO : ')
        if tipo_problema == '1':
            print('executar teste de estanqueidade com traçador químico na rede loca')
            tracador = input(
                'Localizou vestigio do tracador? [1] SIM ou [2] NAO : ')
            if tracador == '1':
                print('REPARAR O PONTO DE VAZAMENTO')
                print()
            if tracador != '1':
                print(
                    'testar impermeabilização do piso do box, conexões externas do vaso sanitário e da pia.')
                print()
                print('REPARAR O PONTO DE VAZAMENTO')
                print()
        if tipo_problema != '1':
            tipo_de_agua = input(
                'O vazamento e de [1] AGUA QUENTE OU [2] AGUA FRIA : ? ')
            if tipo_de_agua == '1':
                print('executar teste com camera termografica e reparar o vazamento')
            if tipo_de_agua != '1':
                print('teste com compressor de ar e geo fone.')
                print()
                print('REPARAR O PONTO DE VAZAMENTO')
                print()

    elif opcao == '5':  # utlizar aqui quando quiser adicionar nova categoraia
        ...

    elif opcao == '6':  # utlizar aqui quando quiser adicionar nova categoria
        ...

    elif opcao == '0':
        os.system('cls')
        print('OBRIGADO POR USAR NOSSOS SERVICOS!!')
        print()
        break

    else:
        print('selecione uma opcao valida')
