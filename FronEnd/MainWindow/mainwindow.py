from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder

Builder.load_string("""
<MainWindow>
    LeftNavigator:
        id:left_navigator
                    
    ScreenWindowContainer:
        id:window_container
""")
class MainWindow(MDBoxLayout):
    pass
