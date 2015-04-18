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
    
    def start(self):
        for i in self.mapArray:
            if i==0 or i==len(self.mapArray)-1:
                for j in i:
                    if j=='o':
                        return (i,j)
            else:
                if i[0]=='o' or i[len(j)-1]=='o':
                    return (i,j)
                    
    #def check(self,preX,preY,curX,curY):
    #    locL=[(curX-1,curY-1),(curX,curY-1),(curX+1,curY-1),(curX-1,curY),(curX+1,curY),
    #    (curX-1,curY+1),(curX,curY+1),(curX+1,curY+1)]
    #    for i in locL:
    #        if i[0]>=0 and i[0]<=len(self.mapArray)-1 and i[1]
    #            if i[0]!=preX and i[1]!=preY:
    #            
        
            