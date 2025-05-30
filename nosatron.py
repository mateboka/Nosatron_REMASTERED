import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1500, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TRON Lite - 2 Players")

# Colors
BLACK = (0, 0, 0)
PLAYER1_COLOR = (0, 255, 255)  # Cyan
PLAYER2_COLOR = (255, 165, 0)  # Orange

# Settings
FPS = 60
TURN_ANGLE = 90  # degrees to turn on key press
SPEED = 4        # pixels per frame

clock = pygame.time.Clock()

# Player class
class Player:
    def __init__(self, x, y, angle, color, left_key, right_key):
        self.x = x
        self.y = y
        self.angle = angle  # In degrees
        self.color = color
        self.left_key = left_key
        self.right_key = right_key
        self.trail = [(x, y)]

    def update(self, keys_pressed):
        if keys_pressed[self.left_key]:
            self.angle = (self.angle - TURN_ANGLE) % 360
        if keys_pressed[self.right_key]:
            self.angle = (self.angle + TURN_ANGLE) % 360

        # Move forward
        rad = math.radians(self.angle)
        self.x += SPEED * math.cos(rad)
        self.y += SPEED * math.sin(rad)

        # Append new position to trail
        self.trail.append((int(self.x), int(self.y)))

    def draw(self, surface):
        if len(self.trail) > 1:
            pygame.draw.lines(surface, self.color, False, self.trail, 3)
        # Draw current head as a circle
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), 5)

# Initialize players
player1 = Player(WIDTH * 0.25, HEIGHT // 2, 0, PLAYER1_COLOR, pygame.K_a, pygame.K_d)
player2 = Player(WIDTH * 0.75, HEIGHT // 2, 180, PLAYER2_COLOR, pygame.K_LEFT, pygame.K_RIGHT)

players = [player1, player2]

def main():
    running = True
    screen.fill(BLACK)

    while running:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update all players
        for p in players:
            p.update(keys_pressed)

        # Draw everything
        screen.fill(BLACK)
        for p in players:
            p.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
