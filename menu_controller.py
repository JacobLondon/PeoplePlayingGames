import pygame

from pyngine.constants import Color, Font, Anchor
from pyngine.label import Label
from pyngine.button import Button
from pyngine.layout import Grid
from pyngine.controller import Controller

from config import settings

class Menu_Controller(Controller):

    def __init__(self, interface):
        Controller.__init__(self, interface)

    def initialize_components(self):

        self.title_layout = Grid(self.background_panel, 4, 4)

        self.title_label = Label(self.interface, 'Press enter to play')
        self.title_label.loc = self.title_layout.get_pixel(3, 3)
        self.title_label.anchor = Anchor.center
        self.title_label.font = Font.menu

        self.start_button = Button(self.interface, 'Click to play')
        self.start_button.loc = self.title_layout.get_pixel(3, 4)
        self.start_button.anchor = Anchor.center

    def load_components(self):
        self.title_label.load()
        self.start_button.load()

    def update_components(self):
        self.title_label.refresh()
        self.start_button.refresh()

    def open_on_close(self):
        from game_controller import Game_Controller
        return Game_Controller(self.interface)

    def return_keydown(self):
        self.start_button_clicked()

    def l_click_down(self):
        if self.start_button.focused:
            self.start_button_clicked()

    def start_button_clicked(self):
        self.done = True
