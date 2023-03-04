import math
import random
import sys



class Game:
    def __init__(self, x, y, nbrBlocks):
        self.x = x
        self.y = y
        self.nbrBlocks = nbrBlocks
        self.GameFinish = False
        self.matrix = [[0 for j in range(y)] for i in range(x)]

        global game 
        game = self

        
    def choose(self,choose):
        if choose == 1:
            for i in range(0,(self.x),1):
                for j in range(0,(self.y),1):
                    if i == 0 or j == 0:
                        self.matrix[i][j] = Block([i,j],False)

            for i in range(1,(self.x-10),1):
                for j in range(1,(self.y-1),1):
                        self.matrix[i][j] = Block([i,j],True)
            

    def removeBlock(self, pos):
        self.matrix[pos[0],pos[1]] = None
        self.nbrBlocks -=1

        if self.nbrBlocks <= 0:
            self.GameFinish == True
    
    def GetFroPosition(self, pos):
        return self.matrix[pos[0]][pos[1]]
                

class Block:
    def __init__(self, pos, outLigne):
        self.position = pos
        if outLigne == True:
            self.durte = 1
        else:
            self.durte = sys.maxsize
    
    def hit(self):
        self.durte = self.durte -1

        if self.durte <= 0:
            Game.removeBlock(self.position)



class Ball:
    def __init__(self, pos , direction , speed, size):
        self.position = pos
        self.direction = []
        self.direction[0] = direction[0] 
        self.direction[1] = direction[1] 
        self.speed = speed
        self.size = size
        self.alive = True

    def bouger(self):
        while self.alive:
            positionSuivante = []
            positionSuivante[0] = 1 if self.direction[0] > self.position[0] else -1 if self.direction[0] < self.position[0] else 0
            positionSuivante[1] = 1 if self.direction[1] > self.position[1] else -1 if self.direction[1] < self.position[1] else 0   

            if positionSuivante[0] > game.x:
                self.alive = False
                return

            next = Game.GetFroPosition(game,positionSuivante)

            if next == None:
                self.position = positionSuivante
            else:
                self.changerDirrection()
                Block.hit(next)



    
    def changerDirrection(self, direction_x , direction_y):
        self.direction_x = direction_x
        self.direction_y = direction_y


