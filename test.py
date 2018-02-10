# added a comment here

import pygame

# for creating the game
# added a new comment
pygame.init()

# some definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

display_width = 800
display_height = 600
block_size = 10
FPS = 60

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

gameExit = False

lead_x = display_width/2
lead_y = display_height/2

lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

# main game loop
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		# make snake move
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				lead_x_change = -block_size/2
				lead_y_change = 0
			elif event.key == pygame.K_RIGHT:
				lead_x_change = block_size/2
				lead_y_change = 0
			elif event.key == pygame.K_UP:
				lead_y_change = -block_size/2
				lead_x_change = 0
			elif event.key == pygame.K_DOWN:
				lead_y_change = block_size/2
				lead_x_change = 0

		# make snake stop
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				lead_x_change = 0
			elif event.key == pygame.K_RIGHT:
				lead_x_change = 0
			elif event.key == pygame.K_UP:
				lead_y_change = 0
			elif event.key == pygame.K_DOWN:
				lead_y_change = 0

	# boundary checking
	if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
		gameExit = True

	# logic
	lead_x += lead_x_change
	lead_y += lead_y_change

	# draw
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, black, [lead_x,lead_y, block_size, block_size])
	pygame.display.update()

	# fps
	clock.tick(FPS)

pygame.quit()
quit()