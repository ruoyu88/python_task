import pygame

from pygame.sprite import Group
from star import Star
import time
import sys
import random
from ship import Ship
class Main:
    
    def __init__(self):
        pygame.init() # 初始化

        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230, 230, 230) 
        
        
        self.star_image = pygame.image.load('images/star.bmp')
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) # 获取屏幕
        pygame.display.set_caption("stars") # 标题

        self.ship = Ship(self)
        self.stars = Group()
    
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:#按下
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:#松开
                self._check_keyup_events(event)
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     mouse_pos = pygame.mouse.get_pos()
            #     self._check_play_button(mouse_pos)

    def update_screen(self):
        self.screen.fill(self.screen_color)  # 填充屏幕颜色
        self.stars.draw(self.screen)
        self.ship.blitme()
        pygame.display.flip()  # 使屏幕可见
        

    def create_star(self):
        star = Star(self.screen)
        star.x = random.randint(0, 1200)
        star.y = random.randint(0, 800)
        star.rect.x = star.x
        star.rect.y = star.y
        self.stars.add(star)
        
    def _check_keydown_events(self, event):
        """响应按下"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_events(self, event):
        """"响应释放"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _run_game(self):
        while True:
            self.ship.update()
            print(self.ship.moving_up, '  ', self.ship.moving_down)
            print(self.ship.rect)
            self._check_events()
            self.create_star()
            self.update_screen() #刷新屏幕
            time.sleep(0.1)
    

ai = Main()
ai._run_game()