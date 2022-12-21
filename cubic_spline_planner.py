import math
import numpy as np
import bisect

class CubicSpline1D:

    def __init__(self,x,y):

        h = np.diff(x)
        # x is an array np.diff gives difference of successive elements

        if np.any( h< 0):
            raise ValueError("x coordinates must be sorted in ascending order")
            #  np.any gives true/false 

        self.a , self.b , self.c , self.d = [],[], [],[]
        self.x = x
        self.yy =y 
        self.nx = len(x)

        #calc coefficient a

        self.a = [[iy for iy in y]]