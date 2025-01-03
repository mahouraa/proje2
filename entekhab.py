import pygame
import random

# تعریف متغیرها
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# توسعه مار
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_dir = (0, 1)
snake_speed = 5

# تولید موقعیت تصادفی برای غذا
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def move_snake():
    global snake_dir
    head = snake[0]
    new_head = (head[0] + snake_dir[0], head[1] + snake_dir[1])
    snake.insert(0, new_head)

    # بررسی برخورد مار با دیوار یا خودش
    if new_head in snake[1:] or new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
        return True

    # بررسی رسیدن به غذا
    if new_head == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    return False

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_dir = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake_dir = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake_dir = (1, 0)

    draw_snake()
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    if move_snake():
        running = False

    pygame.display.flip()
    clock.tick(snake_speed)

pygame.quit()