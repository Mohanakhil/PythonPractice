class Reverse:
    @staticmethod
    def reverse_string(given):
        string_to_list = list(given)
        for i in range(0, (len(string_to_list) // 2)):
            l = len(given)
            temp = string_to_list[i]
            string_to_list[i] = string_to_list[l - 1 - i]
            string_to_list[l - 1 - i] = temp
        reversed_string = ""
        reversed_string = reversed_string.join(string_to_list)
        return reversed_string


class Reverse2:
    @staticmethod
    def reverse2(given_string):
        reversed = ""
        for i in given_string:
            reversed = i + reversed
        return reversed


x = input("enter a string\n")
# print(Reverse.reverse_string(x))
print(Reverse2.reverse2(x))
