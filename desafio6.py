
def converter_para_hms(segundos_totais):
    # divmod retorna (quociente, resto)
    horas, resto = divmod(segundos_totais, 3600)
    minutos, segundos = divmod(resto, 60)
    return horas, minutos, segundos

def converter_para_segundos(h, m, s):
    return (h * 3600) + (m * 60) + s

while True:
    print("\n--- Conversor de Tempo ---")
    print("1. Segundos -> Horas, Minutos e Segundos")
    print("2. Horas, Minutos e Segundos -> Segundos")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        total_s = int(input("Digite o total de segundos: "))
        h, m, s = converter_para_hms(total_s)
        print(f"Resultado: {h}h {m}min {s}s")

    elif opcao == '2':
        h = int(input("Horas: "))
        m = int(input("Minutos: "))
        s = int(input("Segundos: "))
        total_s = converter_para_segundos(h, m, s)
        print(f"Resultado: {total_s} segundos")

    elif opcao == '3':
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida!")
