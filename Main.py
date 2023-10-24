import pygame, sys, JsonController, Button, Entry, Label, FilesController, Player, Screens
from pygame import *
from pygame.sprite import Group

pygame.init()
MainWindow = pygame.display.set_mode((1200, 650))
pygame.display.set_caption('Eagle Defender')

# Set icon
icono=pygame.image.load("imagenes/logo.jpg")
pygame.display.set_icon(icono)

# Set background
bg = pygame.image.load("imagenes/Background.png")
bg2 = pygame.image.load("imagenes/bg2.jpg")

screen = Screens.Screens(MainWindow, bg)

screen.mainScreen()





