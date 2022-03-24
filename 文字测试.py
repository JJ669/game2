import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((1300,718))
pygame.display.set_caption("击落敌机小游戏")
class write():
    def __init__(self,size,text,color):
        self.size=size
        self.text=text
        self.color=color
    def creat(self):
        self.S=pygame.font.SysFont("隶书",self.size)
        self=self.S.render(text,True,color,None)
