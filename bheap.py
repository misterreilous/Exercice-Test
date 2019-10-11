# Ce fichier contient (au moins) cinq erreurs.
# Instructions:
# - tester jusqu'à atteindre 100% de couverture;
# - corriger les bugs;
#  - envoyer le diff ou le dépôt git par email.

##Cette classe implémente les tas

import hypothesis
from hypothesis import given
from hypothesis.strategies import integers, lists


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        j = i
        while j // 2 > 0:
          if self.heapList[j] < self.heapList[j // 2]:
             tmp = self.heapList[j // 2]
             self.heapList[j // 2] = self.heapList[j]
             self.heapList[j] = tmp
          j = j // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize) # premier bug ? percUp modifie la valeur qu'elle utilise

    def percDown(self,i):
      while (i * 2) <= self.currentSize: #troisième bug, serai-ce un supérieur ou égal ?
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      if self.currentSize == 0 : #bug là, si currentsize c'est 0
          return 0
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval #bug ici, erreur de frappe

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i) #deuxième bug, ce doit être percdown 
          i = i - 1

def Remplir(b,l) :
    for elem in l :
        b.insert(elem)

@given(lists(elements=integers()))
def test_insert(l) :
    b = BinHeap()
    Remplir(b,l)
    asse = True
    for i in range (1,b.currentSize+1) :
        j = 0
        n = len(l)
        boolean = False
        while j < n and boolean == False :
            if b.heapList[i] == l[j] :
                l.pop(j)
                boolean = True
            j = j+1
            if j == n and boolean == False :
                asse = False
    assert asse
    
@given(lists(elements=integers()))
def test_del_Min(l) :
    b = BinHeap()
    s = len(l)
    Remplir(b,l)
    if len(l) != 0 :
        min = l[0]
        for elem in l :
            if min > elem :
                min = elem
        mini = b.delMin()
        assert (mini == min and b.currentSize == s-1)
    else :
        assert True
@given(lists(elements=integers()))
def test_buildHeap(l) :
    s = len(l)
    b = BinHeap()
    c = BinHeap()
    Remplir(b,l)
    c.buildHeap(l)
    boolean = True
    for i in (0,s) :
        k = c.delMin()
        p = b.delMin()
        if k != p :
            boolean = False
    assert boolean