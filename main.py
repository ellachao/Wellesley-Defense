import pygame 

class View:
    """
    Window view which contains the gui and game screen
    """
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def start_screen(self):
        black = (0, 0, 0)
        header = pygame.font.SysFont("timesnewroman", 50)
        starter = pygame.font.SysFont("timesnewroman", 50)
        title = header.render("Bubble Pop!", True, black)
        play = header.render("Play", True, black)
        pic = pygame.image.load("map.png").convert()
        self.screen.blit(pic, (0, 0))
        self.screen.blit(title, (200, 70))
        self.screen.blit(play, (200, 100))
        pygame.display.update()

    def update(self):
        pygame.display.update()

class Model:
    """
    Create a model for our bubble pop game
    """
    def __init__(self):
        self.nothing = []

class Controller:
    """
    Create a controller to control all the event 
    """
    def __init__(self, model):
        self.model = model

def main():
    # initialize the pygame environment
    pygame.init()

    # config the screen
    screen_size = (226, 160)
    screen = pygame.display.set_mode(screen_size)
    white = (255, 255, 255)
    screen.fill(white)

    # Initialize MVC
    model = Model()
    view = View(model, screen)
    controller = Controller(model)

    view.start_screen()
    
    pygame.display.set_caption("Wellesley Defense!")
    running = 1

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        view.update

if __name__ == "__main__":
    main()