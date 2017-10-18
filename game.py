import pygame
 
 
#             R    G    B	A
WHITE     = (255, 255, 255, 1)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
PURPLE = ( 150,  50,  204)
# initialize game engine
pygame.init()
# set screen width/height and caption
size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SHOOTO-MAN')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()
 
 #CLASSES
class Ship(pygame.sprite.Sprite):
#This class represents a car. It derives from the "Sprite" class in Pygame.
    
		def __init__(self, color, width, height):
			# Call the parent class (Sprite) constructor
			super(Ship,self).__init__()
			
			# Pass in the color of the car, and its x and y position, width and height.
			# Set the background color and set it to be transparent
			self.image = pygame.Surface([width, height])
			self.image.fill(WHITE)
			self.image.set_colorkey(WHITE)
			self.image.set_alpha(1)
			self.rect = self.image.get_rect()
			screen.blit(self.image, (self.rect.x,self.rect.y)) 
	 
			# Draw the car (a rectangle!)
			pygame.draw.rect(self.image, color, [0, 0, width, height])
        
			self.rect = self.image.get_rect()
		
		def set_Image(self, filename = None):
			if( filename != None):
				self.image = pygame.image.load(filename)
				self.rect = self.image.get_rect()
		
		def moveRight(self, pixels):
			self.rect.x += pixels
		def moveLeft(self, pixels):
			self.rect.x -= pixels
		def moveUp(self,pixels):
			self.rect.y -= pixels
		def moveDown(self,pixels):
			self.rect.y += pixels
	

# CLASSES END

# Loop until the user clicks close button
#
# Variables declarations
Ship_List = pygame.sprite.Group()
player = Ship(WHITE,40,40)
player.rect.x = 300
player.rect.y = 300
Ship_List.add(player)
player.set_Image("ship.png")
#
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
	keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
           player.moveLeft(10)
        if keys[pygame.K_RIGHT]:
           player.moveRight(10)
        if keys[pygame.K_UP]:
           player.moveUp(10)
        if keys[pygame.K_DOWN]:
           player.moveDown(10)
       
	
    # write game logic here
	Ship_List.update()
    # clear the screen before drawing
	screen.fill(BLACK) 
    # write draw code here
	Ship_List.draw(screen)
    pygame.display.update()
    # run at 20 fps
    clock.tick(60)
 
# close the window and quit
pygame.quit()