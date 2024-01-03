from kivy.config import Config
Config.set("graphics","minimum_height","650")
Config.set("graphics","minimum_width","900")
Config.set("input","mouse","mouse,disable_multitouch")
from kivymd.app import MDApp
from FronEnd import *

class SimpleFunTool(MDApp):
    def __init__(self, **kwargs):
        super(SimpleFunTool, self).__init__(**kwargs)

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    window = SimpleFunTool()
    window.run()
