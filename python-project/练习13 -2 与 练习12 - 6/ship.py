import pygame
from pygame.sprite import Sprite
from settings import Settings
class Ship(Sprite):
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = Settings(0)
        self.screen_rect = ai_game.screen.get_rect()
        
        #加载飞船图像并获取其外接矩形
        
        
        #no
        #0：生命标识
        #1：基本状态
        self.image = pygame.image.load('images/小飞船.jpg')
            
        self.rect = self.image.get_rect()
        
        #每艘飞船都放在屏幕底部的中央
        # self.rect.midbottom = self.screen_rect.midbottom
        
        #在飞船的属性中存储一个浮点数
        # self.y = float(self.rect.y)
        
        #移动标志 （飞船一开始不移动）
        self.moving_up = False
        self.moving_down = False
        self.rect.x = 0
        self.rect.y = 400       
    def update(self):
        """根据移动标志调整飞船的位置"""
        
        if self.moving_up and self.rect.y > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.y < 800:
            self.rect.y += self.settings.ship_speed
            
        #根据self.x更新rect对象

        
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        
    # def center_ship(self):
    #     """将飞船放置在屏幕左边的中央"""
    #     self.rect.midbottom = self.screen_rect.midbottom
    #     self.y = float(self.rect.yx)