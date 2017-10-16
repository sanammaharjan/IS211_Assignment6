def convertCelsiusToKelvin(number):
    '''
    It converts given celsius value to kelvin
    :param number: Celsius number in float
    :return: Converted Kelvin value in float
    '''
    given_number = float(number)
    default_kelvin = float(273.15)
    c_value = round(given_number + default_kelvin, 5)
    # print c_value
    return c_value

def convertCelsiusToFahrenheit(number):
    '''
    It converts given celsius value to Fahrenheit
    :param number: Celcius number in float
    :return: Converted Fahrenheit value in float
    '''
    given_number = float(number)
    default_fahrenheit = float(32)
    c_value = round((given_number * 9 /5) + default_fahrenheit, 5)
    # print c_value
    return c_value

def convertFahrenheitToCelsius(number):
    '''
    It converts given Fahrenheit to celsius
    :param number: Fahrenheit number in float
    :return: Converted Celsisu value in float
    '''
    given_number = float(number)
    default_Celsius = float(32)
    c_value = round((given_number - default_Celsius) * 5/9, 5)
    # print c_value
    return c_value

def convertFahrenheitToKelvin(number):
    '''
    It converts given Fahrenheit to Kelvin
    :param number: Fahrenheit number in float
    :return: Converted Kelvin value in float
    '''
    given_number = float(number)
    default_kelvin = float(459.67)
    c_value = round((given_number + default_kelvin) * 5/9, 5)
    # print c_value
    return c_value

def convertKelvinToFahrenheit(number):
    '''
    It converts given Kelvin to Fahrenheit
    :param number: Kelvin value in float
    :return: Converted Fahrenheit value in float
    '''
    given_number = float(number)
    defualt_fahrenheit = float(459.67)
    c_value = round((given_number * 9/5) - defualt_fahrenheit, 5)
    # print c_value
    return c_value


convertCelsiusToKelvin(300.111)
convertCelsiusToFahrenheit(300.45778)
convertFahrenheitToCelsius(36.9)
convertFahrenheitToKelvin(200.1)
convertKelvinToFahrenheit(25.36)