#Exemplo extra da aula 1 - Introdução a Data Science (Siraj Raval)
#Uso do algoritmo 'Árvore de Decisão' para identificar algumas cores
#Cores usadas foram encontradas em: http://erikasarti.com/html/tabela-cores/

from sklearn import tree 

X = [[106, 90, 205], [72, 61, 139], [128, 0, 0], [139, 0, 0], [255, 215, 0], 
                [25, 25, 112], [0, 0, 128], [178, 34, 34], [250, 128, 114], [240, 130, 140]]

Y = [['Azul'], ['Azul'], ['Vermelho'], ['Vermelho'], ['Amarelo'], 
               ['Azul'], ['Azul'], ['Vermelho'], ['Vermelho'], ['Amarelo']]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

predicao = clf.predict([[0, 0, 139], [255, 99, 71], [255, 255, 0]])

print(predicao)