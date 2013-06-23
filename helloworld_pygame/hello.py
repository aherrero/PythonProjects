import sys, pygame
pygame.init()
size = width, height = 640, 480
speed = [1, 1]
colorbackground = 0, 10, 10

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
			
	screen.fill(colorbackground)
	screen.blit(ball, ballrect)
	pygame.display.flip()