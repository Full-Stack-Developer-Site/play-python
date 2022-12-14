import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """管理游戏资源和行为"""
    
    def __init__(self) -> None:
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)

        self.bg_color = self.settings.bg_color

        self.ship = Ship(self)
        self.bulluets = pygame.sprite.Group()


    # 游戏主循环
    def run_game(self) -> None:
        while True:
            self._check_events()

            self.ship.update()
            self._update_bullets()

            self._update_screen()


    # 辅助方法（helper method）
    # 辅助方法在类中执行任务，但并非是通过实例调用的。在Python中，辅助方法的名称以单个下划线打头
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if(event.type) == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    # KeyDown events
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    # KeyUp events
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bulluets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bulluets.add(new_bullet)


    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bulluets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        self.bulluets.update()

        # 使用for循环遍历列表（或Pygame编组）时，Python要求该列表的长度在整个循环中保持不变
        for bullet in self.bulluets.copy():
            if bullet.rect.bottom <= 0:
                self.bulluets.remove(bullet)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()