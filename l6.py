import math
import random
import pygame

# a baker throwing cakes to feed childrend mouth
SCREEN_WIDTH= 800
SCREEN_HEIGHT= 500
PLAYER_START_X= 370
PLAYER_START_Y= 380
CHILDREN_START_Y_MIN=50
CHILDREN_START_Y_MAX=150
CHILDREN_SPEED_X=4
CHILDREN_SPEED_Y=40
CAKES_SPEED_Y=10
COLLISION_DISTANCE= 27

pygame.init()

screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background= pygame.image.load('bg.jpg')

pygame.display.set_caption(" Cakes catastophe")
icon=pygame.image.load('car.png')
pygame.display.set_icon(icon)

playerImg=pygame.image.load('baker.png')
playerX=PLAYER_START_X
playerY=PLAYER_START_Y
playerX_chnage = 0

childrenIng= []
childrenX= []
childrenY=[]
childrenX_change=[]
childrenY_chnage=[]
num_of_children= 6

for i in range(num_of_children):
    childrenIng.append(pygame.image.load('children.png'))
    childrenX.append(random.randint(0, SCREEN_WIDTH - 64))

    childrenY.append(random.randint(CHILDREN_START_Y_MIN, CHILDREN_START_Y_MAX))
    childrenX_change.append(CHILDREN_SPEED_X)
    childrenY_chnage.append(CHILDREN_SPEED_Y)


cakeImg= pygame.image.load('cake.png')
cakeX=0
cakeY= PLAYER_START_Y
cake_change= 0
cakeY_chnage= CAKES_SPEED_Y
cake_state= "ready"

score_value=0
font= pygame.font.Font(None, 32)
textX=10
textY=10

over_font= pygame.font.Font(None,64)

def show_score(x,y):
    score = font.render("Score : "+ str(score_value), True, (255,255,255))
    screen.bilit(score,(x.y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))

def player(x,y):
        screen.blit(playerImg, (x,y))

def children(x,y,i):
     screen.blit(children[i], (x,y))

def fire_cake(x,y):
     global cake_state
     cake_state=" fire"
     screen.blit(cakeImg, (x+16,y +10))

def isCollision(cakeX, cakeY, cakesX, cakesY):
     distance= math.sprt((cakesX - cakesX) ** 2 +(cakesY - cakesY) ** 2)
     return distance < COLLISION_DISTANCE

running = True
while running:
     screen.fill((0,0,0))
     screen.blit(background, (0,0))

     for event in pygame.event.get():
          if event.type ==pygame.QUIT:
               running= False

          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    playerX_chnage= -5
               if event.key == pygame.K_RIGHT:
                    playerX_chnage= 5
               if event.key == pygame.K_SPACE and cake_state == "ready":
                    bulletX = playerX
                    fire_cake(cakeX, cakeY)
          if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT,
     pygame.K_RIGHT]:
               playerX_chnage = 0

     playerX += playerX_chnage
     playerX= max(0, min(playerX, SCREEN_WIDTH - 64))

     for i in range(num_of_children):
          if childrenY[i] > 340:
               for j in range(num_of_children):
                    childrenY[j] = 2000
               game_over_text()
               break
          childrenX[i] += childrenX_change[i]
          if childrenX[i] <= 0 or childrenX[i] >= SCREEN_WIDTH -64:
             childrenX_change[i] *= -1
             childrenY[i] += childrenY_chnage[i]

          if isCollision(childrenX[i], childrenY[i], cakeX, cakeY):
             cakeY= PLAYER_START_Y 
             cake_state ="ready"
             score_value += 1
             childrenX[i] = random.randint(0, SCREEN_WIDTH - 64)
             childrenY[i] = random.randint(CHILDREN_START_Y_MIN, CHILDREN_START_Y_MAX)

          children(childrenX[i], childrenY[i], i)

     if cakeY <= 0:
          bulletY= PLAYER_START_Y
          cake_state =" ready" 
     elif cake_state == "fire":
          fire_cake(cakeX, cakeY)
          cakeY -= cakeY_chnage

     player(playerX, playerY)
     show_score(textX, textY)
     pygame.display.update()
pygame.quit()

     
     
    
     

     


   
