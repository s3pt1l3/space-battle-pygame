import pygame

def run():
    """
    Главная функция, в ней происходит запуск игры
    """
    
    # Инициализация
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Space battle")
    pygame.display.flip()
    
    # Проверка на выход из игры
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

if __name__ == '__main__':
    run()