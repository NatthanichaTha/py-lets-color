import pygame
from button import Button
from constant import *


class Palette:
    def __init__(self, x , y, color_list):
        self.x = x
        self.y = y
        self.button_width = 30
        self.button_height = 30
        self.button_margin = 5
        self.color_list = color_list
        self.button_list = []
        self.current_color = self.color_list[0]
        color_x = self.x
        for color in color_list:
            self.button_list.append(Button(color_x, self.y, self.button_width, self.button_height, color, lambda color=color: self.set_color(color))) 
            color_x += self.button_width + self.button_margin

    def set_color(self, color):
        self.current_color = color

    def handle_event(self, event):
        for btn in self.button_list:
            btn.handle_event(event)

    def draw(self, screen):
        for btn in self.button_list:
            btn.draw(screen)
    
    # def color_selection(self, mouse_x, mouse_y):
    #     color_x = self.x
    #     color_y = self.y
    #     for color in self.color_list:
    #         color_button = pygame.Rect(color_x, color_y, self.button_width, self.button_height)
    #         if color_button.collidepoint(mouse_x, mouse_y):
    #             self.current_color = color
    #             return True 
    #         color_x += self.button_width + self.button_margin
    #     return False
