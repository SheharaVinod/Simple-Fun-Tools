from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string("""
<LeftNavigator>
    canvas.before:
        Color:
            rgb:(0.4,0.4,0.4,1)
        Line:
            width:1
            rectangle:[self.x,self.y,self.x+self.width,self.y+self.height]
                
    orientation:"vertical"
    size_hint_x:None
    width:"200dp"
    #md_bg_color:[1,1,0,0.8]
    AnchorLayout:
        size_hint_y:None
        size:self.width,self.width
        MDBoxLayout:
            size_hint:None,None
            width:170
            size:self.width,self.width
            canvas.before:
                Color:
                    rgba:(1,1,1,1)
                Ellipse:
                    size:self.size
                    pos:self.pos
                    source:"asset/image/logo.jpg"
                
                Color:
                    rgb:(0.4,0.4,0.4,1)
                Line:
                    width:1.2
                    ellipse:(self.x, self.y,self.width,self.width)
    AnchorLayout:
        size_hint:1,None
        height:40
        MDLabel:
            text:"Simple Fun Tools"
            halign:"center"
            font_size:"18sp"
            bold:True
    MDBoxLayout:


""")

class LeftNavigator(MDBoxLayout):
    pass
