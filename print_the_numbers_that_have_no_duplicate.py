number_list = []
for i in range(0,10):
    numbers = int(input(f"Enter number {i+1}: "))
    number_list.append(numbers)

result = []
for number_count in number_list:
    if number_list.count(number_count) == 1:
        result.append(number_count)
print(result)