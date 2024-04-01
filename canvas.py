import pygame
from constant import SCREEN_HEIGHT, SCREEN_WIDTH

class Canvas:
    def __init__(self, image_path: str):
        self.bg_image = pygame.image.load(image_path).convert()
        scale_factor = min(SCREEN_WIDTH / self.bg_image.get_width(), SCREEN_HEIGHT / self.bg_image.get_height())
        self.bg_image = pygame.transform.scale(self.bg_image, (int(self.bg_image.get_width() * scale_factor), int(self.bg_image.get_height() * scale_factor)))

        self.painting_surface = pygame.Surface((self.bg_image.get_width(), self.bg_image.get_height()), pygame.SRCALPHA)
        self.painting_surface_collider = pygame.Rect(0, 0, self.bg_image.get_width(), self.bg_image.get_height())
        self.mouse_surface = pygame.Surface((self.bg_image.get_width(), self.bg_image.get_height()), pygame.SRCALPHA)

        self.painting = False
        self.erasing = False

    def paint_color(self, color, size, x, y):
        pygame.draw.circle(self.painting_surface, color, [x, y], size)

    def erase_color(self, size, x, y):
        opacity = 0
        color = [0, 0, 0, opacity]
        pygame.draw.circle(self.painting_surface, color, [x, y], size)

    def mouse(self, mouse_position, brush_size, color):
        self.mouse_surface.fill(pygame.SRCALPHA)
        pygame.draw.circle(self.mouse_surface, color, mouse_position, brush_size)
    
    def _handle_action(self, color, size, x, y):
        if self.painting:
            opacity = 128
            self.paint_color(color+(opacity,), size, x, y)
        elif self.erasing:
            self.erase_color(size, x, y)

    def handle_event(self, event, color, size):
        x, y = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.painting = True
            elif event.button == 3:
                self.erasing = True

            if self.painting_surface_collider.collidepoint(x, y):
                self._handle_action(color, size, x, y)
            
        elif event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            self.mouse(mouse_position, size, color+(200,))

            if self.painting_surface_collider.collidepoint(x, y):
                self._handle_action(color, size, x, y)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.painting = False
            self.erasing = False
    
    def draw(self, surface):
        surface.blit(self.bg_image, (0,0))
        surface.blit(self.painting_surface, (0,0))
        surface.blit(self.mouse_surface, (0,0))