class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError('You can\'t divide by zero.')
        else:
            return a / b
        
    def power(self, a: float, b: float) -> float:
        return a ** b
    
    def percentage_of_b(self, a: float, b: float) -> float:
        return (a/100) * b
    
    def factorial(self, a: int) -> int:
        if a < 0:
            raise ValueError('Unable to do factorial of negative number')
        else:
            return self.__rec_fact(a)
    
    def __rec_fact(self, a: int) -> int:
        """"""
        if a == 0:
            return 1
        if a == 1:
            return 1
        else:
            return a * self.__rec_fact(a-1)
    
    def fibonacci(self, a: int) -> int:
        if a < 0:
            raise ValueError('Unable to do find fibbonaci  of negative number')
        else:
            return self.__rec_fib(a)
        
    def __rec_fib(self, a: int) -> int:
        if a == 0:
            return 0
        if a == 1:
            return 1
        else:
            return self.__rec_fib(a-2) + self.__rec_fib(a-1)
