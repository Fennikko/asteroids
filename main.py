import pygame
from constants import *

def main():
    print("Staring asteroids!")
    
    color =(0, 0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color)
        pygame.display.flip()
    
    
    
if __name__ == "__main__":
    main()