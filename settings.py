#game settings
import pygame
from pitanja import *
from random import *
import ctypes
global brojac1
brojac1=0
pygame.font.init()
font=pygame.font.SysFont("times new roman",30,bold=False,italic=False)
pozadina=pygame.image.load("Clouds.jpg")
arena=pygame.image.load("Untitled3.png")
start=pygame.image.load("start.png")
user32=ctypes.windll.user32
sirina=user32.GetSystemMetrics(0)
visina=user32.GetSystemMetrics(1)
arena=pygame.transform.scale(arena,(sirina,visina))
pozadina=pygame.transform.scale(pozadina,(sirina,visina))
start=pygame.transform.scale(start,(sirina,visina))
kraj=pygame.image.load("kraj.jpg")
kraj=pygame.transform.scale(kraj,(sirina,visina))
win=pygame.image.load("win.jpg")
win=pygame.transform.scale(win,(sirina,visina))
FPS=30
FONT_NAME="arial"
player_acc=0.9
player_friction=-0.09
mob_acc=0.8
lista=[]
for i in range(0,len(pitanja)):
    lista.append(i)
global player_health
player_health=100
shuffle(lista)
ime="ARENA ZNANJA"
#boje
grey=(128,128,128)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
