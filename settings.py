class Settings:
    def __init__(self):
        # self.screen_width = 560
        # self.screen_height = 900

        self.screen_width = 900
        self.screen_height = 600
        self.speed = 1
        # Obstacle settings = bugs ythe player has to avoid
        self.obstacle_speed = 2.0
        self.obstacle_width = 10
        self.obstacle_height = 10 
        # self.obstacle_colour = (60, 60, 60)
        self.user_speed = 7
        self.bg_colour = (135, 206, 235)
        # Lives settings = bugs the player has to avoid
        self.life_speed = 2.0
        self.life_width = 10
        self.life_height = 10 
        # self.life_colour = (152, 251, 152)
        self.obstacle_load = 100
        
    def reset_game(self):
        self.screen_width = 560
        self.screen_height = 900
        self.speed = 1
        # Obstacle settings = bugs ythe player has to avoid
        self.obstacle_speed = 2.0
        self.obstacle_width = 10
        self.obstacle_height = 10 
        # self.obstacle_colour = (60, 60, 60)
        self.user_speed = 7
        self.bg_colour = (135, 206, 235)
        # Lives settings = bugs the player has to avoid
        self.life_speed = 2.0
        self.life_width = 10
        self.life_height = 10 
        # self.life_colour = (152, 251, 152)
        self.obstacle_load = 100
        print("game reset")