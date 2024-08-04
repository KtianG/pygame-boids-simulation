import pygame
from boid import Boid
from flock import Flock
from variables import (
    BACKGROUND,
    WIDTH,
    HEIGHT,
    FPS,
    BOID_COLOR,
    BOID_COLOR2,
    BOID_COLOR3,
    BOID_COLOR4,
    BOID_COLOR5,
)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def main():
    """
    Main function that initializes the Pygame environment, creates flocks of boids,
    and runs the game loop. It handles user input, updates the state of the boids,
    and draws them to the screen.

    The function performs the following tasks:
    - Initializes the game window and clock.
    - Creates flocks of boids with different colors and sizes.
    - Runs the game loop, handling user input to pause/play the simulation and
      updating and drawing the boids.
    - Handles quitting the game when the user closes the window.
    """

    running = True
    playing = False
    count = 0
    update_frequency = 30

    colors = [BOID_COLOR, BOID_COLOR2, BOID_COLOR3, BOID_COLOR4]
    flocks = []

    for color in colors:
        flock = Flock(color, 30)
        flocks.append(flock)

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
        for flock in flocks:
            flock.update()
            flock.draw(screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
