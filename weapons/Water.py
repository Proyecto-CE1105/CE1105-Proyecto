import pygame

width, height = 500, 400

class Water(pygame.sprite.Sprite):

    water_count = 5
    def __init__(self,waterDir,tankRect,MainWindow):
        super().__init__()
        self.direccion = waterDir
        self.tankPos = tankRect
        self.pantalla =MainWindow
        self.original_image = pygame.image.load("Assets/Weapons/waterball.png")
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = -self.rect.height

    def update(self):
        if self.direccion=="up":
            self.rect.y -= 1
            if self.rect.bottom < 0:
                self.kill()
        elif self.direccion=="down":
            self.rect.y += 1
            if self.rect.top > self.pantalla.get_height():
                self.kill()
        elif self.direccion=="left":
            self.rect.x -= 1
            if self.rect.right < 0:
                self.kill()
        elif self.direccion=="right":
            self.rect.x += 1
            if self.rect.left > self.pantalla.get_width():
                self.kill()
    def place_water(self):
        if Water.can_place_water():
            self.rect.center = self.tankPos.center
            Water.water_count -= 1

    @staticmethod
    def can_place_water():
        return Water.water_count > 0

    def get_left(self):
        return self.rect.left

    def get_right(self):
        return self.rect.right

    def get_top(self):
        return self.rect.top

    def get_bottom(self):
        return self.rect.bottom
