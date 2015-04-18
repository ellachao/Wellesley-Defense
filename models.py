class enemy_test:
    def __init__(self, color, pixel_pos, index_pos, radius, width, moving, speed, health, death):
        self.color = color
        self.pixel_pos = pixel_pos
        self.prev_pos = index_pos
        self.cur_pos = index_pos
        self.radius = radius
        self.width = width
        self.speed = speed
        self.health = health
        self.death = death