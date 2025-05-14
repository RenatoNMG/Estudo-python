

#comentario em python

nome = "Renato"
idade = 50
altura = 1.83
vivo = True


frutas = ["maça","banana","uva"]



def saudação():
    print(f"meu nome é {nome} e tenho {idade} anos minha altura é {altura} e estou {vivo}")

def soma(a,b):
    return a / b

print(soma(10,8))



if idade <= 18:
    print("criança")
elif idade >= 40:
    print("adulto")
else:
    print("idoso")






saudação()
frutas.append("laranja")
frutas.remove("uva")
print(len(frutas))
print(frutas)



for fruta in frutas:
    print(fruta)




for i in range(10):
    print(f"ontando ate {i}")


for i in range(5,10):
    print(f"segundo for contando de 5 a 10 {i}")
20

# while idade > 10:
#     print(idade)
#     idade -= 1
#     idade = int(input("digite sua idade"))


#dicionario

dados = {"nome":"renato","idade":28}
print(dados["idade"])


pessoa = ("joao",25)

print(pessoa[1])

numeros = {1,2,3,4,5}

numerolista = list(numeros)[3]

print(numerolista)




if "laranja" in frutas:
    print("tem laranja")



if "laranja" not in frutas:
    print("não tem laranja em frutas")


try:
    valor = int(input("digite um numero"))
except ValueError:
    print("valor invalido")


listadinamica = [x*6 for x in range(10)]

print(listadinamica)