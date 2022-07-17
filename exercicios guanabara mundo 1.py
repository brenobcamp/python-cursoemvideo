#   EXERCICIOS GUANABARA  aula 09
# 001
#pn = int(input("primeiro numero:"))
#sn = int(input("segundo numero:"))
#soma = pn + sn
#print("A soma de {0} e {1} é igual a {2}".format(pn, sn, soma))

def calculaPotencia(a, b):
    pot = a**b
    print("{} elevado a {} é: {}".format(a, b, pot))
#n1 = float(input("Valor: "))
#n2 = float(input("Potência: "))
#calculaPotencia(n1, n2)

# 005
def antEsuc (a):
    ant = a - 1
    suc = a + 1
    print("O antecessor de {} é {}.\nO sucessor de {} é {}.".format(a, ant, a, suc))
#v = int(input("Valor: "))
#antEsuc(v)

# 006
def exercicio006(a):
    d = a*2
    t = a*3
    r = a**(1/2)
    print("O dobro de {} é {}. O triplo é {}. A raiz quadrada é {:.3f}".format(a, d, t, r))
#exercicio006(int(input("O valor a ser calculado: ")))
 
# 007
def media(y, x):
    med = (y + x)/2
    print("A média das notas {} e {} é igual a {}.".format(y, x, med))
    if (med > 7):
        print("O aluno foi aprovado!")
    else:
        print("O aluno está reprovado.")
#media(int(input("Nota primeira prova: ")),int(input("Nota segunda prova: ")))

#008
def conversao(a):
    cm = a*100
    mm = a*1000
    print("O valor de {} em centimetros é {:.0f}, em milimetro é {:.0f}".format(a, cm, mm))
#conversao(float(input("Valor em metros: ")))

#009
def tabuada(a):
    print("{}x1 = {}\n{}x2 = {}\n{}x3 = {}\n{}x4 = {}\n{}x5 = {}\n{}x6 = {}\n{}x7 = {}\n{}x8 = {}\n{}x9 = {}\n".format(a, a*1, a, a*2, a, a*3, a, a*4, a, a*5, a, a*6, a, a*7, a, a*8, a, a*9))
#tabuada(int(input("Número da tabuada: ")))


def tabuada2(a):
    for a in range(1, 9):
        print("{}x{} = {}".format(a, int(A = ["1","2",'3','4','5','6','7','8','9']), a*int))
#tabuada2(int(input("Número da tabuada: ")))

# 011
def cambio(a):
    dolar = a * 3.27
    print("Você pode comprar {} dolars.".format(dolar))
#cambio(int(input("Você tem: ")))

# 012
def calculaTinta(a, b):
    area = a*b
    litros = area/2
    print("Você precisa de {} litros de tinta para pintar {} m² de parede".format(litros, area))
#calculaTinta(int(input("Coloque a altura em metros: ")), int(input("Coloque a largura em metros: ")))

 # 013
#import random

def sorteio(a, b):
    print ("O numero sorteado é {}".format(random.randint(a, b)))

#sorteio(int(input("Primeiro valor: ")),int(input("Segundo valor:")))

# 014
#import emoji
#print(emoji.emojize("Olá mundo! :earth_americas:", use_aliases= True))

# 015
def arredondar(a):
    print("A parte inteira é {}".format(math.floor(a)))
#arredondar(float(input("Digite um numero real: ")))

# 016
def hipote(a, b):
    hip = math.hypot(a, b)
    print("A hipotenusa do triangulo de catetos {} e {} é: {:.3f}.".format(a, b, hip))
#hipote(float(input("Digite o valor do cateto oposto: ")), float(input("Digite o valor do cateto adjcente: ")))

# 017
#from math import radians, sin, cos, tan
def angulos(a):
    sen = sin(radians(a))
    cos = cos(radians(a))
    tg = tan(radians(a))
    print("Ângulo {}\nSeno: {:.2f}.\nCoseno: {:.2f}.\nTangente: {:.2f}.".format(a, sen, cos, tg))
#angulos(float(input("Digite um angulo: ")))

#018
#import random
#import numpy as np
def sorteio():
    x = []
    for i in range(1, 5):
        x.append(np.array(input("Nome do aluno {}: ".format(i))))
    print("O aluno sorteado é: ", random.choice(x))
# sorteio()

# 019
def sorteioApres():
    x = []
    for i in range(1, 5):
        x.append(np.array(input("Nome do aluno {}: ".format(i))))
    random.shuffle(x)
    for a in range(0, 4):
        print("A aprensentação {} será feita por: {}\n".format(a, x[a]))

#sorteioApres()

# 020
#import playsound
def abrirmp3():
    playsound.playsound("C:\\Universidade\\programação\\projeto-glass-html5\\_media\\musica-lofi.mp3")
#abrirmp3()
# 022
def leianome():
    nome = str(input("Digite seu nome: ")).strip()
    print(nome.upper())
    print(nome.lower())
    print(len(nome) - nome.count(" ")) #correção do guanabara
    div = nome.split()
    print(len(nome[0]))
#leianome()

# 023
def separaNum():
    x = input("Digite um número entre 0 e 9999: ")
    if (len(x) == 4):
        print("unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}".format(x[3], x[2], x[1], x[0]))
    elif (len(x) == 3):
        print("unidade: {}\ndezena: {}\ncentena: {}".format(x[2], x[1], x[0]))
    elif (len(x) == 2):
        print("unidade: {}\ndezena: {}".format( x[1], x[0]))
    else:
        print("unidade: {}".format(x[0]))
#separaNum()

# 024
def findSanto():
    div = input("Digite o nome da cidade: ").split()
    if (div[0].lower() == 'santo'):
        print("Começa com Santo")
    else:
        print("Não começa com Santo")
#findSanto() 
def findSanto2():    # correção do guanabara
    div = input("Digite o nome da cidade: ").strip()
    if (div[:5].lower() == 'santo'):
        print("Começa com Santo")
    else:
        print("Não começa com Santo")
#findSanto2()

# 025
def acheSilva():
    nome = input("Digite seu nome: ").lower()
    if (nome.find("silva") >= 0):
        print("É um SILVA!!!")
    else:
        print("Não é um Silva...")
#acheSilva()

def acheSilva2():
    nome = input("Digite seu nome: ").lower()
    if ("silva" in nome):
        print("É um SILVA!!!")
    else:
        print("Não é um Silva...")
#acheSilva2()

# 026
def lerFrase():
    frase = input("Digite uma frase:\n").lower().strip()
    print("A letra 'a' aparece {} vezes".format(frase.count('a')))
    print("A letra 'a' aparece pela primeira vez na posição ", frase.find('a')+1)
    print("A letra 'a' aparece pela última vez na posição ", frase.rfind('a')+1)
#lerFrase()

# 027
def separaNome():
    nome = input("Digite seu nome: ").lower().title().split()
    print(nome[0], nome[-1])
#separaNome()

from random import choice
# 028
def adivinhar():
    x = "1 2 3 4 5".split()
    a = choice(x)
    b = input("Digite um número de 1 a 5: ")
    if b == a:
        print("Você acertou! Pensei no número {}".format(a))
    else:
        print("Você errou. Pensei no número {}. Tente novamente".format(a))
#adivinhar()

# 029
def multa():
    vel = int(input("Digite a velocidade do carro: "))
    multa = (vel - 80)*7
    if (vel > 80):
        print("Você ultrapassou o limite de velocidade. Multa: R${:.2f}".format(multa))
    else:
        print("Você está dentro do limite de velocidade")
#multa()

# 029
def parImpar():
    num = int(input("Digite um número inteiro: "))
    par = num%2
    if (par == 0):
        print("{} é um número par".format(num))
    else:
        print("{} é um número impar".format(num))
#parImpar()

# 031
def viagem():
    x = int(input("Digite a distância em km: "))
    if (x >= 200):
        a = x*0.45
        print("Valor da passagem: ", a)
    else:
        b = x*0.5
        print("Valor da passagem: ", b)
#viagem()

# 032
def anoBi():
    x = int(input("Digite um ano: "))
    if (x%4 == 0):
        print("É um ano bissexto")
    else:
        print("Não é um ano bissexto")
#anoBi()

# 033
def omaior():
    a = int(input("Digite um número: "))
    b = int(input("Digite um número: "))
    c = int(input("Digite um número: "))
    if (a > b and a>c):
        print("Maior número: ", a)
        if b < c:
            print("Menor número: ", b)
        else:
            print("Menor número: ", c)
    elif (b > a and b>c):
        print("Maior número: ", b)
        if a < c:
            print("Menor número: ", a)
        else:
            print("Menor número: ", c)
    else:
        print("Maior número: ", c)
        if a < b:
            print("Menor número: ", a)
        else:
            print("Menor número: ", b)
#omaior()

# 034
def aumento():
    a = int(input("Digite um número: "))
    if (a> 1250):
        print("O seu novo salário é ", a*1.1)
    else:
        print("O seu novo salário é ", a*1.15)
# aumento()

# 035
def triangulo():
    a = float(input("Valor: "))
    b = float(input("Valor: "))
    c = float(input("Valor: "))
    if a < (b + c) and b < (a + c) and c < (a + b):
        print("Forma triangulo")
    else:
        print("Não forma triangulo")
triangulo()