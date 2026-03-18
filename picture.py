import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
width, height = 800, 600
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
pink = (255, 182, 193)
outline = 5


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Заяц")

# Центр
xc = width // 2
yc = height // 2 - 50

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(white)

    # Уши
    earbl = (xc - 70, yc - 240, 50, 150)
    earbr = (xc + 20, yc - 240, 50, 150)

    # Уши внутри
    earr = (xc - 60, yc - 220, 30, 100)
    earl = (xc + 30, yc - 220, 30, 100)

    # Хвост
    tail = (xc + 80, yc + 150, 35, 35)
    pygame.draw.ellipse(screen, gray, tail, 0)
    pygame.draw.ellipse(screen, black, tail, outline)

    pygame.draw.ellipse(screen, gray, earbl, 0)
    pygame.draw.ellipse(screen, gray, earbr, 0)

    pygame.draw.ellipse(screen, pink, earl, 0)
    pygame.draw.ellipse(screen, pink, earr, 0)

    # Контур
    pygame.draw.ellipse(screen, black, earbl, outline)
    pygame.draw.ellipse(screen, black, earbr, outline)

    # Тело
    body = (xc - 110, yc, 220, 210)
    pygame.draw.ellipse(screen, gray, body, 0)
    pygame.draw.ellipse(screen, black, body, outline)

    # Задние лапы
    legsdl = (xc - 100, yc + 180, 80, 45)
    legsdr = (xc + 20, yc + 180, 80, 45)
    pygame.draw.ellipse(screen, gray, legsdl, 0)
    pygame.draw.ellipse(screen, gray, legsdr, 0)
    pygame.draw.ellipse(screen, black, legsdl, outline)
    pygame.draw.ellipse(screen, black, legsdr, outline)

    # Передние лапы
    legsupl = (xc - 70, yc + 10, 60, 65)
    legsupr = (xc + 10, yc + 10, 60, 65)
    pygame.draw.ellipse(screen, gray, legsupl, 0)
    pygame.draw.ellipse(screen, gray, legsupr, 0)
    pygame.draw.ellipse(screen, black, legsupl, outline)
    pygame.draw.ellipse(screen, black, legsupr, outline)

    # Голова
    head = (xc - 100, yc - 160, 200, 180)
    pygame.draw.ellipse(screen, gray, head, 0)
    pygame.draw.ellipse(screen, black, head, outline)

    # Морда
    eye = 8
    pygame.draw.circle(screen, black, (xc - 35, yc - 85), eye)
    pygame.draw.circle(screen, black, (xc + 35, yc - 85), eye)
    nose = [(xc - 12, yc - 70), (xc + 12, yc - 70), (xc, yc - 55)]
    pygame.draw.polygon(screen, pink, nose)
    pygame.display.flip()
pygame.quit()
sys.exit()