import pygame 
from models import enemy_test

class View:
    """
    Window view which contains the gui and game screen
    """
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def start_screen(self):
        pic = pygame.image.load("map.png").convert()


    def update(self):
        pic = pygame.image.load("map.png").convert()
        self.screen.blit(pic, (0, 0))
        pygame.draw.circle(self.screen, self.model.enemy_test.color, 
            self.model.enemy_test.pos, self.model.enemy_test.radius, 
            self.model.enemy_test.width)
        pygame.display.update()

class Model:
    """
    Create a model for our bubble pop game
    """
    def __init__(self):
        color_list = {
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255)
        }
        self.enemy_test = enemy_test(color_list['blue'], [10, 240], [10, 240], 10, 0, False, 5, 50)

    def update(self):
        if (self.enemy_test.moving == True):
            self.enemy_test.pos[0] = self.enemy_test.speed * (pygame.time.get_ticks() / 1000) + self.enemy_test.start_pos[0]



class Controller:
    """
    Create a controller to control all the event 
    """
    def __init__(self, model):
        self.model = model

    def start(self):
        self.model.enemy_test.moving = True

def main():
    # initialize the pygame environment
    pygame.init()

    # config the screen
    screen_size = (723, 483)
    screen = pygame.display.set_mode(screen_size)
    white = (255, 255, 255)
    screen.fill(white)

    # Initialize MVC
    model = Model()
    view = View(model, screen)
    controller = Controller(model)

    view.start_screen()

    running = 1

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        view.update()
        controller.start()
        model.update()

if __name__ == "__main__":
    main()