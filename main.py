from Include.model import *

# 设置屏幕的宽度
SCREEN_WIDTH = 450
# 设置屏幕的高度
SCREEN_HEIGHT = 600
# 初始化窗口
pygame.init()
# 设置窗口标题
pygame.display.set_caption("飞机大战")
# 设置屏幕大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
# 隐藏光标
pygame.mouse.set_visible(False)
# 设置背景
bg = pygame.image.load("resources/image/bg.png")
# 设置游戏结束的图片
bg_game_over = pygame.image.load("resources/image/bg_game_over.png")
# 加载飞机资源图片
img_plane = pygame.image.load("resources/image/shoot.png")
img_start = pygame.image.load("resources/image/start.png")
img_pause = pygame.image.load("resources/image/pause.png")
img_icon = pygame.image.load("resources/image/plane.png").convert_alpha()
# 顺便设置窗口
pygame.display.set_icon(img_icon)
# 初始化飞机区域
player_rect = []
player_rect.append(pygame.Rect(0, 99, 102, 126))
player_rect.append(pygame.Rect(165, 360, 102, 126))
# 玩家爆炸图片
player_rect.append(pygame.Rect(165, 234, 102, 126))
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))
# 初始化位置
player_pos = [200, 450]
# 生成玩家类
player = Player(img_plane, player_rect, player_pos)
# 设置子弹框
bullet_rect = pygame.Rect(1004, 987, 9, 21)
# 加载子弹图片
bullet_img = img_plane.subsurface(bullet_rect)
# 设置敌人框
enemy_rect = pygame.Rect(534, 612, 57, 43)
# 设置敌人图片
enemy_img = img_plane.subsurface(enemy_rect)
# 设置敌人被击图片
enemy_explosion_imgs = []
enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(267, 347, 57, 43)))
enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(873, 697, 57, 43)))
enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(267, 296, 57, 43)))
enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(930, 697, 57, 43)))
# 设置敌机精灵组
enemies = pygame.sprite.Group()
# 设置敌机被击精灵组
enemies_explosion = pygame.sprite.Group()
# 设置射击频率
shoot_frequency = 0
# 设置敌机频率
enemy_frequency = 0
# 设置玩家被击的图片顺序
player_explosion_index = 16
score = 0
running = True
is_pause = False
is_game_over = False
clock = pygame.time.Clock()
