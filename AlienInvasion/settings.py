class Settings:
	"""A clas to store all settings for the game"""

	def __init__(self):
		"""Initialize the game's settings"""
		#screen settings
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (185,185,185)

		#ship settings
		self.ship_speed_factor = 1.5

		#bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 3
