"""
Exercício Validador de CPFs - aula 47
"""

while True:

    fatorMult1 = 10
    valorSoma1 = 0
    fatorMult2 = 11
    valorSoma2 = 0

    cpfDigitado = input('Digite seu CPF: ')
    cpfCalculo = cpfDigitado[0:9]

    if cpfDigitado.isnumeric():
            verificacao = True
    else:
            verificacao = False
            print('Digite apenas números!')

    if verificacao and len(cpfDigitado) < 11:
            print('CPF incompleto! Está faltando números.')
    elif verificacao and len(cpfDigitado) == 11:
        for i in cpfCalculo:
            valorSoma1 = valorSoma1 + (int(i) * fatorMult1)
            fatorMult1 -= 1
            # print(valorSoma1)

        primeiroDigito = 11 - (valorSoma1 % 11)

        if primeiroDigito > 9:
            primeiroDigito = 0

        # print(f'O valor do primeiro digito verificador é {primeiroDigito}')

        cpfCalculo = cpfCalculo + str(primeiroDigito)

        for j in cpfCalculo:
            valorSoma2 = valorSoma2 + (int(j) * fatorMult2)
            fatorMult2 -= 1
            # print(valorSoma2)

        segundoDigito = 11 - (valorSoma2 % 11)

        if segundoDigito > 9:
            segundoDigito = 0

        # print(f'O valor do segundo digito verificador é {segundoDigito}')

        cpfCalculo = cpfCalculo + str(segundoDigito)

        if cpfDigitado == cpfCalculo:
            cpfDigitado = cpfDigitado[0:3] + '.' + cpfDigitado[3:6] + '.' + cpfDigitado[6:9] + '-' + str(
                primeiroDigito) + str(segundoDigito)
            print(f'O CPF {cpfDigitado} é VÁLIDO!')
        else:
            cpfCalculo = cpfCalculo[0:3] + '.' + cpfCalculo[3:6] + '.' + cpfCalculo[6:9] + '-' + str(
                primeiroDigito) + str(segundoDigito)
            print(f'O CPF {cpfDigitado} é INVÁLIDO!')
            print(f'O CPF calculado foi {cpfCalculo}')






