#%{
#   GAUSSIAN QUAD WITH 3 NODES
#       __init__
#           hard codes weights and x
#               x = nodes for integral -1 to 1
#       xn(a,b)
#           converts x into 3 nodes for an integral a,b
#               xn = (b+a)/2 + (b-a)*x/2
#       sigma(0,n)
#           sigma sum ( w*f(xn) )
#       G3
#           thing = aproximation
#           tn = xn(c + ih ,c + (i+1)h)
#           main
#               (c + (i+1)h - c + ih) / 2 * (sigma(n,tn)
#}

import functions as fc
from numpy import array as numar
class G3:
    def __init__(self,c,d,i,f):
        self.c = c
        self.d = d
        self.change = 1
        self.n = 3
        self.i = i
        self.f = f
        self.h = (d-c)/i
        self.wn = [5/9,8/9,5/9]
        self.x = numar([-(3/5)**(1/2),0,(3/5)**(1/2)])
    
    def xn(self,a,b):
        xn = self.x
        xn = (b+a)/2 + (b-a)*self.x/2
        return xn

    def sigma(self,end,xn):
            return sum(self.wn[i] * self.f(xn[i]) for i in range(int(end)))
    
    def G3(self):
        thing = 0
        for itter in range(self.i):
            tn = self.xn(self.c + self.h*itter,self.c + self.h*(itter+1))
            thing += ((self.c + self.h*(itter+1))-(self.c + self.h*itter))/2 * self.sigma(self.n,tn)
        return thing
    
