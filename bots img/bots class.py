import random
import pygame
pygame.init()

size = (1000,600)
screen = pygame.display.set_mode(size)
fps = 25
clock = pygame.time.Clock()
col = pygame.color.THECOLORS
crab = pygame.transform.scale(pygame.image.load('crab-2.png'),(50,50))
suriken = pygame.transform.rotozoom(pygame.image.load('bots img/shuriken.png'),0,0.1)
list_airbots = []
boss_count = 0
class AirBots:
    def __init__(self,x,y):
        self.y = y
        self.list = [i for i in range(x,x+101)] #координаты х по которым оно будет двигаться вперед
        self.reverse = self.list[::-1] # и обратно
        self.left = random.choice([True,False])
        self.c = 0
        self.count = random.randint(0,fps)
        self.rights = [pygame.transform.scale(pygame.image.load('bots img/bat_right_3.png'),(50,50)),
                       pygame.transform.scale(pygame.image.load('bots img/bat_right_2.png'),(50,50)),
                       pygame.transform.scale(pygame.image.load('bots img/bat_right_1.png'),(50,50))
                      ]
        self.lefts = [pygame.transform.scale(pygame.image.load('bots img/bat_left_3.png'),(50,50)),
                      pygame.transform.scale(pygame.image.load('bots img/bat_left_2.png'),(50,50)),
                      pygame.transform.scale(pygame.image.load('bots img/bat_left_1.png'),(50,50))
                      ]
    def blit(self):
        self.count %=fps
        if 0<=self.c<=100:
            if self.left:
                screen.blit(self.rights[self.count//9],(self.list[self.c],self.y))
            else:
                screen.blit(self.lefts[self.count//9],(self.reverse[self.c],self.y))
            self.c+=5
            self.count+=1
        else:
            self.left = not self.left
            self.c = 0
'''
class Shoot:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def blit(self):
        suriken = pygame.transform.rotozoom(pygame.image.load('bots img/shuriken.png'),0,0.1)
'''
def boss():
    global boss_count
    boss_x,boss_y = 300,size[1]*0.75 - 100
    steps = [pygame.transform.scale(pygame.image.load('bots img/step-1.png'),(70,100)),
             pygame.transform.scale(pygame.image.load('bots img/step-2.png'),(70,100)),
             pygame.transform.scale(pygame.image.load('bots img/step-3.png'),(70,100)),
             pygame.transform.scale(pygame.image.load('bots img/step-4.png'),(70,100))]
    boss_count %= fps
    screen.blit(steps[boss_count//7],(boss_x,boss_y))
    boss_count+=1
    
for i in range(4):
    list_airbots.append(AirBots(random.randint(100,500),size[1]*3//4-80))
done = False

while not done:
    screen.fill(col['white'])
    pygame.draw.line(screen,col['orange'],(100,size[1]*3//4),(size[0]*2//3,size[1]*3//4),50)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = not done
    for i in list_airbots:
        i.blit()
    screen.blit(crab,(500,400))
    boss()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
