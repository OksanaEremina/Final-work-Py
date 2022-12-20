#Дана функция f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
#Определить корни
#Найти интервалы, на которых функция возрастает
#Найти интервалы, на которых функция убывает
#Построить график
#Вычислить вершину
#Определить промежутки, на котором f > 0
#Определить промежутки, на котором f < 0

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from sympy import *
 
f = lambda x: -12*x**4*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30
 
def roots():
    return fsolve(f, [-100, 100])
roots = roots()
 
list_y_new = list(map(f, roots))
sign = lambda x: 'f > 0' if x >= 0 else 'f < 0'
sign = list(map(sign, list_y_new))
# Выводим корни
print(roots)
# Выводим знаки
print(sign)
# 
# Графики
from math import * 
import pygame 

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("func_graph")
all_sprites=pygame.sprite.Group()
clock = pygame.time.Clock()
running = True
fps=60

class Line(pygame.sprite.Sprite):
    def __init__(self,pos,x,y):
        pygame.sprite.Sprite.__init__(self)
        if pos=="x":
            self.image=pygame.Surface((3,400))
            self.image.fill((0,0,0))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
        elif pos=="y":
            self.image=pygame.Surface((400,3))
            self.image.fill((0,0,0))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
            
class Dot(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.surface.Surface((5,5))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
            
def Calc(func):
    i=-10
    while i<=10:
        mass=""
        for j in func:
            if j == "x":
                mass+=str(i)
            else:
                mass+=j
            i+=0.0001
        try:
          res1=eval(mass)
        except:
          res1=10000
        dot=Dot(250+i*10,250-res1*10)
        all_sprites.add(dot)

func = str(input("y = "))
calc = Calc(func)

line = Line("y",250,250)
all_sprites.add(line)
line1 = Line("x",250,250)
all_sprites.add(line1)

while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-20, 10.01, 0.01)
plt.plot(x, x**2)
plt.show()