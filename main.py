import pygame
import sys
from palette import Palette
from int_selection import IntSelector
from constant import *
from canvas import Canvas

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Let's color!")

canvas = Canvas("./cat1.png")
palette_colors = [WHITE, BLACK, GREY, BROWN, PINK, GREEN, BLUE, ORANGE]

palette = Palette(5, canvas.bg_image.get_height() + 5, palette_colors)
brush_size_selector = IntSelector(5, 50, 10, 5, canvas.bg_image.get_height() + palette.button_height+20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        canvas.handle_event(event, palette.current_color, brush_size_selector.current_value)
        palette.handle_event(event)
        brush_size_selector.handle_event(event)
    
    screen.fill(BLACK)
    canvas.draw(screen)
    palette.draw(screen)
    brush_size_selector.draw(screen)

    pygame.display.update()

pygame.quit()
sys.exit()
          