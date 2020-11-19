import pygame as pg
import random
pg.init()
size=(1000,600)
screen = pg.display.set_mode(size)
block_size=35
fps=35
clock=pg.time.Clock()
x=240
y=200
camera_x=0
camera_y=0
class EarthBots:
    def __init__(self,x,y,animal):
        self.y = y
        self.list = [i for i in range(x,x+101)]
        self.reverse = self.list[::-1]
        self.c = 0
        self.animal = animal
        self.count = random.randint(0,fps)
        self.left = random.choice([True,False])
    def blit(self):
        if self.animal == 'bear':
            self.width,self.height = 80,70
        else:
            self.width,self.height = 60,50
        self.rights = [
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_left_1.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_left_2.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_left_3.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_left_4.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_left_5.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_left_6.png'),(self.width,self.height))
        ]
        self.lefts = [
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_right_1.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_right_2.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_right_3.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_right_4.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_right_5.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_right_6.png'),(self.width,self.height))
        ]
        self.count%=(fps+4)
        if 0<=self.c<=100:
            if not self.left:
                screen.blit(self.rights[self.count//8],(self.list[self.c]+camera_x,self.y+camera_y))
            else:
                screen.blit(self.lefts[self.count//8],(self.reverse[self.c]+camera_x,self.y+camera_y))
            self.c+=5
            self.count+=1
        else:
            self.left = not self.left
            self.c = 0


class AirBots:

    def __init__(self,x,y):
        self.y = y-25
        self.x = x
        self.list = [i for i in range(self.x,self.x+151)] #координаты х по которым оно будет двигаться вперед
        self.reverse = self.list[::-1] # и обратно
        self.left = random.choice([True,False])
        self.c = 0
        self.count = random.randint(0,fps)
        self.rights = [pg.transform.scale(pg.image.load('bots img/bat_right_3.png'),(50,50)),
                       pg.transform.scale(pg.image.load('bots img/bat_right_2.png'),(50,50)),
                       pg.transform.scale(pg.image.load('bots img/bat_right_1.png'),(50,50))
                      ]
        self.lefts = [pg.transform.scale(pg.image.load('bots img/bat_left_3.png'),(50,50)),
                      pg.transform.scale(pg.image.load('bots img/bat_left_2.png'),(50,50)),
                      pg.transform.scale(pg.image.load('bots img/bat_left_1.png'),(50,50))
                      ]
    def blit(self):
        self.count %=fps
        if 0<=self.c<=150:
            if not self.left:
                screen.blit(self.rights[self.count//12],(self.list[self.c]+camera_x,self.y+camera_y))
            else:
                screen.blit(self.lefts[self.count//12],(self.reverse[self.c]+camera_x,self.y+camera_y))
            self.c+=5
            self.count+=1
        else:
            self.left = not self.left
            self.c = 0
