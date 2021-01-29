import pygame
from settings import Settings
from button import Button

def run():
    """
    Главная функция, в ней происходит запуск игры
    """
    
    # Инициализация
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space battle")
    
    # Создание кнопки Play
    play_button = Button(ai_settings, screen, "Play")
    
    pygame.display.flip()
    
    # Проверка на выход из игры
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

if __name__ == '__main__':
    run()