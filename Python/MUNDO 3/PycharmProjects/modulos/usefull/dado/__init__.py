def leiaDinheiro(n):
    if not n.isnumeric():
        while True:
            number = str(input(n)).replace(',','.').strip()
            if number.isalpha() or number == '':
                print('\033[31m' + 'ERRO! O dado informado "' + number + '" não é um valor válido!' + '\033[0;0m')
            else:
                return (float(number))
                break