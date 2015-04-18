import os
from models import enemy_test

class Map:
    def __init__(self):
        self.mapArray=[]
        self.read()
        self.mapWidth = len(self.mapArray[0])
        print self.mapWidth
        self.mapHeight = len(self.mapArray)
        print self.mapHeight
        
    def read(self):
        charmap=open('map.txt','r')
        lines=charmap.readlines()
        for line in lines:
            self.mapArray.append(list(line.strip()))
    
    def start(self):
        startPos=[]
        for i in range(len(self.mapArray)):
            for j in range(len(self.mapArray[i])):
                if self.mapArray[i][j]=='o':
                    if i==0 or i==len(self.mapArray)-1 or j==0 or j==len(self.mapArray[i])-1:
                        startPos.append((i,j))
        return startPos
                    
    def check(self,preX,preY,curX,curY):
        locL=[(curX-1,curY-1),(curX,curY-1),(curX+1,curY-1),(curX-1,curY),(curX+1,curY),
        (curX-1,curY+1),(curX,curY+1),(curX+1,curY+1)]
        number=-1
        place=None
        for i in locL:
            if i[0]>=0 and i[0]<=len(self.mapArray[0])-1 and i[1]>=0 and i[1]<=len(self.mapArray)-1:
                if i[0]!=preX or i[1]!=preY:
                    if self.mapArray[i[1]][i[0]]>=number:
                        number=self.mapArray[i[1]][i[0]]
                        place=i
        return place
                
    def reach(self,curX,curY):
        for i in range(len(self.mapArray)):
            for j in range(len(self.mapArray[i])):
                if self.mapArray[i][j]=='p':
                    if curY==i and curX==j:
                        return True
                    else:
                        return False
            