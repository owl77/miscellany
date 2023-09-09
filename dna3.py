import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1600,1000), 0, 32)
screen.fill((255,255,255))
s = input("Genome sector (1-100):")
xx= 800
yy = 500
while(True):

 with open("hg38.2bit","rb") as bil:
  bil.seek(s*48000000)
  data = bil.read(3*1600000)
  for x in range(1599999):
   c = ord(data[x])
   d = bin(c)[2:].rjust(8, '0')
   for n in range(3):
    if int(d[n*2]) == 0 and int(d[n*2+1]) == 0:
     screen.set_at((xx,yy-1),(0,0,0))
     yy = (yy-1)%1000
    if int(d[n*2]) == 1 and int(d[n*2+1]) == 0:
     screen.set_at((xx,yy+1),(0,0,0))
     yy = (yy+1)%1000
    if int(d[n*2]) == 0 and int(d[n*2+1]) == 1:
     screen.set_at((xx+1,yy),(0,0,0))
     xx = (xx+1)%1600
    if int(d[n*2]) == 1 and int(d[n*2+1]) == 1:
     screen.set_at((xx-1,yy),(0,0,0))
     xx = (xx-1)%1600
    pygame.display.update()

