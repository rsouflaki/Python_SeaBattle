import random
import os
from SeaBattle import Position

BOARDSIZE = 10
OFFSET = 10
counter = 0
BOATSIZES = [5, 4, 3 ,3, 2]



def tellUser(question):
    print question

def getReply():
    return raw_input()    


    


def getRandomPosition(maxlimit):
    row = random.randint(0, maxlimit - 1)
    column = random.randint(0, maxlimit - 1)
    return Position.Position(row, column)


def getRandomOrientation():
    orientation = {0:'North', 1:'East', 2:'South', 3:'West'}
    i = random.randint(0, 3)
    return orientation[i]