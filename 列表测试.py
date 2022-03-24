import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((1300,718))
pygame.display.set_caption("子弹飞行")
zd1=pygame.image.load("子弹.png")
bg=pygame.image.load("背景.jpeg")

class bullet():
    def __init__(self,x,y,zd):
        self.x_now=x
        self.y_now=y
        self.zd=zd
        self.speed=0.5
    def fly(self):
        screen.blit(self.zd,(self.x_now,self.y_now))
        self.y_now=self.y_now-self.speed

list_1=[]
def Go(list1,x,y,zd):
    zidan=bullet(x,y,zd)
    list1.append(zidan)
while True:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Go(list_1,638,550,zd1)
    for i in list_1:
        i.fly()
        if i.y_now<=-49 :
            del list_1[0]
    pygame.display.update()
