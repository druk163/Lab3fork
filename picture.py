import pygame
import sys

# Настройки экрана
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
PINK = (255, 182, 193)
OUTLINE = 5

# Глобальное смещение (центр персонажа)
XC, YC = WIDTH // 2, HEIGHT // 2 - 50

# Список объектов: [тип, цвет, (x_offset, y_offset, w, h), контур]
# Типы: 'e' - эллипс, 'c' - круг, 'p' - полигон
OBJECTS = [
    ('e', GRAY, (80, 150, 35, 35), OUTLINE),    # Хвост
    ('e', GRAY, (-70, -240, 50, 150), OUTLINE), # Левое ухо
    ('e', GRAY, (20, -240, 50, 150), OUTLINE),  # Правое ухо
    ('e', PINK, (-60, -220, 30, 100), 0),       # Внутри левого
    ('e', PINK, (30, -220, 30, 100), 0),        # Внутри правого
    ('e', GRAY, (-110, 0, 220, 210), OUTLINE),  # Тело
    ('e', GRAY, (-100, 180, 80, 45), OUTLINE),  # Задняя левая
    ('e', GRAY, (20, 180, 80, 45), OUTLINE),    # Задняя правая
    ('e', GRAY, (-70, 10, 60, 65), OUTLINE),    # Передняя левая
    ('e', GRAY, (10, 10, 60, 65), OUTLINE),     # Передняя правая
    ('e', GRAY, (-100, -160, 200, 180), OUTLINE),# Голова
    ('c', BLACK, (-35, -85, 8), 0),             # Глаз Л
    ('c', BLACK, (35, -85, 8), 0),              # Глаз П
    ('p', PINK, [(-12, -70), (12, -70), (0, -55)], 0) # Нос
]

def draw_scene(surface):
    for obj_type, color, coords, border in OBJECTS:
        if obj_type == 'e':  # Эллипс
            rect = (XC + coords[0], YC + coords[1], coords[2], coords[3])
            pygame.draw.ellipse(surface, color, rect, 0)
            if border > 0:
                pygame.draw.ellipse(surface, BLACK, rect, border)
        
        elif obj_type == 'c':  # Круг
            pos = (XC + coords[0], YC + coords[1])
            pygame.draw.circle(surface, color, pos, coords[2])
            
        elif obj_type == 'p':  # Полигон
            points = [(XC + p[0], YC + p[1]) for p in coords]
            pygame.draw.polygon(surface, color, points)

# Основной цикл
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    draw_scene(screen)
    pygame.display.flip()
    clock.tick(60)
