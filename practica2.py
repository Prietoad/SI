#Lista para datos
frecuencias = [27,16,4,56,22,2,78,45,36,13,12,7]
probabilidades = [0.3, 0.2, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

def calcular_huffman(frecuenciaDic):
    freq = sorted(frecuenciaDic.items(), key=lambda x: x[1], reverse=True)
    nodes = freq

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffmanCode = huffman_code_tree(nodes[0][0])

    print(' Char | Huffman code ')
    print('----------------------')
    for (char, frequency) in freq:
        print(' %-4r |%12s' % (char, huffmanCode[char]))
    return huffmanCode 

# Calculating frequency
def calculate_frecuency(source):
    freq = {}
    for c in source:
        if(c == "\n"):
            if " " in freq:
                freq[" "] += 2
            else:
                freq[" "] = 2
        else:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
    return freq

#Calcula la longitud media
def longitudBinaria(dicHuffman , frecuenciaDic):
    total = 0
    for freq in frecuenciaDic:
        total = total + frecuenciaDic[freq]
    
    suma = 0
    for i in dicHuffman:
        valor = len(dicHuffman[i]) * frecuenciaDic[i]
        suma = suma + valor
    return suma/total

#Ejercicio 1
for i in range(len(probabilidades)):
    probabilidades[i] = probabilidades[i] * 100

frecuenciaDic = {}
iterate = 0
for frecuencia in probabilidades:
    frecuenciaSimbolo = alphabet[iterate]
    frecuenciaDic[frecuenciaSimbolo] = frecuencia
    iterate += 1

print(frecuenciaDic)
huffman = calcular_huffman(frecuenciaDic)
print("\n")

longitudMedia = round(longitudBinaria(huffman, frecuenciaDic),5)
print("Longitud binaria media: "+ str(longitudMedia) + "\n")

#Ejercicio 2
frecuenciaDic = {}
iterate = 0
for frecuencia in frecuencias:
    frecuenciaSimbolo = alphabet[iterate]
    frecuenciaDic[frecuenciaSimbolo] =frecuencia
    iterate += 1

huffman = calcular_huffman(frecuenciaDic)
print("\n")

longitudMedia = round(longitudBinaria(huffman, frecuenciaDic),5)
print("Longitud binaria media: "+ str(longitudMedia) + "\n")

#Ejercicio 3
f = open("datos_2.txt")
fuente = f.read()

frecuenciaDic = calculate_frecuency(fuente) 

huffman = calcular_huffman(frecuenciaDic)

longitudMedia = round(longitudBinaria(huffman, frecuenciaDic), 5)
print("Longitud binaria media: "+ str(longitudMedia) + "\n")





