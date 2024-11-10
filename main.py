import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  while True:
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return

    pygame.Surface.fill(screen, pygame.Color("black"))
    pygame.display.flip()

if __name__ == "__main__":
  main()