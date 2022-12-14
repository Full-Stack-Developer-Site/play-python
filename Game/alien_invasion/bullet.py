import pygame
from pygame.sprite import Sprite

# Bullet类继承了从模块pygame.sprite导入的Sprite类。
# 通过使用精灵（sprite），可将游戏中相关的元素编组，进而同时操作编组中的所有元素
class Bullet(Sprite):
    """管理飞船所发射子弹的类"""

    def __init__(self, ai_game) -> None:
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 子弹并非基于图像，因此必须使用pygame.Rect()类从头开始创建一个矩形
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        # 子弹的初始位置取决于飞船当前的位置
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)