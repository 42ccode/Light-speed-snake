import pygame
import random
import copy

# 初始化游戏
pygame.init()
clock = pygame.time.Clock()  #生成一个控制速度fps
screen = pygame.display.set_mode((500, 500))  #设置游戏界面大小
pygame.display.set_caption("贪吃蛇")  #标题

# 蛇的初始位置
snake_list = [[100, 50], [90, 50], [80, 50]]  #蛇的出生点

# 初始移动方向
move_up = False
move_down = False
move_left = False
move_right = True

# 食物的位置
food_point = [random.randint(10, 490), random.randint(10, 490)]

running = True  # 游戏开关
while running:
    clock.tick(50)  #调整速度
    screen.fill((255, 255, 255))  # 绘制屏幕为白色

    # 检测键盘输入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not move_down:
                move_up = True
                move_down = False
                move_left = False
                move_right = False
            elif event.key == pygame.K_DOWN and not move_up:
                move_up = False
                move_down = True
                move_left = False
                move_right = False
            elif event.key == pygame.K_LEFT and not move_right:
                move_up = False
                move_down = False
                move_left = True
                move_right = False
            elif event.key == pygame.K_RIGHT and not move_left:
                move_up = False
                move_down = False
                move_left = False
                move_right = True

    # 移动蛇的身体
    for i in range(len(snake_list) - 1, 0, -1):
        snake_list[i] = copy.deepcopy(snake_list[i - 1])

    # 移动蛇的头
    if move_up:
        snake_list[0][1] -= 10
    if move_down:
        snake_list[0][1] += 10
    if move_left:
        snake_list[0][0] -= 10
    if move_right:
        snake_list[0][0] += 10

    # 检查蛇是否吃到食物
    if pygame.Rect(snake_list[0], (10, 10)).collidepoint(food_point):
        snake_list.append(snake_list[-1][:])
        food_point = [random.randint(10, 490), random.randint(10, 490)]

    # 绘制食物
    pygame.draw.circle(screen, [255, 0, 0], food_point, 5)

    # 绘制蛇
    for point in snake_list:
        pygame.draw.rect(screen, [0, 255, 0], pygame.Rect(point[0], point[1], 10, 10))

    # 检查蛇是否撞到自己或边界
    for block in snake_list[1:]:
        if snake_list[0] == block:
            running = False
    if snake_list[0][0] < 0 or snake_list[0][0] >= 500 or snake_list[0][1] < 0 or snake_list[0][1] >= 500:
        running = False

    pygame.display.update()

print("game over!")
pygame.quit()
