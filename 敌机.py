import pygame
import sys
import random
pygame.init()
screen=pygame.display.set_mode((1300,718))
bg=pygame.image.load("背景.jpeg")
dj1=pygame.image.load("敌机.png")
ax=pygame.image.load("爱心.png")

class enemy():
    def __init__(self,x,speed,dj):
        self.x=x
        self.y=0
        self.speed=speed
        self.dj=dj
    def fly(self):
        self.y=self.y+self.speed
    
enemy_list=[]

def creat_enemy(list2,x,speed,dj):
    enemy_1=enemy(x,speed,dj)
    list2.append(enemy_1)
i=0
while True:
    screen.blit(bg,(0,0))
    screen.blit(ax,(0,0))
    if i%2000 == 0:
        enemy_x=random.randint(0,1210)
        creat_enemy(enemy_list,enemy_x,0.3,dj1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for enemy1 in enemy_list:
        screen.blit(dj1,(enemy1.x,enemy1.y))
        enemy1.fly()
    pygame.display.update()
    i=i+1
        
