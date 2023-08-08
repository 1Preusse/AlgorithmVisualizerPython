import pygame
import numpy as np



def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            yield array
            j -= 1
            

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item
        yield array
    yield array
    return










pygame.init()

numArray = np.random.random_sample(20)
numArray = np.arange(100)
np.random.shuffle(numArray)
print(numArray)
initOrder = True
initBachground = True
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("My Pygame Window")

running = True
while running:
   # Handle events
   if initBachground:
      window.fill((30, 30, 30))
      initBachground=False
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
            initOrder = False
            for numArray1 in insertion_sort(numArray):
               pygame.display.flip()
               pygame.event.pump()
               pygame.time.delay(10)
               window.fill((30, 30, 30))
               for i in range(len(numArray1)):
                  pygame.draw.rect(window, (0, 220, 10), (100+i*600/len(numArray1), 300+200-(3)*numArray1[i], 600/len(numArray1), 10+(3)*numArray1[i]))
                  
      
   # Draw shapes
   
   if initOrder:
      for i in range(len(numArray)):
         pygame.draw.rect(window, (0, 220, 10), (100+i*600/len(numArray), 300+200-(3)*numArray[i], 600/len(numArray), 10+(3)*numArray[i]))
      
   pygame.display.flip()
pygame.quit()

"""
def sort(arr):
   for i in range()
   """
   
