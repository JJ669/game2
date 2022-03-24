import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((1300,718))
fj1=pygame.image.load("飞机3_1.png")
bg=pygame.image.load("背景.jpeg")
zd1=pygame.image.load("子弹.png")
class plane():
    def __init__(self,speed,fj):
        self.x=600
        self.y=600
        self.speed=speed
        self.fj=fj
    def fly(self):
        Key = pygame.key.get_pressed()
        if Key[pygame.K_UP] and self.y>=0:
            self.y=self.y-self.speed
        if Key[pygame.K_DOWN] and self.y<=650:
            self.y=self.y+self.speed
        if Key[pygame.K_LEFT] and self.x>=0:
            self.x=self.x-self.speed
        if Key[pygame.K_RIGHT] and self.x<=1218:
            self.x=self.x+self.speed
