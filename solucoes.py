# Arquivo: solucoes.py

import string

def sao_anagramas(string1, string2):
    """
    Verifica se duas strings são anagramas uma da outra, ignorando
    espaços e diferenças entre maiúsculas e minúsculas.
    """
    # Remove espaços e converte para minúsculas
    s1_limpa = string1.replace(" ", "").lower()
    s2_limpa = string2.replace(" ", "").lower()

    # Um anagrama deve ter o mesmo número de caracteres
    if len(s1_limpa) != len(s2_limpa):
        return False

    # Converte as strings em listas de caracteres, ordena e compara
    return sorted(s1_limpa) == sorted(s2_limpa)


def cifra_de_cesar(texto, deslocamento):
    """
    Aplica a Cifra de César a uma string, preservando a capitalização e
    caracteres que não sejam letras.
    """
    resultado = ""
    for char in texto:
        if 'a' <= char <= 'z':
            # Cifra letras minúsculas
            inicio_alfabeto = ord('a')
            posicao_original = ord(char) - inicio_alfabeto
            nova_posicao = (posicao_original + deslocamento) % 26
            novo_char = chr(inicio_alfabeto + nova_posicao)
            resultado += novo_char
        elif 'A' <= char <= 'Z':
            # Cifra letras maiúsculas
            inicio_alfabeto = ord('A')
            posicao_original = ord(char) - inicio_alfabeto
            nova_posicao = (posicao_original + deslocamento) % 26
            novo_char = chr(inicio_alfabeto + nova_posicao)
            resultado += novo_char
        else:
            # Mantém outros caracteres inalterados
            resultado += char
    return resultado


def encontrar_maior_palavra(frase):
    """
    Encontra a maior palavra em uma frase, ignorando a pontuação.
    Em caso de empate no comprimento, retorna a primeira palavra encontrada.
    """
    # Cria uma tabela de tradução para remover pontuação
    tabela_pontuacao = str.maketrans('', '', string.punctuation)
    frase_limpa = frase.translate(tabela_pontuacao)
    
    # Divide a frase em uma lista de palavras
    palavras = frase_limpa.split()

    if not palavras:
        return ""

    maior_palavra = ""
    tamanho_max = 0

    for palavra in palavras:
        if len(palavra) > tamanho_max:
            tamanho_max = len(palavra)
            maior_palavra = palavra
    
    return maior_palavra