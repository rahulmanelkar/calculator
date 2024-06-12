class BasicCalculator:
    def __init__(self) -> None:
        self.previous_result = 0
        self._op1 = self._op2 = 0

    def add(self, a,b):
        self._op1 = a
        self._op2 = b
        self.previous_result = self._op1+self._op2
        return self.previous_result

    def subtract(self, a,b):
        self._op1 = a
        self._op2 = b
        self.previous_result =  self._op1 - self._op2
        return self.previous_result
    
    def return_previous(self):
        return self.previous_result
    

def main():
    pass