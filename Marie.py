# Opcodes em Binário, Decimal/ Hexadecimal
opcodes = {
    "Load"     : "0001", # 1  /  1
    "Store"    : "0010", # 2  /  2
    "Add"      : "0011", # 3  /  3
    "Sub"      : "0100", # 4  /  4
    "Input"    : "0101", # 5  /  5
    "Output"   : "0110", # 6  /  6
    "Halt"     : "0111", # 7  /  7
    "Skipcond" : "1000", # 8  /  8
    "Jump"     : "1001", # 9  /  9
    "Clear"    : "1010", # 10 /  A
    "AddI"     : "1011", # 11 /  B
    "JumpI"    : "1100", # 12 /  C
    "LoadI"    : "1101", # 13 /  D
    "StoreI"   : "1110", # 14 /  E
    "JnS"      : "1111"  # 15 /  F
}

def verificacao_de_num_valido(numero):
    try:
        num = int(numero)
        if num >= 0 and num <= 4095:
            return num
        raise ValueError(f"Número {num} fora do intervalo válido (0-4095)")
    except ValueError:
        raise ValueError(f"'{numero}' não é um número válido")

# conversão binário pra 12 bits
def dec_12bit(numero):
    num = verificacao_de_num_valido(numero)
    return format(num, '012b')

# Usuario Entrada ( no data )
print("Inicialização do Decodificador MARIE ('Machine Architecture that is Really Intuitive and Easy')\n")
print("Para finalizar o programa digite 'Halt' ")

linhas = []
while True:
    linha = input("> ")
    if linha.strip().upper() == "HALT":
        break
    if linha.strip():
        linhas.append(linha)

instrucoes_binarias = []

# Processamento
for linha in linhas:
    try:
        linha = linha.strip()
        partes = linha.split()
        instrucao = partes[0]

        # Validação de inputs
        if instrucao not in opcodes:
            print(f"Comando inválido: {instrucao}")
            continue

        opcode = opcodes[instrucao]

        if len(partes) == 2:
            try:
                numero = partes[1]
                endereco_binario = dec_12bit(numero)
            except ValueError as e:
                print(f"Erro: {str(e)}")
                continue
        else:
            endereco_binario = "000000000000"

        linha_final = f"{opcode} {endereco_binario}"
        instrucoes_binarias.append(linha_final)
    except Exception as e:
        print(f"Erro ao processar linha: {str(e)}")

# Saída
for instrucao in instrucoes_binarias:
    print(instrucao)
    print("0111 000000000000")

