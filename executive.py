from calculator import Calculator

class Executive:

    def __init__(self):
        self.my_calc = Calculator()
    def print_menu(self):
        print(
    '''
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Power
    6. Percentage
    7. Factorial
    8. Fibonacci
    9. Exit
    '''
        )
    def get_two_numbers(self):
        user_a = float(input('Enter a: '))
        user_b = float(input('Enter b: '))
        return user_a, user_b
    def run(self):
        try:
            while True:
                self.print_menu()
                user_input = int(input("Enter a choice: "))
                match user_input:
                    case 1:
                        self.get_two_numbers()
                        self.my_calc.add(user_a, user_b)
                    case 2:
                        user_a = float(input('Enter a: ')) 
                        user_b = float(input('Enter b: '))
                        self.my_calc.subtract(user_a, user_b)
                    case 3:
                        user_a = float(input('Enter a: ')) 
                        user_b = float(input('Enter b: '))
                        self.my_calc.multiply(user_a, user_b)
                    case 4:
                        user_a = float(input('Enter a: ')) 
                        user_b = float(input('Enter b: '))
                        self.my_calc.divide(user_a, user_b)
                    case 5:
                        user_a = float(input('Enter a: ')) 
                        user_b = float(input('Enter b: '))
                        self.my_calc.power(user_a, user_b)
                    case 6:
                        user_a = float(input('Enter a: ')) 
                        user_b = float(input('Enter b: '))
                        self.my_calc.percentage_of_b(user_a, user_b)
                    case 7:
                        user_a = float(input('Enter a: ')) 
                        self.my_calc.factorial(user_a)
                    case 8:
                        user_a = float(input('Enter a: ')) 
                        self.my_calc.fibonacci(user_a)
                    case 9:
                        print('Exiting...')
                        break
                    case _:
                        print('Invalid choice .')
        except ZeroDivisionError:
            print('Cannot divide by zero')
        except ValueError:
            print('Cannot do the fib/factorial of a negative number')


    