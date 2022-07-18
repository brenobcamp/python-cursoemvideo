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
compraCasa()