import sys,pygame


def check_event(rocket_1):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			#按下上下左右按键
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				rocket_1.moving_right = True
			elif event.key == pygame.K_LEFT:
				rocket_1.moving_left = True
			elif event.key == pygame.K_UP:
				rocket_1.moving_up = True
			elif event.key == pygame.K_DOWN:
				rocket_1.moving_dowm = True
			#松开上下左右键
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				rocket_1.moving_right = False
			elif event.key == pygame.K_LEFT:
				rocket_1.moving_left = False
			elif event.key == pygame.K_UP:
				rocket_1.moving_up = False
			elif event.key == pygame.K_DOWN:
				rocket_1.moving_dowm = False














































