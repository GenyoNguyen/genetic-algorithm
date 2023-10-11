import pygame
import os
from Population import Population
pygame.font.init()

WIDTH, HEIGHT = 960, 450
alfa = 0
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chuc co ngay Nha giao Viet Nam vui ve")
BG = pygame.image.load(os.path.join("asset", "bg.png"))

font = pygame.font.SysFont("comicsans", 70)
font2 = pygame.font.SysFont("comicsans", 40)
best = ""


target = "Happy Teacher's Day!"
maxpop = 800
mutationRate = 0.01

population = Population(target, maxpop, mutationRate)


def generateSentence():
    population.calFitness()
    population.naturalSelection()
    population.generate()
    population.evaluate()
    return population.best


def draw(best, alfa):
    sentence = font.render(best, True, (255, 0, 0))
    sentence2 = font2.render("Chuc co ngay Nha giao Viet Nam vui ve", True, (0, 0, 255))

    WIN.blit(BG, (0, 0))
    WIN.blit(sentence, (WIDTH/2 - sentence.get_rect().width/2, HEIGHT/2 - sentence.get_rect().height/2))

    sentence2.set_alpha(alfa)
    WIN.blit(sentence2, (WIDTH/2 - sentence2.get_rect().width/2, HEIGHT/2 + sentence.get_rect().height))

    pygame.display.update()


clock = pygame.time.Clock()

running = True
run = False
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        run = True
    if run:
        if not population.isFinished:
            best = generateSentence()
        else:
            if alfa < 255:
                alfa += 1
        draw(best, alfa)
