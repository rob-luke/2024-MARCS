
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




# BAD CODE VERSION
# This code converts temps and does some calculations

def do_stuff(t):
    # Convert to F
    x = t * 1.8 + 32
    # Get diff from normal body temp
    y = x - 98.6
    # Convert back to C
    z = (y - 32) / 1.8
    return z

# Example usage:
# temp = 37
# result = do_stuff(temp)
# print(result)


# CLEAN CODE VERSION
def celsius_to_fahrenheit(celsius_temp):
    """Convert Celsius temperature to Fahrenheit.
    
    Args:
        celsius_temp (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
        
    Raises:
        ValueError: If input is not a valid number
    """
    if not isinstance(celsius_temp, (int, float)):
        raise ValueError("Temperature must be a number")
    if celsius_temp != celsius_temp:  # Check for NaN
        raise ValueError("Temperature cannot be NaN")
        
    FAHRENHEIT_MULTIPLIER = 1.8
    FAHRENHEIT_OFFSET = 32
    return (celsius_temp * FAHRENHEIT_MULTIPLIER) + FAHRENHEIT_OFFSET

def calculate_celsius_difference_from_body_temp(patient_temp_celsius):
    """Calculate the difference between patient temperature and normal body temperature.
    
    Args:
        patient_temp_celsius (float): Patient's temperature in Celsius
        
    Returns:
        float: Temperature difference in Celsius
        
    Raises:
        ValueError: If input is not a valid number
    """
    if not isinstance(patient_temp_celsius, (int, float)):
        raise ValueError("Temperature must be a number")
    if patient_temp_celsius != patient_temp_celsius:  # Check for NaN
        raise ValueError("Temperature cannot be NaN")
    
    NORMAL_BODY_TEMP_FAHRENHEIT = 98.6
    FAHRENHEIT_OFFSET = 32
    CELSIUS_MULTIPLIER = 1/1.8
    
    patient_temp_fahrenheit = celsius_to_fahrenheit(patient_temp_celsius)
    temp_difference_fahrenheit = patient_temp_fahrenheit - NORMAL_BODY_TEMP_FAHRENHEIT
    
    return (temp_difference_fahrenheit - FAHRENHEIT_OFFSET) * CELSIUS_MULTIPLIER

# Example usage:
# try:
#     patient_temp = 37
#     temp_difference = calculate_celsius_difference_from_body_temp(patient_temp)
#     print(temp_difference)
# except ValueError as e:
#     print(f"Error: {e}")
