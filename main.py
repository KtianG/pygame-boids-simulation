import pygame
import random
from boid import Boid
from variables import BACKGROUND, WIDTH, HEIGHT, FPS, NUM_BOIDS, MAX_SPEED

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def main():

    running = True
    playing = False
    count = 0
    update_frequency = 30
    boids = []
    for _ in range(NUM_BOIDS):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        vel_x = (random.random() - 0.5) * 2 * MAX_SPEED
        vel_y = (random.random() - 0.5) * 2 * MAX_SPEED
        boids.append(Boid(x, y, vel_x, vel_y))

    test_boid = Boid(WIDTH // 2, HEIGHT // 2, 1, 1)

    while running:
        clock.tick(FPS)

        if playing:
            count += 1
            if count >= update_frequency:
                count = 0

        pygame.display.set_caption("Playing" if playing else "Paused")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                    count = 0

        screen.fill(BACKGROUND)
        for boid in boids:
            boid.move()
            boid.draw(screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
