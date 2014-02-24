import kivy
kivy.require('1.7.2')
import sys
import datetime
import time
import random

from builder import *
from functools import partial
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_string("""

<ProTab>:
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
                        values: root.objects
                    Spinner:
                        id: sp2
                        text: 'Empty'
                        values: root.block_list
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
                        values: root.objects
                    Spinner:
                        id: sp4
                        text: 'Empty'
                        values: root.block_list
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
                        values: root.objects
                    Spinner:
                        id: sp6
                        text: 'Empty'
                        values: root.block_list
    TabbedPanelItem:
        text: 'BitMapper'
        BoxLayout:
            orientation: 'vertical'
            padding: 5
            spacing: 5
            GridLayout:
                rows: 2
                spacing: 4
                size_hint_y: .55
                Label:
                    text: 'Design'
                    size_hint_y: .05
                TextInput:
                    id: map1
                    multiline: True
                    on_text_validate: root.goto_next(char1)
            GridLayout:
                size_hint_y: .2
                cols: 6
                spacing: 4
                TextInput:
                    id: char1
                    multiline: False
                    hint_text: 'Character 1 Block'
                    on_text_validate: root.goto_next(char2)
                Spinner:
                    id: char1spn
                    values: root.block_list
                    text: 'Empty'
                TextInput:
                    id: char2
                    multiline: False
                    hint_text: 'Character 2 Block'
                    on_text_validate: root.goto_next(char3)
                Spinner:
                    id: char2spn
                    values: root.block_list
                    text: 'Empty'
                TextInput:
                    id: char3
                    multiline: False
                    hint_text: 'Character 3 Block'
                    on_text_validate: root.goto_next(char4)
                Spinner:
                    id: char3spn
                    values: root.block_list
                    text: 'Empty'
                TextInput:
                    id: char4
                    multiline: False
                    hint_text: 'Character 4 Block'
                    on_text_validate: root.goto_next(char5)
                Spinner:
                    id: char4spn
                    values: root.block_list
                    text: 'Empty'
                TextInput:
                    id: char5
                    multiline: False
                    hint_text: 'Character 5 Block'
                    on_text_validate: root.goto_next(char6)
                Spinner:
                    id: char5spn
                    values: root.block_list
                    text: 'Empty'
                TextInput:
                    id: char6
                    multiline: False
                    hint_text: 'Character 6 Block'
                    on_text_validate: root.goto_next(char7)
                Spinner:
                    id: char6spn
                    values: root.block_list
                    text: 'Empty'
                TextInput:
                    id: char7
                    multiline: False
                    hint_text: 'Character 7 Block'
                    on_text_validate: root.goto_next(char8)
                Spinner:
                    id: char7spn
                    values: root.block_list
                    text: 'Empty'
                TextInput:
                    id: char8
                    multiline: False
                    hint_text: 'Character 8 Block'
                    on_text_validate: root.goto_next(char9)
                Spinner:
                    id: char8spn
                    values: root.block_list
                    text: 'Empty'
                TextInput:
                    id: char9
                    multiline: False
                    hint_text: 'Character 9 Block'
                    on_text_validate: root.goto_next(char10)
                Spinner:
                    id: char9spn
                    values: root.block_list
                    text: 'Empty'
                TextInput:
                    id: char10
                    multiline: False
                    hint_text: 'Character 10 Block'
                    on_text_validate: root.goto_next(char11)
                Spinner:
                    id: char10spn
                    values: root.block_list
                    text: 'Empty'
                TextInput:
                    id: char11
                    multiline: False
                    hint_text: 'Character 11 Block'
                    on_text_validate: root.goto_next(char12)
                Spinner:
                    id: char11spn
                    values: root.block_list
                    text: 'Empty'
                TextInput:
                    id: char12
                    multiline: False
                    hint_text: 'Character 12 Block'
                    on_text_validate: root.goto_next(dirx1)
                Spinner:
                    id: char12spn
                    values: root.block_list
                    text: 'Empty'
            GridLayout:
                size_hint_y: .1
                cols: 12
                spacing: 4
                Label:
                    text: 'DirX1'
                TextInput:
                    id: dirx1
                    multiline: False
                    text: '0'
                    on_text_validate: root.goto_next(diry1)
                Label:
                    text: 'DirY1'
                TextInput:
                    id: diry1
                    multiline: False
                    text: '0'
                    on_text_validate: root.goto_next(dirz1)
                Label:
                    text: 'DirZ1'
                TextInput:
                    id: dirz1
                    multiline: False
                    text: '0'
                    on_text_validate: root.goto_next(dirx2)
                Label:
                    text: 'DirX2'
                TextInput:
                    id: dirx2
                    multiline: False
                    text: '0'
                    on_text_validate: root.goto_next(diry2)
                Label:
                    text: 'DirY2'
                TextInput:
                    id: diry2
                    multiline: False
                    text: '0'
                    on_text_validate: root.goto_next(dirz2)
                Label:
                    text: 'DirZ2'
                TextInput:
                    id: dirz2
                    multiline: False
                    text: '0'
                    on_text_validate: root.goto_next(cx)
                Label:
                    text: 'Start X'
                TextInput:
                    id: cx
                    text: '0'
                    multiline: False
                    on_text_validate: root.goto_next(cy)
                Label:
                    text: 'Start Y'
                TextInput:
                    id: cy
                    text: '0'
                    multiline: False
                    on_text_validate: root.goto_next(cz)
                Label:
                    text: 'Start Z'
                TextInput:
                    id: cz
                    text: '0'
                    multiline: False
                    on_text_validate: root.goto_next(hstb)
                Label:
                    text: 'Host'
                TextInput:
                    id: hstb
                    text: '127.0.0.1'
                    multiline: False
                    on_text_validate: root.goto_next(prtb)
                Label:
                    text: 'Port'
                TextInput:
                    id: prtb
                    text: '4080'
                    multiline: False
                    on_text_validate: root.goto_next(char1)
                Label:
                    text: ''
                Button:
                    id: bcmd
                    text: 'Print'
                    on_press: root.prnt(map1, char1.text, char2.text, \
                    char3.text, char4.text, char5.text, char6.text, char7.text, \
                    char8.text, char9.text, char10.text, char11.text, \
                    char12.text, cx.text, cy.text, cz.text, dirx1.text, \
                    diry1.text, dirz1.text, dirx2.text, diry2.text, dirz2.text, \
                    char1spn.text, char2spn.text, char3spn.text, char4spn.text, \
                    char5spn.text, char6spn.text, char7spn.text, char8spn.text, \
                    char9spn.text, char10spn.text, char11spn.text, \
                    char12spn.text, hstb.text, prtb.text)
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
                            id: btn_mx15
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_mx15, sx15)
                        Button:
                            id: btn_px15
                            text:'>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_px15, sx15)
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
                            id: btn_mx16
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_mx16, sx16)
                        Button:
                            id: btn_px16
                            text: '>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_px16, sx16)
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
                            id: btn_my15
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_my15, sy15)
                        Button:
                            id: btn_py15
                            text: '>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_py15, sy15)
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
                            id: btn_my16
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_my16, sy16)
                        Button:
                            id: btn_py16
                            text: '>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_py16, sy16)
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
                            id: btn_mz15
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_mz15, sz15)
                        Button:
                            id: btn_pz15
                            text: '>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_pz15, sz15)
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
                            id: btn_mz16
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_mz16, sz16)
                        Button:
                            id: btn_pz16
                            text: '>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_pz16, sz16)
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
                        on_text_validate: root.goto_next(count)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            id: btn_mrad8
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_mrad8, srad8)
                        Button:
                            id: btn_prad8
                            text: '>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_prad8, srad8)
                    Label:
                        text: 'Radius Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_rad
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(swx1)
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
                cols: 2
                spacing: 4
                size_hint_y: .15
                GridLayout:
                    cols: 3
                    size_hint_x: .25
                    Label:
                        text: 'Count'
                        size_hint_x: .4
                    TextInput:
                        id: count
                        text: str(0)
                        multiline: False
                        size_hint_x: .4
                        on_text_validate: root.goto_next(inc_x1)
                    GridLayout:
                        cols: 2
                        size_hint_x: .2
                        Button:
                            text: '<'
                            on_press: root.mns_c(int(count.text), count)
                        Button:
                            text:'>'
                            on_press: root.pls_2(int(count.text), count)
                GridLayout:
                    cols: 9
                    spacing: 4
                    size_hint_y: .15
                    size_hint_x: .75
                    GridLayout:
                        rows: 2
                        size_hint_x: .096
                        Label:
                            text: 'X-Z Switch'
                        Label:
                            text: 'Interval'
                    TextInput:
                        id: swx1
                        text: str(0)
                        multiline: False
                        size_hint_x: .099
                        on_text_validate: root.goto_next(swy1)
                    GridLayout:
                        cols: 2
                        size_hint_x: .0489
                        Button:
                            text: '<'
                            on_press: root.mns_c(int(swx1.text), swx1)
                        Button:
                            text:'>'
                            on_press: root.pls_2(int(swx1.text), swx1)
                    GridLayout:
                        rows: 2
                        size_hint_x: .098
                        Label:
                            text: 'Y Switch'
                        Label:
                            text: 'Interval'
                    TextInput:
                        id: swy1
                        text: str(0)
                        multiline: False
                        size_hint_x: .096
                        on_text_validate: root.goto_next(swr1)
                    GridLayout:
                        cols: 2
                        size_hint_x: .05
                        Button:
                            text: '<'
                            on_press: root.mns_c(int(swy1.text), swy1)
                        Button:
                            text:'>'
                            on_press: root.pls_2(int(swy1.text), swy1)
                    GridLayout:
                        rows: 2
                        size_hint_x: .098
                        Label:
                            text: 'Rad Switch'
                        Label:
                            text: 'Interval'
                    TextInput:
                        id: swr1
                        text: str(0)
                        multiline: False
                        size_hint_x: .096
                        on_text_validate: root.goto_next(invx)
                    GridLayout:
                        cols: 2
                        size_hint_x: .05
                        Button:
                            text: '<'
                            on_press: root.mns_c(int(swr1.text), swr1)
                        Button:
                            text:'>'
                            on_press: root.pls_2(int(swr1.text), swr1)
            GridLayout:
                cols: 7
                spacing: 2
                size_hint_y: .15
                GridLayout:
                    rows: 2
                    size_hint_x: .079
                    Label:
                        text: 'X-Z +/-'
                    Label:
                        text: 'Interval'
                TextInput:
                    id: invx
                    text: str(0)
                    multiline: False
                    size_hint_x: .08
                    on_text_validate: root.goto_next(hst8)
                GridLayout:
                    cols: 2
                    size_hint_x: .039
                    Button:
                        text: '<'
                        on_press: root.mns_c(int(invx.text), invx)
                    Button:
                        text:'>'
                        on_press: root.pls_2(int(invx.text), invx)
                Label:
                    text: 'Fill=%s' % fill8.active
                    size_hint_x: .1
                Switch:
                    id: fill8
                    size_hint_x: .1
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
                    on_text_validate: root.goto_next(tix15)
            GridLayout:
                cols: 3
                size_hint_y: .1
                Spinner:
                    id: sp15
                    text: 'Sphere'
                    values: root.objects
                Spinner:
                    id: sp16
                    text: 'Empty'
                    values: root.block_list
                Button:
                    id: cmd8
                    text: 'Build It!'
                    on_press: root.ibuild(tix15.text, inc_x1.text, tix16.text, \
                    inc_x2.text, tiy15.text, inc_y1.text, tiy16.text, \
                    inc_y2.text, tiz15.text, inc_z1.text, tiz16.text, \
                    inc_z2.text, tirad8.text, inc_rad.text, count.text, \
                    swx1.text, swy1.text, swr1.text, invx.text, sp15.text, \
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
                            id: btn1
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn1, sx17)
                        Button:
                            id: btn2
                            text:'>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn2, sx17)
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
                            id: btn_mx18
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_mx18, sx18)
                        Button:
                            id: btn_px18
                            text: '>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_px18, sx18)
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
                            id: btn_my17
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_my17, sy17)
                        Button:
                            id: btn_py17
                            text: '>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_py17, sy17)
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
                            id: btn_my18
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_my18, sy18)
                        Button:
                            id: btn_py18
                            text: '>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_py18, sy18)
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
                            id: btn_mz17
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_mz17, sz17)
                        Button:
                            id: btn_pz17
                            text: '>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_pz17, sz17)
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
                            id: btn_mz18
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_mz18, sz18)
                        Button:
                            id: btn_pz18
                            text: '>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_pz18, sz18)
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
                        on_text_validate: root.goto_next(count2)
                    GridLayout:
                        cols: 2
                        size_hint_x: .1
                        Button:
                            id: btn_mrad9
                            text: '<'
                            size_hint_x: .1
                            on_press: root.ival('down', btn_mrad9, srad9)
                        Button:
                            id: btn_prad9
                            text: '>'
                            size_hint_x: .1
                            on_press: root.ival('up', btn_prad9, srad9)
                    Label:
                        text: 'Radius Inc'
                        size_hint_x: .2
                    TextInput:
                        id: inc_rad2
                        text: str(0)
                        multiline: False
                        size_hint_x: .2
                        on_text_validate: root.goto_next(swx)
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
                cols: 2
                spacing: 4
                size_hint_y: .15
                GridLayout:
                    cols: 3
                    size_hint_x: .25
                    Label:
                        text: 'Count'
                        size_hint_x: .4
                    TextInput:
                        id: count2
                        text: str(0)
                        multiline: False
                        size_hint_x: .4
                        on_text_validate: root.goto_next(inc_x3)
                    GridLayout:
                        cols: 2
                        size_hint_x: .2
                        Button:
                            text: '<'
                            on_press: root.mns_c(int(count2.text), count2)
                        Button:
                            text:'>'
                            on_press: root.pls_2(int(count2.text), count2)
                GridLayout:
                    cols: 9
                    spacing: 4
                    size_hint_y: .15
                    size_hint_x: .75
                    GridLayout:
                        rows: 2
                        size_hint_x: .096
                        Label:
                            text: 'X-Z Switch'
                        Label:
                            text: 'Interval'
                    TextInput:
                        id: swx
                        text: str(0)
                        multiline: False
                        size_hint_x: .099
                        on_text_validate: root.goto_next(swy)
                    GridLayout:
                        cols: 2
                        size_hint_x: .0489
                        Button:
                            text: '<'
                            on_press: root.mns_c(int(swx.text), swx)
                        Button:
                            text:'>'
                            on_press: root.pls_2(int(swx.text), swx)
                    GridLayout:
                        rows: 2
                        size_hint_x: .098
                        Label:
                            text: 'Y Switch'
                        Label:
                            text: 'Interval'
                    TextInput:
                        id: swy
                        text: str(0)
                        multiline: False
                        size_hint_x: .096
                        on_text_validate: root.goto_next(swr)
                    GridLayout:
                        cols: 2
                        size_hint_x: .05
                        Button:
                            text: '<'
                            on_press: root.mns_c(int(swy.text), swy)
                        Button:
                            text:'>'
                            on_press: root.pls_2(int(swy.text), swy)
                    GridLayout:
                        rows: 2
                        size_hint_x: .098
                        Label:
                            text: 'Rad Switch'
                        Label:
                            text: 'Interval'
                    TextInput:
                        id: swr
                        text: str(0)
                        multiline: False
                        size_hint_x: .096
                        on_text_validate: root.goto_next(inx1)
                    GridLayout:
                        cols: 2
                        size_hint_x: .05
                        Button:
                            text: '<'
                            on_press: root.mns_c(int(swr.text), swr)
                        Button:
                            text:'>'
                            on_press: root.pls_2(int(swr.text), swr)
            GridLayout:
                cols: 7
                spacing: 2
                size_hint_y: .15
                GridLayout:
                    rows: 2
                    size_hint_x: .079
                    Label:
                        text: 'X-Z +/-'
                    Label:
                        text: 'Interval'
                TextInput:
                    id: inx1
                    text: str(0)
                    multiline: False
                    size_hint_x: .08
                    on_text_validate: root.goto_next(hst9)
                GridLayout:
                    cols: 2
                    size_hint_x: .039
                    Button:
                        text: '<'
                        on_press: root.mns_c(int(inx1.text), inx1)
                    Button:
                        text:'>'
                        on_press: root.pls_2(int(inx1.text), inx1)
                Label:
                    text: 'Fill=%s' % fill9.active
                    size_hint_x: .1
                Switch:
                    id: fill9
                    size_hint_x: .1
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
                    on_text_validate: root.goto_next(tix17)
            GridLayout:
                cols: 3
                size_hint_y: .1
                Spinner:
                    id: sp17
                    text: 'Sphere'
                    values: root.objects
                Spinner:
                    id: sp18
                    text: 'Empty'
                    values: root.block_list
                Button:
                    id: cmd9
                    text: 'Build It!'
                    on_press: root.ibuild(tix17.text, inc_x3.text, tix18.text, \
                    inc_x4.text, tiy17.text, inc_y3.text, tiy18.text, \
                    inc_y4.text, tiz17.text, inc_z3.text, tiz18.text, \
                    inc_z4.text, tirad9.text, inc_rad2.text, count2.text, \
                    swx.text, swy.text, swr.text, inx1.text, sp17.text, \
                    sp18.text, fill9.active, hst9.text, prt9.text)

""")

def mns1(btn, slider, dt):
    if slider.value > slider.min:
        slider.value -= 1
    elif slider.value == slider.min:
        slider.value -= 0
        return False
    if btn.state == 'normal':
        return False

def pls1(btn, slider, dt):
    if slider.value < slider.max:
        slider.value += 1
    elif slider.value == slider.max:
        slider.value += 0
        return False
    if btn.state == 'normal':
        return False

def int2(string_obj):
    number = int(float(string_obj))
    return number

def cntr_slider(slider):
        mid = ((slider.max - slider.min) / 2) + slider.min
        return mid

def get_blk_id(blk_name):
        if blk_name == '?':
            blk_id = random.randint(0, 23)
        else:
            blk_id = Test.block_list.index(blk_name)
        return blk_id


class ProTab(TabbedPanel):

    objects = ['Sphere', 'Up Pyramid', 'Down Pyramid', 'Cuboid', 'Cylinder X',
               'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', 'Circle Z',
               'Cone Y']

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

    def fill_txt(self, label, switch):
        if switch.active == False:
            label.text = 'Hollow'
        elif switch.active == True:
            label.text = 'Filled'
        return label.text

    def prnt(self, bitmap, char1, char2, char3, char4, char5, char6, char7,
             char8, char9, char10, char11, char12, pos_x, pos_y, pos_z, dir_x,
             dir_y, dir_z, dir_xx, dir_yy, dir_zz, char_blk1, char_blk2,
             char_blk3, char_blk4, char_blk5, char_blk6, char_blk7, char_blk8,
             char_blk9, char_blk10, char_blk11, char_blk12, host, port):
        client = Client(host, int2(port))
        chars = [char1, char2, char3, char4, char5, char6, char7, char8, char9,
                 char10, char11, char12]
        blks = [get_blk_id(char_blk1), get_blk_id(char_blk2),
                get_blk_id(char_blk3), get_blk_id(char_blk4),
                get_blk_id(char_blk5), get_blk_id(char_blk6),
                get_blk_id(char_blk7), get_blk_id(char_blk8),
                get_blk_id(char_blk9), get_blk_id(char_blk10),
                get_blk_id(char_blk11), get_blk_id(char_blk12)]
        pattern = bitmap.text.splitlines(True)
        blk_assnmnt = dict(zip(chars, blks))
        client.bitmap(int2(pos_x), int2(pos_y), int2(pos_z), (int2(dir_x),
                        int2(dir_y), int2(dir_z)), (int2(dir_xx), int2(dir_yy),
                        int2(dir_zz)), pattern, blk_assnmnt)
        time.sleep(3)

    def goto_next(self, txt_inp):
        txt_inp.focus = True
        txt_inp.select_all()

    def min(self, txt_inp, slider):
        slider.min = int2(txt_inp.text)
        slider.value = cntr_slider(slider)

    def max(self, txt_inp, slider):
        slider.max = int2(txt_inp.text)
        slider.value = cntr_slider(slider)

    def int_set(self, txt_inp, slider):
        slider.value = int2(txt_inp.text)

    def pls(self, slider):
        if slider.value < slider.max:
            slider.value += 1
        elif slider.value == slider.max:
            slider.value += 0

    def mns(self, slider):
        if slider.value > slider.min:
            slider.value -= 1
        elif slider.value == slider.min:
            slider.value -= 0

    def pls_2(self, value, txt_inp):
        value += 1
        txt_inp.text = str(value)

    def mns_2(self, value, txt_inp):
        value -= 1
        txt_inp.text = str(value)

    def mns_c(self, value, txt_inp):
        if int2(txt_inp.text) <= 0:
            value -= 0
        else:
            value -=1
        txt_inp.text = str(value)

    def ival(self, direction, btn, slider):
        if direction == 'down':
            Clock.schedule_interval(partial(mns1, btn, slider), 1 / 12.)
        if direction == 'up':
            Clock.schedule_interval(partial(pls1, btn, slider), 1 / 12.)

    def ibuild(self, txt_inp_x1, inc_x1, txt_inp_x2, inc_x2, txt_inp_y1, inc_y1,
               txt_inp_y2, inc_y2, txt_inp_z1, inc_z1, txt_inp_z2, inc_z2,
               txt_inp_rad, inc_rad, cnt, swxz, swy, swr, inv_xz, fnc_spnr,
               blk_spnr, fill, host, port):
        blk_id = get_blk_id(blk_spnr)
        client = Client(host, int(port)) 
        x1, x2, y1, y2, z1, z2, rad = int2(txt_inp_x1), int2(txt_inp_x2), \
        int2(txt_inp_y1), int2(txt_inp_y2), int2(txt_inp_z1), \
        int2(txt_inp_z2), int2(txt_inp_rad)
        count = int2(cnt)
        xi = int2(inc_x1)
        xxi = int2(inc_x2)
        yi = int2(inc_y1)
        yyi = int2(inc_y2)
        zi = int2(inc_z1)
        zzi = int2(inc_z2)
        radi = int2(inc_rad)
        switch_x_z = int2(swxz)
        switch_y = int2(swy)
        switch_rad = int2(swr)
        invert_x_z = int2(inv_xz)
        now = datetime.datetime.utcnow()
        history_list = '<|_Start_|>', str(now), 'Obj_________'+str(fnc_spnr), \
                       'Blk-Type____'+str(blk_spnr), 'Fill________'+str(fill), \
                       'X1__________'+str(x1), 'X1 Inc______'+str(xi), \
                       'X2__________'+str(x2), 'X2 Inc______'+str(xxi), \
                       'Y1__________'+str(y1), 'Y1 Inc______'+str(yi), \
                       'Y2__________'+str(y2), 'Y2 Inc______'+str(yyi), \
                       'Z1__________'+str(z1), 'Z1 Inc______'+str(zi), \
                       'Z2__________'+str(z2), 'Z2 Inc______'+str(zzi), \
                       'Radius______'+str(rad), 'Radius Inc__'+str(radi), \
                       'Count_______'+str(cnt), 'X-Z Switch__'+str(switch_x_z), \
                       'Y-Switch____'+str(switch_y), \
                       'Invrt X-Z___'+str(invert_x_z), \
                       'Rad Switch__'+str(switch_rad), \
                       'Host________'+host, 'Port________'+port, \
                       '<|_End_|>', '============================'
        log = open("log.txt", "a")
        for items in history_list:
            log.write(items+'\n')
        log.close()
        first = True
        while count > 0:
            if invert_x_z != 0:
                if first == False:
                    if count % invert_x_z == 0:
                        xi, xxi, zi, zzi = xi - (xi+xi), xxi - (xxi+xxi), \
                                           zi - (zi+zi), zzi - (zzi+zzi)
                else:
                    pass
            if switch_x_z != 0:
                if first == False:
                    if count % switch_x_z == 0:
                        xi, xxi, zi, zzi = zi, zzi, xi, xxi
                else:
                    pass
            if switch_y != 0:
                if first == False:
                    if count % switch_y == 0:
                        yi, yyi = yi - yi*2, yyi - yyi*2
                else:
                    pass
            if switch_rad != 0:
                if first == False:
                    if count % switch_rad == 0:
                        radi = radi - radi*2
                else:
                    pass
            if fnc_spnr == 'Up Pyramid':
                client.set_blocks(pyramid(x1, x2, y1, z1, z2, fill), blk_id)
            elif fnc_spnr == 'Down Pyramid':
                client.set_blocks(upyramid(x1, x2, y1, z1, z2, fill), blk_id)
            elif fnc_spnr == 'Sphere':
                client.set_blocks(sphere(x1, y1, z1, rad, fill), blk_id)
            elif fnc_spnr == 'Circle X':
                client.set_blocks(circle_x(x1, y1, z1, rad, fill), blk_id)
            elif fnc_spnr == 'Circle Y':
                client.set_blocks(circle_y(x1, y1, z1, rad, fill), blk_id)
            elif fnc_spnr == 'Circle Z':
                client.set_blocks(circle_z(x1, y1, z1, rad, fill), blk_id)
            elif fnc_spnr == 'Cuboid':
                client.set_blocks(cuboid(x1, x2, y1, y2, z1, z2, fill), blk_id)
            elif fnc_spnr == 'Cylinder X':
                client.set_blocks(cylinder_x(x1, x2, y1, z1, rad, fill), blk_id)
            elif fnc_spnr == 'Cylinder Y':
                client.set_blocks(cylinder_y(x1, y1, y2, z1, rad, fill), blk_id)
            elif fnc_spnr == 'Cylinder Z':
                client.set_blocks(cylinder_z(x1, y1, z1, z2, rad, fill), blk_id)
            elif fnc_spnr == 'Cone Y':
                client.set_blocks(cone_y(x1, y1, z1, rad, fill), blk_id)
            count -= 1
            x1, x2, y1, y2, z1, z2, rad, first = x1 + xi, x2 + xxi, y1 + yi, \
                                                 y2 + yyi, z1 + zi, z2 + zzi, \
                                                 rad + radi, False
        time.sleep(3)
    def cmd(self, txt_inp_x1, txt_inp_x2, txt_inp_y1, txt_inp_y2, txt_inp_z1,
            txt_inp_z2, txt_inp_rad, fnc_spnr, blk_spnr, fill, host, port):
        blk_id = get_blk_id(blk_spnr)
        client = Client(host, int(port))
        if fnc_spnr == 'Up Pyramid':
            client.set_blocks(pyramid(int2(txt_inp_x1), int2(txt_inp_x2), \
                                      int2(txt_inp_y1), int2(txt_inp_z1), \
                                      int2(txt_inp_z2), fill), blk_id)
        elif fnc_spnr == 'Down Pyramid':
            client.set_blocks(upyramid(int2(txt_inp_x1), int2(txt_inp_x2), \
                                       int2(txt_inp_y1), int2(txt_inp_z1), \
                                       int2(txt_inp_z2), fill), blk_id)
        elif fnc_spnr == 'Sphere':
            client.set_blocks(sphere(int2(txt_inp_x1), int2(txt_inp_y1), \
                                     int2(txt_inp_z1), int2(txt_inp_rad), \
                                     fill), blk_id)
        elif fnc_spnr == 'Circle X':
            client.set_blocks(circle_x(int2(txt_inp_x1), int2(txt_inp_y1), \
                                       int2(txt_inp_z1), int2(txt_inp_rad), \
                                       fill), blk_id)
        elif fnc_spnr == 'Circle Y':
            client.set_blocks(circle_y(int2(txt_inp_x1), int2(txt_inp_y1), \
                                       int2(txt_inp_z1), int2(txt_inp_rad), \
                                       fill), blk_id)
        elif fnc_spnr == 'Circle Z':
            client.set_blocks(circle_z(int2(txt_inp_x1), int2(txt_inp_y1), \
                                       int2(txt_inp_z1), int2(txt_inp_rad), \
                                       fill), blk_id)
        elif fnc_spnr == 'Cuboid':
            client.set_blocks(cuboid(int2(txt_inp_x1), int2(txt_inp_x2), \
                                     int2(txt_inp_y1), int2(txt_inp_y2), \
                                     int2(txt_inp_z1), int2(txt_inp_z2), \
                                     fill), blk_id)
        elif fnc_spnr == 'Cylinder X':
            client.set_blocks(cylinder_x(int2(txt_inp_x1), int2(txt_inp_x2), \
                                         int2(txt_inp_y1), int2(txt_inp_z1), \
                                         int2(txt_inp_rad), fill), blk_id)
        elif fnc_spnr == 'Cylinder Y':
            client.set_blocks(cylinder_y(int2(txt_inp_x1), int2(txt_inp_y1), \
                                         int2(txt_inp_y2), int2(txt_inp_z1), \
                                         int2(txt_inp_rad), fill), blk_id)
        elif fnc_spnr == 'Cylinder Z':
            client.set_blocks(cylinder_z(int2(txt_inp_x1), int2(txt_inp_y1), \
                                         int2(txt_inp_z1), int2(txt_inp_z2), \
                                         int2(txt_inp_rad), fill), blk_id)
        elif fnc_spnr == 'Cone Y':
            client.set_blocks(cone_y(int2(txt_inp_x1), int2(txt_inp_y1), \
                                     int2(txt_inp_z1), int2(txt_inp_rad), \
                                     fill), blk_id)
        time.sleep(3)

class ProBuilderApp(App):
    def build(self):
        return ProTab()

if __name__ == '__main__':
    ProBuilderApp().run()
