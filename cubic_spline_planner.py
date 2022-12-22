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

        self.a = [iy for iy in y]


        # calc coefficient c 

        A = self.__calc_A(h)
        B = self.__calc_B(h,self.a)
        


        

def CubicSpline2D:

    def __init(self,x,y):
        self.s = self.calc_S(x,y)
        self.sx =  CubicSpline1D(self.s,x)
        self.sy = CubicSpline1D(self.s,y)



    def __calc_s(self,x,y):

        dx = np.diff(x)
        dy = np.diff(y)
        self.ds =  np.hypot(dx,dy)
        s = [0]
        s.extend(np.cumsum(self.ds))
        return s
