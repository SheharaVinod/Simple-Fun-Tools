from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string("""
<ScreenWindowContainer>
    orientation:"vertical"
    
    MDBoxLayout:
        size_hint_y:None
        height:"80dp"
        md_bg_color:[1,0,0,0.2]
        
        
    MDScreenManager:

""")

class ScreenWindowContainer(MDBoxLayout):
    pass
