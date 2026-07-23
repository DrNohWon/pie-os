"""
P.I.E. Screen Manager
"""


from pie_core.input import TouchInput



class ScreenManager:


    def __init__(self):

        self.current = None
        self.touch = TouchInput()



    def set_screen(
        self,
        screen
    ):

        self.current = screen



    def handle_events(
        self
    ):


        if self.current is None:

            return



        event = self.touch.read()


        if event:

            print(
                "TOUCH EVENT:",
                event
            )


            self.current.touch(
                event
            )



    def draw(self):


        if self.current:

            self.current.draw()
