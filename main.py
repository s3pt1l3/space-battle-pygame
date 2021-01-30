import pygame
from pygame.sprite import Group

from stats import GameStats
from settings import Settings
from button import Button
from ship import Ship
from scoreboard import Scoreboard
import game_functions as gf

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
    
    # Музыка
    music = pygame.mixer.music.load('music/music.mp3')
    pygame.mixer.music.play(-1)
    
    # Создание экземпляров классов для хранения статистики и очков
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Создание корабля, пришельцев и пуль
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Создание инопланетного флота
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    pygame.display.flip()
    # Главный игровой цикл
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)

if __name__ == '__main__':
    run()