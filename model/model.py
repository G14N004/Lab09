import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo=nx.DiGraph()
        self._nodi=DAO.getNodi()
        self._idMap={}
        for n in self._nodi:
            self._idMap[n.ID]=n


    def buildGraph(self,distanza):
        #aggiungo nodi
        self._grafo.clear()
        for arco in DAO.getArchi(distanza,self._idMap):
            self._grafo.add_node(arco.v1)
            self._grafo.add_node(arco.v2)
            self._grafo.add_edge(arco.v1,arco.v2, weight=arco.peso)
        #aggiungo archi

        #self.addArchi(distanza)

    def addArchi(self, distanza):
        archi=DAO.getArchi(distanza,self._idMap)
        for a in archi :
            self._grafo.add_edge(a.v1,a.v2,weight=a.peso)

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)


    def stampaArchi(self,distanza):
        return  DAO.getArchi(distanza,self._idMap)

    def getGrafo(self):
        return self._grafo










