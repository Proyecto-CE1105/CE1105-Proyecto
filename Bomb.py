import pygame
import sys
from pygame.locals import *


width, height = 500, 400

class Bomb(pygame.sprite.Sprite):
    """
    A class representing a bomb in the game.

    Attributes:
        bomb_count (int): Variable to count the number of placed bombs.
    """

    bomb_count = 5

    def __init__(self):
        """
        Initialize a Bomb object.

        Original image is loaded and transformed to appropriate dimensions.

        Args:
            None

        Returns:
            None
        """
        super().__init__()
        self.original_image = pygame.image.load("imagenes/Bomb_Image.webp")
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = -self.rect.height

    def update(self):
        """
        Update the bomb's position.

        Moves the bomb upward and removes it if it goes off-screen.

        Args:
            None

        Returns:
            None
        """
        self.rect.y -= 1

        if self.rect.bottom < 0:
            self.kill()

    def place_bomb(self, mouse_position):
        """
        Place a bomb at the specified mouse position.

        Checks if a bomb can be placed and adjusts the bomb count.

        Args:
            mouse_position (tuple): The (x, y) position where the bomb is placed.

        Returns:
            None
        """
        if Bomb.can_place_bomb():
            self.rect.center = mouse_position
            Bomb.bomb_count -= 1

    @staticmethod
    def can_place_bomb():
        """
        Check if a bomb can be placed.

        Returns:
            bool: True if a bomb can be placed, False otherwise.
        """
        return Bomb.bomb_count > 0

