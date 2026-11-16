"""
o programa será um verificador, o programa deverá verificar se a cidade onde eu morava começa com a palavra SANTA,
se sim, retorna true, se não, retorna false, o programa deverá ser capaz de identificar independente de haver espaço, 
letras de tamanhos diferentes
"""

palavra = input("cidade que voce morava: ").strip().upper()
lista_palavra = palavra.split()

print(lista_palavra[0] == "SANTA")