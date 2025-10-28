import os
import math
import random


def raiz_quadrada():
    numero = float(input("Digite um número para calcular a raiz quadrada: "))
    if numero < 0:
        print("Não é possível calcular a raiz quadrada de um número negativo!")
    else:
        resultado = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {resultado}")
    input("Precione enter para continuar.")


def potencia():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    resultado = math.pow(base, expoente)
    print(f"{base} elevado a {expoente} é igual a {resultado}")
    input("Precione enter para continuar.")


def numero_aleatorio():
    inicio = int(input("Digite o valor inicial do intervalo: "))
    fim = int(input("Digite o valor final do intervalo: "))
    if inicio > fim:
        print("O valor inicial deve ser menor ou igual ao valor final.")
    else:
        numero = random.randint(inicio, fim)
        print(f"Número aleatório gerado entre {inicio} e {fim}: {numero}")
        input("Precione enter para continuar.")

def calculo():
    Num1 = float(input("Digite o primeiro número: "))
    Num2 = float(input("Digite o segundo número: "))
    soma = Num1 + Num2
    subtracao = Num1 - Num2
    multiplicacao = Num1 * Num2
    divisao = Num1 / Num2
    potencia = math.pow(Num1, Num2)
    print(f"soma: {soma}")
    print(f"subtração: {subtracao}")
    print(f"multiplicação: {multiplicacao}")
    print(f"divisão: {divisao}")
    print(f"potência: {potencia}")
    input("Precione enter para continuar.")

def main():

    while True:
        os.system("cls")
        print("\n----Menu de operações----")
        print("1 Raiz quadrada")
        print("2 Potência")
        print("3 Número aleatório")
        print("4 Cálculos")
        print("5 Sair")
    
        opcao = input("Escolha uma opção: ")

        if opcao == '1' :
            raiz_quadrada()
        elif opcao == '2':
            potencia()
        elif opcao == '3':
            numero_aleatorio()
        elif opcao == '4':
            calculo()
        elif opcao == '5':
            print("Saindo do porgrama... Até logo!")
            break
        else:
            print("Opção invalida! Tente novamente")
        

if __name__ == "__main__":
    main()