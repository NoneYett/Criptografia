from unidecode import unidecode #biblioteca para trabalhar com dados de texto que estao em Unicode

def main():
    textoLingua = open("nove_noites.txt", 'r', encoding="utf8")   #abre o arquivo de texto para poder pegar a frequencia das letras na lingua portuguesa.
    freq = frequencia(textoLingua)    #descobre a frequencia das letras no portugues
    textoLingua.close()

    #exemplo para testar se o codigo esta funcionando
    codificado = encripta("estou testando meu codigo para o trabalho de matematica discreta", 7) 
    textoCriptografado = open("textoCriptografado.txt", 'w', encoding="utf8")
    textoCriptografado.write(codificado)
    textoCriptografado.close()

    textoCriptografado = open("textoCriptografado.txt", 'r', encoding="utf8")
    print(decodifica(textoCriptografado, freq)) #para o decodifica e passado o texto criptografado
    textoCriptografado.close()

def encripta(texto, desloc): #funcao para criptografado um texto
    str = ""

    for c in texto:
        if(c >= 'a' and c <= 'z'): #entra no if apenas se o caracter no momento for uma letra
            ascii = ord(c)  #pega o valor que o caracter representa na tabela ascii
            ascii += desloc #incremente esse valor igual ao deslocamento, equivamente a deslocar a letra para direita no alfabeto
            
            if(ascii > 122): ascii -= 26  #faz roda o deslocamento para o começo do alfabeto, caso o deslocamento passe da letra z
            
            str += chr(ascii)   #transforma novamente o valor ascii no caracter
        
        else: str += c  #caso não seja uma letra ele vai simplesmente adicionar devolta ao texto criptografado

    return str  #retorna o texto ja criptografado

def decripta(texto, desloc): #funcao para decripta um texto que esta criptografado
    str = ""

    for linha in texto:
        #faz o tratamento do texto
        linha = unidecode(linha).lower()   #deixa todo texto em minusculo

        for c in linha:
            if(c >= 'a' and c <= 'z'):  
                ascii = ord(c)   #a mesma logica da funcao encripta é usado para essa funcao
                ascii -= desloc  #a diferenca eh que o deslocamento agora decrementa o valor ascii, equivalente a mover para esquerda no alfabeto
                
                if(ascii < 97): ascii += 26
                
                str += chr(ascii)
            
            else: str += c

    texto.seek(0)
    return str  #retorna  texto decriptografado

def frequencia(texto):  #funcao para ver a frequencia de um texto no arquivo
    dic = dict()
    tam = 0

    for x in range(26): dic[chr(97 + x)] = 0    #atribui ao dicionario todas as letras do alfabeto

    for linha in texto:
        #faz o tratamento do texto
        linha = unidecode(linha).lower()   #deixa todo texto em minusculo
        
        for c in linha:
            if(c >= 'a' and c <= 'z'):  #entra no if apenas se o caracter for uma letra
                dic[c] += 1 #conta quantas vezes aquele caracter c apareceu
                tam += 1    #conta o numero total de caracteres

    for key in dic: dic[key] = dic[key]/tam #divide o valor de vezes que cada caracter aparece pelo numero de caracter total

    texto.seek(0)
    return dic  #retorna o dicionario com a frequencia de cara caracter

def decodifica(texto, freq):  #funcao para decodificar um texto codificado
    maiorfreq = 'a'
    maiortexto = 'a'
    
    for key in freq:    #procura qual a letra mais frequente nesse dicionario feito com a frequencia da lingua portuguesa
        if(freq[maiorfreq] < freq[key]): maiorfreq = key
        
    freqtexto = frequencia(texto) #ver qual a frequencia do texto codificado
    
    for key in freq:    #procura qual a letra mais frequente no texto codificado
        if(freqtexto[maiortexto] < freqtexto[key]): maiortexto = key

    desloc = ord(maiortexto) - ord(maiorfreq)#ver qual a diferenca de deslocamento entre a letra mais frequente no texto codificado e da lingua portuguesa

    str = decripta(texto, desloc) #decodiica o texto usando o deslocamento entre as letras mais frequentes
    return str  #retorna o texto decodificado


if(__name__ == '__main__'):
    main()
