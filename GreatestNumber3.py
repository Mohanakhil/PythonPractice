class GreatestNumber:
    @staticmethod
    def greatest_number_in_list(numbers_list):
        maximum = numbers_list[0]
        for i in range(1, len(numbers_list)):
            if numbers_list[i] > maximum:
                maximum = numbers_list[i]
        return maximum


n = int(input("enter no of elements in list"))
list_of_numbers = []
for i in range(0, n):
    list_of_numbers.append(int(input("enter now")))

print("max out of all is"+str(GreatestNumber.greatest_number_in_list(list_of_numbers)))
