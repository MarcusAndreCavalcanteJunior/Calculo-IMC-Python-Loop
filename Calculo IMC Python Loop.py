while True:
    try:
        peso = float(input('Informe o seu peso (kg): '))
        altura = float(input('Informe sua altura (m): '))
        imc = peso / (pow(altura, 2))

        print(f'Seu IMC é {imc:.2f}')

        if imc < 18.5:
            print('Abaixo do peso')
        elif 18.5 <= imc < 24.9:
            print('Peso Normal')
        elif 25 <= imc < 29.9:
            print('Sobrepeso')
        elif 30 <= imc < 34.9:
            print('Obesidade Grau I')
        elif 35 <= imc < 39.9:
            print('Obesidade Grau II')
        else:
            print('Obesidade Grau III ou Mórbida')

        repetir = input("Deseja calcular o IMC novamente? (s/n): ").strip().lower()
        if repetir != 's':
            print("Encerrando o programa.")
            break
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
