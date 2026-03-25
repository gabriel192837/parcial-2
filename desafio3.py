# Criamos uma lista vazia para guardar os nomes
nomes = []

print("Digite os 5 nomes desejados:")

# Criamos um laço que vai rodar 5 vezes
for i in range(5):
    # O input lê o que o usuário digita
    nome_escolhido = input(f"Digite o {i+1}º nome: ")
    # O append adiciona o nome no final da lista
    nomes.append(nome_escolhido)

print("\n--- Lista de nomes escolhidos ---")

# Imprimindo a lista final
for nome in nomes:
    print(nome)
