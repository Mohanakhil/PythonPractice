class PrimeNo:
    def __init__(self):
        PrimeNo.x = 100

    def m1(self):
        PrimeNo.y = 120

    @classmethod
    def m2(cls):
        cls.z = 300
        cls.a = 400

    @staticmethod
    def m3():
        PrimeNo.h = 890


p = PrimeNo()
p.m1()
PrimeNo.m2()
PrimeNo.m3()
print(PrimeNo.__dict__)
