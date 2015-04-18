import pygame 
from models import enemy_test
from math import sqrt, pow

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

        if (not self.model.enemy_test.death):
            pygame.draw.circle(self.screen, self.model.enemy_test.color, 
                self.model.enemy_test.pos, self.model.enemy_test.radius, 
                self.model.enemy_test.width)
            pygame.draw.line(self.screen, (255, 0, 0), [self.model.enemy_test.pos[0] - 10, self.model.enemy_test.pos[1] - 15], 
                [self.model.enemy_test.pos[0] - 10 + self.model.enemy_test.health / 3, self.model.enemy_test.pos[1] - 15], 4)
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
        self.enemy_test = enemy_test(color_list['blue'], [10, 240], [10, 240], 10, 0, False, 10, 50, False)

    def update(self):
        if (self.enemy_test.moving == True):
            self.enemy_test.pos[0] = self.enemy_test.speed * (pygame.time.get_ticks() / 1000) + self.enemy_test.start_pos[0]

        if (self.enemy_test.health <= 0):
            self.enemy_test.death = True


class Controller:
    """
    Create a controller to control all the event 
    """
    def __init__(self, model):
        self.model = model
        self.last_click_time = 0

    def start(self):
        self.model.enemy_test.moving = True

    def update(self):
        if (pygame.mouse.get_pressed() == (1, 0, 0) and pygame.time.get_ticks() - self.last_click_time > 100):
            self.last_click_time = pygame.time.get_ticks()
            p = pygame.mouse.get_pos(0)
            x = p[0] 
            y = p[1]
            flag = True
            if (sqrt(pow((x - self.model.enemy_test.pos[0]), 2) + pow((y - self.model.enemy_test.pos[1]), 2)) 
                <= self.model.enemy_test.radius
                and flag):
                self.model.enemy_test.health -= 10
                print self.model.enemy_test.health
                flag = False

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
        controller.update()

if __name__ == "__main__":
    main()