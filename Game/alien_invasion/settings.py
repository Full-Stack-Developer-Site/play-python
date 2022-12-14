class Settings:
    def __init__(self) -> None:
        # 游戏界面设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.caption = "Alien Invastion"
        
        # 飞船设置
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 0.8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3