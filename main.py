import pygame
import sys
from palette import Palette
from int_selection import IntSelector
from constant import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Let's color!")
drawing_image = pygame.image.load("cat1.png").convert()

scale_factor = min(SCREEN_WIDTH / drawing_image.get_width(), SCREEN_HEIGHT / drawing_image.get_height())
scaled_drawing_image = pygame.transform.scale(drawing_image, (int(drawing_image.get_width() * scale_factor), int(drawing_image.get_height() * scale_factor)))
drawing_width = scaled_drawing_image.get_width()
drawing_height = scaled_drawing_image.get_height()

painting_surface = pygame.Surface((drawing_width, drawing_height), pygame.SRCALPHA)
painting_surface_collider = pygame.Rect(0, 0, drawing_width, drawing_height)
mouse_surface = pygame.Surface((drawing_width, drawing_height), pygame.SRCALPHA)
palette_colors = [WHITE, BLACK, GREY, BROWN, PINK, GREEN, BLUE, ORANGE]
palette = Palette(5, drawing_height + 5, palette_colors)
palette.draw(screen)
brush_size_selector = IntSelector(5, 50, 10, 5, drawing_height + palette.button_height+20)
brush_size_selector.draw(screen)

def paint_color(color, size, x, y):
    pygame.draw.circle(painting_surface, color, [x, y], size)

def erase_color(color, size, x, y):
    pygame.draw.circle(painting_surface, color, [x, y], size)

def mouse(mouse_position, brush_size):
    mouse_surface.fill(pygame.SRCALPHA)
    pygame.draw.circle(mouse_surface, palette.current_color+(200,), mouse_position, brush_size)

running = True
painting = False
erasing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                if painting_surface_collider.collidepoint(x, y):
                    painting = True
                    opacity = 128
                    paint_color(palette.current_color+(opacity,), brush_size_selector.current_value, x, y)
            elif event.button == 3:
                x, y = pygame.mouse.get_pos()
                if painting_surface_collider.collidepoint(x, y):
                    erasing = True
                    opacity = 0
                    color = [0, 0, 0, opacity]
                    erase_color(color, brush_size_selector.current_value, x, y)
        elif event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            mouse(mouse_position, brush_size_selector.current_value)

            if painting == True:
                x, y = pygame.mouse.get_pos()
                if painting_surface_collider.collidepoint(x, y):
                    opacity = 128
                    paint_color(palette.current_color+(opacity,),brush_size_selector.current_value, x, y)
            elif erasing == True:
                x, y = pygame.mouse.get_pos()
                if painting_surface_collider.collidepoint(x, y):
                    opacity = 0
                    color = [0, 0, 0, opacity]
                    paint_color(color,brush_size_selector.current_value, x, y)
        elif event.type == pygame.MOUSEBUTTONUP:
            painting = False
            erasing = False
        palette.handle_event(event)
        brush_size_selector.handle_event(event)
    
    screen.fill(BLACK)
    screen.blit(scaled_drawing_image, (0,0))
    screen.blit(painting_surface, (0,0))
    screen.blit(mouse_surface, (0,0))
    palette.draw(screen)
    brush_size_selector.draw(screen)

    pygame.display.update()

pygame.quit()
sys.exit()
          