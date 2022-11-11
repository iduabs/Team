import pygame


# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        # 设置图片的区域
        self.rect = self.image.get_rect()
        self.rect.midbottom = pos
        self.speed = 10

    def move(self):
        self.rect.top -= self.speed


# 敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self, img, explosion_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.explosion_img = explosion_img
        self.speed = 2
        # 设置击毁序列
        self.explosion_index = 0

    def move(self):
        # 敌人的子弹只能一直向下
        self.rect.top += self.speed


# 玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self, img, rect, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        # 将飞机图片部分分隔
        for i in range(len(rect)):
            self.image.append(img.subsurface(rect[i]).convert_alpha())
        # 获取飞机的区域
        self.rect = rect[0]
        self.rect.topleft = pos
        self.speed = 8
        # 生成精灵组实例
        self.bullets = pygame.sprite.Group()
        self.img_index = 0
        # 判断飞机是否被打中
        self.is_hit = False
