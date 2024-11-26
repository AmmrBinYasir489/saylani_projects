def key_with_highest_value(d):
    if not d:
        return None

    highest_key = None
    highest_value = float('1') 

    for key in d:
        if d[key] > highest_value:
            highest_value = d[key]
            highest_key = key

    return highest_key
sample_dict = {'a': 10, 'b': 25, 'c': 22, 'd': 20}
print(f"The key with the highest value is: {key_with_highest_value(sample_dict)}")
