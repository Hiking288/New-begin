import sys,pygame
from rocket_info import Rocket
from rockrt_settings import Settings
import rocket_functions as RF

def run_game():
	#pygame的初始化
	pygame.init()
	game_settings = Settings()
	screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height)) #设置屏幕显示尺寸
	pygame.display.set_caption('Game Of Rocket') #设置title
	rocket_1 = Rocket(game_settings,screen)

	while True:
		
		screen.fill(game_settings.bg_color)
		RF.check_event(rocket_1)
		rocket_1.update_moving_status()
		rocket_1.blit_rocket()
		pygame.display.flip()



run_game()











































