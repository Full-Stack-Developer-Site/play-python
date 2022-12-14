import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


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


    # 发射子弹
    def _fire_bullet(self):
        if len(self.bulluets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bulluets.add(new_bullet)


    # 刷新屏幕
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bulluets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)

        pygame.display.flip()


    # 更新子弹 - 删除消失的子弹
    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        self.bulluets.update()

        # 使用for循环遍历列表（或Pygame编组）时，Python要求该列表的长度在整个循环中保持不变
        for bullet in self.bulluets.copy():
            if bullet.rect.bottom <= 0:
                self.bulluets.remove(bullet)

        self._check_bullet_alien_collisions()
        

    # 子弹和外星人碰撞
    def _check_bullet_alien_collisions(self):
        # 检查是否有子弹击中了外星人
        # 如果是，就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bulluets, self.aliens, True, True)

        if not self.aliens:
            self.bulluets.empty()
            self._create_fleet()


    # 创建外星人
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

        self.aliens.add(alien)


    # 创建外星人舰队
    def _create_fleet(self):
        # 创建一个外星人并计算一行可容纳多少个外星人
        # 外星人的间距为外星人宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # 计算屏幕可容纳多少外星人
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    # 更新外星人
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print('Ship Hit!!!')


    # 游戏主循环
    def run_game(self) -> None:
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    # 检查外星人是否到边缘
    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    # 外星人下移
    def _change_fleet_direction(self):
        """将整群外星人下移，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()