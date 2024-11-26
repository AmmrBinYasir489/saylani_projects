def number_list(list):
    largest = list[0]
    for number in list:
        if number > largest:
            largest = number
    return largest

lists = [10, 100, 60, 10]
number_list(lists)
print(f"thr greater number is {number_list(lists)}")