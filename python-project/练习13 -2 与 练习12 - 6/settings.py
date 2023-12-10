class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self, no):
        """"初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        #飞船的设置
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        #子弹类型的初始化
        self.bullet_no = 0
        #子弹数量上限
        self.bullets_allowed = 5
        # self.bullet_speed = 15
        # self.bullet_width = 100
        # self.bullet_height = 15
        # self.bullet_color = (0, 255, 0)
    
        #外星人的设置
        self.alien_speed = 50
        self.fleet_drop_speed = 30
        #以什么速度加快游戏的节奏
        self.speedup_scale = 1.1
        #外星人分数的提高速度
        self.score_scale = 1.5
        
        #道具限量与其编号
        self.prop_limit = 1
        self.prop_no = no
        #掉率设置
        #
        self.prop_rate = 2
        #道具最大编号
        self.prop_nums = 2
        
        self.prop_speed = 10
        self.prop_width = 40
        self.prop_height = 40
        #1 加生命
        #2 子弹变1类
        #3 子弹变2类
        self.prop_color = (255, 0, 0)
        
        if no == 0:
            self.prop_color = (255, 0, 0)
            
        elif no == 1:
            self.prop_color = (0, 255, 0)
            
        elif no == 2:
            self.prop_color = (0, 0, 255)
        self.initialize_dynamic_settings()
    
            
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而改变的设置"""
        self.ship_speed = 15
        self.bullet_speed = 25
        self.alien_speed = 10
        
        #fleet_direction为1代表向右移动， 为-1代表向左移动
        self.fleet_direction = 1.0
        
        #积分设置
        self.alien_points = 50
        
        
    def increase_speed(self):
        """提高速度设置的值和外星人分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)