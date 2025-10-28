#c-*- config: utf-8 -*-
import os

while True:
    os.system("cls")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    resultado = numero1 * numero2

    print(f"O resultado de {numero1} * {numero2} é: {resultado}")

    continua = input("Deseja continuar? (s/n)").strip().lower()

    if continua != "s":
        print("Programa encerrado, até logo!")
        break

print("-" * 81)