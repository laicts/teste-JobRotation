
def inverteString(palavra):
    palavra_invertida = palavra[::-1]
    print(f'Palavra invertida: {palavra_invertida}')
    return palavra_invertida



inverteString(palavra = input('Digite uma palavra para ser invertida:'))