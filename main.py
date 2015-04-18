import pygame 
import constants as c
from models import enemy_test
from math import sqrt, pow

class View:
    """
    Window view which contains the gui and game screen
    """
    def __init__(self, model, screen):
        # self.modelList = model
        # print self.modelList
        self.model = model
        self.screen = screen

    def start_screen(self):
        pic = pygame.image.load("map.png").convert()


    def update(self):
        pic = pygame.image.load("map.png").convert()
        self.screen.blit(pic, (0, 0))

        for enemy in self.model.enemyList:

            if (not enemy.death):
                pygame.draw.circle(self.screen, enemy.color,
                    enemy.pos, enemy.radius,
                    enemy.width)
                pygame.draw.line(self.screen, (255, 0, 0), [enemy.pos[0] - 10, enemy.pos[1] - 15],
                    [enemy.pos[0] - 10 + enemy.health / 3, enemy.pos[1] - 15], 4)
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
        self.enemyList = [enemy_test(color_list['blue'], [10, 240], [10, 240], 10, 0, False, 10, 50, False),
                            enemy_test(color_list['red'], [240,15], [15,240], 10, 0, False, 30, 50, False),
                           enemy_test(color_list['green'], [350,500], [350,500], 10, 0, False, 5, 50, False)]
        # self.enemy_test = [enemy_test(color_list['blue'], [10, 240], [10, 240], 10, 0, False, 10, 50, False),
        #                     enemy_test(color_list['red'], [240,10], [10,240], 10, 0, False, 10, 50, False),
        #                    enemy_test(color_list['green'], [350,500], [350,500], 10, 0, False, 5, 50, False)]

        # self.enemy_test = enemy_test(color_list['blue'], [10, 240], [10, 240], 10, 0, False, 10, 50, False)
        # self.enemyList.append(self.enemy_test)


    def update(self):
        for enemy in self.enemyList:
            if (enemy.moving == True):
                enemy.pos[0] = enemy.speed * (pygame.time.get_ticks() / 1000) + enemy.start_pos[0]

            if (enemy.health <= 0):
                enemy.death = True

        # if (self.enemy_test.moving == True):
        #     self.enemy_test.pos[0] = self.enemy_test.speed * (pygame.time.get_ticks() / 1000) + self.enemy_test.start_pos[0]
        #
        # if (self.enemy_test.health <= 0):
        #     self.enemy_test.death = True


class Controller:
    """
    Create a controller to control all the event 
    """
    def __init__(self, model):
        self.model = model
        self.last_click_time = 0

    def start(self):
        for enemy in self.model.enemyList:
            enemy.moving = True

    def update(self):
        if (pygame.mouse.get_pressed() == (1, 0, 0) and pygame.time.get_ticks() - self.last_click_time > 100):
            self.last_click_time = pygame.time.get_ticks()
            p = pygame.mouse.get_pos(0)
            x = p[0] 
            y = p[1]
            flag = True
            for enemy in self.model.enemyList:
                if (sqrt(pow((x - enemy.pos[0]), 2) + pow((y - enemy.pos[1]), 2))
                    <= enemy.radius
                    and flag):
                    enemy.health -= 10
                    print enemy.health
                    flag = False

def main():
    # initialize the pygame environment
    pygame.init()

    # config the screen
    screen_size = (c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
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