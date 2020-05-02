import math
import pygame
import random
from pygame import mixer
pygame.init ( )

screen = pygame.display.set_mode ((800, 600))  # screen size

background = pygame.image.load ("sky.jpg")

pygame.display.set_caption ("EggsFunda")

icon = pygame.image.load ("icon_food.png")
pygame.display.set_icon (icon)

playerImg = pygame.image.load ("basket2.png")

# variables
playerX = 350
playerY = 460
playerX_change = 0

leave_count = 0
score = 0

eggImg = []
eggX = []
eggY = []
eggY_change = 4
# num_of_egg = 3

#Sound
back = mixer.Sound("background.wav")
back.play(-1)

# for i in range (num_of_egg):
eggImg.append (pygame.image.load ("food3.png"))
eggImg.append (pygame.image.load ("food3.png"))
eggImg.append (pygame.image.load ("food3.png"))

eggX.append (150)
eggX.append (400)
eggX.append (650)

eggY.append (random.randint (-50, 0))
eggY.append (random.randint (-10, 0))
eggY.append (random.randint (-30, 0))

font = pygame.font.Font ("freesansbold.ttf", 32)
Gfont = pygame.font.Font ("freesansbold.ttf", 64)


def gameOver():
    go = Gfont.render ("Game Over!", True, (255, 0, 0))
    screen.blit (go, (240, 250))


def scoreBoard():
    Scorefont = font.render ("Score: " + str (score), True, (30, 0, 255))
    screen.blit (Scorefont, (10, 10))


def isCollision(playerX, playerY, eggX, eggY):
    distance = math.sqrt (pow ((playerX - eggX), 2) + pow ((playerY - eggY), 2))
    if distance < 70:
        touch = mixer.Sound ("beep-07.wav")
        touch.play ( )
        return True
    else:
        return False


def player(x, y):
    screen.blit (playerImg, (x, y))


def egg(x, y, i):
    screen.blit (eggImg[i], (x, y))


running = True

while running:
    screen.blit (background, (0, 0))
    for event in pygame.event.get ( ):
        if event.type == pygame.QUIT:
            running = False

        # keystroke

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10

            if event.key == pygame.K_RIGHT:
                playerX_change = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change

    if playerX >= 736:
        playerX = 736
    elif playerX <= 0:
        playerX = 0

    for i in range (3):
        eggY[i] += eggY_change
        egg (eggX[i], eggY[i], i)

        if isCollision (playerX, playerY, eggX[i], eggY[i]):
            score += 10
            eggY[i] = random.randint (-100, 20)
        elif not isCollision (playerX, playerY, eggX[i], eggY[i]) and eggY[i] > 730:
            leave_count += 1
            broken = mixer.Sound("explosion.wav")
            broken.play()
            eggY[i] = random.randint (-100, 20)

        if leave_count > 20:
            for i in range(3):
                eggY_change = 0
            gameOver ( )
            break

    player (playerX, playerY)
    scoreBoard ( )
    pygame.display.update ( )
