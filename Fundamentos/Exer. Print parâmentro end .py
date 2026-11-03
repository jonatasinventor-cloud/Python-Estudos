# Exercício 02 - Modificação de Parâmetros end e sep

print("olá, mundo!", end=" <-> ")
print("Meu nome é Jônatas Nunes", end=" -> ")
print("Moro na Noruega")

# Utilizando o parãmetro sep para separar as palavras com o caractere "|"
# o sep="|"(separador) é utilizado para separar os argumentos passados para a função print() com o caractere "|" 
# mas não significa que eu tenha que usar o caractere "|" para separar as palavras, posso usar qualquer outro caractere ou até mesmo uma palavra.

print("Estou aprendendo Python" , " e estou testando a função print()",sep="|")

# o parâmetro sep="" pode ser alterado para colocar qualquer caracter dentro das aspas, aparecendo onde teria virgula.

print("Estou aprendendo Python" , " e estou testando a função print()",sep=" -\(6-6)/- ")

# o operador de concatenação "+" está somando números(em formato de texto) e juntando textos.(string)
# e estou personalizando o parâmetro end para colocar uma frase no final da linha, sem pular para a próxima linha.

print("Tenho:" + "5" + " anos de idade", end=" e eu sei que ")

# Realizando operações matemáticas dentro da função print(), nesse caso, o operador de soma "+" está somando números.
print("O resultado de 5 + 10 - 5 é:", 5 + 10 - 5) 