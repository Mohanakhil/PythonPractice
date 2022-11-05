class Factorial:
    @staticmethod
    def factorial(n):
        fact = 1
        while n > 0:
            fact = fact * n
            n = n - 1
        return fact


x = int(input("enter no"))
print(Factorial.factorial(x))
