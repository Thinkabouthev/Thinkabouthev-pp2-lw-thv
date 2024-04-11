import pygame
import math

# Устанавливаем размеры экрана
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
SALMON = (250, 128, 114)
GOLD = (255, 215, 0)
TAN = (210, 180, 140)
NAVY = (0, 0, 128)
INDIGO = (75, 0, 130)

# Размеры элементов в меню
MENU_ITEM_WIDTH = 20
MENU_ITEM_HEIGHT = 20
MENU_ITEM_SPACING = 20  # расстояние между элементами.

# Размеры ластика
ERASER_WIDTH = 40
ERASER_HEIGHT = 40

# Радиус кисти
DEFAULT_RADIUS = 5

# Размеры прямоугольника и окружности при рисовании с клавиатуры
RECTANGLE_SIZE = 100
CIRCLE_RADIUS = 50

# Инициализация Pygame
pygame.init()

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption('Paint(2.0)')

# Переменные для рисования
draw_on = False
last_pos = (0, 0)  # хранениу последней позиции курсора мыши

# Меню с цветами
menu_colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK, BLACK, GRAY, BROWN, CYAN, MAGENTA, LIGHT_BLUE, LIGHT_GREEN, SALMON, GOLD, TAN, NAVY, INDIGO]
for i, color in enumerate(menu_colors):  # нумерация цветов
    pygame.draw.rect(screen, color, (0, MENU_ITEM_SPACING * i, MENU_ITEM_WIDTH, MENU_ITEM_HEIGHT))

# Ластик
eraser = pygame.transform.scale(pygame.image.load("eraser.png"), (ERASER_WIDTH, ERASER_HEIGHT))
screen.blit(eraser, [0, MENU_ITEM_SPACING * len(menu_colors)])


# Функция для рисования плавной линии
def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)  # center of circle (x,y)


# Функция для рисования квадрата
def draw_square(canvas, color, center, size):
    x, y = center
    half_size = size // 2
    pygame.draw.rect(canvas, color, (x - half_size, y - half_size, size, size))


# Функция для рисования прямоугольного треугольника
def draw_right_triangle(canvas, color, start, size):
    x, y = start
    pygame.draw.polygon(canvas, color, [(x, y), (x, y + size), (x + size, y)])


def draw_right_triangle2(canvas, color, start, size):
    x, y = start
    pygame.draw.polygon(canvas, color, [(x, y), (x + size, y), (x + size, y + size)])

# Функция для рисования равностороннего треугольника
def draw_equilateral_triangle(canvas, color, start, size):
    x, y = start
    height = int(size * math.sqrt(3) / 2)
    pygame.draw.polygon(canvas, color, [(x, y), (x + size, y), (x + size / 2, y - height)])


# Функция для рисования ромба
def draw_rhombus(canvas, color, center, size):
    x, y = center
    half_size = size // 2
    pygame.draw.polygon(canvas, color, [(x, y - half_size), (x + half_size, y), (x, y + half_size), (x - half_size, y)])


# Главный цикл игры
try:
    while True:
        e = pygame.event.wait()

        if e.type == pygame.QUIT:
            raise StopIteration

        if e.type == pygame.MOUSEBUTTONDOWN:
            spot = pygame.mouse.get_pos()
            if spot[0] < MENU_ITEM_WIDTH:
                if 0 <= spot[1] < MENU_ITEM_SPACING * len(menu_colors):
                    color = menu_colors[spot[1] // MENU_ITEM_SPACING]
                elif MENU_ITEM_SPACING * len(menu_colors) <= spot[1] < MENU_ITEM_SPACING * (len(menu_colors) + 1):
                    color = WHITE
            elif spot[0] > MENU_ITEM_WIDTH:
                pygame.draw.circle(screen, color, e.pos, DEFAULT_RADIUS)
            draw_on = True
        elif e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        elif e.type == pygame.MOUSEMOTION:
            spot = pygame.mouse.get_pos()
            if draw_on and spot[0] > MENU_ITEM_WIDTH:
                pygame.draw.circle(screen, color, e.pos, DEFAULT_RADIUS)
                roundline(screen, color, e.pos, last_pos, DEFAULT_RADIUS)
            last_pos = e.pos
        elif e.type == pygame.KEYDOWN:
            spot = pygame.mouse.get_pos()
            if e.key == pygame.K_s:
                draw_square(screen, color, spot, RECTANGLE_SIZE)
            elif e.key == pygame.K_r:
                pygame.draw.rect(screen, color, (spot[0], spot[1], RECTANGLE_SIZE, RECTANGLE_SIZE + RECTANGLE_SIZE/2 ))
            elif e.key == pygame.K_c:
                pygame.draw.circle(screen, color, spot, CIRCLE_RADIUS)
            elif e.key == pygame.K_t:
                draw_right_triangle(screen, color, spot, RECTANGLE_SIZE)
            elif e.key == pygame.K_p:
                draw_right_triangle2(screen, color, spot, RECTANGLE_SIZE)
            elif e.key == pygame.K_e:
                draw_equilateral_triangle(screen, color, spot, RECTANGLE_SIZE)
            elif e.key == pygame.K_o:
                draw_rhombus(screen, color, spot, RECTANGLE_SIZE)
            
                

        pygame.display.flip()

except StopIteration:
    pass

pygame
