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

def Go(list1,x,y,zd):
    zidan=bullet(x+28,y-50,zd)
    list1.append(zidan) 
