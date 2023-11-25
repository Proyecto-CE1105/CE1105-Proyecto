from componentes.Bloque import Bloque

# Clase Bloque de Concreto (clase hija de Bloque)
class BloqueConcreto(Bloque):
    def __init__(self):
        super().__init__((169, 169, 169), 50, 50)  # Color gris claro

    def metodo_especifico_concreto(self):
        print("Método específico de bloque de concreto")