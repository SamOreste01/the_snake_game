from cProfile import label
from tabnanny import check
from tkinter import *
import random
from webbrowser import Elinks

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = '#ADD8E6'
FOOD_COLOR = '#FF0000'
BACKGROUND_COLOR = '#000000'

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag ='snake')
            self.squares.append(square)

