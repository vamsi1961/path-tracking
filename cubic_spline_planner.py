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
        self.c = np.linalg.solve(A,B)

        for i in range(self.nx -1):
            d = (self.c[i+1] - self.c[i])/(3.0 * h[i])
            b = 1/h[i] * (self.a[i+1] - self.a[i]) - h[i]/3.0*(2.0 * self.c[i] + self.c[i+1])

            self.b.append(b)
            self.d.append(d)
        
    def calc_position(self,x):

        if x < self.x[0]:
            return None
        
        elif x > self.x[-1]:
            return None

        i = self.__search_index(x)
        dx = x - self.x[i]

        position = self.a[i] + self.b[i]*dx + self.c[i]*dx**2.0 + self.d[i]*dx**3.0

        return position


    def calc_first_derivatiove(self,x):

        if x < self.x[0]:
            return None
    
        elif x > self.x[-1]:
            return None

        i = self.__search_index(x)
        dx = x - self.x[i]

        dy = self.b[i] + 2.0*self.c[i]*dx + self.d[i] * dx**2.0

        return dy


    def calc_second_derivative(self,x):

        if x < self.x[0]:
            return None
        elif x > self.x[-1]:
            return None

        i = self.__search_index(x)
        dx = x - self.x[i]
        ddy = 2.0 * self.c[i] + 6.0 * self.d[i] * dx
        return ddy

    def __calc_A(self,h):

        A = np.zeros((self.nx , self.nx))

        A[0,0] = 1.0

        for i in range(self.nx - 1):
            if i != (self.nx - 2):
                A[i+1,i+1] = 2.0*(h[i] + h[i+1])

            A[i+1 , i] = h[i]
            A[i, i+1]  = h[i]

        A[0,1] = 0.0
        A[self.nx - 1 , self.nx -2] = 0.0
        A[self.nx - 1, self.nx-1] = 1.0

        return A

    def __calc_B(self,h,a):

        B = np.zeros(self.nx)
        for i in range(self.nx - 2):

            B[i+1] = 3.0*(a[i+2] - a[i+1]) / h[i+1] - 3.0*(a[i+1] - a[i])/h[i]

        return B



class CubicSpline2D:

    def __init__(self,x,y):

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

    def calc_position(self , s):

        x = self.sx.calc_position(s)
        x = self.sy.calc_position(s)

        return x,y

    def calc_curvature(self ,s):

        dx = self.sx.calc_first_derivatiove(s)
        ddx = self.sx.calc_second_derivative(s)
        dy = self.sy.calc_first_derivatiove(s)
        ddy  = self.sy.calc_second_derivative(s)

        k = (ddy*dx  - ddx*dy) / (dx**2 + dy**2)**1.5

        return k


    def calc_yaw(self , s):

        dx = self.sx.calc_first_derivatiove(s)
        dy = self.sy.calc_first_derivatiove(s)

        yaw = math.atan2(dy,dx)

        return yaw

    
def calc_spline_course(x,y,ds =0.1):

    sp = CubicSpline2D(x,y)

    s = list(np.arange(0,sp.s[-1] , ds)) 

    rx,ry,ryaw,rk = [],[],[],[]

    for i_S in s:
        

    



    