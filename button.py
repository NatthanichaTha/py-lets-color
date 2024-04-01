import pygame
from constant import *

class Button:
    def __init__(self, x:int, y:int, width:int, height:int, bg_color, callback):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.callback = callback
        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.Font('sans.ttf', 20)
        
    def draw_outer_line(self, screen, x, y):
        pygame.draw.rect(screen, WHITE, (x - 2, y - 2, self.width + 4, self.height + 4), 2)
    
    def draw(self, surface):
        self.draw_outer_line(surface, self.x, self.y)
        pygame.draw.rect(surface, self.bg_color, (self.x, self.y, self.width, self.height))
    
    def draw_button_with_text(self, surface, button_text):
        self.draw_outer_line(surface, self.x, self.y)
        pygame.draw.rect(surface, self.bg_color, (self.x, self.y, self.width, self.height))
        text = self.font.render(button_text, True, BLACK, None)
        textRect = text.get_rect()
        textRect.center = (self.x + self.width/2, self.y + self.height/2 )
        surface.blit(text, textRect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.collider.collidepoint(mouse_x, mouse_y):
                self.callback()
