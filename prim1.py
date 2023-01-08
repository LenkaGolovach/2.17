import pygame

# Инициализируем Pygame
pygame.init()

# Устанавливаем размеры окна
screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновляем экран
    pygame.display.flip()

# Завершаем работу Pygame
pygame.quit()
