class PrimeNumber:
    @staticmethod
    def is_prime(n):
        count = 0
        for i in range(2, n + 1):
            if n % i == 0:
                count = count + 1
        print("count is "+str(count))
        if count == 1:
            print(str(n) + " is prime no")
        else:
            print(str(n) + " is odd no")


x = int(input("enter any no\n"))
PrimeNumber.is_prime(x)
