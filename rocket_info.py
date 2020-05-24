import pygame

class Rocket():

	def __init__(self,game_settings,screen):
		self.screen = screen
		self.image = pygame.image.load('images\\rocket.bmp') #加载火箭的图片
		self.rect = self.image.get_rect() #获得火箭的外矩形
		self.screen_rect = screen.get_rect() #获得屏幕的尺寸
		#让火箭显示在屏幕中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		self.game_settings = game_settings
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_dowm = False

	def update_moving_status(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.game_settings.moving_speed_factor
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= self.game_settings.moving_speed_factor
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.rect.centery -= self.game_settings.moving_speed_factor
		if self.moving_dowm and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += self.game_settings.moving_speed_factor


	#打印出来火箭
	def blit_rocket(self):
		self.screen.blit(self.image,self.rect)
























