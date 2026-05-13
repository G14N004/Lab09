from dataclasses import dataclass

from model.aeroporti import Aeroporti


@dataclass
class ArcoPesato:
    v1:Aeroporti
    v2:Aeroporti
    peso:int

    def __str__(self):
        return f"{self.v1.__str__()},{self.v2.__str__()} ---> distanza : {self.peso}"