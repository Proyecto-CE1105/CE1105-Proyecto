import Bloque

# Clase Bloque de Madera (clase hija de Bloque)
class BloqueMadera(Bloque):
    def __init__(self):
        super().__init__((210, 105, 30), 50, 50)  # Color marrón

    def metodo_especifico_madera(self):
        print("Método específico de bloque de madera")