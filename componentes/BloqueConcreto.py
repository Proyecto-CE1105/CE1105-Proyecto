from componentes.Bloque import Bloque

# Clase Bloque de Concreto (clase hija de Bloque)
class BloqueConcreto(Bloque):
    def __init__(self, x, y, width, hegth):
        super().__init__((169, 169, 169), 50, 50, )  # Color gris claro
        self.vida = 100

    def metodo_especifico_concreto(self):
        print("Método específico de bloque de concreto")

    def bajar_vida(self, ataque):
        self.vida -= ataque
        if self.vida <=0:
            self.kill()
