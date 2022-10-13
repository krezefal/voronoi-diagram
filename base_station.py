from random import randint


class BaseStation:
    def __init__(self, red=None, green=None, blue=None, /, *, x, y, rand_color):
        self.x = x
        self.y = y

        self.color = ()

        if rand_color is not False:
            self.color += (randint(0, 255), )
            self.color += (randint(0, 255), )
            self.color += (randint(0, 255), )
        else:
            self.color += red
            self.color += green
            self.color += blue
