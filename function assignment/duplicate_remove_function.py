def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = [1, 2, 3, 2, 4, 1, 5]
print(f"List after removing duplicates: {remove_duplicates(my_list)}")