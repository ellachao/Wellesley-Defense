import os
from models import enemy_test

class Map:
    def __init__(self):
        self.mapArray=[]
        self.read()
        
    def read(self):
        charmap=open('map.txt','r')
        lines=charmap.readlines()
        for line in lines:
            self.mapArray.append(list(line.strip()))

        