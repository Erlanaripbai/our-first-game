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
dy = -5
dx = 0
gravity = 1 
jump_is_allowed = False
camera_x = 0
camera_y=0
naruto=pg.image.load('naruto.png')
naruto=pg.transform.scale(naruto,(block_size,block_size))
bg=pg.image.load("fon.jpg")
bg1=pg.image.load("fon1.jpg")
fon=pg.image.load('fon4.png')
bg = pg.transform.scale(bg, size)
bg1 = pg.transform.scale(bg1, size)
fon =pg.transform.scale(fon, (1000,300))
cloud=pg.image.load("c.png")
block1=pg.image.load("b.png")
block2=pg.image.load("2.png")
block3=pg.image.load("3.png")
block=pg.image.load("6.png")
block5=pg.image.load("13.png")
block6=pg.image.load("14.png")
block8=pg.image.load("5.png")
block7=pg.image.load("7.png")
block7c=pg.image.load("7c.png")
block9=pg.image.load("8.png")
block10=pg.image.load("10.png")
block11=pg.image.load("e.png")
block12=pg.image.load("q.png")
block13=pg.image.load("r.png")
block14=pg.image.load("t.png")
block15=pg.image.load("y.png")
block16=pg.image.load("g.png")
block17=pg.image.load("h.png")
block18=pg.image.load("m.png")
block19=pg.image.load("d.png")
block20=pg.image.load("i.png")
block21=pg.image.load("j.png")
block22=pg.image.load("f.png")
level=pg.transform.scale(pg.image.load("level.png"),(block_size+20,block_size+20))
cloud = pg.transform.scale(pg.image.load("c.png"), (block_size+40,block_size+50))
block1 = pg.transform.scale(block1, (block_size,block_size))
block2 = pg.transform.scale(block2, (block_size,block_size))
block3 = pg.transform.scale(block3, (block_size,block_size))
block = pg.transform.scale(block, (block_size,block_size))
block5 = pg.transform.scale(block5, (block_size,block_size))
block6 = pg.transform.scale(block6, (block_size,block_size))
block7 = pg.transform.scale(block7, (block_size,block_size))
block7c = pg.transform.scale(block7c, (block_size,block_size))
block8 = pg.transform.scale(block8, (block_size,block_size))
block9 = pg.transform.scale(block9, (block_size,block_size))
block10 = pg.transform.scale(block10, (block_size,block_size))
block11 = pg.transform.scale(block11, (block_size,block_size))
block12 = pg.transform.scale(block12, (block_size,block_size))
block13 = pg.transform.scale(block13, (block_size,block_size))
block14 = pg.transform.scale(block14, (block_size,block_size))
block15 = pg.transform.scale(block15, (block_size,block_size))
block16 = pg.transform.scale(block16, (block_size,block_size))
block17 = pg.transform.scale(block17, (block_size,block_size))
block18 = pg.transform.scale(block18, (block_size,block_size))
block19 = pg.transform.scale(block19, (block_size,block_size))
block20 = pg.transform.scale(block20, (block_size,block_size))
block21 = pg.transform.scale(block21, (block_size,block_size))
block22 = pg.transform.scale(block22, (block_size,block_size))
level1=[
    "          c                 c        c             c               c                c           c                    c       c           c                                                        ", 
    "                                                               c         c                       c          c c                   c    c   c                        ",
    "    c                 c                  c        c           c  c         c     ccc               c      c     c        c      c            c                   " ,
    "                c              c                                                 c    c                                                                    " ,
    "                                                                                          " ,
    "                                                                                          " ,
    "                                                                                          " ,
    "                                                                                  ghhhhhhh        " ,
    "                                                                                                " ,
    "          k                                             ghhhhhh              gh                   ",
    "         ghhhhhh                  ghhhh                gm         gh      k                                                                                      bbbbbbb    ",
    "                            gh             gh       gh                ghhhhhhh                                                                                   mmmmmmm        ",
    "                 gh       gh                    ghhh                                                                                                             mmmmmmm          ",
    "                        p                    p                                                    L                     k                                        mmmmmmm       ",
    "        p             dbbbbbi          dbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbi       dbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbmmmmmmmm",
    "bbbbbbbbbbbbbbbbbbbbbbfmmmmmjbbbbbbbbbbfmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm       mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",
    "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm       mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",
    "666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666m       m666666666666666666666666666666666666666666666666666666666666666",
    "666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666m       m666666666666666666666666666666666666666666666666666666666666666",
    "666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666q       t666666666666666666666666666666666666666666666666666666666666666",
    "666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666q       t666666666666666666666666666666666666666666666666666666666666666",
    ]
interval=[
    "",
    ]
level2=[
    "66666666666666666666q       t66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666",
    "66666666666666666666q       t66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666",
    "66666666666666666666q       zeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeey66666666666",
    "66666666666666666666q                                                                                                                                           t66666666666",
    "66666666666666666666q                                                                                                                                           t66666666666",
    "66666666666666666666q                                                                                                                                           t66666666666",
    "66666666666666666666q                                                                                                                                           t66666666666",
    "66666666666666666666q                                                                                                                                           t66666666666",
    "66666666666666666666q                                                                                                                                           t66666666666",
    "66666666666666666666q                                                                                                                                           t66666666666",
    "66666666666666666666q                                                                                                   k                                       t66666666666",
    "66666666666666666666q                                                                                                                                           t66666666666",
    "66666666666666666666q                                             k                                 k                 k                                         t66666666666",
    "66666666666666666666q                   k                  o                                               k                                                    t66666666666",
    "66666666666666666666q       k        82222227           82222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222w66666666666",
    "6666666666666666666692222222222222222w666666922222222222w6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666",
    "6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666",
    "6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666",
    "6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666",
    "6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666",
    ]


#Bots

#BATS
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
list_bats=[]
list_bats1=[]
for i in range(len(level1)):
    for j in range(len(level1[i])):
        if level1[i][j]=='k':
            list_bats.append(AirBots(j*block_size,i*block_size))
for i in range(len(level2)):
    for j in range(len(level2[i])):
        if level2[i][j]=='k':
                list_bats1.append(AirBots(j*block_size,i*block_size))


#BEARS AND BOARS
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
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_left_1.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_left_2.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_left_3.png'),(self.width,self.height))
        ]
        self.lefts = [
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_right_1.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_right_2.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_right_3.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_right_1.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_right_2.png'),(self.width,self.height)),
            pg.transform.scale(pg.image.load('bots img/' + self.animal + '_right_3.png'),(self.width,self.height))
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
list_earthbots = []
list_earthbots1 = []

for i in range(len(level2)):
    for j in range(len(level2[i])):
        if level2[i][j]=='o':
            list_earthbots1.append(EarthBots(j*block_size,i*block_size,'bear'))
for i in range(len(level1)):
    for j in range(len(level1[i])):
        if level1[i][j]=='p':
            list_earthbots.append(EarthBots(j*block_size,i*block_size,'boar'))



m=[]
done=True
m=level1
while done:
    if m==level1:screen.blit(bg1,(0,0))
    elif m==level2:screen.blit(bg,(0,0))


        
    if m==level1:
        if y>600:
            m=interval
            x=860
            y=300
            camera_x,camera_y=0,0
            screen.fill((0,0,0))
    if m==interval and y>600:
        m=level2
        x=860
        y=200
        camera_x,camera_y=0,0
        
    dy = dy + gravity
    if dy > 10:
        dy = 10
    # save x and y
    save_x, save_y = x, y

    # increase y
    y = y + dy
    rect1 = pg.Rect(x, y, block_size, block_size)
    collide = False
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "2"or m[i][j]=="w"or m[i][j] == "s"or m[i][j] == "3"or m[i][j] == "7" or m[i][j] == "b"  or m[i][j] == "d" or m[i][j] == "i"or m[i][j] == "g" or m[i][j] == "h"or m[i][j] == "6" :
                rect2 = pg.Rect(j*block_size, i*block_size, block_size, block_size)
                if rect1.colliderect(rect2):
                    collide = True

                if m[i][j] == "d" and x==i:
                    y-=dx/2
    
    if collide:
        y = save_y
        # collide while going down?
        if dy > 0:
            jump_is_allowed = True
        dy = 0
    if y+camera_y > size[1]*1:
        camera_y=camera_y-10
    if y+camera_y < size[1]*0.2:
        camera_y=camera_y + 10


    # change x
    x = x + dx
    rect1 = pg.Rect(x, y, block_size, block_size)
    collide = False
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "2" or m[i][j] == "s" or m[i][j] == "t" or m[i][j] == "3"or m[i][j] == "b" or m[i][j] == "q"or m[i][j] == "g" or m[i][j] == "h"or m[i][j] == "level2" or m[i][j] == "m" or m[i][j] == "6" :
                rect2 = pg.Rect(j*block_size, i*block_size, block_size, block_size)
                if rect1.colliderect(rect2):
                    collide = True
        

    if collide:
        x = save_x

    if x + camera_x > size[0]*0.7:
        camera_x = camera_x - 10
    if x + camera_x < size[0]*0.3:
        camera_x = camera_x + 10
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = False
        if event.type == pg.KEYDOWN:  # Pressed something
            if event.key == pg.K_SPACE or event.key == pg.K_UP:  # What exactly did we press?
                if jump_is_allowed:
                    dy = -15
                    jump_is_allowed = False
            if event.key == pg.K_LEFT:
                dx = -10
            if event.key == pg.K_RIGHT:
                dx = 10
        if event.type == pg.KEYUP:  # Released something
            if event.key == pg.K_LEFT:
                if dx < 0:
                    dx = 0
            if event.key == pg.K_RIGHT:
                if dx > 0:
                    dx = 0
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "b":
                screen.blit(block1, (j*block_size + camera_x,i*block_size+ camera_y))
            if m[i][j] == "L":
                screen.blit(level, (j*block_size + camera_x,i*block_size+ camera_y))    
            if m[i][j] == "c":
                screen.blit(cloud, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "2":
                screen.blit(block2, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "3":
                screen.blit(block3, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "s":
                screen.blit(block5, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "6":
                screen.blit(block, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "7":
                screen.blit(block7, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "z":
                screen.blit(block7c, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "8":
                screen.blit(block8, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "9":
                screen.blit(block9, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "w":
                screen.blit(block10, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "q":
                screen.blit(block12, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "e":
                screen.blit(block11, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "r":
                screen.blit(block13, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "t":
                screen.blit(block14, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "y":
                screen.blit(block15, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "g":
                screen.blit(block16, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "h":
                screen.blit(block17, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "m":
                screen.blit(block18, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "d":
                screen.blit(block19, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "i":
                screen.blit(block20, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "j":
                screen.blit(block21, (j*block_size + camera_x, i*block_size+ camera_y))
            if m[i][j] == "f":
                screen.blit(block22, (j*block_size + camera_x, i*block_size+ camera_y))
    if m==level1:
        for i in list_bats:i.blit()
        for i in list_earthbots:i.blit()
    elif m==level2:
        for i in list_bats1:i.blit()
        for i in list_earthbots1:i.blit()
    screen.blit(naruto,(x+camera_x,y+ camera_y))
    if m==interval:
        screen.fill((0,0,0))
        screen.blit(fon,(0,150))
    pg.display.flip()
    clock.tick(fps)
    

pg.quit()

        
