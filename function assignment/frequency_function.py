def count_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

string = "hello world"
frequency = count_frequency(string)
print(frequency)