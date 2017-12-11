# Modulo para algoritmo de Disjoint Set - Union Find

class Node:
    def __init__(self, id):        
        self.parent = id
        self.rank = 0

class UnionFind:
    def __init__(self, size):
        self.nodes = list()
        for i in range(0, size):
            self.nodes.append(Node(i))
        
    def find(self, x):
        if self.nodes[x].parent != x:            
            self.nodes[x].parent = self.find(self.nodes[x].parent)
        return self.nodes[x].parent
        
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if self.nodes[xRoot].rank > self.nodes[yRoot].rank:
            self.nodes[yRoot].parent = xRoot
            return (xRoot, yRoot)
        elif self.nodes[xRoot].rank < self.nodes[yRoot].rank:
            self.nodes[xRoot].parent = yRoot
            return (yRoot, xRoot)
        elif xRoot != yRoot:            
            self.nodes[yRoot].parent = xRoot
            self.nodes[xRoot].rank += 1
            return (xRoot, yRoot)
        else:
            return (-1,-1)