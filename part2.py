class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return divider / denominator
        except ZeroDivisionError:
            return f"Division by zero is not allowed"


print(DivisionByNull.divide_by_null(int(input("Input divider ")), int(input("Input denominator "))))
