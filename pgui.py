'''
code file: pgui.py
date: June 2022
comments:
    displays mouse position and color at pointer on screen
    With pgui.py in focus
    user presses 'Enter' to update the output
'''
from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
import os, sys
from tkinter.font import Font
import time
import pyautogui
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        self.style = Style()

        root.geometry("170x75")

        self.vlbl_screen = StringVar()
        lbl_screen = Label(self, text='', textvariable=self.vlbl_screen)
        lbl_screen.grid(row=1, column=1, sticky='ew')

        self.vlbl_position = StringVar()
        lbl_position = Label(self, text='', textvariable=self.vlbl_position)
        lbl_position.grid(row=2, column=1, sticky='ew')

        self.vent_color = StringVar()
        self.ent_color = Entry(self, textvariable=self.vent_color)
        self.ent_color.grid(row=3, column=1, sticky='ew')

        self.process_position()
        root.bind("<Return>", self.process_position)


    def rgb_to_hex(self, rgb):
        return '%02x%02x%02x' % rgb


    def process_position(self, event=None):
        SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
        MOUSE_X, MOUSE_Y = pyautogui.position()
        PIXEL = pyautogui.screenshot(
            region=(
                MOUSE_X, MOUSE_Y, 1, 1
            )
        )
        COLOR = PIXEL.getcolors()
        HEXCOLOR = "#" + self.rgb_to_hex(COLOR[0][1]).upper()
        self.vlbl_screen.set(f"Screen: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.vlbl_position.set(f"Mouse: x={MOUSE_X} y={MOUSE_Y}")
        self.vent_color.set(f"Color: {HEXCOLOR}")
        self.style.configure("TEntry", background=HEXCOLOR) # global


root = ThemedTk(theme="scidblue")

# change working directory to path for this file
p = os.path.realpath(__file__)
os.chdir(os.path.dirname(p))

root.title("pgui")
root.resizable(0, 0) # no resize & removes maximize button
root.attributes("-topmost", True)  # Keep on top of other windows
app = Application(root)
app.mainloop()
