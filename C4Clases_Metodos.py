class Stones:
    coleccion_de_piedras = []
    tipo = "Piedra"
    def __init__(self,name):
        self.name = name

        if len(Stones.coleccion_de_piedras) <= 4:
            Stones.coleccion_de_piedras.append(self)
        else:
            del Stones.coleccion_de_piedras[0]
            Stones.coleccion_de_piedras.append(self)

    @staticmethod
    def mostrar_coleccion():
        for piedra in Stones.coleccion_de_piedras:
            print(piedra.name)


ruby = Stones("Ruby")
Diamante = Stones("Diamante")
Zafiro = Stones("Zafiro")
Esmeralda = Stones("Esmeralda")
Perla = Stones("Perla")
print("Primera Coleccion")
Stones.mostrar_coleccion()
print("\n")

Geoda = Stones("Geoda")
print("Segunda Coleccion")
Stones.mostrar_coleccion()