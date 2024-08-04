import numpy as np
import random
from boid import Boid
from variables import (
    WIDTH,
    HEIGHT,
    BOID_WIDTH,
    MAX_SPEED,
    MAX_ACCELERATION,
    DESIRED_SEPARATION,
    NEIGHBOR_DIST,
    RANDOMNESS,
    SEPARATION_WEIGHT,
    ALIGNMENT_WEIGHT,
    COHESION_WEIGHT,
)


class Flock:
    """
    Represents a collection of boids (a flock) in the simulation.

    Attributes:
        boids (list): A list of Boid objects representing the flock.
    """

    def __init__(self, color, num_boids):
        """
        Initializes the Flock with a specified number of boids.

        Args:
            color (tuple): The color of the boids (RGB).
            num_boids (int): The number of boids to create in the flock.
        """
        self.boids = []
        for _ in range(num_boids):
            x = random.randint(WIDTH // 4, WIDTH // 4 * 3)
            y = random.randint(HEIGHT // 4, HEIGHT // 4 * 3)
            vel_x = (random.random() - 0.5) * 2 * MAX_SPEED
            vel_y = (random.random() - 0.5) * 2 * MAX_SPEED
            self.boids.append(Boid(color, x, y, vel_x, vel_y))

    def update(self):
        """
        Updates the positions and velocities of all boids in the flock
        based on flocking rules, and moves each boid accordingly.
        """
        for boid in self.boids:
            self.apply_flocking_rules(boid)
            boid.move()

    def apply_flocking_rules(self, boid):
        """
        Applies the flocking rules to a single boid to calculate and
        update its velocity based on interactions with other boids.

        Args:
            boid (Boid): The boid to which the flocking rules will be applied.
        """
        # Initialize forces
        separation_force = np.array([0.0, 0.0])
        alignment_force = np.array([0.0, 0.0])
        cohesion_force = np.array([0.0, 0.0])
        count = 0

        boid_velocity = np.array([boid.vel_x, boid.vel_y])
        boid_speed = np.linalg.norm(boid_velocity)

        for other in self.boids:
            if other == boid:
                continue
            distance = np.sqrt((boid.x - other.x) ** 2 + (boid.y - other.y) ** 2)
            if distance < NEIGHBOR_DIST:

                # Calculate vector from boid to other boid
                vector_to_other = np.array([other.x - boid.x, other.y - boid.y])
                distance_to_other = np.linalg.norm(vector_to_other)
                vector_to_other_normalized = (
                    vector_to_other / distance_to_other
                    if distance_to_other > 0
                    else vector_to_other
                )

                # Calculate angle between boid's velocity and vector_to_other
                angle = np.arccos(
                    np.dot(boid_velocity, vector_to_other_normalized)
                    / (boid_speed * distance_to_other)
                )
                angle_degrees = np.degrees(angle)

                if angle_degrees <= 90:
                    # Separation
                    if distance < DESIRED_SEPARATION:
                        if distance < BOID_WIDTH:
                            separation_force += (
                                (random.choice([-1, 1])),
                                (random.choice([-1, 1])),
                            )
                        else:
                            separation_multiplier = DESIRED_SEPARATION / distance
                            separation_force += (
                                (boid.x - other.x) * separation_multiplier,
                                (boid.y - other.y) * separation_multiplier,
                            )

                    # Alignment
                    alignment_force += np.array([other.vel_x, other.vel_y])

                    # Cohesion
                    cohesion_force += np.array([other.x, other.y])

                    count += 1

        if count > 0:
            rand_force_x = (random.random() - 0.5) * 2 * RANDOMNESS
            rand_force_y = (random.random() - 0.5) * 2 * RANDOMNESS

            # Normalize forces
            separation_force /= count
            alignment_force /= count
            cohesion_force /= count
            rand_force = np.array([rand_force_x, rand_force_y]) / count

            # Apply weights
            total_force = (
                SEPARATION_WEIGHT * separation_force
                + ALIGNMENT_WEIGHT * alignment_force
                + COHESION_WEIGHT * (cohesion_force - np.array([boid.x, boid.y]))
                + rand_force
            )

            # Limit the total force to MAX_ACCELERATION
            force_magnitude = np.linalg.norm(total_force)
            if force_magnitude > MAX_ACCELERATION:
                total_force = (total_force / force_magnitude) * MAX_ACCELERATION

            # Update boid velocity
            boid.vel_x += total_force[0]
            boid.vel_y += total_force[1]

    def draw(self, screen):
        """
        Draws all boids in the flock on the given screen.

        Args:
            screen (pygame.Surface): The surface to draw the boids on.
        """
        for boid in self.boids:
            boid.draw(screen)
