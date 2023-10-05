import pygame, sys, JsonController, Button
from pygame import *

import Entry
import GUIController

pygame.init()

#Create window and refactor name
MainWindow = pygame.display.set_mode((1200, 650))
pygame.display.set_caption('Eagle Defender')

#Set icon
icono=pygame.image.load("imagenes/logo.jpg")
pygame.display.set_icon(icono)

#Set background
bg = pygame.image.load("imagenes/Background.png")

#Elements displayed on MainWindow
buttonPlay = Button.Button(200,200,150,50, '', (255,0,255))
user_entry = Entry.Entry((255,255,0),(255,0,255),(255,0,255),'',False)

WantToShowObjects=True

#Run while true the window and also update it
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() #Close the window

        #Check the mouse events
        if event.type == MOUSEBUTTONDOWN and event.button == 1: #Check if the mouse was pressed with the left key
            if buttonPlay.is_clicked(mouse.get_pos()):
                WantToShowObjects = False

            #This checks the events related with the user_entry
            if user_entry.is_clicked(mouse.get_pos()):
                user_entry.color = user_entry.colorActive
                user_entry.activeness = True
            else:
                user_entry.color = user_entry.colorPassive
                user_entry.activeness = False

        #This allow us to write in the entry
        if event.type == pygame.KEYDOWN:
            if user_entry.activeness == True:
                if event.key == pygame.K_BACKSPACE:
                    user_entry.text = user_entry.text[:-1] #Remove the last letter
                else:
                    user_entry.text += event.unicode #Add a new letter
    MainWindow.blit(bg, (0, 0))  # Show the background

    #This is for eliminate or create objects in the window
    if WantToShowObjects==True:
        if buttonPlay.is_clicked(mouse.get_pos()):
            buttonPlay.color = (255, 255, 100)
            buttonPlay.drawButton(MainWindow)
        else:
            buttonPlay.color = (255, 0, 255)
            buttonPlay.drawButton(MainWindow)

    user_entry.drawEntry(MainWindow)
   # input_user.w = max(100, user_text_entry.get_width() +100)




    pygame.display.update()