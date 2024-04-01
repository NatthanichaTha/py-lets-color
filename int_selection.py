import pygame
from constant import *
from button import Button

class IntSelector:
    def __init__(self, min, max, default, x, y):
        self.min = min
        self.max = max
        self.current_value = default
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15
        self.margin = 50
        self.increase_button = Button(self.x, self.y, self.width, self.height,GREEN,self.increase)
        self.decrease_button = Button(self.x+self.margin, self.y, self.width, self.height,RED,self.decrease)
        self.font = pygame.font.Font('sans.ttf', 15)

    # def draw(self, surface):
    #     self.increase_button.draw(surface)
    #     self.decrease_button.draw(surface)
    #     self.show_current_value(surface)
    
    def show_current_value(self, surface):
        text = str(self.current_value)
        text = self.font.render(text, True, WHITE, BLACK)
        textRect = text.get_rect()
        textRect.center = (self.x + (self.margin/3)*2 , self.y + self.height/2 )
        surface.blit(text, textRect)

    def draw(self, surface):
        self.increase_button.draw_button_with_text(surface, "+")
        self.decrease_button.draw_button_with_text(surface, "-")
        self.show_current_value(surface)
    
    def increase(self):
        self.current_value += 1
    
    def decrease(self):
        self.current_value -= 1
    
    def handle_event(self, event):
        self.increase_button.handle_event(event)
        self.decrease_button.handle_event(event)
    

        