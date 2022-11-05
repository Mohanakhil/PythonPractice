import random


class Otp:
    @staticmethod
    def generate_otp(length):
        otp = ""
        for i in range(0, length):
            list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.choice(list_of_numbers)
            y = random.randrange(0, 9)
            otp = otp + str(y)
        return otp


length = int(input("enter length of password you want"))
print("otp generated is " + Otp.generate_otp(length))
