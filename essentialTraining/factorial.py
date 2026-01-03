class Factorial:
    def __init__(self, n):
        self.number = self.factorial(n)
        print("Factorial initialized")

    def factorial(self, n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

    def fact(self):
        print(f"factorial print check {self.number}")

check = Factorial(5)
check.fact()