from kivy.config import Config
Config.set("graphics","minimum_height","400")
Config.set("graphics","height","500")
Config.set("graphics","minimum_width","700")
Config.set("graphics","width","900")
Config.set("input","mouse","mouse,disable_multitouch")
from kivymd.app import MDApp


class SimpleFunTool(MDApp):
    def __init__(self, **kwargs):
        super(SimpleFunTool, self).__init__(**kwargs)

    def build(self):
        return


if __name__ == '__main__':
    window = SimpleFunTool()
    window.run()
