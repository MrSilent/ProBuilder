import kivy
kivy.require('1.7.2')
import time
import random

from builder import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

USERNAME = ''
IDENTITY_TOKEN = ''

block_list = ['Empty', 'Grass', 'Sand', 'Stone', 'Brick', 'Wood', 'Cement',
              'Dirt', 'Plank', 'Snow', 'Glass', 'Cobble', 'Light Stone',
              'Dark Stone', 'Chest', 'Leaves', 'Cloud', 'Tall Grass', 'Yellow Flower',
              'Red Flower', 'Purple Flower', 'Sun Flower', 'White Flower',
              'Blue Flower', '?', '?', '?', '?', '?', '?', '?', '?', 'Yellow',
              'Light Green', 'Droid Green', 'Cyan', 'Pine', 'D-Rea',
              'Charcol', 'Navy', 'Light Grey', 'Dark Grey', 'Purple', 'Red',
              'Pink', 'Hot Pink', 'Olive', 'Khaki', 'Black', 'Mdnt Blue', 'Maroon',
              'Brown', 'Taupe', 'Rust', 'Tan', 'Shironeri', 'Denim', 'Royal B',
              'Indigo', 'Turquoise', 'Lavender', 'White', 'Steel Blue', 'Steel']    

Builder.load_string("""

#:set block_list ['Empty', 'Grass', 'Sand', 'Stone', 'Brick', 'Wood', \
                'Cement', 'Dirt', 'Plank', 'Snow', 'Glass', 'Cobble', 'Light Stone', \
                'Dark Stone', 'Chest', 'Leaves', 'Cloud', 'Tall Grass', 'Yellow Flower', \
                'Red Flower', 'Purple Flower', 'Sun Flower', 'White Flower', \
                'Blue Flower', '?', '?', '?', '?', '?', '?', '?', '?', 'Yellow', \
              'Light Green', 'Droid Green', 'Cyan', 'Pine', 'D-Rea', 'Charcol', \
              'Navy', 'Light Grey', 'Dark Grey', 'Purple', 'Red', 'Pink', \
              'Hot Pink', 'Olive', 'Khaki', 'Black', 'Mdnt Blue', 'Maroon', \
              'Brown', 'Taupe', 'Rust', 'Tan', 'Shironeri', 'Denim', 'Royal B', \
              'Indigo', 'Turquoise', 'Lavender', 'White', 'Steel Blue', 'Steel']

<Test>:
    do_default_tab: False

    TabbedPanelItem:
        text: sp1.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .2
                TextInput:
                    id: tix1
                    multiline: False
                    size_hint_x: .2
                    text: str(int(sx1.value))
                    on_text: root.int_set(self, sx1)
                    on_text_validate: root.goto_next(tix2)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sxmin
                        size_hint_x: .3
                        text: str(sx1.min)
                        on_text: root.min(self, sx1)
                    TextInput:
                        id: sxmax
                        size_hint_x: .3
                        text: str(sx1.max)
                        on_text: root.max(self, sx1)
                Slider:
                    id: sx1
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/X2'
                    size_hint_x: .2
                TextInput:
                    id: tix2
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sx2.value))
                    on_text: root.int_set(self, sx2)
                    on_text_validate: root.goto_next(tiy1)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sx2min
                        size_hint_x: .3
                        text: str(sx2.min)
                        on_text: root.min(self, sx2)
                    TextInput:
                        id: sx2max
                        size_hint_x: .3
                        text: str(sx2.max)
                        on_text: root.max(self, sx2)
                Slider:
                    id: sx2
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .2
                TextInput:
                    id: tiy1
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sy1.value))
                    on_text: root.int_set(self, sy1)
                    on_text_validate: root.goto_next(tiy2)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    Label:
                        text: ''
                    Label:
                        text: ''
                    Label:
                        text: '    Min     '
                    Label:
                        text: '  Max    '
                Slider:
                    id: sy1
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/Y2'
                    size_hint_x: .2
                TextInput:
                    id: tiy2
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sy2.value))
                    on_text: root.int_set(self, sy2)
                    on_text_validate: root.goto_next(tiz1)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3 
                    Label:
                        text: ' Column  '
                    Label:
                        text: 'Column  '
                    Label:
                        text: ''
                    Label:
                        text: ''
                Slider:
                    id: sy2
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .2
                TextInput:
                    id: tiz1
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sz1.value))
                    on_text: root.int_set(self, sz1)
                    on_text_validate: root.goto_next(tiz2)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sz1min
                        size_hint_x: .3
                        text: str(sz1.min)
                        on_text: root.min(self, sz1)
                    TextInput:
                        id: sz1max
                        size_hint_x: .3
                        text: str(sz1.max)
                        on_text: root.max(self, sz1)
                Slider:
                    id: sz1
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/Z2'
                    size_hint_x: .2
                TextInput:
                    id: tiz2
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sz2.value))
                    on_text: root.int_set(self, sz2)
                    on_text_validate: root.goto_next(tirad)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sz2min
                        size_hint_x: .3
                        text: str(sz2.min)
                        on_text: root.min(self, sz2)
                    TextInput:
                        id: sz2max
                        size_hint_x: .3
                        text: str(sz2.max)
                        on_text: root.max(self, sz2)
                Slider:
                    id: sz2
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Radius'
                    size_hint_x: .2
                TextInput:
                    id: tirad
                    size_hint_x: .2
                    multiline: False
                    text: str(int(srad.value))
                    on_text: root.int_set(self, srad)
                    on_text_validate: root.goto_next(hst1)
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
                GridLayout:
                    cols: 1
                    size_hint_x: .3
                    Label:
                        text: ''
                Slider:
                    id: srad
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                rows: 2
                spacing: 2
                size_hint_y: .2
                GridLayout:
                    cols: 4
                    GridLayout:
                        cols: 2
                        size_hint_x: .21
                        Label:
                            id: flabel
                            text: root.fill_txt(self, fill)
                            size_hint_x: .16
                        CheckBox:
                            id: fill
                            on_active: root.fill_txt(flabel, self)
                            size_hint_x: .16
                    GridLayout:
                        cols: 4
                        size_hint_x: .5
                        Label:
                            text: 'Host'
                            size_hint_x: .21
                        TextInput:
                            id: hst1
                            size_hint_x: .29
                            text: '127.0.0.1'
                            multiline: False
                            on_text_validate: root.goto_next(prt1)
                        Label:
                            text: 'Port'
                            size_hint_x: .2
                        TextInput:
                            id: prt1
                            size_hint_x: .25
                            text: '4080'
                            multiline: False
                            on_text_validate: root.goto_next(tix1)
                GridLayout:
                    cols: 3
                    spacing: 2
                    size_hint_y: .8
                    Button:
                        id: cmd
                        text: 'Build It!'
                        on_press: root.cmd(tix1.text, tix2.text, tiy1.text, \
                        tiy2.text, tiz1.text, tiz2.text, tirad.text, sp1.text, \
                        sp2.text, fill.active, hst1.text, prt1.text)
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
    TabbedPanelItem:
        text: sp3.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .2
                TextInput:
                    id: tix3
                    multiline: False
                    size_hint_x: .2
                    text: str(int(sx3.value))
                    on_text: root.int_set(self, sx3)
                    on_text_validate: root.goto_next(tix4)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sx3min
                        size_hint_x: .3
                        text: str(sx3.min)
                        on_text: root.min(self, sx3)
                    TextInput:
                        id: sxmax
                        size_hint_x: .3
                        text: str(sx3.max)
                        on_text: root.max(self, sx3)
                Slider:
                    id: sx3
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/X2'
                    size_hint_x: .2
                TextInput:
                    id: tix4
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sx4.value))
                    on_text: root.int_set(self, sx4)
                    on_text_validate: root.goto_next(tiy3)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sx4min
                        size_hint_x: .3
                        text: str(sx4.min)
                        on_text: root.min(self, sx4)
                    TextInput:
                        id: sx4max
                        size_hint_x: .3
                        text: str(sx4.max)
                        on_text: root.max(self, sx4)
                Slider:
                    id: sx4
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .2
                TextInput:
                    id: tiy3
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sy3.value))
                    on_text: root.int_set(self, sy3)
                    on_text_validate: root.goto_next(tiy4)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    Label:
                        text: ''
                    Label:
                        text: ''
                    Label:
                        text: '    Min     '
                    Label:
                        text: '  Max    '
                Slider:
                    id: sy3
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/Y2'
                    size_hint_x: .2
                TextInput:
                    id: tiy4
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sy4.value))
                    on_text: root.int_set(self, sy4)
                    on_text_validate: root.goto_next(tiz3)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3 
                    Label:
                        text: ' Column  '
                    Label:
                        text: 'Column  '
                    Label:
                        text: ''
                    Label:
                        text: ''
                Slider:
                    id: sy4
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .2
                TextInput:
                    id: tiz3
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sz3.value))
                    on_text: root.int_set(self, sz3)
                    on_text_validate: root.goto_next(tiz4)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sz3min
                        size_hint_x: .3
                        text: str(sz3.min)
                        on_text: root.min(self, sz3)
                    TextInput:
                        id: sz3max
                        size_hint_x: .3
                        text: str(sz3.max)
                        on_text: root.max(self, sz3)
                Slider:
                    id: sz3
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/Z2'
                    size_hint_x: .2
                TextInput:
                    id: tiz4
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sz4.value))
                    on_text: root.int_set(self, sz4)
                    on_text_validate: root.goto_next(tirad2)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sz4min
                        size_hint_x: .3
                        text: str(sz4.min)
                        on_text: root.min(self, sz4)
                    TextInput:
                        id: sz4max
                        size_hint_x: .3
                        text: str(sz4.max)
                        on_text: root.max(self, sz4)
                Slider:
                    id: sz4
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Radius'
                    size_hint_x: .2
                TextInput:
                    id: tirad2
                    size_hint_x: .2
                    multiline: False
                    text: str(int(srad2.value))
                    on_text: root.int_set(self, srad2)
                    on_text_validate: root.goto_next(hst2)
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
                GridLayout:
                    cols: 1
                    size_hint_x: .3
                    Label:
                        text: ''
                Slider:
                    id: srad2
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                rows: 2
                spacing: 2
                size_hint_y: .2
                GridLayout:
                    cols: 4
                    GridLayout:
                        cols: 2
                        size_hint_x: .21
                        Label:
                            id: flabel2
                            text: root.fill_txt(self, fill2)
                            size_hint_x: .16
                        CheckBox:
                            id: fill2
                            on_active: root.fill_txt(flabel2, self)
                            size_hint_x: .16
                    GridLayout:
                        cols: 4
                        size_hint_x: .5
                        Label:
                            text: 'Host'
                            size_hint_x: .21
                        TextInput:
                            id: hst2
                            size_hint_x: .29
                            text: '127.0.0.1'
                            multiline: False
                            on_text_validate: root.goto_next(prt2)
                        Label:
                            text: 'Port'
                            size_hint_x: .2
                        TextInput:
                            id: prt2
                            size_hint_x: .25
                            text: '4080'
                            multiline: False
                            on_text_validate: root.goto_next(tix3)
                GridLayout:
                    cols: 3
                    spacing: 2
                    size_hint_y: .8
                    Button:
                        id: cmd2
                        text: 'Build It!'
                        on_press: root.cmd(tix3.text, tix4.text, tiy3.text, \
                        tiy4.text, tiz3.text, tiz4.text, tirad2.text, sp3.text, \
                        sp4.text, fill2.active, hst2.text, prt2.text)
                    Spinner:
                        id: sp3
                        text: 'Cuboid'
                        values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                        'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', \
                        'Circle Z', 'Cone Y'
                    Spinner:
                        id: sp4
                        text: 'Empty'
                        values: block_list
    TabbedPanelItem:
        text: sp5.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .2
                TextInput:
                    id: tix5
                    multiline: False
                    size_hint_x: .2
                    text: str(int(sx5.value))
                    on_text: root.int_set(self, sx5)
                    on_text_validate: root.goto_next(tix6)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sx5min
                        size_hint_x: .3
                        text: str(sx1.min)
                        on_text: root.min(self, sx5)
                    TextInput:
                        id: sx5max
                        size_hint_x: .3
                        text: str(sx1.max)
                        on_text: root.max(self, sx5)
                Slider:
                    id: sx5
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/X2'
                    size_hint_x: .2
                TextInput:
                    id: tix6
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sx6.value))
                    on_text: root.int_set(self, sx6)
                    on_text_validate: root.goto_next(tiy5)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sx6min
                        size_hint_x: .3
                        text: str(sx6.min)
                        on_text: root.min(self, sx6)
                    TextInput:
                        id: sx6max
                        size_hint_x: .3
                        text: str(sx6.max)
                        on_text: root.max(self, sx6)
                Slider:
                    id: sx6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .2
                TextInput:
                    id: tiy5
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sy5.value))
                    on_text: root.int_set(self, sy5)
                    on_text_validate: root.goto_next(tiy6)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    Label:
                        text: ''
                    Label:
                        text: ''
                    Label:
                        text: '    Min     '
                    Label:
                        text: '  Max    '
                Slider:
                    id: sy5
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/Y2'
                    size_hint_x: .2
                TextInput:
                    id: tiy6
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sy6.value))
                    on_text: root.int_set(self, sy6)
                    on_text_validate: root.goto_next(tiz5)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3 
                    Label:
                        text: ' Column  '
                    Label:
                        text: 'Column  '
                    Label:
                        text: ''
                    Label:
                        text: ''
                Slider:
                    id: sy6
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .2
                TextInput:
                    id: tiz5
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sz5.value))
                    on_text: root.int_set(self, sz5)
                    on_text_validate: root.goto_next(tiz6)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sz5min
                        size_hint_x: .3
                        text: str(sz5.min)
                        on_text: root.min(self, sz5)
                    TextInput:
                        id: sz5max
                        size_hint_x: .3
                        text: str(sz5.max)
                        on_text: root.max(self, sz5)
                Slider:
                    id: sz5
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/Z2'
                    size_hint_x: .2
                TextInput:
                    id: tiz6
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sz6.value))
                    on_text: root.int_set(self, sz6)
                    on_text_validate: root.goto_next(tirad3)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sz6min
                        size_hint_x: .3
                        text: str(sz6.min)
                        on_text: root.min(self, sz6)
                    TextInput:
                        id: sz6max
                        size_hint_x: .3
                        text: str(sz6.max)
                        on_text: root.max(self, sz6)
                Slider:
                    id: sz6
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Radius'
                    size_hint_x: .2
                TextInput:
                    id: tirad3
                    size_hint_x: .2
                    multiline: False
                    text: str(int(srad3.value))
                    on_text: root.int_set(self, srad3)
                    on_text_validate: root.goto_next(hst3)
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
                GridLayout:
                    cols: 1
                    size_hint_x: .3
                    Label:
                        text: ''
                Slider:
                    id: srad3
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                rows: 2
                spacing: 2
                size_hint_y: .2
                GridLayout:
                    cols: 4
                    GridLayout:
                        cols: 2
                        size_hint_x: .21
                        Label:
                            id: flabel3
                            text: root.fill_txt(self, fill3)
                            size_hint_x: .16
                        CheckBox:
                            id: fill3
                            on_active: root.fill_txt(flabel3, self)
                            size_hint_x: .16
                    GridLayout:
                        cols: 4
                        size_hint_x: .5
                        Label:
                            text: 'Host'
                            size_hint_x: .21
                        TextInput:
                            id: hst3
                            size_hint_x: .29
                            text: '127.0.0.1'
                            multiline: False
                            on_text_validate: root.goto_next(prt3)
                        Label:
                            text: 'Port'
                            size_hint_x: .2
                        TextInput:
                            id: prt3
                            size_hint_x: .25
                            text: '4080'
                            multiline: False
                            on_text_validate: root.goto_next(tix5)
                GridLayout:
                    cols: 3
                    spacing: 2
                    size_hint_y: .8
                    Button:
                        id: cmd3
                        text: 'Build It!'
                        on_press: root.cmd(tix5.text, tix6.text, tiy5.text, \
                        tiy6.text, tiz5.text, tiz6.text, tirad3.text, sp5.text, \
                        sp6.text, fill3.active, hst3.text, prt3.text)
                    Spinner:
                        id: sp5
                        text: 'Cylinder Y'
                        values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                        'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', \
                        'Circle Z', 'Cone Y'
                    Spinner:
                        id: sp6
                        text: 'Empty'
                        values: block_list
    TabbedPanelItem:
        text: sp7.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .2
                TextInput:
                    id: tix7
                    multiline: False
                    size_hint_x: .2
                    text: str(int(sx7.value))
                    on_text: root.int_set(self, sx7)
                    on_text_validate: root.goto_next(tix8)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sx7min
                        size_hint_x: .3
                        text: str(sx7.min)
                        on_text: root.min(self, sx7)
                    TextInput:
                        id: sx7max
                        size_hint_x: .3
                        text: str(sx7.max)
                        on_text: root.max(self, sx7)
                Slider:
                    id: sx7
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/X2'
                    size_hint_x: .2
                TextInput:
                    id: tix8
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sx8.value))
                    on_text: root.int_set(self, sx8)
                    on_text_validate: root.goto_next(tiy7)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sx8min
                        size_hint_x: .3
                        text: str(sx8.min)
                        on_text: root.min(self, sx8)
                    TextInput:
                        id: sx8max
                        size_hint_x: .3
                        text: str(sx8.max)
                        on_text: root.max(self, sx8)
                Slider:
                    id: sx8
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .2
                TextInput:
                    id: tiy7
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sy7.value))
                    on_text: root.int_set(self, sy7)
                    on_text_validate: root.goto_next(tiy8)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    Label:
                        text: ''
                    Label:
                        text: ''
                    Label:
                        text: '    Min     '
                    Label:
                        text: '  Max    '
                Slider:
                    id: sy7
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/Y2'
                    size_hint_x: .2
                TextInput:
                    id: tiy8
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sy8.value))
                    on_text: root.int_set(self, sy8)
                    on_text_validate: root.goto_next(tiz7)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3 
                    Label:
                        text: ' Column  '
                    Label:
                        text: 'Column  '
                    Label:
                        text: ''
                    Label:
                        text: ''
                Slider:
                    id: sy8
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .2
                TextInput:
                    id: tiz7
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sz7.value))
                    on_text: root.int_set(self, sz7)
                    on_text_validate: root.goto_next(tiz8)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sz7min
                        size_hint_x: .3
                        text: str(sz7.min)
                        on_text: root.min(self, sz7)
                    TextInput:
                        id: sz7max
                        size_hint_x: .3
                        text: str(sz7.max)
                        on_text: root.max(self, sz7)
                Slider:
                    id: sz7
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/Z2'
                    size_hint_x: .2
                TextInput:
                    id: tiz8
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sz8.value))
                    on_text: root.int_set(self, sz8)
                    on_text_validate: root.goto_next(tirad4)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sz8min
                        size_hint_x: .3
                        text: str(sz8.min)
                        on_text: root.min(self, sz8)
                    TextInput:
                        id: sz8max
                        size_hint_x: .3
                        text: str(sz8.max)
                        on_text: root.max(self, sz8)
                Slider:
                    id: sz8
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Radius'
                    size_hint_x: .2
                TextInput:
                    id: tirad4
                    size_hint_x: .2
                    multiline: False
                    text: str(int(srad4.value))
                    on_text: root.int_set(self, srad4)
                    on_text_validate: root.goto_next(hst4)
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
                GridLayout:
                    cols: 1
                    size_hint_x: .3
                    Label:
                        text: ''
                Slider:
                    id: srad4
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                rows: 2
                spacing: 2
                size_hint_y: .2
                GridLayout:
                    cols: 4
                    GridLayout:
                        cols: 2
                        size_hint_x: .21
                        Label:
                            id: flabel4
                            text: root.fill_txt(self, fill4)
                            size_hint_x: .16
                        CheckBox:
                            id: fill4
                            on_active: root.fill_txt(flabel4, self)
                            size_hint_x: .16
                    GridLayout:
                        cols: 4
                        size_hint_x: .5
                        Label:
                            text: 'Host'
                            size_hint_x: .21
                        TextInput:
                            id: hst4
                            size_hint_x: .29
                            text: '127.0.0.1'
                            multiline: False
                            on_text_validate: root.goto_next(prt4)
                        Label:
                            text: 'Port'
                            size_hint_x: .2
                        TextInput:
                            id: prt4
                            size_hint_x: .25
                            text: '4080'
                            multiline: False
                            on_text_validate: root.goto_next(tix7)
                GridLayout:
                    cols: 3
                    spacing: 2
                    size_hint_y: .8
                    Button:
                        id: cmd4
                        text: 'Build It!'
                        on_press: root.cmd(tix7.text, tix8.text, tiy7.text, \
                        tiy8.text, tiz7.text, tiz8.text, tirad4.text, sp7.text, \
                        sp8.text, fill4.active, hst4.text, prt4.text)
                    Spinner:
                        id: sp7
                        text: 'Up Pyramid'
                        values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                        'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', \
                        'Circle Z', 'Cone Y'
                    Spinner:
                        id: sp8
                        text: 'Empty'
                        values: block_list
    TabbedPanelItem:
        text: sp9.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .2
                TextInput:
                    id: tix9
                    multiline: False
                    size_hint_x: .2
                    text: str(int(sx9.value))
                    on_text: root.int_set(self, sx9)
                    on_text_validate: root.goto_next(tix0)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sx9min
                        size_hint_x: .3
                        text: str(sx9.min)
                        on_text: root.min(self, sx9)
                    TextInput:
                        id: sx9max
                        size_hint_x: .3
                        text: str(sx9.max)
                        on_text: root.max(self, sx9)
                Slider:
                    id: sx9
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/X2'
                    size_hint_x: .2
                TextInput:
                    id: tix0
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sx0.value))
                    on_text: root.int_set(self, sx0)
                    on_text_validate: root.goto_next(tiy9)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sx0min
                        size_hint_x: .3
                        text: str(sx0.min)
                        on_text: root.min(self, sx0)
                    TextInput:
                        id: sx0max
                        size_hint_x: .3
                        text: str(sx0.max)
                        on_text: root.max(self, sx0)
                Slider:
                    id: sx0
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .2
                TextInput:
                    id: tiy9
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sy9.value))
                    on_text: root.int_set(self, sy9)
                    on_text_validate: root.goto_next(tiy0)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    Label:
                        text: ''
                    Label:
                        text: ''
                    Label:
                        text: '    Min     '
                    Label:
                        text: '  Max    '
                Slider:
                    id: sy9
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/Y2'
                    size_hint_x: .2
                TextInput:
                    id: tiy0
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sy0.value))
                    on_text: root.int_set(self, sy0)
                    on_text_validate: root.goto_next(tiz9)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3 
                    Label:
                        text: ' Column  '
                    Label:
                        text: 'Column  '
                    Label:
                        text: ''
                    Label:
                        text: ''
                Slider:
                    id: sy0
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .2
                TextInput:
                    id: tiz9
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sz9.value))
                    on_text: root.int_set(self, sz9)
                    on_text_validate: root.goto_next(tiz0)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sz9min
                        size_hint_x: .3
                        text: str(sz9.min)
                        on_text: root.min(self, sz9)
                    TextInput:
                        id: sz9max
                        size_hint_x: .3
                        text: str(sz9.max)
                        on_text: root.max(self, sz9)
                Slider:
                    id: sz9
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/Z2'
                    size_hint_x: .2
                TextInput:
                    id: tiz0
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sz0.value))
                    on_text: root.int_set(self, sz0)
                    on_text_validate: root.goto_next(tirad5)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sz0min
                        size_hint_x: .3
                        text: str(sz0.min)
                        on_text: root.min(self, sz0)
                    TextInput:
                        id: sz2max
                        size_hint_x: .3
                        text: str(sz0.max)
                        on_text: root.max(self, sz0)
                Slider:
                    id: sz0
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Radius'
                    size_hint_x: .2
                TextInput:
                    id: tirad5
                    size_hint_x: .2
                    multiline: False
                    text: str(int(srad5.value))
                    on_text: root.int_set(self, srad5)
                    on_text_validate: root.goto_next(hst5)
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
                GridLayout:
                    cols: 1
                    size_hint_x: .3
                    Label:
                        text: ''
                Slider:
                    id: srad5
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                rows: 2
                spacing: 2
                size_hint_y: .2
                GridLayout:
                    cols: 4
                    GridLayout:
                        cols: 2
                        size_hint_x: .21
                        Label:
                            id: flabel5
                            text: root.fill_txt(self, fill5)
                            size_hint_x: .16
                        CheckBox:
                            id: fill5
                            on_active: root.fill_txt(flabel5, self)
                            size_hint_x: .16
                    GridLayout:
                        cols: 4
                        size_hint_x: .5
                        Label:
                            text: 'Host'
                            size_hint_x: .21
                        TextInput:
                            id: hst5
                            size_hint_x: .29
                            text: '127.0.0.1'
                            multiline: False
                            on_text_validate: root.goto_next(prt5)
                        Label:
                            text: 'Port'
                            size_hint_x: .2
                        TextInput:
                            id: prt5
                            size_hint_x: .25
                            text: '4080'
                            multiline: False
                            on_text_validate: root.goto_next(tix9)
                GridLayout:
                    cols: 3
                    spacing: 2
                    size_hint_y: .8
                    Button:
                        id: cmd5
                        text: 'Build It!'
                        on_press: root.cmd(tix9.text, tix0.text, tiy9.text, \
                        tiy0.text, tiz9.text, tiz0.text, tirad5.text, sp9.text, \
                        sp0.text, fill5.active, hst5.text, prt5.text)
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
    TabbedPanelItem:
        text: sp11.text
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/X1'
                    size_hint_x: .2
                TextInput:
                    id: tix11
                    multiline: False
                    size_hint_x: .2
                    text: str(int(sx11.value))
                    on_text: root.int_set(self, sx11)
                    on_text_validate: root.goto_next(tix12)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sx11min
                        size_hint_x: .3
                        text: str(sx11.min)
                        on_text: root.min(self, sx11)
                    TextInput:
                        id: sx11max
                        size_hint_x: .3
                        text: str(sx11.max)
                        on_text: root.max(self, sx11)
                Slider:
                    id: sx11
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/X2'
                    size_hint_x: .2
                TextInput:
                    id: tix12
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sx12.value))
                    on_text: root.int_set(self, sx12)
                    on_text_validate: root.goto_next(tiy11)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sx12min
                        size_hint_x: .3
                        text: str(sx12.min)
                        on_text: root.min(self, sx12)
                    TextInput:
                        id: sx12max
                        size_hint_x: .3
                        text: str(sx12.max)
                        on_text: root.max(self, sx12)
                Slider:
                    id: sx12
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/Y1'
                    size_hint_x: .2
                TextInput:
                    id: tiy11
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sy11.value))
                    on_text: root.int_set(self, sy11)
                    on_text_validate: root.goto_next(tiy12)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    Label:
                        text: ''
                    Label:
                        text: ''
                    Label:
                        text: '    Min     '
                    Label:
                        text: '  Max    '
                Slider:
                    id: sy11
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/Y2'
                    size_hint_x: .2
                TextInput:
                    id: tiy12
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sy12.value))
                    on_text: root.int_set(self, sy12)
                    on_text_validate: root.goto_next(tiz11)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3 
                    Label:
                        text: ' Column  '
                    Label:
                        text: 'Column  '
                    Label:
                        text: ''
                    Label:
                        text: ''
                Slider:
                    id: sy12
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Ctr/Z1'
                    size_hint_x: .2
                TextInput:
                    id: tiz11
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sz11.value))
                    on_text: root.int_set(self, sz11)
                    on_text_validate: root.goto_next(tiz12)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sz11min
                        size_hint_x: .3
                        text: str(sz11.min)
                        on_text: root.min(self, sz11)
                    TextInput:
                        id: sz11max
                        size_hint_x: .3
                        text: str(sz11.max)
                        on_text: root.max(self, sz11)
                Slider:
                    id: sz11
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'End/Z2'
                    size_hint_x: .2
                TextInput:
                    id: tiz12
                    size_hint_x: .2
                    multiline: False
                    text: str(int(sz12.value))
                    on_text: root.int_set(self, sz12)
                    on_text_validate: root.goto_next(tirad6)
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
                GridLayout:
                    cols: 2
                    size_hint_x: .3
                    TextInput:
                        id: sz12min
                        size_hint_x: .3
                        text: str(sz12.min)
                        on_text: root.min(self, sz12)
                    TextInput:
                        id: sz12max
                        size_hint_x: .3
                        text: str(sz12.max)
                        on_text: root.max(self, sz12)
                Slider:
                    id: sz12
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
            GridLayout:
                cols: 5
                spacing: 2
                size_hint_y: .1
                Label:
                    text: 'Radius'
                    size_hint_x: .2
                TextInput:
                    id: tirad6
                    size_hint_x: .2
                    multiline: False
                    text: str(int(srad6.value))
                    on_text: root.int_set(self, srad6)
                    on_text_validate: root.goto_next(hst6)
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
                GridLayout:
                    cols: 1
                    size_hint_x: .3
                    Label:
                        text: ''
                Slider:
                    id: srad6
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                rows: 2
                spacing: 2
                size_hint_y: .2
                GridLayout:
                    cols: 4
                    GridLayout:
                        cols: 2
                        size_hint_x: .21
                        Label:
                            id: flabel6
                            text: root.fill_txt(self, fill6)
                            size_hint_x: .16
                        CheckBox:
                            id: fill6
                            on_active: root.fill_txt(flabel6, self)
                            size_hint_x: .16
                    GridLayout:
                        cols: 4
                        size_hint_x: .5
                        Label:
                            text: 'Host'
                            size_hint_x: .21
                        TextInput:
                            id: hst6
                            size_hint_x: .29
                            text: '127.0.0.1'
                            multiline: False
                            on_text_validate: root.goto_next(prt6)
                        Label:
                            text: 'Port'
                            size_hint_x: .2
                        TextInput:
                            id: prt6
                            size_hint_x: .25
                            text: '4080'
                            multiline: False
                            on_text_validate: root.goto_next(tix11)
                GridLayout:
                    cols: 3
                    spacing: 2
                    size_hint_y: .8
                    Button:
                        id: cmd6
                        text: 'Build It!'
                        on_press: root.cmd(tix11.text, tix12.text, tiy11.text, \
                        tiy12.text, tiz11.text, tiz12.text, tirad6.text, sp11.text, \
                        sp12.text, fill6.active, hst6.text, prt6.text)
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
    TabbedPanelItem:
        text: 'iBuilder 1'
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 2
                spacing: 2
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'Ctr/X1'
                        size_hint_x: .2
                    TextInput:
                        id: tix15
                        multiline: False
                        size_hint_x: .2
                        text: str(sx15.value)
                        on_text: root.int_set(self, sx15)
                        on_text_validate: root.goto_next(tix16)
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
                    Label:
                        text: 'X1 Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_x1
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(inc_x2)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_x1.text), inc_x1)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_x1.text), inc_x1)
                Slider:
                    id: sx15
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'End/X2'
                        size_hint_x: .2
                    TextInput:
                        id: tix16
                        size_hint_x: .2
                        multiline: False
                        text: str(sx16.value)
                        on_text: root.int_set(self, sx16)
                        on_text_validate: root.goto_next(tiy15)
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
                    Label:
                        text: 'X2 Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_x2
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(inc_y1)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_x2.text), inc_x2)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_x2.text), inc_x2)
                Slider:
                    id: sx16
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'Ctr/Y1'
                        size_hint_x: .2
                    TextInput:
                        id: tiy15
                        size_hint_x: .2
                        multiline: False
                        text: str(sy15.value)
                        on_text: root.int_set(self, sy15)
                        on_text_validate: root.goto_next(tiy16)
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
                    Label:
                        text: 'Y1 Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_y1
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(inc_y2)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_y1.text), inc_y1)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_y1.text), inc_y1)
                Slider:
                    id: sy15
                    min: 0
                    max: 255
                    step: 1
                    value: 12
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'End/Y2'
                        size_hint_x: .2
                    TextInput:
                        id: tiy16
                        size_hint_x: .2
                        multiline: False
                        text: str(sy16.value)
                        on_text: root.int_set(self, sy16)
                        on_text_validate: root.goto_next(tiz15)
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
                    Label:
                        text: 'Y2 Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_y2
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(inc_z1)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_y2.text), inc_y2)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_y2.text), inc_y2)
                Slider:
                    id: sy16
                    min: 0
                    max: 255
                    step: 1
                    value: 12
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'Ctr/Z1'
                        size_hint_x: .2
                    TextInput:
                        id: tiz15
                        size_hint_x: .2
                        multiline: False
                        text: str(sz15.value)
                        on_text: root.int_set(self, sz15)
                        on_text_validate: root.goto_next(tiz16)
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
                    Label:
                        text: 'Z1 Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_z1
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(inc_z2)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_z1.text), inc_z1)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_z1.text), inc_z1)
                Slider:
                    id: sz15
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'End/Z2'
                        size_hint_x: .2
                    TextInput:
                        id: tiz16
                        size_hint_x: .2
                        multiline: False
                        text: str(sz16.value)
                        on_text: root.int_set(self, sz16)
                        on_text_validate: root.goto_next(tirad8)
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
                    Label:
                        text: 'Z2 Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_z2
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(inc_rad)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_z2.text), inc_z2)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_z2.text), inc_z2)
                Slider:
                    id: sz16
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'Radius'
                        size_hint_x: .2
                    TextInput:
                        id: tirad8
                        size_hint_x: .2
                        multiline: False
                        text: str(srad8.value)
                        on_text: root.int_set(self, srad8)
                        on_text_validate: root.goto_next(hst8)
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
                    Label:
                        text: 'Radius Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_rad
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(count)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_rad.text), inc_rad)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_rad.text), inc_rad)
                Slider:
                    id: srad8
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 7
                spacing: 2
                size_hint_y: .15
                Label:
                    text: 'Count'
                    size_hint_x: .12
                TextInput:
                    id: count
                    text: str(0)
                    multiline: False
                    size_hint_x: .2
                    on_text_validate: root.goto_next(tix15)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns_c(int(count.text), count)
                    Button:
                        text:'>'
                        size_hint_x: .1
                        on_press: root.pls_2(int(count.text), count)
                Label:
                    text: 'Fill=%s' % fill8.active
                    size_hint_x: .2
                Switch:
                    id: fill8
                    size_hint_x: .2
                TextInput:
                    id: hst8
                    text: '127.0.0.1'
                    multiline: False
                    size_hint_x: .2
                    on_text_validate: root.goto_next(prt8)
                TextInput:
                    id: prt8
                    text: '4080'
                    multiline: False
                    size_hint_x: .2
                    on_text_validate: root.goto_next(inc_x1)
            GridLayout:
                cols: 3
                size_hint_y: .1
                Spinner:
                    id: sp15
                    text: 'Sphere'
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                    'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', \
                    'Circle Z', 'Cone Y'
                Spinner:
                    id: sp16
                    text: 'Empty'
                    values: block_list
                Button:
                    id: cmd8
                    text: 'Build It!'
                    on_press: root.ibuild(tix15.text, inc_x1.text, tix16.text, inc_x2.text, \
                    tiy15.text, inc_y1.text, tiy16.text, inc_y2.text, tiz15.text, inc_z1.text, \
                    tiz16.text, inc_z2.text, tirad8.text, inc_rad.text, count.text, sp15.text, \
                    sp16.text, fill8.active, hst8.text, prt8.text)
    TabbedPanelItem:
        text: 'iBuilder 2'
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                cols: 2
                spacing: 2
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'Ctr/X1'
                        size_hint_x: .2
                    TextInput:
                        id: tix17
                        multiline: False
                        size_hint_x: .2
                        text: str(sx17.value)
                        on_text: root.int_set(self, sx17)
                        on_text_validate: root.goto_next(tix18)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns(sx17)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls(sx17)
                    Label:
                        text: 'X1 Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_x3
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(inc_x4)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_x3.text), inc_x3)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_x3.text), inc_x3)
                Slider:
                    id: sx17
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'End/X2'
                        size_hint_x: .2
                    TextInput:
                        id: tix18
                        size_hint_x: .2
                        multiline: False
                        text: str(sx18.value)
                        on_text: root.int_set(self, sx18)
                        on_text_validate: root.goto_next(tiy17)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns(sx18)
                        Button:
                            text: '>'
                            size_hint_x: .1
                            on_press: root.pls(sx18)
                    Label:
                        text: 'X2 Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_x4
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(inc_y3)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_x4.text), inc_x4)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_x4.text), inc_x4)
                Slider:
                    id: sx18
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'Ctr/Y1'
                        size_hint_x: .2
                    TextInput:
                        id: tiy17
                        size_hint_x: .2
                        multiline: False
                        text: str(sy17.value)
                        on_text: root.int_set(self, sy17)
                        on_text_validate: root.goto_next(tiy18)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns(sy17)
                        Button:
                            text: '>'
                            size_hint_x: .1
                            on_press: root.pls(sy17)
                    Label:
                        text: 'Y1 Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_y3
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(inc_y4)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_y3.text), inc_y3)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_y3.text), inc_y3)
                Slider:
                    id: sy17
                    min: 0
                    max: 255
                    step: 1
                    value: 12
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'End/Y2'
                        size_hint_x: .2
                    TextInput:
                        id: tiy18
                        size_hint_x: .2
                        multiline: False
                        text: str(sy18.value)
                        on_text: root.int_set(self, sy18)
                        on_text_validate: root.goto_next(tiz17)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns(sy18)
                        Button:
                            text: '>'
                            size_hint_x: .1
                            on_press: root.pls(sy18)
                    Label:
                        text: 'Y2 Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_y4
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(inc_z3)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_y4.text), inc_y4)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_y4.text), inc_y4)
                Slider:
                    id: sy18
                    min: 0
                    max: 255
                    step: 1
                    value: 12
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'Ctr/Z1'
                        size_hint_x: .2
                    TextInput:
                        id: tiz17
                        size_hint_x: .2
                        multiline: False
                        text: str(sz17.value)
                        on_text: root.int_set(self, sz17)
                        on_text_validate: root.goto_next(tiz18)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns(sz17)
                        Button:
                            text: '>'
                            size_hint_x: .1
                            on_press: root. pls(sz17)
                    Label:
                        text: 'Z1 Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_z3
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(inc_z4)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_z3.text), inc_z3)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_z3.text), inc_z3)
                Slider:
                    id: sz17
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'End/Z2'
                        size_hint_x: .2
                    TextInput:
                        id: tiz18
                        size_hint_x: .2
                        multiline: False
                        text: str(sz18.value)
                        on_text: root.int_set(self, sz18)
                        on_text_validate: root.goto_next(tirad9)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns(sz18)
                        Button:
                            text: '>'
                            size_hint_x: .1
                            on_press: root.pls(sz18)
                    Label:
                        text: 'Z2 Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_z4
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(inc_rad2)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_z4.text), inc_z4)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_z4.text), inc_z4)
                Slider:
                    id: sz18
                    min: -5000
                    max: 5000
                    step: 1
                    value: 0
                GridLayout:
                    cols: 6
                    spacing: 2
                    size_hint_y: .15
                    Label:
                        text: 'Radius'
                        size_hint_x: .2
                    TextInput:
                        id: tirad9
                        size_hint_x: .2
                        multiline: False
                        text: str(srad9.value)
                        on_text: root.int_set(self, srad9)
                        on_text_validate: root.goto_next(hst9)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns(srad9)
                        Button:
                            text: '>'
                            size_hint_x: .1
                            on_press: root.pls(srad9)
                    Label:
                        text: 'Radius Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_rad2
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(count2)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            text: '<'
                            size_hint_x: .1
                            on_press: root.mns_2(int(inc_rad2.text), inc_rad2)
                        Button:
                            text:'>'
                            size_hint_x: .1
                            on_press: root.pls_2(int(inc_rad2.text), inc_rad2)
                Slider:
                    id: srad9
                    min: 0
                    max: 255
                    step: 1
                    value: 12
            GridLayout:
                cols: 7
                spacing: 2
                size_hint_y: .15
                Label:
                    text: 'Count'
                    size_hint_x: .12
                TextInput:
                    id: count2
                    text: str(0)
                    multiline: False
                    size_hint_x: .2
                    on_text_validate: root.goto_next(tix17)
                GridLayout:
                    cols: 2
                    size_hint_x: .1
                    Button:
                        text: '<'
                        size_hint_x: .1
                        on_press: root.mns_c(int(count2.text), count2)
                    Button:
                        text:'>'
                        size_hint_x: .1
                        on_press: root.pls_2(int(count2.text), count2)
                Label:
                    text: 'Fill=%s' % fill9.active
                    size_hint_x: .2
                Switch:
                    id: fill9
                    size_hint_x: .2
                TextInput:
                    id: hst9
                    text: '127.0.0.1'
                    multiline: False
                    size_hint_x: .2
                    on_text_validate: root.goto_next(prt9)
                TextInput:
                    id: prt9
                    text: '4080'
                    multiline: False
                    size_hint_x: .2
                    on_text_validate: root.goto_next(inc_x3)
            GridLayout:
                cols: 3
                size_hint_y: .1
                Spinner:
                    id: sp17
                    text: 'Sphere'
                    values: 'Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', \
                    'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', \
                    'Circle Z', 'Cone Y'
                Spinner:
                    id: sp18
                    text: 'Empty'
                    values: block_list
                Button:
                    id: cmd9
                    text: 'Build It!'
                    on_press: root.ibuild(tix17.text, inc_x3.text, tix18.text, inc_x4.text, \
                    tiy17.text, inc_y3.text, tiy18.text, inc_y4.text, tiz17.text, inc_z3.text, \
                    tiz18.text, inc_z4.text, tirad9.text, inc_rad2.text, count.text, sp17.text, \
                    sp18.text, fill9.active, hst9.text, prt9.text)

""")

def int2(x):
    y = int(float(x))
    return y

def cntr_slider(slider):
        mid = ((slider.max - slider.min) / 2) + slider.min
        return mid

def blkid(sp2):
        if sp2 == '?':
            blk_id = random.randint(0, 23)
        else:
            blk_id = block_list.index(sp2)
        return blk_id

class Test(TabbedPanel):

    def fill_txt(self, label, switch):
        if switch.active == False:
            label.text = 'Hollow'
        elif switch.active == True:
            label.text = 'Filled'
        return label.text

    def goto_next(self, txt_inp):
        txt_inp.focus = True
        txt_inp.select_all()

    def min(self, txt_inp, slider):
        value = int2(txt_inp.text)
        slider.min = value
        slider.value = cntr_slider(slider)

    def max(self, txt_inp, slider):
        value = int2(txt_inp.text)
        slider.max = value
        slider.value = cntr_slider(slider)
        
    def int_set(obj, ti, slider):
        y = int2(ti.text)
        slider.value = y
    
    def pls(self, slider):
        if slider.value < slider.max:
            slider.value += 1
        elif slider.value == slider.max:
            slider.value += 0

    def pls_2(self, value, txt_inp):
        value += 1
        txt_inp.text = str(value)

    def mns(self, slider):
        if slider.value > slider.min:
            slider.value -= 1
        elif slider.value == slider.min:
            slider.value -= 0

    def mns_2(self, value, txt_inp):
        value -= 1
        txt_inp.text = str(value)

    def mns_c(self, value, txt_inp):
        if int2(txt_inp.text) <= 0:
            value -= 0
        else:
            value -=1
        txt_inp.text = str(value)

    def ibuild(self, tix1, inc_x1, tix2, inc_x2, tiy1, inc_y1, \
               tiy2, inc_y2, tiz1, inc_z1, tiz2, inc_z2, tirad, inc_rad, count, sp1, sp2, fill, hst1, prt1):
        blk_id = blkid(sp2)
        client = Client(hst1, int(prt1), USERNAME, IDENTITY_TOKEN)
        x1 = int2(tix1)
        x2 = int2(tix2)
        y1 = int2(tiy1)
        y2 = int2(tiy2)
        z1 = int2(tiz1)
        z2 = int2(tiz2)
        rad = int2(tirad)
        cnt = int2(count)
        xi = int2(inc_x1)
        xxi = int2(inc_x2)
        yi = int2(inc_y1)
        yyi = int2(inc_y2)
        zi = int2(inc_z1)
        zzi = int2(inc_z2)
        radi = int2(inc_rad)
        while cnt > 0:
            if sp1 == 'Up Pyramid':
                client.set_blocks(pyramid(x1, x2, y1, z1, z2, fill), blk_id)
            if sp1 == 'Down Pyramid':
                client.set_blocks(upyramid(x1, x2, y1, z1, z2, fill), blk_id)
            if sp1 == 'Sphere':
                client.set_blocks(sphere(x1, y1, z1, rad, fill), blk_id)
            if sp1 == 'Circle X':
                client.set_blocks(circle_x(x1, y1, z1, rad, fill), blk_id)
            if sp1 == 'Circle Y':
                client.set_blocks(circle_y(x1, y1, z1, rad, fill), blk_id)
            if sp1 == 'Circle Z':
                client.set_blocks(circle_z(x1, y1, z1, rad, fill), blk_id)
            if sp1 == 'Cuboid':
                client.set_blocks(cuboid(x1, x2, y1, y2, z1, z2, fill), blk_id)
            if sp1 == 'Cylinder X':
                client.set_blocks(cylinder_x(x1, x2, y1, z1, rad, fill), blk_id)
            if sp1 == 'Cylinder Y':
                client.set_blocks(cylinder_y(x1, y1, y2, z1, rad, fill), blk_id)
            if sp1 == 'Cylinder Z':
                client.set_blocks(cylinder_z(x1, y1, z1, z2, rad, fill), blk_id)
            if sp1 == 'Cone Y':
                client.set_blocks(cone_y(x1, y1, z1, rad, fill), blk_id)
            cnt -= 1
            x1, x2, y1, y2, z1, z2, rad = x1 + xi, x2 + xxi, y1 + yi, y2 + yyi, \
                                        z1 + zi, z2 + zzi, rad + radi
        time.sleep(3)
            
    def cmd(self, tix1, tix2, tiy1, tiy2, tiz1, \
            tiz2, tirad, sp1, sp2, fill, hst1, prt1):
        blk_id = blkid(sp2)
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
            client.set_blocks(cone_y(int2(tix1), int2(tiy1), \
                                     int2(tiz1), int2(tirad), fill), blk_id)
        if sp1 == 'iBuilder X':
            client.set_blocks(ibuilder_x(int2(tix1), int2(tix2), int2(tirad), int2(tiy1), \
                                     int2(tiy2), int2(tiz1), int2(tiz2), fill), blk_id)
        if sp1 == 'iBuilder Z':
            client.set_blocks(ibuilder_z(int2(tix1), int2(tix2), int2(tiy1), \
                                     int2(tiy2), int2(tiz1), int2(tiz2), int2(tirad), fill), blk_id)
        time.sleep(5)

class ProBuilderApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    ProBuilderApp().run()
