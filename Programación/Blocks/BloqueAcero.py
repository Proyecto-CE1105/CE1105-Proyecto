import Blocks.Bloque as Bloque

# Clase Bloque de Acero (clase hija de Bloque)
class BloqueAcero(Bloque):
    def __init__(self):
        super().__init__((169, 169, 169), 50, 50)  # Color gris claro

    def metodo_especifico_acero(self):
        print("Método específico de bloque de acero")