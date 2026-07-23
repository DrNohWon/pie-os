"""
P.I.E. Label Widget
"""

from pie_ui.widgets.widget import Widget


class Label(Widget):


    def __init__(
        self,
        x,
        y,
        text,
        font
    ):

        super().__init__(
            x,
            y,
            0,
            0
        )

        self.text = text
        self.font = font



    def draw(self, renderer):

        renderer.text(
            self.text,
            (self.x,self.y),
            self.font,
            (255,255,255)
        )
