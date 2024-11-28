def flattened_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list
    
nest_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(f"list after flattening = {flattened_list(nest_list)}")