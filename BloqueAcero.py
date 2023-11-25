import Bloque

class BloqueAcero(Bloque):
    def __init__(self):
        super().__init__((169, 169, 169), 50, 50)

    def metodo_especifico_acero(self):
        print("Método específico de bloque de acero")