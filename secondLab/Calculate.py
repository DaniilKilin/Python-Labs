class Calculate:
    def __init__(self, res=0):
        self.result = res

    def plus(self, a=None, b=0):
        if a is None:
            self.result = self.result + b
        if a is not None:
            self.result =  a + b
        return self.result

    def minus(self, a=None, b=0):
        if a is None:
            self.result = self.result - b
        if a is not None:
            self.result = a - b
        return self.result

    def multiply(self, a=None, b=0):
        if a is None:
            self.result = self.result * b
        if a is not None:
            self.result = a * b
        return self.result

    def divide(self, a=None, b=1):
        if b!=0:
            if a is None:
                self.result = self.result / b
                return self.result
            if a is not None:
                self.result = a / b
                return self.result
        return "Нельзя делить на 0"