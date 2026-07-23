"""
P.I.E. Button Widget

Compatible with HomeScreen:
Button(x,y,w,h,text,font,callback)
"""

import pygame



class Button:


    def __init__(
        self,
        x,
        y,
        width,
        height,
        text,
        font,
        callback
    ):

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.text = text

        self.font = font

        self.callback = callback


        self.color = (
            70,
            70,
            70
        )

        self.text_color = (
            255,
            255,
            255
        )



    def contains(
        self,
        x,
        y
    ):

        return (

            self.x <= x <= self.x + self.width

            and

            self.y <= y <= self.y + self.height

        )



    def touch(
        self,
        event
    ):


        #
        # ADS7846 release event
        # has correct coordinates
        #

        if event["pressed"] == 0:


            if self.contains(
                event["x"],
                event["y"]
            ):

                print(
                    self.text,
                    "pressed"
                )


                self.callback()



    def draw(
        self,
        renderer
    ):


        renderer.rectangle(

            (
                self.x,
                self.y,
                self.width,
                self.height
            ),

            self.color

        )


        renderer.text(

            self.text,

            (
                self.x + 20,
                self.y + 10
            ),

            self.font,

            self.text_color

        )
