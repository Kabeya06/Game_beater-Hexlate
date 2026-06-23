pip install kivy

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label

import json

class wheel:
    colours {
    'up' : ''
    'up_right' : ''
    'up_left' : ''
    'down' : ''
    'down_right' : ''
    'down_left' : ''
    }

    previous_state = dict()




'''

Goals

    collect game data a) assign colours numerical values b) asign positional data c) grab screen data from game

    spin wheels a) use kivy to make ui

    move wheels

'''
