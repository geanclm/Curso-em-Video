def leiaDinheiro(n):
    if not n.isnumeric():
        while True:
            number = str(input(n)).replace(',','.').strip()
            if number.isalpha() or number == '':
                print('\033[31m' + 'ERRO! O dado informado "' + number + '" não é um valor válido!' + '\033[0;0m')
            else:
                return (float(number))
                break

def arquivo(arq):
    # função para verificar existência do arquivo
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(arq):
    # função para criar o arquivo
    try:
        a = open(arq, "w+")
        a.close()
    except:
        print('ERRO ao criar o arquivo!')
    else:
        print(f'Arquivo {arq} criado com sucesso!')

def zerar():
    # zerar arquivo
    with open("dados.txt", "w") as arquivo:
        arquivo.write('')

def escreverArquivo(arq):
    # adicionar dados
    from usefull.number import leiaInt
    try:
        a = open(arq,"at")
        nome = input('Nome para cadastro: ')
        idade = leiaInt(f'Idade de {nome} dados: ')
        a.write(f'{nome};{idade}\n')
    except:
        print('ERRO ao gravar dados no arquivo!')
    else:
        print('Novo registro adicionado no arquivo.')
        a.close()

def lerArquivo(arq):
    from usefull.moeda import textoAlinhado
    try:
        a = open(arq, "rt")
    except:
        print('ERRO ao ler o arquivo!')
    else:
         textoAlinhado('    PESSOAS CADASTRADAS     ')
         for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
    finally:
        a.close()