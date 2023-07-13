import sys, pygame, random
from pygame.locals import *
from sprite_loader import *
from man import*
pygame.init()
screen_info = pygame.display.Info()

#1. Set up our screen - what we're going to be drawing on
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)

#2. Set up a clock to control the refresh rate of our game
clock = pygame.time.Clock()

color = (3, 86, 232)

cat_images = []
man_images = {}


def get_images():
  cats = SpriteSheet('runningcat.png')

  for i in range(4):
    for j in range(2):
      cat_images.append(cats.get_image(j*512, i*256, 512, 256))
      cat_images[-1] = pygame.transform.smoothscale(cat_images[-1], (200,100))

  men = SpriteSheet('man.png')
  directions = ["n", "w", "s", "e"]
  for i in range(4):
    for j in range(9):
      man_images[directions[i]+str(j)] = men.get_image(j*64, i*64, 64, 64)
      
      


def main():
  global screen

  get_images()
  cat_image = cat_images[0]
  cat_rect = cat_image.get_rect()
  player = Man((100,200), man_images)
      #main game loop - this constantly updates ou  r game
  while True:
        #controls refresh rate of our game
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
        
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
      player.up()
    if keys[K_DOWN]:
      player.down()
    if keys[K_RIGHT]:
      player.right()
    if keys[K_LEFT]:
      player.left()
    
    screen.fill(color)
    player.update()
    player.draw(screen)
    frame = pygame.time.get_ticks() // 60 % 8
    cat_image = cat_images[frame]
    screen.blit(cat_image, cat_rect)
    
    
    
    pygame.display.flip()
       

if __name__ == '__main__':
  main()
  
