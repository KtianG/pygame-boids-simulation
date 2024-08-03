import numpy as np
import pygame
import random
from variables import (
    WIDTH,
    HEIGHT,
    BOID_LENGTH,
    BOID_WIDTH,
    BOID_COLOR,
    MAX_SPEED,
    RANDOMNESS,
    MIN_SPEED,
)


class Boid:

    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.alignment = 0

    def move(self):
        self.apply_random_force()
        self.check_boundaries()
        self.x += self.vel_x
        self.y += self.vel_y

    def check_boundaries(self):
        margin = 50
        force_strength = 0.05

        # Check the distance to each edge and apply a force to move away if within margin

        if self.x < margin:
            self.vel_x += force_strength
        if self.x > WIDTH - margin:
            self.vel_x -= force_strength
        if self.y < margin:
            self.vel_y += force_strength
        if self.y > HEIGHT - margin:
            self.vel_y -= force_strength

    def apply_random_force(self):
        # Generate random force within the range of [-random_strength, random_strength]
        rand_force_x = (random.random() - 0.5) * 2 * RANDOMNESS
        rand_force_y = (random.random() - 0.5) * 2 * RANDOMNESS

        # Update velocity with random force
        self.vel_x += rand_force_x
        self.vel_y += rand_force_y

        # Normalize velocity to maintain maximum speed
        speed = np.sqrt(self.vel_x**2 + self.vel_y**2)
        if speed > MAX_SPEED:
            self.vel_x = (self.vel_x / speed) * MAX_SPEED
            self.vel_y = (self.vel_y / speed) * MAX_SPEED
        elif speed < MIN_SPEED:
            self.vel_x = (self.vel_x / speed) * MIN_SPEED
            self.vel_y = (self.vel_y / speed) * MIN_SPEED

    def draw(self, screen):
        angle = np.arctan2(self.vel_y, self.vel_x)

        # Calculate the tip of the triangle
        tip = (
            self.x + BOID_LENGTH * np.cos(angle),
            self.y + BOID_LENGTH * np.sin(angle),
        )

        # Calculate the base corners of the triangle
        left_base = (
            self.x + BOID_WIDTH * np.cos(angle + np.pi / 2),
            self.y + BOID_WIDTH * np.sin(angle + np.pi / 2),
        )
        right_base = (
            self.x + BOID_WIDTH * np.cos(angle - np.pi / 2),
            self.y + BOID_WIDTH * np.sin(angle - np.pi / 2),
        )

        # Draw the triangle
        pygame.draw.polygon(screen, BOID_COLOR, [tip, left_base, right_base])
