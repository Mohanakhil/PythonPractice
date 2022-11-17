class LengthOfGivenString:
    @staticmethod
    def calculate_length(input_string):
        count = 0
        for _ in input_string:
            count += 1
        return count

s = input("enter any string\n")
print(LengthOfGivenString.calculate_length(s))
