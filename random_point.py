from functools import cache
import pygame
import random
import math

pygame.init()
pygame.display.set_caption("fair random point in circle")

WHITE = (255, 255, 255)
GRAY = (70, 70, 70)
BLACK = (0, 0 ,0)
FPS = 1000
size = (600, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = False

@cache
def font(size):
    return pygame.font.Font('./font/NotoSansKR-Medium.otf', size)

def write(txt, font_size, color, pos, criterion="center"):
    text = font(font_size).render(txt, True, color)
    text_pos = text.get_rect()
    if criterion == "center":
        text_pos.center = pos
    elif criterion == "top":
        text_pos.top = pos
    elif criterion == "topleft":
        text_pos.topleft = pos
    elif criterion == "topright":
        text_pos.topright = pos
    elif criterion == "bottom":
        text_pos.bottom = pos
    elif criterion == "bottomleft":
        text_pos.bottomleft = pos
    elif criterion == "bottomright":
        text_pos.bottomright = pos
    screen.blit(text, text_pos)

radius = 250
dot_pos = []
dot_count = 0
short_count = 0
out_count = 0
all_count = 0

method = 3

def getAbsCoord(x, y):
    pos = (x, y)
    return (size[0]//2 + pos[0], size[1]//2 + pos[1])

def getLength(probability):
    return radius * math.sqrt(probability)

while not done:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    if method == 1:
        length = random.uniform(0, radius)
        theta = math.radians(random.uniform(0, 360))
        all_count += 1
    elif method == 2:
        while True:
            all_count += 1
            x = random.uniform(-radius, radius)
            y = random.uniform(-radius, radius)
            length = math.sqrt(x*x + y*y)
            if length <= radius:
                break
            out_count += 1
    elif method == 3:
        length = getLength(random.random())
        theta = math.radians(random.uniform(0, 360))
        all_count += 1

    if length <= radius/2:
        short_count += 1
    dot_count += 1

    if method == 2:
        dot_pos.append(getAbsCoord(x, y))
    else:
        dot_pos.append(getAbsCoord(length*math.cos(theta), length*math.sin(theta)))

    for i in dot_pos:
        pygame.draw.circle(screen, WHITE, i, 1)

    write(f"{short_count/dot_count:.2f}", 50, WHITE, (0, 0), "topleft")
    write(f"{out_count/all_count:.2f}", 50, WHITE, (size[0], 0), "topright")
    pygame.draw.circle(screen, WHITE, (size[0]//2, size[1]//2), radius, 1)

    pygame.display.update()

pygame.quit()