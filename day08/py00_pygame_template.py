import pygame   
from pygame.locals import QUIT  
import sys     

pygame.init()
Surface = pygame.display.set_mode((640, 400))
FPSLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Template')

def main():
    while True:
        Surface.fill((0,0,0))
        for event in pygame.event.get():    
            if event.type == QUIT:  
                pygame.quit()   
                sys.exit()     

        pygame.display.update() 
        FPSLOCK.tick(30)    

if __name__ == '__main__':
    main()