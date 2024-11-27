def temp_convert(temp, scale):
    if scale == 'F':
        return (temp * 9/5) + 32
    elif scale == 'C':
        return (temp - 32) * 5/9
    else:
        return None
    
celsius_temp = 25
fahrenheit_temp = temp_convert(celsius_temp, 'F')
print(f"celsius temperature {celsius_temp} in fahrenheit is {fahrenheit_temp}")

fahrenheit_temp = 77
celsius_temp = temp_convert(fahrenheit_temp, 'C')
print(f"celsius temperature {fahrenheit_temp} in fahrenheit is {celsius_temp}")