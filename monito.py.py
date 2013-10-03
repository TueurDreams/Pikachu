import pygame
from pygame. locals import *
import sys
import time

pygame. init()

def imagen(archivo, transparencia =False):
    try: image =  pygame.image.load(archivo)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparencia:
        color= image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image
visor = pygame.display.set_mode((1200,300),0,32)
pygame.display.set_caption('Pikachu')
pos = 0
Pikachu = imagen('pika.png',True) 
Pika2 = pygame.transform.flip(Pikachu,True,False)



#diccionario 
pika = {}
pica2 = {}
pica3 = {}
pica4 = {}
pica3 = (0,0,38,41)
pica4 = (474,0,38,41)
pika[0] = (1,41,45,37)
pica2[5] = (236,41,46,36)
pika[1] = (47,42,46,37)
pica2[4] = (283,41,45,37)
pika[2] = (94,41,44,37)
pica2[3] = (329,41,44,37) 
pika[3] = (139,41,44,37)
pica2[2] = (374,41,44,37) 
pika[4] = (184,41,45,37)
pica2[1] = (419,41,46,37) 
pika[5] = (230,41,46,37)
pica2[0] = (466,41,44,37)


cual = 0
#tiempo
cuanto = 100
tiempo = 0


derecha = False
izquierda = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

#Posicion

    teclasPulsadas = pygame.key.get_pressed()
    if teclasPulsadas[K_d]:
        izquierda= True
        derecha=False 
        pos = pos + 0.5
        if pygame.time.get_ticks()-tiempo > cuanto:
            tiempo = pygame.time.get_ticks()
            cual = cual + 1
            if cual ==6:
                cual = 0
        visor.blit(Pika2,(pos,30),(pica2[cual]))
        pygame.display.update()
        
    elif teclasPulsadas[K_a]:
        derecha = True
        izquierda = False
        pos = pos - 0.5
        if pygame.time.get_ticks()-tiempo > cuanto:
            tiempo = pygame.time.get_ticks()
            cual = cual + 1
            if cual ==6:
                cual = 0
        visor.blit(Pikachu,(pos,30),(pika[cual]))
        pygame.display.update()
    else :
        if pygame.time.get_ticks() -tiempo > cuanto:
            tiempo = pygame.time.get_ticks()
            cual = cual + 1
            if cual ==6:
                cual = 0
        if izquierda:
            visor.blit(Pika2,(pos,30),(pica4))
        if derecha:
            visor.blit(Pikachu,(pos,30),(pica3))
            
        pygame.display.update()
    


#Fondo
    visor.fill((233,233,233))


   
   

