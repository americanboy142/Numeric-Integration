#%{
#   SIMPSONS RULE
#       sigma
#           sum of f(x)
#               x = a - h + 2ih 
#               or
#               x = a + 2ih
#               depending on call
#
#       simpsons
#           h/3 * (f(a) + f(b) + 4(sigma(n/2,a-h)) + 2(sigma(n-2/2,a)))
#
#}

class simpsons_rule:
    
    def __init__(self,a,b,n,func):
        self.a = a
        self.b = b
        self.n = n
        self.h = (self.b-self.a)/self.n
        self.f = func
        pass
    
    # will replace both sums
    # input: (upper bound i.e.(n/2,(n-2)/2), special: alows return to very)
    def sigma(self,end,special):
        return sum(self.f(special+2*i*self.h) for i in range(1,int(end)))

    def simpsons(self):
        return self.h / 3 * ((self.f(self.a) + self.f(self.b)) + 4 * self.sigma(self.n / 2,self.a - self.h)+ 2 * self.sigma((self.n - 2) / 2,self.a))


