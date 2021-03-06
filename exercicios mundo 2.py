# Exercicios do Curso em Video de Python Mundo 2
# 036
from asyncio.windows_events import NULL
from math import factorial
from numpy import append, median

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
        print("\033[1;33mO número em binário é: {:b}\033[m".format(num))
    elif modo == 2:
        print("\033[1;33mO número em octal é: {:o}\033[m".format(num))
    elif modo == 3:
        print("\033[1;33mO número em hexadecimal é: {:X}\033[m".format(num))
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
        data = ano + 17
        print("Você já passou {} anos da idade de se alistar. Você deveria ter se alistado em {}".format(tempo, data))
    else:
        futuro = (-17 + idade)*-1
        dataf = ano + futuro
        print("Faltam {} anos para você se alistar. Você deve se alistar em {}".format(futuro, dataf))
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
        if a == b == c:
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
    peso = float(input("Digite seu peso [kg]: "))
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
    print("="*15, "Loja", "="*15)
    valor = float(input("Digite o valor do produto: R$"))
    pag = int(input("FORMAS DE PAGAMENTO\n[1] Dinheiro\n[2] Cartão\nDigite a forma de pagamento: "))
    #\n2x no cartão: 3\n3x ou mais no cartão: 4\n"))
    if pag == 1:
        print("O produto tem desconto de 10 por cento e sai por R${:.2f}".format(valor*0.9))
    elif pag == 2:
        print("[1] À vista\n[2] Parcelado em 2x\n[3] Parcelado em 3x ou mais")
        parcela = int(input("Digite a forma de pagamento: "))
        if parcela == 1:
            print("O produto tem desconto de 5 por cento e sai por R${:.2f}".format(valor*0.95))
        elif parcela == 2:
            print("O produto não tem desconto e sai por R${:.2f}".format(valor))
        elif parcela == 3:
            par = int(input("Em quantas vezes? (até 12x) "))
            if par <= 12:
                print("O produto recebe juros de 20 por cento e sai por R${:.2f}.\nParcelado em {} vezes, cada parcela é {}".format(valor*1.2, par, (valor*1.2)/par))
            else:
                print("Número de parcelas inválido. Tente novamente")
        else:
            print("Erro! Digite um método válido")
    else:
        print("Opção inválida. Tente novamente\n")
        desconto()
#desconto()

# 045
def jokenpo():
    from random import choice
    from time import sleep
    player = input("Escolha pedra, papel ou tesoura: ").strip().lower()
    maq = choice("pedra papel tesoura".split())
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!\n")
    print("="*20, "\n")
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
    else:
        print("Erro! Digite pedra, papel ou tesoura\n")
        jokenpo()
#jokenpo()

# 046
def anoNovo():
    from time import sleep
    for c in range(10, 0, -1):
        print(c)
        sleep(0.5)
        if c == 1:
            print("\U0001f386\U0001f37e"*10, "HAPPY NEW YEAR!", "\U0001f386\U0001f37e"*10)
#anoNovo()

# 047
def pares():
    for c in range(2, 51, 2):
        print(c, end =" ")
#pares()

# 048
def impares():
    s = 0
    cont = 0
    for c in range(1, 501, 2):
        if c%3 == 0:
            s += c
            cont += 1
    print("A soma de todos os números impares divisiveis por 3 ({}) de 1 a 500 é: {}".format(cont,s))
#impares()

# 049
def tabuada():
    x = int(input("Digite um número para saber sua tabuada: "))
    for c in range(1, 11):
        print("{} x {} = {}".format(x, c, x*c))
#tabuada()

# 050
def somadospares():
    y = 0
    a = 0
    for c in range(1, 7):
        x = int(input("[{}] Digite um número: ".format(c)))
        if x%2 == 0:
            y += x
            a += 1
    print("Você digitou {} números pares. A soma dos números pares digitados é: {}".format(a, y))
#somadospares()

# 051
def PA():
    a = int(input("Digite o primeiro termo da progressão aritmética: "))
    b = int(input("Digite a razão da progressão: "))
    print("="*20, "\nPA de {} com razão {}:".format(a, b))
    print(a, end = " ")
    for x in range(1, 10):
        print("{}".format(a + x*b), end = " ")
#PA()

# 052
def primo():
    x = int(input("Digite um número para saber se ele é primo: "))
    if x%x == 0 and x%2 != 0:
        for c in range(1, x+1):
            if c == x or c == 1 or x/c != NULL:
                print("\033[32m ", c, end = "\033[m ")
            else:
                print("\033[31m ", c, end = "\033[m ")
        print("\nEsse número é primo")
    else:
        soma = 0
        for b in range(1, x+1):
            if x%b == 0:
                print("\033[32m ", b, end = "\033[m ")
                soma += 1
            else:
                print("\033[31m ", b, end = "\033[m ")
        print("\nEsse número não é primo")
        print("O número {} foi divisível {} vezes".format(x, soma))
#primo()

# 053
def palindromo():
    frase = str(input("Digite uma frase: ")).strip()
    fraset = frase.lower().replace(" ", "")
    palindromo = fraset[-1]
    for c in range(len(fraset)-2, -1, -1):
        palindromo += fraset[c]
    if palindromo == fraset:
        print("A frase '{}' é um palindromo!".format(frase))
    elif palindromo != fraset:
        print("A frase '{}' não é um palindromo!".format(frase))
#palindromo()

def pal2(): ## resposta da internet
    frase = input("Qual é a frase?").upper().replace(" ", "")
    if frase == frase[::-1]:
        print("palindromo")
    else:
        print("Não é palindromo")
#pal2()

# 054
def osMaiores():
    from datetime import date
    ano = []
    atual = date.today().year
    soma = 0
    idades = []
    for c in range(1, 8):
        ano.append(int(input("Digite a idade da pessoa {}: ".format(c))))
    for b in range(0, 7):
        idades.append(int(atual - ano[b]))
    for i in range(0, 7):
        if (atual - ano[i]) >= 21:
            soma += 1
    print("Os anos relatados foram: {}\nAs idades relatadas foram: {}\nTotal de pessoas que são maiores de idade: {}\nTotal de pessoas que são menores: {}".format(ano, idades, soma, 7-soma))
#osMaiores()

# 055
def pesos():
    pesos = []
    for c in range(1, 6):
         pesos.append(int(input("Digite a peso da pessoa {}: ".format(c))))
    print("Os pesos inseridos foram: {}\nO maior peso é {} e o menor é {}".format(pesos, max(pesos), min(pesos)))
#pesos()

# 056
def osQuatro():
    nome = []
    idade = []
    sexo = [] 
    soma = 0
    for c in range(1, 5):
        nome.append(str(input("Digite o nome da pessoa {}: ".format(c).strip().capitalize())))
        idade.append(int(input("Digite a idade da pessoa {}: ".format(c))))
        sexo.append(str(input("Digite o sexo da pessoa {}: ".format(c))).strip())
    print("A média de idade do grupo é: ", (median(idade[0:3])))
    for m in range(0, 4):
        if idade[m] == max(idade) and sexo[m] == 'h':
            print("O homem com maior idade é {} com {} anos".format(nome[m].capitalize(), idade[m]))
        if idade[m] < 20 and sexo[m] == 'm':
            soma += 1
    print("Quantidade de mulheres com menos de 20 anos: ", soma)
#osQuatro()

#Aula 014
# 057
def sexo ():
    sexo = input("Digite seu sexo [M/F]: ").lower().strip()[0]
    if sexo not in "MmFf":
        while sexo != 'm' and sexo != 'f':
            print ("Digite M ou F")
            sexo = input("Digite seu sexo [M/F]: ").lower()
    if sexo in 'Mm':
        print("Você é do sexo masculino")
    else:
        print("Você é do sexo feminino")
#sexo()

# 058 28 melhorado
from random import choice
def adivinhe():
    opcoes = "1 2 3 4 5 6 7 8 9 10".split()
    computador = choice(opcoes)
    palpites = 1
    jogador = input("Pensei em um número de 1 a 10. Tente adivinhar: ")
    if jogador != computador:
        while jogador != computador:
            jogador = input("Você errou! Tente novamente\nDigite um número de 1 a 10: ")
            palpites += 1
    if palpites == 1:
        print("Você acertou de primeira! Pensei no número {}".format(computador))
    else:
        print("Agora você acertou! Você levou {} palpites para acertar que pensei no número {}".format(palpites, computador))
#adivinhe()

# 059
def calculadora():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    exit = 0
    print("="*20, " Menu ", "="*20, "\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos valores\n[5] Sair do programa\n")
    while exit == 0:
        opcao = int(input("Digite a operação a ser realizada: "))
        if opcao == 1:
            print("A soma de {} e {} é igual a {}".format(num1, num2,num1+num2))
        elif opcao == 2:
            print("A soma de {} por {} é igual a {}".format(num1, num2,num1*num2))
        elif opcao == 3:
            if num1 > num2:
                print("{} é maior que {}".format(num1, num2))
            elif num1 < num2:
                print("{} é maior que {}".format(num2, num1))
            else:
                print("Os valores são iguais!")
        elif opcao == 4:
            print("Digite os valores novamente")
            num1 = int(input("Digite o primeiro valor: "))
            num2 = int(input("Digite o segundo valor: "))
        elif opcao == 5:
            print("Programa encerrado")
            exit += 1
        else:
            print("Digite uma opção válida")
            calculadora()        
#calculadora()

# 060
def inserirNum():
    x = int(input("Digite um número: "))
    return x

def fatorial():
    num1 = inserirNum()
    fat = 1
    print("Fatorial de {}!: ".format(num1), end = "")
    for p in range(num1, 0, -1):
        fat = fat*p
        if p == num1:
            print("{}".format(p), end="")
        else:
            print("x{}".format(p), end="")
    print(" = {}".format(fat))
#fatorial()

def fatorialWhile():
    num = inserirNum()
    seq = 0
    fact = 1
    print("Fatorial de {}: ".format(num), end = "")
    fatstr = ""
    while seq != num:
        seq += 1
        fact = fact*seq
        if seq == 1:
            fatstr= fatstr + str(seq)
        else:
            fatstr= fatstr + "x" + str(seq)
    print(fatstr[::-1], "=", fact)  
#fatorialWhile()
def fatorialWhile2():
    num = inserirNum()
    seq = num
    fac = 1
    print("Fatorial de {}!: ".format(num), end = "")
    while seq > 0:
        print("{}x".format(seq), end = "")
        fac = fac * seq
        seq-= 1 
    print(" = {}".format(fac))
#fatorialWhile2()

# 061 51 melhorado
def PA2():
    ptermo = int(input("Digite o primeiro termo da progressão aritmética: "))
    razao = int(input("Digite a razão da progressão: "))
    print("="*20, "\nPA de {} com razão {}:".format(ptermo, razao))
    print(ptermo, end = " ")
    pa = 0
    while pa < 9:
        pa += 1
        print("{}".format(ptermo + pa*razao), end = " ")
#PA2()

# 062
def PA3():    
    pa = 0   
    termos = 1
    ptermo = int(input("Digite o primeiro termo da progressão aritmética: "))
    razao = int(input("Digite a razão da progressão: "))
    
    print("="*20, "\nPA de {} com razão {}:".format(ptermo, razao))
    print(ptermo, end = " ")
    
    while pa < 9:
        pa += 1
        print("{}".format(ptermo + pa*razao), end = " ")
    while termos > 0:    
        termos = int(input("\nDeseja ver mais termos? Digite a quantidade (Digite 0 para sair): "))
        if termos > 0:
            t = termos + pa
            while pa <= t:
                print("{}".format(ptermo + pa*razao), end = " ") 
                pa += 1
        else:
            print("Programa encerrado com {} termos mostrados.".format(t+1))
            termos = 0
#PA3()

# 063
def fibonacci():
    num = inserirNum()
    b = num - 1
    a = 0
    print(num, end = " ")
    while b != a:
        num = num+(num-1)
        a += 1
        print(num, end = " ")
#fibonacci()

def fibonacci2():
    num = inserirNum()
    t1 = 0
    t2 = 1
    t3 = 0
    c = 0
    print("{} - {} ".format(t1, t2), end = " ")
    while c <= num:
        t3 = t1 + t2
        print("{} - ".format(t3), end = "")
        t1 = t2
        t2 = t3
        c += 1
#fibonacci2()


# 064
def os999 ():
    num = 0
    soma = 0
    total = 0
    while num != 999:
        num = int(input("Digite um número (Digite 999 para sair): "))
        if num != 999:
            soma = soma + num
            total += 1
        else:
            print("Total de números digitados: {}\nSoma dos números digitados: {}".format(total, soma))
#os999()

# 065
def mediaSoma ():
    a = 1
    numero = []
    media = 0
    soma = 0
    while a > 0:
        num = inserirNum()
        numero.append(num)
        media = media + num
        soma += 1
        b = input("Quer continuar [S/N]: ").upper().strip()
        if b == "N":
            a = 0
            print("Números digitados: ", numero)
            print("A média entre os valores digitados é: {}\nO maior valor digitado é {}\nO menor valor digitador é {}".format(media/soma, max(numero), min(numero)))
#mediaSoma()



    
            


