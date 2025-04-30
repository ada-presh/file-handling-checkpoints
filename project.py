import math

class Calculator:
    def __init__(self):
        # Initialize dictionary with basic operations
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': self.safe_divide
        }

    def safe_divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return x / y

    def add_operation(self, symbol, function):
        self.operations[symbol] = function

    def calculate(self, num1, op, num2=None):
        try:
            if not isinstance(num1, (int, float)):
                raise ValueError("First input is not a number.")
            if num2 is not None and not isinstance(num2, (int, float)):
                raise ValueError("Second input is not a number.")
            if op not in self.operations:
                raise ValueError(f"Invalid operation symbol: {op}")
            
            func = self.operations[op]
            if num2 is not None:
                return func(num1, num2)
            else:
                return func(num1)
        except Exception as e:
            print("Error:", e)
            raise

# Advanced operations
def exponentiation(x, y):
    return math.pow(x, y)

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)

def logarithm(x):
    if x <= 0:
        raise ValueError("Cannot compute logarithm of non-positive number.")
    return math.log(x)

# Main program
if __name__ == "__main__":
    calc = Calculator()

    # Add advanced operations
    calc.add_operation('^', exponentiation)
    calc.add_operation('sqrt', square_root)
    calc.add_operation('log', logarithm)

    while True:
        print("\nAvailable operations: +, -, *, /, ^, sqrt, log")
        op = input("Enter operation (or 'exit' to quit): ").strip()
        if op.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = None

            if op not in ['sqrt', 'log']:
                num2 = float(input("Enter the second number: "))

            result = calc.calculate(num1, op, num2)
            print(f"Result: {result}")

        except Exception:
            print("Calculation failed. Please try again.")
