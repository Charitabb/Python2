class Monomial:
    def __init__(self, a, k=[]):
        self.a = a
        self.k = k
    
    def ismonomial(self):
        x = 0
        if len(self.k) > 0:
            for i in range(len(self.k)):
                if self.k[i] > 0 and type(self.k[i]) is int:
                    x += 1
            return x == len(self.k)
        else:
            return False
            
    
    def highest(self):
        if self.ismonomial() is True:
            return max(self.k)
        else:
            return None
                

    def iscoefficient(self):
        return len(self.k) == 0
    

    def variable(self):
        return len(self.k)
    
    def __str__(self):
        index = 0
        result = str(self.a)
        for i in range(len(self.k)):
            result += f"x_{index}"
            if self.k[index] > 1:
                result += f"^{self.k[index]}"
            index += 1
        return result



my_list = [27,35,6]
mymonomial = Monomial(-5, my_list)
print(mymonomial.ismonomial())
print(mymonomial.highest())
print(mymonomial.iscoefficient())
print(mymonomial.variable())
print(mymonomial.__str__())