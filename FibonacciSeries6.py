class Fibonacci:
    @staticmethod
    def fibonacci(length):
        first = 1
        second = 1
        print(str(first)+" "+str(second),end=" ")
        for i in range(length - 2):
            third = first + second
            first = second
            second = third
            print(str(third),end=" ")


length = int(input("enter length of fibonacci series you want"))
Fibonacci.fibonacci(length)
