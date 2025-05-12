 Decodificador MARIE (Machine Architecture that is Really Intuitive and Easy)
 - É uma arquitetura de computador simplificada, criada para fins educacionais
- Foi desenvolvida para ajudar estudantes a entenderem conceitos básicos de arquitetura de computadores
- O nome é um acrônimo para "Machine Architecture that is Really Intuitive and Easy"

 Principais caracteristicas

1. Formato de Instrução:

    - Usa palavras de 16 bits
    - 4 bits para opcode (código da operação)
    - 12 bits para endereço de memória

------------------------------------------------------------------------------------------------------------------------

2. Conjunto de instruções básicas:

2.1 Instruções de Transferência de Dados:

- Load (0001):    Carrega um valor da memória para o acumulador (AC)
- Store (0010):   Armazena o valor do AC na memória
- LoadI (1101):   Carregamento indireto (carrega usando endereço armazenado na memória)
- StoreI (1110):  Armazenamento indireto (armazena usando endereço armazenado na memória)

2.2 Instruções Aritméticas:

- Add (0011):     Soma um valor da memória ao AC
- Sub (0100):     Subtrai um valor da memória do AC
- AddI (1011):    Adição indireta (soma usando endereço armazenado na memória)
- Clear (1010):   Zera o valor do AC (AC = 0)

2.3 Instruções de I/O:

- Input (0101):   Lê um valor do dispositivo de entrada para o AC
- Output (0110):  Envia o valor do AC para o dispositivo de saída

2.4 Instruções de Controle de Fluxo:

- Halt (0111):    Para a execução do programa
- Skipcond (1000): Pula a próxima instrução baseado em uma condição:
                    - Se bits[11-10] = 00, pula se AC < 0
                    - Se bits[11-10] = 01, pula se AC = 0
                    - Se bits[11-10] = 10, pula se AC > 0
- Jump (1001):    Salta para o endereço especificado
- JumpI (1100):   Salto indireto (salta para endereço armazenado na memória)
- JnS (1111):     Jump and Store - Armazena o endereço de retorno e salta

------------------------------------------------------------------------------------------------------------------------

Detalhes Adicionais:

1.Formato das Instruções:

   [4 bits do opcode][12 bits do endereço/operando]

2. Exemplo de Uso com Códigos Binários:

   Load X     -> 0001 XXXXXXXXXXXX  (Carrega valor do endereço X)
   Store X    -> 0010 XXXXXXXXXXXX  (Armazena AC no endereço X)
   Add X      -> 0011 XXXXXXXXXXXX  (AC = AC + M[X])
   Sub X      -> 0100 XXXXXXXXXXXX  (AC = AC - M[X])

3. Características Especiais das Instruções Indiretas:

   LoadI:  AC ← M[M[X]]   (Carrega valor do endereço apontado por X)
   StoreI: M[M[X]] ← AC   (Armazena AC no endereço apontado por X)
   JumpI:  PC ← M[X]      (Salta para endereço armazenado em X)
   AddI:   AC ← AC + M[M[X]] (Soma valor do endereço apontado por X)

4. Exemplo de Programa Completo:

   Load 20     # 0001 000000010100  (Carrega valor do endereço 20)
   Add 21      # 0011 000000010101  (Soma valor do endereço 21)
   Store 22    # 0010 000000010110  (Armazena resultado no endereço 22)
   Output      # 0110 000000000000  (Mostra resultado)
   Halt        # 0111 000000000000  (Finaliza programa)

5. Uso do JnS (Jump and Store):

   JnS X:

     1. Armazena (PC + 1) no endereço X
     2. Salta para o endereço X + 1

------------------------------------------------------------------------------------------------------------------------

1. Funcionamento:

- O decodificador converte instruções em linguagem de montagem para código binário
- Cada instrução é convertida em um formato de 16 bits
- O programa verifica se os números estão dentro do intervalo válido (0-4095)
- Gera uma representação binária das instruções

------------------------------------------------------------------------------------------------------------------------
 Exemplo de Uso

    > Load 15      |     #Resulta em: 0001 000000001111
    > Add 20       |     #Resulta em: 0011 000000010100
    > Store 25     |     #Resulta em: 0010 000000011001
    > Halt         |     #Resulta em: 0111 000000000000



