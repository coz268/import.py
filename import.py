import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))

cat_image = pygame.image.load('cat.png')

cats = []

for i in range(5):
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    cats.append((x, y))

score = 0

font = pygame.font.Font(None, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for cat in cats:
                if cat_image.get_rect().move(cat).collidepoint(pos):
                    score += 1
                    cats.remove(cat)
                    break
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((255, 255, 255))

    for cat in cats:
        screen.blit(cat_image, cat)

    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
