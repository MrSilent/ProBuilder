import kivy

from builder import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

USERNAME = 'xmrsilentx'
IDENTITY_TOKEN ='c3d63b61bb424d7fa62de0cb9523ec6f'
    

Builder.load_string("""

#:set block_list ['Empty', 'Grass', 'Sand', 'Stone', 'Brick', 'Wood', 'Cement', 'Dirt', 'Plank', 'Snow', 'Glass', 'Cobble', 'Light Stone', 'Dark Stone', 'Chest', 'Leaves', 'Tall Grass']
<Test>:
    do_default_tab: False

    TabbedPanelItem:
        text: sp1.text
        BoxLayout:
            orientation: 'vertical'
            spacing: 5
            GridLayout:
                cols: 2
                TextInput:
                    id: tix1
                    size_hint_x: None
                    size_hint_y: .6 
                    width: 200
                    multiline: False
                    text: str(sx1.value)
                Slider:
                    id: sx1
                    size_hint_x: None
                    size_hint_y: .6
                    width: 1720
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                TextInput:
                    id: tix2
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sx2.value)
                Slider:
                    id: sx2
                    size_hint_y: .6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                TextInput:
                    id: tiy1
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sy1.value)
                Slider:
                    id: sy1
                    size_hint_y: .6
                    min: 0
                    max: 255
                    step: 1
                    value: 127
                TextInput:
                    id: tiy2
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sy2.value)
                Slider:
                    id: sy2
                    size_hint_y: .6
                    min: 0
                    max: 255
                    step: 1
                    value: 127
                TextInput:
                    id: tiz1
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sz1.value)
                Slider:
                    id: sz1
                    size_hint_y: .6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                TextInput:
                    id: tiz2
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sz2.value)
                Slider:
                    id: sz2
                    size_hint_y: .6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                TextInput:
                    id: tirad
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(srad.value)
                Slider:
                    id: srad
                    size_hint_y: .6
                    min: 0
                    max: 255
                    step: 1
                    value: 127
                GridLayout:
                    cols: 2
                    row_default_height: .4
                    padding: 5
                    spacing: 5
                    Label:
                        text: 'Fill=%s' % fill.active
                        size_hint: 1, .4
                    Switch:
                        id: fill
                        size_hint: 1, .4
                GridLayout:
                    cols: 2
                    row_default_height: .4
                    padding: 5
                    spacing: 5
                    TextInput:
                        id: hst1
                        text: 'michaelfogleman.com'
                        multiline: False
                        size_hint: 1, .4
                    TextInput:
                        id: prt1
                        text: '4080'
                        multiline: False
                        size_hint: 1, 4
            BoxLayout:
                orientation: 'vertical'
                padding: 5
                spacing: 5
                Spinner:
                    id: sp1
                    text: 'Sphere'
                    size_hint: 1, .4
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', 'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', 'Circle Z', 'Cone Y'
                Spinner:
                    id: sp2
                    text: 'Empty'
                    size_hint: 1, .4
                    values: block_list
                Button:
                    id: cmd
                    text: 'Build It!'
                    size_hint_y: .4
                    on_press: root.cmd(sx1.value, sx2.value, sy1.value, sy2.value, sz1.value, sz2.value, srad.value, sp1.text, sp2.text, fill.active, hst1.text, prt1.text)
    TabbedPanelItem:
        text: sp2.text
        BoxLayout:
            orientation: 'vertical'
            spacing: 5
            GridLayout:
                cols: 2
                TextInput:
                    id: tix3
                    size_hint_x: None
                    size_hint_y: .6 
                    width: 200
                    multiline: False
                    text: str(sx3.value)
                Slider:
                    id: sx3
                    size_hint_x: None
                    size_hint_y: .6
                    width: 1720
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                TextInput:
                    id: tix4
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sx4.value)
                Slider:
                    id: sx4
                    size_hint_y: .6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                TextInput:
                    id: tiy3
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sy3.value)
                Slider:
                    id: sy3
                    size_hint_y: .6
                    min: 0
                    max: 255
                    step: 1
                    value: 127
                TextInput:
                    id: tiy4
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sy4.value)
                Slider:
                    id: sy4
                    size_hint_y: .6
                    min: 0
                    max: 255
                    step: 1
                    value: 127
                TextInput:
                    id: tiz3
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sz3.value)
                Slider:
                    id: sz3
                    size_hint_y: .6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                TextInput:
                    id: tiz4
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sz4.value)
                Slider:
                    id: sz4
                    size_hint_y: .6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                TextInput:
                    id: tirad1
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(srad1.value)
                Slider:
                    id: srad1
                    size_hint_y: .6
                    min: 0
                    max: 255
                    step: 1
                    value: 127
                GridLayout:
                    cols: 2
                    row_default_height: .4
                    padding: 5
                    spacing: 5
                    Label:
                        text: 'Fill=%s' % fill1.active
                        size_hint: 1, .4
                    Switch:
                        id: fill1
                        size_hint: 1, .4
                GridLayout:
                    cols: 2
                    row_default_height: .4
                    padding: 5
                    spacing: 5
                    TextInput:
                        id: hst2
                        text: 'michaelfogleman.com'
                        multiline: False
                        size_hint: 1, .4
                    TextInput:
                        id: prt2
                        text: '4080'
                        multiline: False
                        size_hint: 1, 4
            BoxLayout:
                orientation: 'vertical'
                padding: 5
                spacing: 5
                Spinner:
                    id: sp3
                    text: 'Pyramid'
                    size_hint: 1, .4
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', 'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', 'Circle Z', 'Cone Y'
                Spinner:
                    id: sp4
                    text: 'Empty'
                    size_hint: 1, .4
                    values: block_list
                Button:
                    id: cmd2
                    text: 'Build It!'
                    size_hint_y: .4
                    on_press: cmd(sx3.value, sx4.value, sy3.value, sy4.value, sz3.value, sz4.value, srad1.value, sp3.text, sp4.text, fill1.active, hst2.text, prt2.text)
    TabbedPanelItem:
        text: sp3.text
        BoxLayout:
            orientation: 'vertical'
            spacing: 5
            GridLayout:
                cols: 2
                TextInput:
                    id: tix5
                    size_hint_x: None
                    size_hint_y: .6 
                    width: 200
                    multiline: False
                    text: str(sx5.value)
                Slider:
                    id: sx5
                    size_hint_x: None
                    size_hint_y: .6
                    width: 1720
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                TextInput:
                    id: tix6
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sx6.value)
                Slider:
                    id: sx6
                    size_hint_y: .6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                TextInput:
                    id: tiy5
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sy5.value)
                Slider:
                    id: sy5
                    size_hint_y: .6
                    min: 0
                    max: 255
                    step: 1
                    value: 127
                TextInput:
                    id: tiy6
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sy6.value)
                Slider:
                    id: sy6
                    size_hint_y: .6
                    min: 0
                    max: 255
                    step: 1
                    value: 127
                TextInput:
                    id: tiz5
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sz5.value)
                Slider:
                    id: sz5
                    size_hint_y: .6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                TextInput:
                    id: tiz6
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(sz6.value)
                Slider:
                    id: sz6
                    size_hint_y: .6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                TextInput:
                    id: tirad2
                    size_hint_x: None
                    size_hint_y: .6
                    multiline: False
                    text: str(srad2.value)
                Slider:
                    id: srad2
                    size_hint_y: .6
                    min: 0
                    max: 255
                    step: 1
                    value: 127
                GridLayout:
                    cols: 2
                    row_default_height: .4
                    padding: 5
                    spacing: 5
                    Label:
                        text: 'Fill=%s' % fill2.active
                        size_hint: 1, .4
                    Switch:
                        id: fill2
                        size_hint: 1, .4
                GridLayout:
                    cols: 2
                    row_default_height: .4
                    padding: 5
                    spacing: 5
                    TextInput:
                        id: hst3
                        text: '127.0.0.1'
                        multiline: False
                        size_hint: 1, .4
                    TextInput:
                        id: prt3
                        text: '4080'
                        multiline: False
                        size_hint: 1, 4
            BoxLayout:
                orientation: 'vertical'
                padding: 5
                spacing: 5
                Spinner:
                    id: sp5
                    text: 'Cylinder Y'
                    size_hint: 1, .4
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', 'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', 'Circle Z', 'Cone Y'
                Spinner:
                    id: sp6
                    text: 'Empty'
                    size_hint: 1, .4
                    values: block_list
                Button:
                    id: cmd2
                    text: 'Build It!'
                    size_hint_y: .4
                    on_press: cmd(sx5.value, sx6.value, sy5.value, sy6.value, sz5.value, sz6.value, srad2.value, sp5.text, sp6.text, fill2.active, hst3.text, prt3.text)

""")

class Test(TabbedPanel):

    def cmd(unknown, tix1, tix2, tiy1, tiy2, tiz1, tiz2, tirad, sp1, sp2, fil, hst1, prt1):
        client = Client(hst1, int(prt1), USERNAME, IDENTITY_TOKEN)
        x = 0
        if sp2 == 'Empty':
            x = 0
        if sp2 == 'Grass':
            x = 1
        if sp2 == 'Sand':
            x = 2
        if sp2 == 'Stone':
            x = 3
        if sp2 == 'Brick':
            x = 4
        if sp2 == 'Wood':
            x = 5
        if sp2 == 'Cement':
            x = 6
        if sp2 == 'Dirt':
            x = 7
        if sp2 == 'Plank':
            x = 8
        if sp2 == 'Snow':
            x = 9
        if sp2 == 'Glass':
            x = 10
        if sp2 == 'Cobble':
            x = 11
        if sp2 == 'Light':
            x = 12
        if sp2 == 'Dark':
            x = 13
        if sp2 == 'Chest':
            x  = 14
        if sp2 == 'Leaves':
            x = 15
        if sp2 == 'Tall Grass':
            x = 17
        print tix1
        print tix2
        print tiy1
        print tiy2
        print tiz1
        print tiz2
        print tirad
        print x
        print sp2
        print fil
        print hst1
        print int(prt1)
        

        if sp1 == 'Up Pyramid':
            client.set_blocks(pyramid(int(tix1), int(tix2), int(tiy1), int(tiz1), int(tiz2), fil), int(x))
        if sp1 == 'Down Pyramid':
            client.set_blocks(upyramid(int(tix1), int(tix2), int(tiy1), int(tiz1), int(tiz2), fil), int(x))
        if sp1 == 'Sphere':
            client.set_blocks(sphere(int(tix1), int(tiy1), int(tiz1), int(tirad), fill=fil), x)
        if sp1 == 'Circle X':
            client.set_blocks(circle_x(int(tix1), int(tiy1), int(tiz1), int(tirad), fil), int(x))
        if sp1 == 'Circle Y':
            client.set_blocks(circle_y(int(tix1), int(tiy1), int(tiz1), int(tirad), fil), int(x))
        if sp1 == 'Circle Z':
            client.set_blocks(circle_z(int(tix1), int(tiy1), int(tiz1), int(tirad), fil), int(x))
        if sp1 == 'Cuboid':
            client.set_blocks(cuboid(int(tix1), int(tix2), int(tiy1), int(tiy2), int(tiz1), int(tiz2), fil), int(x))
        if sp1 == 'Cylinder X':
            client.set_blocks(cylinder_x(int(tix1), int(tix2), int(tiy1), int(tiz1), int(tirad), fil), int(x))
        if sp1 == 'Cylinder Y':
            client.set_blocks(cylinder_y(int(tix1), int(tiy1), int(tiy2), int(tiz1), int(tirad), fil), int(x))
        if sp1 == 'Cylinder Z':
            client.set_blocks(cylinder_z(int(tix1), int(tiy1), int(tiz1), int(tiz2), int(tirad), fil), int(x))
        if sp1 == 'Cone Y':
            client.set_blocks(cone_y(int(tix1), int(tiy1), int(tiy2), int(tiz1), int(tirad), fil), int(x))

class TabbedPanelApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    TabbedPanelApp().run()
