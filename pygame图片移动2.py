import pygame
import sys
import random
import time

#载入图片
pygame.init()
screen=pygame.display.set_mode((1300,718))
pygame.display.set_caption("击落敌机小游戏")
text_1=pygame.font.SysFont("隶书",30)  #记分器
text_2=pygame.font.SysFont("隶书",100) #开始游戏
text_3=pygame.font.SysFont("隶书",20)  #技能提示
fj=pygame.image.load("玩家飞机.png")
bg=pygame.image.load("背景.jpeg")
zd=pygame.image.load("子弹.png")
dj=pygame.image.load("敌机.png")
ax=pygame.image.load("爱心.png")
over=pygame.image.load("游戏结束.png")
skill_1=pygame.image.load("加速.png")

#各种类
class bullet():   #子弹
    def __init__(self,x,y,draw):
        self.x=x
        self.y=y
        self.draw=draw
        self.speed=0.5
    def fly(self):
        screen.blit(self.draw,(self.x,self.y))
        self.y=self.y-self.speed
        
class plane():    #玩家飞机
    def __init__(self,speed,draw):
        self.x=600
        self.y=600
        self.speed=speed
        self.draw=draw
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

class enemy():    #敌机
    def __init__(self,x,speed,draw,point):
        self.x=x
        self.y=0
        self.speed=speed
        self.draw=draw
        self.point=point
    def fly(self):
        self.y=self.y+self.speed

class life():   #生命
    def __init__(self,x,y,draw):
        self.x=x
        self.y=y
        self.draw=draw


#各种列表
bullet_list=[]
enemy_list=[]
life_list=[]

#函数区域
def bullet_go(list1,x,y,zd):
    zidan=bullet(x+28,y-50,zd)
    list1.append(zidan)

def creat_enemy(list2,x,speed,dj):
    enemy_1=enemy(x,speed,dj,5)
    list2.append(enemy_1)

def clear_destroied_enemy_bullet(list1,list2,bullet,scores):  #子弹击中敌机
    for enemy in list2:
        if bullet.x>enemy.x-27 and bullet.x<enemy.x+83:
            if bullet.y<enemy.y+45 and bullet.y>enemy.y-49:
                list1.remove(bullet)
                list2.remove(enemy)
                scores[0]=scores[0]+enemy.point
                

def plane_crash(list2,enemy,plane):
    if plane.x>enemy.x-70 and plane.x<enemy.x+70:
        if plane.y<enemy.y+50 and plane.y>enemy.y-60:
            return 1
    return 0
                
#初始化数据
speed=0.7   #驾驶飞船速度，简易:1,普通:0.7,困难:0.5
plane_1=plane(speed,fj)
i=0
scores=[0]    #一开始的分数
life_num=3  #一开始的命
ready=1     #游戏界面
k=0         #判断游戏结束
jn1=0       #1技能释放判断
life_1=life(0,0,ax)
life_2=life(30,0,ax)
life_3=life(60,0,ax)
life_list.append(life_1)
life_list.append(life_2)
life_list.append(life_3)
text2=text_2.render("开始游戏",True,"white",None)
text3_1=text_3.render("X",True,"white",None)
text3_2=text_3.render("加速",True,"white",None)


#游戏开始界面
while ready:
    screen.blit(bg,(0,0))
    screen.blit(text2,(485,275))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            M_x=event.pos[0]
            M_y=event.pos[1]
            #游戏开始判断
            if M_x>485 and M_x<885:
                if M_y>275 and M_y<375:
                    ready=0
            #操作方式查询判断
            
            

    pygame.display.update()



#游戏主程序
while True:
    screen.blit(bg,(0,0))
    screen.blit(skill_1,(1260,400))
    screen.blit(text3_1,(1272,440))
    screen.blit(text3_2,(1255,375))
    screen.blit(fj,(plane_1.x,plane_1.y))
    text1=text_1.render(f"分值:{scores[0]}",True,"red",None)
    screen.blit(text1,(1100,0))

    open_time=time.time()
    if life_num <=0:
        k=1
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_go(bullet_list,plane_1.x,plane_1.y,zd)
            if event.key == pygame.K_x :
                if jn1 == 0:
                    jn1=1
                    plane_1.speed=plane_1.speed*2
                elif jn1 == 1:
                    jn1=0
                    plane_1.speed=speed

    t=(time.time()-open_time)/10
                
    if i%1000 == 0:
        enemy_x=random.randint(0,1210)
        creat_enemy(enemy_list,enemy_x,0.3+0.1*t,dj)
        
    for enemy1 in enemy_list:
        screen.blit(enemy1.draw,(enemy1.x,enemy1.y))
        enemy1.fly()
        if enemy1.y >718:
            enemy_list.remove(enemy1)
            life_num=life_num-1
            del life_list[-1]
        if plane_crash(enemy_list,enemy1,plane_1):
            k=1
        
    for bullet_1 in bullet_list:
        bullet_1.fly()
        clear_destroied_enemy_bullet(bullet_list,enemy_list,bullet_1,scores)
        if bullet_1.y<=-49 :
            del bullet_list[0]
            
    for life_draw in life_list:
        screen.blit(life_draw.draw,(life_draw.x,life_draw.y))

    if k == 1:
        screen.blit(over,(450,230))
    
    plane_1.fly()
    pygame.display.update()
    i=i+1
    
    if k == 1:
        print("游戏结束")
        break

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
