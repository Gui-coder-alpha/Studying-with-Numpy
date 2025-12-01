from manim import *

class CreateCircle(Scene):
    def construction(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.7)
        self.play(Create(circle))