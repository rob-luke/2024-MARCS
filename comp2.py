
def do_stuff(t):
    # Convert to F
    x = t * 1.8 + 32
    # Get diff from normal body temp
    y = x - 98.6
    # Convert back to C
    z = (y - 32) / 1.8
    return z

# Example usage:
result = do_stuff(37)
print(result)


def celsius_to_fahrenheit(celsius_temp):
    FAHRENHEIT_MULTIPLIER = 1.8
    FAHRENHEIT_OFFSET = 32
    return (celsius_temp * FAHRENHEIT_MULTIPLIER) + FAHRENHEIT_OFFSET

def calculate_celsius_difference_from_body_temp(patient_temp_celsius):
    NORMAL_BODY_TEMP_FAHRENHEIT = 98.6
    
    patient_temp_fahrenheit = celsius_to_fahrenheit(patient_temp_celsius)
    temp_difference_fahrenheit = patient_temp_fahrenheit - NORMAL_BODY_TEMP_FAHRENHEIT
    
    CELSIUS_MULTIPLIER = 1/1.8
    return (temp_difference_fahrenheit - FAHRENHEIT_OFFSET) * CELSIUS_MULTIPLIER

# Example usage:
patient_temp = 37
temp_difference = calculate_celsius_difference_from_body_temp(patient_temp)
print(temp_difference)
