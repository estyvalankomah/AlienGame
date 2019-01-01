import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
	"""A class to report scoring information"""

	def __init__(self,ai_settings,screen,stats):
		"""initialize scorekeeping attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		#font settings for scoring information
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,20)
		#prepare initial score images
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""Turn the score into a rendered image"""
		rounded_score = round(self.stats.score)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
		#display the score at the top right of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.left = self.score_rect.right - 100
		self.score_rect.top = 20

		score_text = "Score:"
		self.score_text_image = self.font.render(score_text,True,self.text_color,self.ai_settings.bg_color)
		#display "Score" at the top right of the screen
		self.score_text_rect = self.score_text_image.get_rect()
		self.score_text_rect.right = self.score_rect.left - 10
		self.score_text_rect.left = self.score_text_rect.right - 40
		self.score_text_rect.top = 20

	def prep_high_score(self):
		"""Turn the high score into a rendered image"""
		high_score = round(self.stats.high_score)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
		#Center the high score at the top of the screen
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.right = self.screen_rect.right - 300
		self.high_score_rect.left = self.high_score_rect.right - 30
		self.high_score_rect.top = 20

		highScore_text = "High Score:"
		self.highScore_text_image = self.font.render(highScore_text,True,self.text_color,self.ai_settings.bg_color)
		#display "High Score" at the center top of the screen
		self.highScore_text_rect = self.highScore_text_image.get_rect()
		self.highScore_text_rect.right = self.high_score_rect.left - 10
		self.highScore_text_rect.left = self.highScore_text_rect.right - 70
		self.highScore_text_rect.top = 20

	def prep_level(self):
		"""Turn the level into a rendered image"""
		self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
		#position the level at the top
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.highScore_text_rect.left - 60
		self.level_rect.left = self.level_rect.right - 60
		self.level_rect.top = 20

		level_text = "Level:"
		self.level_text_image = self.font.render(level_text,True,self.text_color,self.ai_settings.bg_color)
		#display "Level" at the top
		self.level_text_rect = self.level_text_image.get_rect()
		self.level_text_rect.right = self.level_rect.left - 10
		self.level_text_rect.left = self.level_text_rect.right - 40
		self.level_text_rect.top = 20

	def prep_ships(self):
		ships_text = "Ships left:"
		self.ships_text_image = self.font.render(ships_text,True,self.text_color,self.ai_settings.bg_color)
		#display "Ships left" at the top
		self.ships_text_rect = self.ships_text_image.get_rect()
		self.ships_text_rect.left = self.screen_rect.left + 20
		self.ships_text_rect.right = self.ships_text_rect.left + 70
		self.ships_text_rect.top = 20

		"""Turn the number of ships left into a rendered image"""
		self.ships_image = self.font.render(str(self.stats.ships_left),True,self.text_color,self.ai_settings.bg_color)
		#position the level at the top
		self.ships_rect = self.ships_image.get_rect()
		self.ships_rect.left = self.ships_text_rect.right + 10
		self.ships_rect.right = self.ships_rect.left + 10
		self.ships_rect.top = 20

	def show_score(self):
		"""draw score and level to the screen"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.score_text_image,self.score_text_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.highScore_text_image,self.highScore_text_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.screen.blit(self.level_text_image,self.level_text_rect)
		self.screen.blit(self.ships_text_image,self.ships_text_rect)
		self.screen.blit(self.ships_image,self.ships_rect)



	