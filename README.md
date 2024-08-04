# Boid Simulation

A boid simulation project using Pygame that models the flocking behavior of boids. This project demonstrates basic concepts of swarm intelligence and agent-based modeling using Python and Pygame.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Configuration](#configuration)

## Features

- Simulates flocking behavior of boids with separation, alignment, and cohesion rules.
- Two flocks of boids with different colors and sizes.
- Dynamic visualization using Pygame.


## How It Works

The simulation consists of the following components:

- **Boid Class**: Represents an individual boid with attributes for position, velocity, and behavior. Each boid applies random forces, checks for boundary conditions, and follows basic flocking rules.
  
- **Flock Class**: Manages a collection of boids, applies flocking behavior rules (separation, alignment, cohesion), and updates their positions and velocities.

- **Main Script (`main.py`)**: Initializes Pygame, creates two flocks of boids with different colors, and runs the game loop. It updates the boids, and renders them to the screen.

## Configuration

The simulation's behavior and appearance can be configured by modifying the `variables.py` file. Here you can adjust parameters such as:

- `BACKGROUND`: Background color of the simulation.
- `WIDTH` and `HEIGHT`: Dimensions of the game window.
- `FPS`: Frames per second for the simulation.
- `NUM_BOIDS`: Number of boids in each flock.
- `BOID_COLOR` and `BOID_COLOR2`: Colors for different flocks.
- `MAX_SPEED`, `MIN_SPEED`, `MAX_ACCELERATION`: Movement constraints for the boids.
- `SEPARATION_WEIGHT`, `ALIGNMENT_WEIGHT`, `COHESION_WEIGHT`: Weights for flocking behavior rules.
