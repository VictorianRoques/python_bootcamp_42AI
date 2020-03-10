class Vector:
    def __init__(self, values):
        if type(values) is list:
            self.values = values
            self.size = len(values)
        elif type(values) is int:
            self.size = values
            self.values = []
            size = values
            x = float(0)
            while size > 0:
                size = size - 1
                self.values.append(x)
                x = x + 1
        elif type(values) is tuple:
            self.values = []
            self.size = values[1] - values[0]
            size = self.size
            if self.size <= 0:
                return (print("Len is negative or nul"))
            x = float(values[0])
            while size > 0:
                size = size - 1
                self.values.append(x)
                x = x + 1

    def __add__(self, vector_y):
        if (self.size  == vector_y.size):
            return (Vector(list(map(lambda x, y: x + y, self.values, vector_y.values))))
        else:
            return (print("ERROR vector have not the same sizes"))

    def __radd__(self, vector_y):
        return (self.__add__(vector_y))
    
    def __sub__(self, vector_y):
        if (self.size  == vector_y.size):
            return (Vector(list(map(lambda x, y: x - y, self.values, vector_y.values))))
        else:
            return (print("ERROR vector have not the same sizes"))
    def __rsub__(self, vector_y):
        return (self.__rsub__(vector_y))
    
    def __truediv__(self, other):
        for x in self.values:
            if x == 0:
                return ("ERROR div by 0 imposible")
        return (Vector(list(map(lambda x: x / other, self.values))))
    
    def __rtruediv__(self, other):
        return(self.__truediv__(other))
    
    def __mul__(self, other):
        if type(other) is Vector:
            if self.size == other.size:
                return (sum(list(map(lambda x, y: x * y, self.values, other.values))))
            else:
                return (print("ERROR"))
        return (Vector(list(map(lambda x: x * other, self.values))))

    def __rmul__(self, Vector):
        self.__mul__(other)
    
    def __str__(self):
        return ("{}".format(self.values))
    
    def __repr__(self):
        return ("{}".format(self.values))