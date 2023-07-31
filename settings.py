class Settings():
    """ A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        #Screen setttings
        self.screen_width= 1200
        self.screen_height=800
        self.bg_color=(255,255,255)

        #ship settings
        self.ship_speed_factor=1.5
        self.ship_limit=1

        #Bullet settings
        self.bullet_speed_factor=3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=10

        #Alien settings
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        self.fleet_direction=1

        self.speedUp_scale=1.1
        self.initialize_dynamic_settings()

        self.score_scale=1.5


    def initialize_dynamic_settings(self):
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.fleet_direction=1

        self.alien_points=50

    def increase_speed(self):
        self.ship_speed_factor*=self.speedUp_scale
        self.bullet_speed_factor*=self.speedUp_scale
        self.alien_speed_factor*=self.speedUp_scale
        self.alien_points=int(self.alien_points*self.score_scale)
        print(self.alien_points)
