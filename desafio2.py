# Passo 1: peça o valor ao usuário
numero = int(input("Insira um número inteiro para a verificação: "))

# Passo 2: confirme o resto da divisão por 2
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
