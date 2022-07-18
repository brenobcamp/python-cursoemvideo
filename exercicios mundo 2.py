# Exercicios do Curso em Video de Python Mundo 2
# 036
def compraCasa():
    valor = int(input("Digite o valor da casa: "))
    salario = int(input("Digite o salário do comprador: "))
    anos = int(input("Digite em quantos anos irá pagar: "))
    parcela = valor/(anos*12)
    if parcela <= salario*0.3:
        print("\033[1;32;43mO empréstimo foi aprovado!\033[m\nA parcela por mês é de R${:.2f}".format(parcela))
    else:
        print("\033[1;31;43mEmprestimo negado!\033[m\nO valor da parcela é maior que trinta por cento do salário")
#compraCasa()

# 037
def conversao():
    num = int(input("Digite o número a ser convertido: "))
    modo = int(input("Digite a conversão desejada:\n1 para binário\n2 para octal\n3 para hexadecimal\n"))
    if modo == 1:
        print("\033[1;33mO número em binário é: {}\033[m".format(bin(num)))
    elif modo == 2:
        print("\033[1;33mO número em octal é: {}\033[m".format(oct(num)))
    elif modo == 3:
        print("\033[1;33mO número em hexadecimal é: {}\033[m".format(hex(num)))
    else:
        print("Erro! Digite 1, 2 ou 3")
#conversao()

# 038
def maioroumenor():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    if n1 > n2:
        print("O primeiro valor {} é maior que o segundo {}".format(n1, n2))
    elif n2 > n1:
        print("O segundo valor {} é maior que o primeiro {}".format(n2, n1))
    elif n2 == n1:
        print("Os dois valores são iguais! {} = {}".format(n1, n2))
    else:
        print("Erro!")
#maioroumenor()


# 039
def alistamento():
    from datetime import date
    ano = int(input("Digite o ano de nascimento: "))
    anoat = date.today().year
    idade = anoat - ano
    if idade == 17:
        print("Você está em idade de se alistar!")
    elif idade > 17:
        tempo = idade - 17
        print("Você já passou {} anos da idade de se alistar.".format(tempo))
    else:
        futuro = (-17 + idade)*-1
        print("Faltam {} anos para você se alistar.".format(futuro))
#alistamento()

# 040
def nota():
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))
    med = (n1 + n2)/2
    if n1 > 10 or n2 > 10:
        print("Insira notas entre 0 e 10")
    elif med < 5:
        print("O aluno ficou com média {} e foi reprovado!".format(med))
    elif med >= 5 and med < 7:
        print("O aluno ficou com média {} e está de recuperação!".format(med))
    elif med >= 7:
            print("O aluno ficou com média {} e foi aprovado!".format(med))
#nota()

# 041
def nadador():
    from datetime import date
    nasc = int(input("Digite o ano de nascimento do atleta: "))
    ano = date.today().year
    idade = ano - nasc
    if idade <= 9 and idade > 5:
        print("O atleta tem {} anos e é da categoria Mirim.".format(idade))
    elif idade <= 14 and idade > 9:
        print("O atleta tem {} anos e é da categoria Infantil.".format(idade))
    elif idade > 14 and idade < 19:
        print("O atleta tem {} anos e é da categoria Junior.".format(idade))
    elif idade == 19 or idade == 20:
        print("O atleta tem {} anos e é da categoria Sênior.".format(idade))
    elif idade > 20:
        print("O atleta tem {} anos e é da categoria Master.".format(idade))
    elif idade < 4:
        print("O nadador tem {} anos e ainda não pode competir.".format(idade))
#nadador()

# 042
def triangulo():
    a = float(input("Valor: "))
    b = float(input("Valor: "))
    c = float(input("Valor: "))
    if a < (b + c) and b < (a + c) and c < (a + b):
        print("Forma triângulo")
        if a == b and a == c and b == c:
            print("O triangulo formado é equilátero")
        elif a == b or a == c or b == c:
            print("O triangulo formado é isósceles")
        else:
            print("O triangulo formado é escaleno")
    else:
        print("Não forma triângulo.")
#triangulo()

# 043
def imc():
    peso = float(input("Digite seu peso: "))
    alt = float(input("Digite sua altura [em metros]: "))
    imc = peso/(alt**2)
    if imc < 18.5:
        print("Você está abaixo do peso.\nIMC: {:.1f}".format(imc))
    elif imc >= 18.5 and imc <= 25:
        print("Você está no peso ideal.\nIMC: {:.1f}".format(imc))
    elif imc > 25 and imc <=30:
        print("Você está com sobrepeso.\nIMC: {:.1f}".format(imc))
    elif imc > 30 and imc <= 40:
        print("Você está obeso.\nIMC: {:.1f}".format(imc))
    elif imc > 40:
        print("Você está com obesidade mórbida.\nIMC: {:.1f}".format(imc))
#imc()

# 044
def desconto():
    valor = float(input("Digite o valor do produto: R$"))
    pag = int(input("Digite a forma de pagamento:\nÀ vista em dinheiro: 1\nÀ vista no cartão: 2\n2x no cartão: 3\n3x ou mais no cartão: 4\n"))
    if pag == 1:
        print("O produto tem desconto de 10 por cento e sai por R${:.2f}".format(valor*0.9))
    elif pag == 2:
        print("O produto tem desconto de 5 por cento e sai por R${:.2f}".format(valor*0.95))
    elif pag == 3:
        print("O produto não tem desconto e sai por R${:.2f}".format(valor))
    elif pag == 4:
        print("O produto recebe juros de 20 por cento e sai por R${:.2f}".format(valor*1.2))
#desconto()

# 045
def jokenpo():
    from random import choice
    player = input("Escolha pedra, papel ou tesoura: ").strip().lower()
    maq = choice("pedra papel tesoura".split())
    if player == maq:
        print("Empatamos!\nNós dois escolhemos {}".format(player.capitalize()))
    elif player == 'papel' and maq == 'tesoura':
        print("Eu ganhei!\nMinha tesoura corta seu papel")
    elif player == 'tesoura' and maq == 'papel':
        print("Você ganhou!\nSua tesoura corta meu papel")
    elif player == 'papel' and maq == 'pedra':
        print("Você ganhou!\nSeu papel envolve minha pedra")
    elif player == 'pedra' and maq == 'papel':
        print("Eu ganhei!\nMeu papel envolve sua pedra")
    elif player == 'tesoura' and maq == 'pedra':
        print("Eu ganhei!\nMinha pedra quebra sua tesoura")
    elif player == 'pedra' and maq == 'tesoura':
        print("Você ganhou!\nSua pedra quebra minha tesoura")
jokenpo()
    