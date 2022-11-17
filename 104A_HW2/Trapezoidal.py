#%{
#   TRAPAZOID COMPOSITE RULE 
#       sigma       
#           sums f(x) at x = a+ih 1 -> n-1
#       Trap
#           h * (sigma(n-1) + (f(b) + f(a)) / 2)
#}

class Trap:

    def __init__(self,a,b,n,f):
        self.a = a
        self.b = b
        self.n = n
        self.f = f
        self.h = (b-a)/n

    def sigma(self,end):
            return sum(self.f(self.a+i*self.h) for i in range(1,int(end)))

    def Trap(self):
        return self.h*(self.sigma(self.n-1)+(self.f(self.b)+self.f(self.a))/2)




