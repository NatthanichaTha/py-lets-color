import pygame
import sys
import os
from palette import Palette
from int_selection import IntSelector
from constant import *
from canvas import Canvas
from button import Button
import random

def capture():
    capture_surface = pygame.Surface((canvas.bg_image.get_width(), canvas.bg_image.get_height()), pygame.SRCALPHA)
    capture_surface.blit(canvas.bg_image, (0, 0))
    capture_surface.blit(canvas.painting_surface, (0, 0))
    pygame.image.save(capture_surface,"Capture.png") 
    

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Let's color!")

canvas_img_list = os.listdir("canvas_img")
canvas_img = os.path.join("canvas_img",str(random.choice(canvas_img_list)))
canvas = Canvas(canvas_img)
palette_colors = [WHITE,BLACK,RED,PINK,PURPLE,DEEP_PURPLE,DEEP_BLUE,BLUE,LIGHT_BLUE,CYAN,TEAL,GREEN,LIGHT_GREEN,LIME,YELLOW,AMBER,ORANGE,DEEP_ORANGE]

palette = Palette(5, canvas.bg_image.get_height() + 5, palette_colors)
brush_size_selector = IntSelector(5, 50, 10, 5, canvas.bg_image.get_height() + palette.button_height+20)
capture_button = Button(SCREEN_WIDTH-60, SCREEN_HEIGHT-50, 50, 30, BLUE, capture)

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
    capture_button.draw_button_with_text(screen, "Save")
    canvas.draw(screen)

    pygame.display.update()
    capture_button.handle_event(event)
    
pygame.quit()
sys.exit()
          