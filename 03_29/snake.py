import pygame
import random

# Размер окна
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
# Размер одного блока
BLOCK_SIZE = SCREEN_HEIGHT // 50

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Условные обознчения направлений
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")


# Отрисовка Игрока
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, BLACK, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])



def main_loop():
    # Иницилизация игрока
    snake_x = SCREEN_WIDTH / 2
    snake_y = SCREEN_HEIGHT / 2

    snake_list = [[snake_x, snake_y]]
    snake_len = 1 # Фактическая длинна змеи
    snake_dir = LEFT

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                # Обработка нажатий
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_LEFT]:
                    snake_dir = LEFT
                if pressed[pygame.K_RIGHT]:
                    snake_dir = RIGHT
                if pressed[pygame.K_UP]:
                    snake_dir = UP
                if pressed[pygame.K_DOWN]:
                    snake_dir = DOWN
                if pressed[pygame.K_SPACE]:
                    snake_len += 1

        # Проверка На изменение направления
        if snake_dir == LEFT:
            snake_x -= BLOCK_SIZE
        if snake_dir == RIGHT:
            snake_x += BLOCK_SIZE
        if snake_dir == UP:
            snake_y -= BLOCK_SIZE
        if snake_dir == DOWN:
            snake_y += BLOCK_SIZE

        # Движение змеи
        snake_head = [snake_x, snake_y]
        snake_list.insert(0, snake_head) # Добвление новой головы
        if len(snake_list) > snake_len:  # Если размер змеи не изменился
            del snake_list[-1]           # Удаление последнего элемента

        screen.fill(WHITE)
        draw_snake(snake_list)
        pygame.display.update()
        pygame.time.Clock().tick(10)


if __name__ == "__main__":
    main_loop()
