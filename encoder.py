from xml.dom import minidom

def encode(mt, palavra):
    maquina_xml = minidom.parse(mt)

    
    tipo = maquina_xml.getElementsByTagName("type").item(0)
    if tipo.firstChild.data != 'turing':
        print("ISSO NÃO É UMA MÁQUINA DE TURING")
    

    transicoes = maquina_xml.getElementsByTagName("transition")

    resposta = []

    simbolos = []

    for transicao in transicoes:
        origem = transicao.getElementsByTagName("from").item(0)
        destino = transicao.getElementsByTagName("to").item(0)
        leitura = transicao.getElementsByTagName("read").item(0)
        escrita = transicao.getElementsByTagName("write").item(0)
        movimento = transicao.getElementsByTagName("move").item(0)
        
        origem = int(origem.firstChild.data)
        destino = int(destino.firstChild.data)
        leitura = leitura.firstChild.data if leitura.hasChildNodes() else None
        escrita = escrita.firstChild.data if escrita.hasChildNodes() else None
        movimento = movimento.firstChild.data
        
        if '!' in leitura:
            print("MÁQUINA DE TURING NÃO PODE USER O OPERADOR '!' DO JFLAP")
            return
        if escrita == '~':
            print("MÁQUINA DE TURING NÃO PODE USER O OPERADOR '~' DO JFLAP")
            return
        if movimento == 'S':
            print("MÁQUINA DE TURING NÃO PODE USAR O MOVIMENTO 'S' PORQUE O BRUNO NÃO ESPECIFICOU")
            return

        if leitura and leitura not in simbolos:
            simbolos.append(leitura)

        if escrita and escrita not in simbolos:
            simbolos.append(escrita)

        # print("Leitura: ", leitura, " - Escrita: ", escrita)

        codigo = "q1" + ('1' * origem)

        codigo += 'a1' + ('1' * simbolos.index(leitura)) if leitura else 'b'

        codigo += 'a1' + ('1' * simbolos.index(escrita)) if escrita else 'b'

        codigo += movimento

        codigo += 'q1' + ('1' * destino)o)])

        resposta.append(codigo)
        # print(codigo)
        # print(origem, "-", destino, "-", leitura, "-", escrita, "-", movimento)

    palavra_final = ''

    for caracter in palavra:
        if caracter not in simbolos:
            simbolos.append(caracter)
        palavra_final += 'a1' + ('1' * simbolos.index(caracter)) 

    print("\nResultado:\n")
    print('#'.join(resposta) + '$' + palavra_final)

    print('\n--------------------------------\n\nTabela de símbolos:\n')

    for indice, simbolo in enumerate(simbolos):
        print(simbolo, "equivale a", 'a1' + ('1' * indice))


print("CONVERSOR DE MÁQUIDA DE TURING DO JFLAP PARA AS ESPECIFICAÇÕES DO TRABALHO DO BRUNO\n")

file = input("Entre com o nome do arquivo: ")
word = input("Entre com a palavra da máquina: ")

encode(file, word)