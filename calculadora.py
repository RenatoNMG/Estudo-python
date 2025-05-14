print("Calculadora")

validade = True
resultado = 0


while validade:
    try:
        operacao = input("qual opercaração quer fazer")
        numero1 = int(input("Digite um numero"))
        numero2 = int(input("Digite o segundo numero"))
        validade = False
    except ValueError:
        print("digite um numero valido")
        validade = True

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2


print(resultado)



