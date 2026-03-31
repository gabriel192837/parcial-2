def adicionar(x, y): return x + y
def subtrair(x, y): return x - y
def multiplicar(x, y): return x * y
def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

print("--- Calculadora Simples ---")
print("Escolha a operação:")
print("1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair")

while True:
    escolha = input("\nDigite o número da operação (1/2/3/4/5): ")

    if escolha == '5':
        print("Saindo... Até logo!")
        break

    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))

            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    else:
        print("Opção inválida!")
