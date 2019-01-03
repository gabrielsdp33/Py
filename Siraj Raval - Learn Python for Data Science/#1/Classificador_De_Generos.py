#Exercício aula 1 - Introdução a Data Science (Siraj Raval)

from sklearn import tree
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Dados e seus gênero respectivo
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['Masculino', 'Masculino', 'Feminino', 'Feminino', 'Masculino', 'Masculino', 'Feminino', 'Feminino', 'Feminino', 'Masculino', 'Masculino']

#Instâncias dos algoritmos de classificação
ClfTree = tree.DecisionTreeClassifier()
ClfSvm = SVC()
ClfKNN = KNeighborsClassifier()

# Treinos
ClfTree.fit(X, Y)
ClfSvm.fit(X, Y)
ClfKNN.fit(X, Y)

# Testes
PredicaoTree = ClfTree.predict(X)
PrecisaoTree = accuracy_score(Y, PredicaoTree) * 100
print('Precisão DecisionTree: {}'.format(PrecisaoTree))

PredicaoSVM = ClfSvm.predict(X)
PrecisaoSVM = accuracy_score(Y, PredicaoSVM) * 100
print('Precisão SVM: {}'.format(PrecisaoSVM))


PredicaoKNN = ClfKNN.predict(X)
PrecisaoKNN = accuracy_score(Y, PredicaoKNN) * 100
print('Precisão KNN: {}'.format(PrecisaoKNN))

#Escolha do melhor algoritmo
indiceDeMaiorPrecisao = np.argmax([PrecisaoTree, PrecisaoSVM, PrecisaoKNN])
Algoritmos = {0: 'Tree', 1: 'SVM', 2: 'KNN'}
print('O melhor algoritmo classificador de gêneros é: {}'.format(Algoritmos[indiceDeMaiorPrecisao])