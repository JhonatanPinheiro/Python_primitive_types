#Faça um programa que leia algo pelo telcado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

a = input('Informe algo: ')

print(type(a));#Mostra o tipo da nossa variavel se é bool,str,int ou float

print(a.islower())


#Deixa a primeira inicial maiúscula.
print(a.capitalize())
#Procura quantas ocorrências da busca existem na String.
print(a.count('a'), end=' letras ( a ) \n')
#Verifica se a String inicia com determinado caractere, retornando verdadeiro ou falso.
print(a.startswith('jh'))
#Verifica se a String termina com determinado caractere, retornando verdadeiro ou falso.
print(a.endswith('tan'))

#Verifica se a String tem conteúdo alfa-numérico
print(a.isalnum())
#Verifica se a String tem o conteúdo apenas alfabético
print(a.isalpha())
#Verifica se a String tem o conteúdo minúsculo.
print(a.islower())
#Verifica se a String tem o conteúdo em maiúsculo
print(a.isupper())




b = input('\n------\n\nInforme B: ')
#Converte o conteúdo da String para minúsculo.
print(b.lower())
#Converte o conteúdo da String para maiúsculo.
print(b.upper())
#Inverte a situação da String.
print(b.swapcase())
#Converte para maiúscula todos os primeiros caracteres da String.
print(b.title())
#Une duas ou mais strings utilizando um delimitador.
print(";".join(("jhonatan","Silva")))




#Corta a String em uma lista, utilizando o espaço como delimitador
c = input('\n------\n\nInforme C: ')
print(c.split(";"))




d = input('\n-----\n\nInforme D:')
#Ajusta a String para a (quantidade de espaços) esquerda utilizando um tamanho determinado.
print(d.ljust(30))
#Ajusta a String para a (quantidade de espaços) direita utilizando um tamanho determinado.
print(d.rjust(30))
#Ajusta a String para o centro utilizando um tamanho determinado
print(d.center(30))
#Remove os espaços em branco do lado esquerdo de uma String
print(d.lstrip())
#Remove os espaços em branco do lado direito de uma String.
print(d.rstrip())
#Remove todos os espaços em branco de uma String
print(d.strip())
#Procura por uma ocorrência de determinado caractere em um String, e retorna o seu endereço dentro da String. Retornando -1 indica que não existe tal caractere na String.
print(d.find("Linda"))
#Procura por um caractere e substitui por outro.
print(d.replace("Slva","Silva"))
