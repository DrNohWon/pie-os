"""
P.I.E. Base Widget

Parent class for all UI elements.
"""


class Widget:


    def __init__(
        self,
        x,
        y,
        width,
        height
    ):

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.visible = True



    def contains(self, x, y):

        return (
            self.x <= x <= self.x + self.width
            and
            self.y <= y <= self.y + self.height
        )



    def draw(self, renderer):

        pass



    def touch(self, event):

        pass
