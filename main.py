import pygame
import numpy as np
pygame.init()

numArray = np.random.random_sample(100)
print(numArray)

window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("My Pygame Window")

running = True
while running:
   # Handle events
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
    
   # Draw shapes
   window.fill((30, 30, 30))
   
   for i in range(len(numArray)):
      pygame.draw.rect(window, (0, 220, 10), (100+i*600/len(numArray), 300+200-(400)*numArray[i], 600/len(numArray), 10+(400)*numArray[i]))
      
   pygame.display.flip()
pygame.quit()