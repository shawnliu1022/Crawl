import pygame
class Camera(object):
    def __init__(self, func, width, height):
        self.function = func
        self.width = width
        self.height = height
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.function(self.state, target.rect)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect # l = left,  t = top
    _, _, w, h = camera      # w = width, h = height
    return pygame.Rect(-l+400, -t+250, w, h)
    
def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+400, -t+250, w, h # center player

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-800), l)   # stop scrolling at the right edge
    t = max(-(camera.height-500), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top

    return pygame.Rect(l, t, w, h)