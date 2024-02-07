# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a 
# soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma 
# mensagem avisando se o número informado pertence ou não a sequência.

number_choice = int(input('Digite um número inteiro'))

fibonacci_sequence = [0, 1]

for num in range(2, number_choice):
    fibonacci_sequence.append(fibonacci_sequence[num-1] + fibonacci_sequence[num-2])
    print(fibonacci_sequence)

if number_choice in fibonacci_sequence:
    print('Esse número está presente na sequência de Fibonacci')
else: 
    print('Número não está presente na sequência de Fibonacci')