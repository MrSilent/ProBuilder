import kivy
kivy.require('1.7.2')
import time

from builder import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

USERNAME = ''
IDENTITY_TOKEN =''

block_list = ['Empty', 'Grass', 'Sand', 'Stone', 'Brick', 'Wood', 'Cement',
              'Dirt', 'Plank', 'Snow', 'Glass', 'Cobble', 'Light Stone',
              'Dark Stone', 'Chest', 'Leaves', 'Tall Grass']    

Builder.load_string("""

#:set block_list ['Empty', 'Grass', 'Sand', 'Stone', 'Brick', 'Wood', \
                'Cement', 'Dirt', 'Plank', 'Snow', 'Glass', 'Cobble', 'Light Stone', \
                'Dark Stone', 'Chest', 'Leaves', 'Tall Grass']

<Test>:
    do_default_tab: False

    TabbedPanelItem:
        text: sp1.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .4
                TextInput:
                    id: tix1
                    multiline: False
                    size_hint_x: .4
                    text: str(sx1.value)
                    on_text: root.int_set(self, sx1)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx1)
                    Button:
                        text:'>'
                        size_hint_x: .1
                        on_press: root.pls(sx1)
                Slider:
                    id: sx1
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/X2'
                    size_hint_x: .4
                TextInput:
                    id: tix4
                    size_hint_x: .4
                    multiline: False
                    text: str(sx2.value)
                    on_text: root.int_set(self, sx2)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx2)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sx2)
                Slider:
                    id: sx2
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .4
                TextInput:
                    id: tiy1
                    size_hint_x: .4
                    multiline: False
                    text: str(sy1.value)
                    on_text: root.int_set(self, sy1)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy1)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy1)
                Slider:
                    id: sy1
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Y2'
                    size_hint_x: .4
                TextInput:
                    id: tiy2
                    size_hint_x: .4
                    multiline: False
                    text: str(sy2.value)
                    on_text: root.int_set(self, sy2)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy2)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy2)
                Slider:
                    id: sy2
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .4
                TextInput:
                    id: tiz1
                    size_hint_x: .4
                    multiline: False
                    text: str(sz1.value)
                    on_text: root.int_set(self, sz1)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz1)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root. pls(sz1)
                Slider:
                    id: sz1
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Z2'
                    size_hint_x: .4
                TextInput:
                    id: tiz2
                    size_hint_x: .4
                    multiline: False
                    text: str(sz2.value)
                    on_text: root.int_set(self, sz2)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz2)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sz2)
                Slider:
                    id: sz2
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Radius'
                    size_hint_x: .4
                TextInput:
                    id: tirad
                    size_hint_x: .4
                    multiline: False
                    text: str(srad.value)
                    on_text: root.int_set(self, srad)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(srad)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(srad)
                Slider:
                    id: srad
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Fill=%s' % fill.active
                Switch:
                    id: fill
                TextInput:
                    id: hst1
                    text: '127.0.0.1'
                    multiline: False
                TextInput:
                    id: prt1
                    text: '4080'
                    multiline: False
            GridLayout:
                cols: 2
                Spinner:
                    id: sp1
                    text: 'Sphere'
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                    'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', \
                    'Circle Z', 'Cone Y'
                Spinner:
                    id: sp2
                    text: 'Empty'
                    values: block_list
            BoxLayout:
                orientation: 'vertical'
                Button:
                    id: cmd
                    text: 'Build It!'
                    on_press: root.cmd(tix1.text, tix2.text, tiy1.text, \
                    tiy2.text, tiz1.text, tiz2.text, tirad.text, sp1.text, \
                    sp2.text, fill.active, hst1.text, prt1.text)
    TabbedPanelItem:
        text: sp3.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .4
                TextInput:
                    id: tix3
                    multiline: False
                    size_hint_x: .4
                    text: str(sx3.value)
                    on_text: root.int_set(self, sx3)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx3)
                    Button:
                        text:'>'
                        size_hint_x: .1
                        on_press: root.pls(sx3)
                Slider:
                    id: sx3
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/X2'
                    size_hint_x: .4
                TextInput:
                    id: tix4
                    size_hint_x: .4
                    multiline: False
                    text: str(sx4.value)
                    on_text: root.int_set(self, sx4)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx4)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sx4)
                Slider:
                    id: sx4
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .4
                TextInput:
                    id: tiy3
                    size_hint_x: .4
                    multiline: False
                    text: str(sy3.value)
                    on_text: root.int_set(self, sy3)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy3)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy3)
                Slider:
                    id: sy3
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Y2'
                    size_hint_x: .4
                TextInput:
                    id: tiy4
                    size_hint_x: .4
                    multiline: False
                    text: str(sy4.value)
                    on_text: root.int_set(self, sy4)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy4)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy4)
                Slider:
                    id: sy4
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .4
                TextInput:
                    id: tiz3
                    size_hint_x: .4
                    multiline: False
                    text: str(sz3.value)
                    on_text: root.int_set(self, sz3)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz3)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root. pls(sz3)
                Slider:
                    id: sz3
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Z2'
                    size_hint_x: .4
                TextInput:
                    id: tiz4
                    size_hint_x: .4
                    multiline: False
                    text: str(sz4.value)
                    on_text: root.int_set(self, sz4)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz4)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sz4)
                Slider:
                    id: sz4
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Radius'
                    size_hint_x: .4
                TextInput:
                    id: tirad2
                    size_hint_x: .4
                    multiline: False
                    text: str(srad2.value)
                    on_text: root.int_set(self, srad2)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(srad2)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(srad2)
                Slider:
                    id: srad2
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Fill=%s' % fill2.active
                Switch:
                    id: fill2
                TextInput:
                    id: hst2
                    text: '127.0.0.1'
                    multiline: False
                TextInput:
                    id: prt2
                    text: '4080'
                    multiline: False
            GridLayout:
                cols: 2
                Spinner:
                    id: sp3
                    text: 'Up Pyramid'
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                    'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', \
                    'Circle Z', 'Cone Y'
                Spinner:
                    id: sp4
                    text: 'Empty'
                    values: block_list
            BoxLayout:
                orientation: 'vertical'
                Button:
                    id: cmd2
                    text: 'Build It!'
                    on_press: root.cmd(tix3.text, tix4.text, tiy3.text, \
                    tiy4.text, tiz3.text, tiz4.text, tirad2.text, sp3.text, \
                    sp4.text, fill2.active, hst2.text, prt2.text)
    TabbedPanelItem:
        text: sp5.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .4
                TextInput:
                    id: tix5
                    multiline: False
                    size_hint_x: .4
                    text: str(sx5.value)
                    on_text: root.int_set(self, sx5)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx5)
                    Button:
                        text:'>'
                        size_hint_x: .1
                        on_press: root.pls(sx5)
                Slider:
                    id: sx5
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/X2'
                    size_hint_x: .4
                TextInput:
                    id: tix6
                    size_hint_x: .4
                    multiline: False
                    text: str(sx6.value)
                    on_text: root.int_set(self, sx6)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx6)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sx6)
                Slider:
                    id: sx6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .4
                TextInput:
                    id: tiy5
                    size_hint_x: .4
                    multiline: False
                    text: str(sy5.value)
                    on_text: root.int_set(self, sy5)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy5)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy5)
                Slider:
                    id: sy5
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Y2'
                    size_hint_x: .4
                TextInput:
                    id: tiy6
                    size_hint_x: .4
                    multiline: False
                    text: str(sy6.value)
                    on_text: root.int_set(self, sy6)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy6)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy6)
                Slider:
                    id: sy6
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .4
                TextInput:
                    id: tiz5
                    size_hint_x: .4
                    multiline: False
                    text: str(sz5.value)
                    on_text: root.int_set(self, sz5)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz5)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root. pls(sz5)
                Slider:
                    id: sz5
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Z2'
                    size_hint_x: .4
                TextInput:
                    id: tiz6
                    size_hint_x: .4
                    multiline: False
                    text: str(sz6.value)
                    on_text: root.int_set(self, sz6)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz6)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sz6)
                Slider:
                    id: sz6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Radius'
                    size_hint_x: .4
                TextInput:
                    id: tirad3
                    size_hint_x: .4
                    multiline: False
                    text: str(srad3.value)
                    on_text: root.int_set(self, srad3)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(srad3)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(srad3)
                Slider:
                    id: srad3
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Fill=%s' % fill3.active
                Switch:
                    id: fill3
                TextInput:
                    id: hst3
                    text: '127.0.0.1'
                    multiline: False
                TextInput:
                    id: prt3
                    text: '4080'
                    multiline: False
            GridLayout:
                cols: 2
                Spinner:
                    id: sp5
                    text: 'Cuboid'
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                    'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', \
                    'Circle Y', 'Circle Z', 'Cone Y'
                Spinner:
                    id: sp6
                    text: 'Empty'
                    values: block_list
            BoxLayout:
                orientation: 'vertical'
                Button:
                    id: cmd3
                    text: 'Build It!'
                    on_press: root.cmd(tix5.text, tix6.text, tiy5.text, \
                    tiy6.text, tiz5.text, tiz6.text, tirad3.text, sp5.text, \
                    sp6.text, fill3.active, hst3.text, prt3.text)
    TabbedPanelItem:
        text: sp7.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .4
                TextInput:
                    id: tix7
                    multiline: False
                    size_hint_x: .4
                    text: str(sx7.value)
                    on_text: root.int_set(self, sx7)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx7)
                    Button:
                        text:'>'
                        size_hint_x: .1
                        on_press: root.pls(sx7)
                Slider:
                    id: sx7
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/X2'
                    size_hint_x: .4
                TextInput:
                    id: tix8
                    size_hint_x: .4
                    multiline: False
                    text: str(sx8.value)
                    on_text: root.int_set(self, sx8)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx8)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sx8)
                Slider:
                    id: sx8
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .4
                TextInput:
                    id: tiy7
                    size_hint_x: .4
                    multiline: False
                    text: str(sy7.value)
                    on_text: root.int_set(self, sy7)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy7)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy7)
                Slider:
                    id: sy7
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Y2'
                    size_hint_x: .4
                TextInput:
                    id: tiy8
                    size_hint_x: .4
                    multiline: False
                    text: str(sy8.value)
                    on_text: root.int_set(self, sy8)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy8)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy8)
                Slider:
                    id: sy8
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .4
                TextInput:
                    id: tiz7
                    size_hint_x: .4
                    multiline: False
                    text: str(sz7.value)
                    on_text: root.int_set(self, sz7)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz7)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root. pls(sz7)
                Slider:
                    id: sz7
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Z2'
                    size_hint_x: .4
                TextInput:
                    id: tiz8
                    size_hint_x: .4
                    multiline: False
                    text: str(sz8.value)
                    on_text: root.int_set(self, sz8)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz8)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sz8)
                Slider:
                    id: sz8
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Radius'
                    size_hint_x: .4
                TextInput:
                    id: tirad4
                    size_hint_x: .4
                    multiline: False
                    text: str(srad4.value)
                    on_text: root.int_set(self, srad4)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(srad4)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(srad4)
                Slider:
                    id: srad4
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Fill=%s' % fill4.active
                Switch:
                    id: fill4
                TextInput:
                    id: hst4
                    text: '127.0.0.1'
                    multiline: False
                TextInput:
                    id: prt4
                    text: '4080'
                    multiline: False
            GridLayout:
                cols: 2
                Spinner:
                    id: sp7
                    text: 'Cylinder Y'
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                    'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', \
                    'Circle Z', 'Cone Y'
                Spinner:
                    id: sp8
                    text: 'Empty'
                    values: block_list
            BoxLayout:
                orientation: 'vertical'
                Button:
                    id: cmd4
                    text: 'Build It!'
                    on_press: root.cmd(tix7.text, tix8.text, tiy7.text, \
                    tiy8.text, tiz7.text, tiz8.text, tirad4.text, sp7.text, \
                    sp8.text, fill4.active, hst4.text, prt4.text)
    TabbedPanelItem:
        text: sp9.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .4
                TextInput:
                    id: tix9
                    multiline: False
                    size_hint_x: .4
                    text: str(sx9.value)
                    on_text: root.int_set(self, sx9)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx9)
                    Button:
                        text:'>'
                        size_hint_x: .1
                        on_press: root.pls(sx9)
                Slider:
                    id: sx9
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/X2'
                    size_hint_x: .4
                TextInput:
                    id: tix0
                    size_hint_x: .4
                    multiline: False
                    text: str(sx0.value)
                    on_text: root.int_set(self, sx0)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx0)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sx0)
                Slider:
                    id: sx0
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .4
                TextInput:
                    id: tiy9
                    size_hint_x: .4
                    multiline: False
                    text: str(sy9.value)
                    on_text: root.int_set(self, sy9)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy9)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy9)
                Slider:
                    id: sy9
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Y2'
                    size_hint_x: .4
                TextInput:
                    id: tiy0
                    size_hint_x: .4
                    multiline: False
                    text: str(sy0.value)
                    on_text: root.int_set(self, sy0)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy0)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy0)
                Slider:
                    id: sy0
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .4
                TextInput:
                    id: tiz9
                    size_hint_x: .4
                    multiline: False
                    text: str(sz9.value)
                    on_text: root.int_set(self, sz9)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz9)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root. pls(sz9)
                Slider:
                    id: sz9
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Z2'
                    size_hint_x: .4
                TextInput:
                    id: tiz0
                    size_hint_x: .4
                    multiline: False
                    text: str(sz0.value)
                    on_text: root.int_set(self, sz0)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz0)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sz0)
                Slider:
                    id: sz0
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Radius'
                    size_hint_x: .4
                TextInput:
                    id: tirad5
                    size_hint_x: .4
                    multiline: False
                    text: str(srad5.value)
                    on_text: root.int_set(self, srad5)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(srad5)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(srad5)
                Slider:
                    id: srad5
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Fill=%s' % fill5.active
                Switch:
                    id: fill5
                TextInput:
                    id: hst1
                    text: '127.0.0.1'
                    multiline: False
                TextInput:
                    id: prt5
                    text: '4080'
                    multiline: False
            GridLayout:
                cols: 2
                Spinner:
                    id: sp9
                    text: 'Circle Y'
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                    'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', \
                    'Circle Z', 'Cone Y'
                Spinner:
                    id: sp0
                    text: 'Empty'
                    values: block_list
            BoxLayout:
                orientation: 'vertical'
                Button:
                    id: cmd5
                    text: 'Build It!'
                    on_press: root.cmd(tix9.text, tix0.text, tiy9.text, \
                    tiy0.text, tiz9.text, tiz0.text, tirad5.text, sp9.text, \
                    sp0.text, fill5.active, hst5.text, prt5.text)
    TabbedPanelItem:
        text: sp11.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .4
                TextInput:
                    id: tix11
                    multiline: False
                    size_hint_x: .4
                    text: str(sx11.value)
                    on_text: root.int_set(self, sx11)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx11)
                    Button:
                        text:'>'
                        size_hint_x: .1
                        on_press: root.pls(sx11)
                Slider:
                    id: sx11
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/X2'
                    size_hint_x: .4
                TextInput:
                    id: tix12
                    size_hint_x: .4
                    multiline: False
                    text: str(sx12.value)
                    on_text: root.int_set(self, sx12)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx12)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sx12)
                Slider:
                    id: sx12
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .4
                TextInput:
                    id: tiy11
                    size_hint_x: .4
                    multiline: False
                    text: str(sy11.value)
                    on_text: root.int_set(self, sy11)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy11)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy11)
                Slider:
                    id: sy11
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Y2'
                    size_hint_x: .4
                TextInput:
                    id: tiy12
                    size_hint_x: .4
                    multiline: False
                    text: str(sy12.value)
                    on_text: root.int_set(self, sy12)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy12)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy12)
                Slider:
                    id: sy12
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .4
                TextInput:
                    id: tiz11
                    size_hint_x: .4
                    multiline: False
                    text: str(sz11.value)
                    on_text: root.int_set(self, sz11)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz11)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root. pls(sz11)
                Slider:
                    id: sz11
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Z2'
                    size_hint_x: .4
                TextInput:
                    id: tiz12
                    size_hint_x: .4
                    multiline: False
                    text: str(sz12.value)
                    on_text: root.int_set(self, sz12)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz12)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sz12)
                Slider:
                    id: sz12
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Radius'
                    size_hint_x: .4
                TextInput:
                    id: tirad6
                    size_hint_x: .4
                    multiline: False
                    text: str(srad6.value)
                    on_text: root.int_set(self, srad6)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(srad6)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(srad6)
                Slider:
                    id: srad6
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Fill=%s' % fill6.active
                Switch:
                    id: fill6
                TextInput:
                    id: hst6
                    text: '127.0.0.1'
                    multiline: False
                TextInput:
                    id: prt6
                    text: '4080'
                    multiline: False
            GridLayout:
                cols: 2
                Spinner:
                    id: sp11
                    text: 'Cone Y'
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                    'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', \
                    'Circle Z', 'Cone Y'
                Spinner:
                    id: sp12
                    text: 'Empty'
                    values: block_list
            BoxLayout:
                orientation: 'vertical'
                Button:
                    id: cmd6
                    text: 'Build It!'
                    on_press: root.cmd(tix11.text, tix12.text, tiy11.text, \
                    tiy12.text, tiz11.text, tiz12.text, tirad6.text, sp11.text, \
                    sp12.text, fill6.active, hst6.text, prt6.text)
    TabbedPanelItem:
        text: sp13.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .4
                TextInput:
                    id: tix13
                    multiline: False
                    size_hint_x: .4
                    text: str(sx13.value)
                    on_text: root.int_set(self, sx13)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx13)
                    Button:
                        text:'>'
                        size_hint_x: .1
                        on_press: root.pls(sx13)
                Slider:
                    id: sx13
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/X2'
                    size_hint_x: .4
                TextInput:
                    id: tix14
                    size_hint_x: .4
                    multiline: False
                    text: str(sx14.value)
                    on_text: root.int_set(self, sx14)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx14)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sx14)
                Slider:
                    id: sx14
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .4
                TextInput:
                    id: tiy13
                    size_hint_x: .4
                    multiline: False
                    text: str(sy13.value)
                    on_text: root.int_set(self, sy13)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy13)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy13)
                Slider:
                    id: sy13
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Y2'
                    size_hint_x: .4
                TextInput:
                    id: tiy14
                    size_hint_x: .4
                    multiline: False
                    text: str(sy14.value)
                    on_text: root.int_set(self, sy14)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy14)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy14)
                Slider:
                    id: sy14
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .4
                TextInput:
                    id: tiz13
                    size_hint_x: .4
                    multiline: False
                    text: str(sz13.value)
                    on_text: root.int_set(self, sz13)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz13)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root. pls(sz13)
                Slider:
                    id: sz13
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Z2'
                    size_hint_x: .4
                TextInput:
                    id: tiz14
                    size_hint_x: .4
                    multiline: False
                    text: str(sz14.value)
                    on_text: root.int_set(self, sz14)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz14)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sz14)
                Slider:
                    id: sz14
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Radius'
                    size_hint_x: .4
                TextInput:
                    id: tirad7
                    size_hint_x: .4
                    multiline: False
                    text: str(srad7.value)
                    on_text: root.int_set(self, srad7)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(srad7)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(srad7)
                Slider:
                    id: srad7
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Fill=%s' % fill7.active
                Switch:
                    id: fill7
                TextInput:
                    id: hst7
                    text: '127.0.0.1'
                    multiline: False
                TextInput:
                    id: prt7
                    text: '4080'
                    multiline: False
            GridLayout:
                cols: 2
                Spinner:
                    id: sp13
                    text: 'Cylinder X'
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                    'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', \
                    'Circle Z', 'Cone Y'
                Spinner:
                    id: sp14
                    text: 'Empty'
                    values: block_list
            BoxLayout:
                orientation: 'vertical'
                Button:
                    id: cmd7
                    text: 'Build It!'
                    on_press: root.cmd(tix13.text, tix14.text, tiy13.text, \
                    tiy14.text, tiz13.text, tiz14.text, tirad7.text, sp13.text, \
                    sp14.text, fill7.active, hst7.text, prt7.text)
    TabbedPanelItem:
        text: sp15.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .4
                TextInput:
                    id: tix15
                    multiline: False
                    size_hint_x: .4
                    text: str(sx15.value)
                    on_text: root.int_set(self, sx15)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx15)
                    Button:
                        text:'>'
                        size_hint_x: .1
                        on_press: root.pls(sx15)
                Slider:
                    id: sx15
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/X2'
                    size_hint_x: .4
                TextInput:
                    id: tix16
                    size_hint_x: .4
                    multiline: False
                    text: str(sx16.value)
                    on_text: root.int_set(self, sx16)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sx16)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sx16)
                Slider:
                    id: sx16
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .4
                TextInput:
                    id: tiy15
                    size_hint_x: .4
                    multiline: False
                    text: str(sy15.value)
                    on_text: root.int_set(self, sy15)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy15)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy15)
                Slider:
                    id: sy15
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Y2'
                    size_hint_x: .4
                TextInput:
                    id: tiy16
                    size_hint_x: .4
                    multiline: False
                    text: str(sy16.value)
                    on_text: root.int_set(self, sy16)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sy16)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sy16)
                Slider:
                    id: sy16
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .4
                TextInput:
                    id: tiz15
                    size_hint_x: .4
                    multiline: False
                    text: str(sz15.value)
                    on_text: root.int_set(self, sz15)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz15)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root. pls(sz15)
                Slider:
                    id: sz15
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'End/Z2'
                    size_hint_x: .4
                TextInput:
                    id: tiz16
                    size_hint_x: .4
                    multiline: False
                    text: str(sz16.value)
                    on_text: root.int_set(self, sz16)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(sz16)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(sz16)
                Slider:
                    id: sz16
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Radius'
                    size_hint_x: .4
                TextInput:
                    id: tirad8
                    size_hint_x: .4
                    multiline: False
                    text: str(srad8.value)
                    on_text: root.int_set(self, srad8)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns(srad8)
                    Button:
                        text: '>'
                        size_hint_x: .1
                        on_press: root.pls(srad8)
                Slider:
                    id: srad8
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 4
                spacing: 2
                Label:
                    text: 'Fill=%s' % fill8.active
                Switch:
                    id: fill8
                TextInput:
                    id: hst8
                    text: '127.0.0.1'
                    multiline: False
                TextInput:
                    id: prt8
                    text: '4080'
                    multiline: False
            GridLayout:
                cols: 2
                Spinner:
                    id: sp15
                    text: 'Circle X'
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                    'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', \
                    'Circle Z', 'Cone Y'
                Spinner:
                    id: sp16
                    text: 'Empty'
                    values: block_list
            BoxLayout:
                orientation: 'vertical'
                Button:
                    id: cmd8
                    text: 'Build It!'
                    on_press: root.cmd(tix15.text, tix16.text, tiy15.text, \
                    tiy16.text, tiz15.text, tiz16.text, tirad8.text, sp15.text, \
                    sp16.text, fill8.active, hst8.text, prt8.text)

""")

def int2(x):
    y = int(float(x))
    return y

class Test(TabbedPanel):

    def int_set(obj, ti, slider):
        y = int2(ti.text)
        slider.value = y
        return slider.value
    
    def pls(y, x):
        x.value += 1
        return x.value

    def mns(y, x):
        x.value -= 1
        return x.value
        
    def cmd(widget_id, tix1, tix2, tiy1, tiy2, tiz1, \
            tiz2, tirad, sp1, sp2, fill, hst1, prt1):
        blk_id = block_list.index(sp2)
        client = Client(hst1, int(prt1), USERNAME, IDENTITY_TOKEN)

        if sp1 == 'Up Pyramid':
            client.set_blocks(pyramid(int2(tix1), int2(tix2), \
                                      int2(tiy1), int2(tiz1), int2(tiz2), fill), blk_id)
        if sp1 == 'Down Pyramid':
            client.set_blocks(upyramid(int2(tix1), int2(tix2), \
                                       int2(tiy1), int2(tiz1), int2(tiz2), fill), blk_id)
        if sp1 == 'Sphere':
            client.set_blocks(sphere(int2(tix1), int2(tiy1), \
                                     int2(tiz1), int2(tirad), fill), blk_id)
        if sp1 == 'Circle X':
            client.set_blocks(circle_x(int2(tix1), int2(tiy1), \
                                       int2(tiz1), int2(tirad), fill), blk_id)
        if sp1 == 'Circle Y':
            client.set_blocks(circle_y(int2(tix1), int2(tiy1), \
                                       int2(tiz1), int2(tirad), fill), blk_id)
        if sp1 == 'Circle Z':
            client.set_blocks(circle_z(int2(tix1), int2(tiy1), \
                                       int2(tiz1), int2(tirad), fill), blk_id)
        if sp1 == 'Cuboid':
            client.set_blocks(cuboid(int2(tix1), int2(tix2), int2(tiy1), \
                                     int2(tiy2), int2(tiz1), int2(tiz2), fill), blk_id)
        if sp1 == 'Cylinder X':
            client.set_blocks(cylinder_x(int2(tix1), int2(tix2), int2(tiy1), \
                                         int2(tiz1), int2(tirad), fill), blk_id)
        if sp1 == 'Cylinder Y':
            client.set_blocks(cylinder_y(int2(tix1), int2(tiy1), int2(tiy2), \
                                         int2(tiz1), int2(tirad), fill), blk_id)
        if sp1 == 'Cylinder Z':
            client.set_blocks(cylinder_z(int2(tix1), int2(tiy1), int2(tiz1), \
                                         int2(tiz2), int2(tirad), fill), blk_id)
        if sp1 == 'Cone Y':
            client.set_blocks(cone_y(int2(tix1), int2(tiy1), int2(tiy2), \
                                     int2(tiz1), int2(tirad), fill), blk_id)
        time.sleep(5)

class ProBuilderApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    ProBuilderApp().run()
