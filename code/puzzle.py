import math
import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
import random
from pygame.time import Clock



class Puzzle():
    def __init__(self, image_file_name, image_size, puzzle_size, pos, show_scramble=False) -> None:
        self.loadedimage = pygame.image.load(f'image.jpg')
        self.loadedimage = pygame.transform.scale(self.loadedimage, image_size)
        
        self.pos = pos
        self.dim = image_size

        self.size = puzzle_size

        self.puzzle = []
        for i in range(puzzle_size[0]):
            self.puzzle.append([])
            for j in range(puzzle_size[1]):
                self.puzzle[i].append((i,j))

        self.void = (puzzle_size[0]-1, puzzle_size[1]-1)
        self.puzzle[self.void[0]][self.void[1]] = (-1,-1)

        self.show_scramble = show_scramble
        self.scramble_moves = 0
        self.moves = [self.move_up, self.move_down, self.move_left, self.move_right]

        self.animating = None
        self.buffer = (0,0)
        self.ANIMATION_SPEED = 0.1

        self.revealing = False
        self.revealing_animation = 0
        self.REVEALING_ANIMATION_SPEED = 10

    def render(self, screen):
        pos = self.pos
        dim = self.dim
        cell_width = dim[0]//self.size[0]
        cell_height = dim[1]//self.size[1]

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.animating == (i,j):
                    screen.blit(self.loadedimage, (pos[0]+i*cell_width + int(self.buffer[0]*cell_width),pos[1]+j*cell_height+int(self.buffer[1]*cell_height)),(self.puzzle[i][j][0]*cell_width,self.puzzle[i][j][1]*cell_height,cell_width, cell_height))
                else:
                    screen.blit(self.loadedimage, (pos[0]+i*cell_width,pos[1]+j*cell_height),(self.puzzle[i][j][0]*cell_width,self.puzzle[i][j][1]*cell_height,cell_width, cell_height))

        for i in range(self.size[0]+1):
            pygame.draw.line(screen,[0]*3, (pos[0]+i*cell_width,pos[1]), (pos[0]+i*cell_width,pos[1]+self.size[1]*cell_height),10)

        for j in range(self.size[1]+1):
            pygame.draw.line(screen,[0]*3, (pos[0],pos[1]+j*cell_height), (pos[0]+self.size[0]*cell_width, pos[1]+j*cell_height),10)

    def reveal(self, screen):
        if self.revealing == False:
            self.revealing = True
            self.revealing_animation = 255

        image = self.loadedimage.copy()
        image.set_alpha(255-self.revealing_animation)
        screen.blit(image,self.pos)

        
    def __reduce_buffer(self):
        if self.buffer[0] > 0:
            self.buffer = (max(0,self.buffer[0]-self.ANIMATION_SPEED), self.buffer[1])

        if self.buffer[0] < 0:
            self.buffer = (min(0,self.buffer[0]+self.ANIMATION_SPEED), self.buffer[1])

        if self.buffer[1] > 0:
            self.buffer = (self.buffer[0], max(0,self.buffer[1]-self.ANIMATION_SPEED))

        if self.buffer[1] < 0:
            self.buffer = (self.buffer[0], min(0,self.buffer[1]+self.ANIMATION_SPEED))

    def move_up(self, animate=True, anim_time=1):
        if self.void[1] < self.size[1]-1:
            self.puzzle[self.void[0]][self.void[1]] = self.puzzle[self.void[0]][self.void[1]+1]
            self.puzzle[self.void[0]][self.void[1]+1] = (-1,-1)
            self.void = (self.void[0],self.void[1]+1)
            if animate:
                self.animating = (self.void[0], self.void[1]-1)
                self.buffer = (0,1*anim_time)
        

    def move_down(self, animate=True, anim_time=1):
        if self.void[1] > 0:
            self.puzzle[self.void[0]][self.void[1]] = self.puzzle[self.void[0]][self.void[1]-1]
            self.puzzle[self.void[0]][self.void[1]-1] = (-1,-1)
            self.void = (self.void[0],self.void[1]-1)
            if animate:
                self.animating = (self.void[0], self.void[1]+1)
                self.buffer = (0,-1*anim_time)

    def move_left(self, animate=True, anim_time=1):
        if self.void[0] < self.size[0]-1:
            self.puzzle[self.void[0]][self.void[1]] = self.puzzle[self.void[0]+1][self.void[1]]
            self.puzzle[self.void[0]+1][self.void[1]] = (-1,-1)
            self.void = (self.void[0]+1,self.void[1])
            if animate:
                self.animating = (self.void[0]-1, self.void[1])
                self.buffer = (1*anim_time,0)

    def move_right(self, animate=True,anim_time=1):
        if self.void[0] > 0:
            self.puzzle[self.void[0]][self.void[1]] = self.puzzle[self.void[0]-1][self.void[1]]
            self.puzzle[self.void[0]-1][self.void[1]] = (-1,-1)
            self.void = (self.void[0]-1,self.void[1])
            if animate:
                self.animating = (self.void[0]+1, self.void[1])
                self.buffer = (-1*anim_time,0)

    def is_solved(self, animate=True):
        if self.scramble_moves > 0:
            return False
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.puzzle[i][j] != (-1,-1) and self.puzzle[i][j] != (i,j):
                   return False
        return True

    def update(self):
        if self.animating != None:
            self.__reduce_buffer()
            if self.buffer == (0,0):
                self.animating = None
        elif self.scramble_moves > 0:
            self.scramble()
        elif self.revealing:
            if self.revealing_animation > 0:
                self.revealing_animation = max(0, self.revealing_animation - self.REVEALING_ANIMATION_SPEED)

    def moves_allowed(self):
        if self.scramble_moves > 0:
            return False
        if self.animating != None:
            return False
        if self.is_solved():
            return False
        return True

    def scramble(self):
        if self.scramble_moves == 0:
            self.scramble_moves = random.randint(self.size[0]*self.size[1]**2, self.size[0]*self.size[1]**3)
        
        if self.show_scramble:
            random.choice(self.moves)(True, 0.001)
            self.scramble_moves -=1
        else:
            for i in range(self.scramble_moves):
                random.choice(self.moves)(False)
            self.scramble_moves = 0


