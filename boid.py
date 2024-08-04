import numpy as np
import pygame
import random
from variables import (
    WIDTH,
    HEIGHT,
    BOID_LENGTH,
    BOID_WIDTH,
    MAX_SPEED,
    RANDOMNESS,
    MIN_SPEED,
)


class Boid:
    """
    Represents a single boid in the simulation.

    Attributes:
        x (float): The x-coordinate of the boid's position.
        y (float): The y-coordinate of the boid's position.
        vel_x (float): The x-component of the boid's velocity.
        vel_y (float): The y-component of the boid's velocity.
        color (tuple): The color of the boid in RGB format.
    """

    def __init__(self, color, x, y, vel_x, vel_y):
        """
        Initializes a Boid instance.

        Args:
            color (tuple): The color of the boid (RGB).
            x (float): Initial x-coordinate position of the boid.
            y (float): Initial y-coordinate position of the boid.
            vel_x (float): Initial x-component of the boid's velocity.
            vel_y (float): Initial y-component of the boid's velocity.
        """

        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.color = color

    def move(self):
        """
        Updates the position of the boid based on its velocity,
        applying random forces and boundary checks.
        """

        self.apply_random_force()
        self.check_boundaries()

        # Normalize velocity to maintain maximum speed
        speed = np.sqrt(self.vel_x**2 + self.vel_y**2)
        if speed > MAX_SPEED:
            self.vel_x = (self.vel_x / speed) * MAX_SPEED
            self.vel_y = (self.vel_y / speed) * MAX_SPEED
        elif speed < MIN_SPEED:
            self.vel_x = (self.vel_x / speed) * MIN_SPEED
            self.vel_y = (self.vel_y / speed) * MIN_SPEED

        self.x += self.vel_x
        self.y += self.vel_y

    def check_boundaries(self):
        """
        Applies a force to the boid if it is within a margin
        of the screen edges, pushing it away from the edges.
        """
        margin = 50
        force_strength = 0.05

        # Check the distance to each edge and apply a force to move away if within margin

        if self.x < margin:
            if self.x == 0:
                self.vel_x = -self.vel_x
            else:
                self.vel_x += force_strength * margin / self.x
        if self.x > WIDTH - margin:
            if WIDTH == self.x:
                self.vel_x = -self.vel_x
            else:
                self.vel_x -= force_strength * margin / (WIDTH - self.x)
        if self.y < margin:
            if self.y == 0:
                self.vel_y = -self.vel_y
            else:
                self.vel_y += force_strength * margin / self.y
        if self.y > HEIGHT - margin:
            if HEIGHT == self.y:
                self.vel_y = -self.vel_y
            else:
                self.vel_y -= force_strength * margin / (HEIGHT - self.y)

    def apply_random_force(self):
        """
        Applies a small random force to the boid's velocity,
        ensuring that the velocity remains within the specified
        maximum and minimum speed limits.
        """
        rand_force_x = (random.random() - 0.5) * 2 * RANDOMNESS
        rand_force_y = (random.random() - 0.5) * 2 * RANDOMNESS
        self.vel_x += rand_force_x
        self.vel_y += rand_force_y

    def draw(self, screen):
        """
        Draws the boid on the screen as a triangle, oriented
        in the direction of its velocity.

        Args:
            screen (pygame.Surface): The surface to draw the boid on.
        """

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
        pygame.draw.polygon(screen, self.color, [tip, left_base, right_base])
