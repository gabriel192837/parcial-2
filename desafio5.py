
# Solicita os dados ao usuário
# Usamos float() para permitir números decimais (ex: 5.5)
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

# Realiza o cálculo
area = (base * altura) / 2

# Exibe o resultado
# O :.2f formata o número para ter apenas 2 casas decimais
print(f"\nA área do triângulo com base {base} e altura {altura} é: {area:.2f}")
