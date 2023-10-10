""" Fitxer que conté l'agent barca en profunditat.

S'ha d'implementar el mètode:
    actua()
"""
from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca, SENSOR


class BarcaProfunditat(Barca):
    def __init__(self):
        super(BarcaProfunditat, self).__init__()
        self.__oberts = list()
        self.__tancats = set()
        self.__accions = None

    def cerca(self):
        while len(self.__oberts) != 0:
            estado = self.__oberts.pop()
            if Estat.es_meta(estado):
                print(Estat.__str__(estado))
                return estado.accions_previes
            else:
                if (estado in self.__tancats) is False:
                    self.__tancats.add(estado)
                    if Estat.es_segur(estado):
                        self.__oberts = Estat.genera_fill(estado) + self.__oberts

        return -1

    def actua(
            self, percepcio: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        if self.__accions is None:
            self.__oberts.append(Estat(percepcio[SENSOR.LLOC], percepcio[SENSOR.LLOP_ESQ], percepcio[SENSOR.QUICA_ESQ]))
            self.__accions = self.cerca()
        if len(self.__accions) != 0:
            return AccionsBarca.MOURE, self.__accions.pop()
        return AccionsBarca.ATURAR
