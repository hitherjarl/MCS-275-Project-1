"""
* Author: Mohamed Imran Mohamed Siddique 
* Created on: 09/29/18                            
* netID: isiddi5
* Class: MCS275 Lab: Tuesday 12PM                             
"""


import random
import matplotlib.pyplot as plt

class Dice:

    def __init__(self, min, max):
        # the least number the dice could be
        self.min = min
        # the higest number the dice could be
        self.max = max

    def __repr__(self):
        # returns a rand number as a string
        return "%s" % random.randint(self.min, self.max)

class Sierpinski:

    def __init__(self, coor, itera, curx, cury):
        # variable for the vertexs [[0,0],[20,20],[40,0]]
        self.coor = coor
        # the number of iterations which is 1000
        self.itera = itera
        # the initial srating point for x
        self.curx = curx
        # the initial starting point for y
        self.cury = cury

    def generate_data(self):
        #a list where all the generated coordinates will be saved at
        points = []

        # initial point
        curx, cury = (1,1)
        #move the point into the list
        points.append((curx, cury))

        for i in range(self.itera):
            #calls the Dice class
            t = Dice(1,6)
            #sets each output from Dice into w
            w = repr(t)
            if (w == str("1")):
                #if w is 1, then it picks vertex [0,0]
                vertx, verty = self.coor[0]
                #uses the cureent x and y, finds the midpoint using the function x = (vertexx + x) /2.0
                curx = (vertx + curx) / 2.0
                #same goes for y, finds the midpoint using the function y = (vertexy + y) /2.0
                cury = (verty + cury) / 2.0
                points.append((curx, cury))
            elif (w == str("2")):
                vertx, verty = self.coor[0]
                curx = (vertx + curx) / 2.0
                cury = (verty + cury) / 2.0
                points.append((curx, cury))
            elif (w == str("3")):
                vertx, verty = self.coor[1]
                curx = (vertx + curx) / 2.0
                cury = (verty + cury) / 2.0
                points.append((curx, cury))
            elif (w == str("4")):
                vertx, verty = self.coor[1]
                curx = (vertx + curx) / 2.0
                cury = (verty + cury) / 2.0
                points.append((curx, cury))
            elif (w == str("5")):
                vertx, verty = self.coor[2]
                curx = (vertx + curx) / 2.0
                cury = (verty + cury) / 2.0
                points.append((curx, cury))
            else:
                vertx, verty = self.coor[2]
                curx = (vertx + curx) / 2.0
                cury = (verty + cury) / 2.0
                points.append((curx, cury))
        #set coordinates variable as points to pass into the plot_data method
        self.coor = points

    def plot_data(self):
        px = [x for (x, y) in self.coor]
        py = [y for (x, y) in self.coor]
        #plots all the data that was saved in list points and returns a plot
        plt.plot(px, py, 'r.')
        return plt.show()


s = Sierpinski([[0,0],[20,20],[40,0]], 1000, 1, 1)
s.generate_data()
s.plot_data()