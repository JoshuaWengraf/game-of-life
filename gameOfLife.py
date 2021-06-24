# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 12:46:20 2021

Conways Game of Life simulation. Outputs each stage of the simulation as an image. The rules of the simulation are: 

Each grid cell can be in one of two possible states: live or dead
 
(1) Any live cell with zero or one neighbors dies, as if by solitude.

(2) Any live cell with two or three live neighbours lives on

(3) Any live cell with more than three live neighbours dies, as if by overcrowding

(4) Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction



@author: Joshua Wengraf.
"""

import numpy as np
import matplotlib.pyplot as plt
        
def neighboursCount(i,j, grid):    
    
    neighbours = 0
    
    steps_x = [-1, 0, 1]
    steps_y = [-1, 0, 1]
    
    for step_x in steps_x:
        for step_y in steps_y:
            if step_x != 0 or step_y != 0:
                if grid[i + step_x, j + step_y] == True:
                    neighbours = neighbours + 1
            
    return neighbours;


def addGlider(i,j, grid):
    
    grid[i,j] = 1
    grid[i,j+1] = 1
    grid[i,j+2] = 1
    grid[i+1,j+2] = 1
    grid[i+2,j+1] = 1

def addBeeHive(i, j, grid):
    
    grid[i+3,j] = 1
    grid[i+2,j-1] = 1
    grid[i+2,j+1] = 1
    grid[i+1,j-1] = 1
    grid[i+1,j+1] = 1
    grid[i,j] = 1
    
    
gridSize = 15
    
grid = np.zeros([gridSize+1, gridSize+1])

addGlider(9,5, grid)
addBeeHive(11,2, grid)

Number_of_iterations = 40
for iteration in range(0, Number_of_iterations):
    
    newGridPoints = []
    deadGridPoints = []
    
    for i in range(0, gridSize):
        for j in range(0, gridSize):
            if grid[i,j] == 1: # if cell is live
                if neighboursCount(i,j, grid) < 2: 
                    deadGridPoints.append([i,j])
            
                if neighboursCount(i,j, grid) > 3:
                    deadGridPoints.append([i,j])
        
            if grid[i,j] == 0: #if cell is dead
                if neighboursCount(i,j, grid) == 3:
                    newGridPoints.append([i,j])
                    
    for newGridPoint in newGridPoints:
        i_new, j_new = newGridPoint
        grid[i_new, j_new] = 1
        
    for deadGridPoint in deadGridPoints:
        i_new, j_new = deadGridPoint
        grid[i_new, j_new] = 0
    
    fig = plt.figure()       
    plt.imshow(grid)
    plt.xticks([])
    plt.yticks([])
    plt.savefig('gameOfLife' + str(iteration) + '.png')
    plt.close(fig)
            
    print(iteration)
   
print('program completed') 
       
                     
