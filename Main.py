import pygame, sys, JsonController, Button, Entry, Label, FilesController, Player
from pygame import *
from pygame.sprite import Group

pygame.init()

fps = 60
clock = pygame.time.Clock()
tanque = pygame.image.load("imagenes/Tank_Image.png")

# Create window and refactor name
MainWindow = pygame.display.set_mode((1200, 650))
pygame.display.set_caption('Eagle Defender')

# Set icon
icono=pygame.image.load("imagenes/logo.jpg")
pygame.display.set_icon(icono)

# Set background
bg = pygame.image.load("imagenes/Background.png")
bg2 = pygame.image.load("imagenes/bg2.jpg")

#File controller
FileDialog = FilesController.FileControllers(' ', ' ')

#Users controller
userFile = JsonController.JsonControllerUsers

# Elements displayed on MainWindow
buttonSignIn = Button.Button(650,300,150,50, 'Sign In', (86, 140, 255),30)
buttonSignUp = Button.Button(850,300,150,50, 'Sign Up', (86, 140, 255),30)
buttonEnter = Button.Button(740, 350, 100, 50, 'Enter', (86, 140, 255), 20)
buttonRegisterUser = Button.Button(740, 500, 150, 50, 'Register User', (111, 84, 247), 25)
buttonSelectSong = Button.Button(760, 400, 100, 25, 'Select Music', (86, 140, 255), 23)
buttonSelectPhoto = Button.Button(760, 450, 100, 25, 'Select Photo', (86, 140, 255), 23)

user_entry = Entry.Entry(750, 250, (8, 42, 79),(12, 76, 143),(12, 76, 143),'',False)
password_entry = Entry.Entry(750, 300, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
email_entry = Entry.Entry(750, 350, (8, 42, 79),(12, 76, 143),(12, 76, 143),'',False)

labelUser = Label.Label('User:',20,675,250,(0,0,0))
labelEmail = Label.Label('Email:',20, 675,350,(0,0,0))
labelPassword = Label.Label('Password:',20, 675,300, (0,0,0))
labelMusic = Label.Label('Music:',20, 675,400,(0,0,0))
labelPhoto = Label.Label('Photo:',20, 675,450,(0,0,0))
labelCharacter = Label.Label('Atacante',60, 700,180,(0,0,0))
labelShowGameScreen = Label.Label(str(user_entry.showText()),80, 10,10,(0,0,0))

tanqueSprite=Group()
mitanque= Player.Player(MainWindow)
tanqueSprite.add(mitanque)

WantToShowObjects = True
WantToShowObjectsSignIn = False
WantToShowObjectsSignUp = False
WantToPlay = False
Atacante= True
Defensor= False
listoDefensor = True

#song = pygame.mixer.music.load('Songs/Trouble.mp3')

# Run while true the window and also update it
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() # Close the window

        # Check the mouse events
        if event.type == MOUSEBUTTONDOWN and event.button == 1: # Check if the mouse was pressed with the left key
            if buttonSignIn.is_clicked(mouse.get_pos()):
                WantToShowObjects = False
                WantToShowObjectsSignIn = True
            if buttonSignUp.is_clicked(mouse.get_pos()):
                WantToShowObjects = False
                WantToShowObjectsSignUp = True
            if buttonSelectSong.is_clicked(mouse.get_pos()):
                FileDialog.music = FileDialog.selectFile()
            if buttonSelectPhoto.is_clicked(mouse.get_pos()):
                FileDialog.photo = FileDialog.selectFile()
            if buttonRegisterUser.is_clicked(mouse.get_pos()):
                userFile.addUsers(1,user_entry.text, email_entry.text, password_entry.text, FileDialog.music, FileDialog.photo)
            if buttonEnter.is_clicked(mouse.get_pos()):
                if userFile.verifyUser(0,user_entry.text,password_entry.text) and listoDefensor:
                    Atacante = False
                    Defensor = True
                    listoDefensor = False
                elif userFile.verifyUser(0,user_entry.text,password_entry.text):
                    WantToPlay = True
                    WantToShowObjectsSignIn = False

        # This checks the events related with the user_entry
        if user_entry.is_clicked(mouse.get_pos()):
            user_entry.color = user_entry.colorActive
            user_entry.activeness = True
        else:
            user_entry.color = user_entry.colorPassive
            user_entry.activeness = False

        # This checks the events related with the password_entry
        if password_entry.is_clicked(mouse.get_pos()):
            password_entry.color = password_entry.colorActive
            password_entry.activeness = True
        else:
            password_entry.color = password_entry.colorPassive
            password_entry.activeness = False

        # This checks the events related with the email_entry
        if email_entry.is_clicked(mouse.get_pos()):
            email_entry.color = email_entry.colorActive
            email_entry.activeness = True
        else:
            email_entry.color = email_entry.colorPassive
            email_entry.activeness = False

        if buttonEnter.is_clicked(mouse.get_pos()):
            buttonEnter.color = user_entry.colorActive
            buttonEnter.activeness = True
        else:
            buttonEnter.color = user_entry.colorPassive
            buttonEnter.activeness = False

        # This allow us to write in the entry
        if event.type == pygame.KEYDOWN:
            if user_entry.activeness == True:
                if event.key == pygame.K_BACKSPACE:
                    user_entry.text = user_entry.text[:-1] #Remove the last letter
                else:
                    user_entry.text += event.unicode #Add a new letter
            elif email_entry.activeness == True:
                if event.key == pygame.K_BACKSPACE:
                    email_entry.text = email_entry.text[:-1] #Remove the last letter
                else:
                    email_entry.text += event.unicode #Add a new letter

            elif password_entry.activeness == True:
                if event.key == pygame.K_BACKSPACE:
                    password_entry.text = password_entry.text[:-1] #Remove the last letter
                else:
                    password_entry.text += event.unicode #Add a new letter


        # This is for eliminate or create objects in the window
    if WantToShowObjects == True:
        MainWindow.blit(bg, (0, 0))  # Show the background
        if buttonSignIn.is_clicked(mouse.get_pos()):
            buttonSignIn.color = (2, 82, 253)
            buttonSignIn.drawButton(MainWindow)
            buttonSignUp.color = (86, 140, 255)
            buttonSignUp.drawButton(MainWindow)
        elif buttonSignUp.is_clicked(mouse.get_pos()):
            buttonSignUp.color = (2, 82, 253)
            buttonSignUp.drawButton(MainWindow)
            buttonSignIn.color = (86, 140, 255)
            buttonSignIn.drawButton(MainWindow)
        else:
            buttonSignIn.color = (86, 140, 255)
            buttonSignIn.drawButton(MainWindow)
            buttonSignUp.color = (86, 140, 255)
            buttonSignUp.drawButton(MainWindow)

    if WantToShowObjectsSignIn == True:
        MainWindow.blit(bg, (0, 0))  # Show the background
        if Atacante:
            labelCharacter.draw(MainWindow)
        if Defensor:
            labelCharacter.update_text("Defensor")
        labelCharacter.draw(MainWindow)
        user_entry.drawEntry(MainWindow)
        password_entry.drawEntry(MainWindow)
        buttonEnter.drawButton(MainWindow)

        labelUser.draw(MainWindow)
        labelPassword.draw(MainWindow)

    if WantToShowObjectsSignUp == True:
        MainWindow.blit(bg, (0, 0))  # Show the background
        user_entry.drawEntry(MainWindow)
        email_entry.drawEntry(MainWindow)
        password_entry.drawEntry(MainWindow)

        labelUser.draw(MainWindow)
        labelEmail.draw(MainWindow)
        labelPassword.draw(MainWindow)
        labelMusic.draw(MainWindow)
        labelPhoto.draw(MainWindow)

        buttonRegisterUser.drawButton(MainWindow)
        buttonSelectSong.drawButton(MainWindow)
        buttonSelectPhoto.drawButton(MainWindow)

        if buttonSelectSong.is_clicked(mouse.get_pos()):
            buttonSelectSong.color = (2, 82, 253)
            buttonSelectSong.drawButton(MainWindow)
            buttonSelectPhoto.color = (86, 140, 255)
            buttonSelectPhoto.drawButton(MainWindow)
            buttonRegisterUser.color = (111, 84, 247)
            buttonRegisterUser.drawButton(MainWindow)
        elif buttonSelectPhoto.is_clicked(mouse.get_pos()):
            buttonSelectSong.color = (86, 140, 255)
            buttonSelectSong.drawButton(MainWindow)
            buttonSelectPhoto.color = (2, 82, 253)
            buttonSelectPhoto.drawButton(MainWindow)
            buttonRegisterUser.color = (111, 84, 247)
            buttonRegisterUser.drawButton(MainWindow)
        elif buttonRegisterUser.is_clicked(mouse.get_pos()):
            buttonSelectSong.color = (86, 140, 255)
            buttonSelectSong.drawButton(MainWindow)
            buttonSelectPhoto.color = (86, 140, 255)
            buttonSelectPhoto.drawButton(MainWindow)
            buttonRegisterUser.color = (78, 42, 255)
            buttonRegisterUser.drawButton(MainWindow)
        else:
            buttonSelectSong.color = (86, 140, 255)
            buttonSelectSong.drawButton(MainWindow)
            buttonSelectPhoto.color = (86, 140, 255)
            buttonSelectPhoto.drawButton(MainWindow)
            buttonRegisterUser.color = (111, 84, 247)
            buttonRegisterUser.drawButton(MainWindow)

    if WantToPlay == True:
        user_entry.drawEntry(MainWindow)
        MainWindow.blit(bg2, (0, 0))
        labelShowGameScreen.draw(MainWindow)


        MainWindow.blit(pygame.transform.scale(pygame.image.load("imagenes/mapBack.jpg"), (500, 400)), (0, 00))
        clock.tick(fps)

        tanqueSprite.update(MainWindow)
        tanqueSprite.draw(MainWindow)


    pygame.display.update()