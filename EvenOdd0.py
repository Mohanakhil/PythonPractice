class MyClass:
    def __init__(self, x):
        self.x = x

    # instance method
    def check_evenodd(self):
        if self.x % 2 == 0:
            print("even")
        else:
            print("odd")


n = int(input("enter any no"))
m1 = MyClass(n)
m1.check_evenodd()
