import unittest

class ConversionNotPossible(Exception):
    def __init__(self, msg):
        self.msg = "Please check both units, conversion is not possible."

def convert(fromUnit, toUnit, value):
    ftempConverter = False
    ttempConverter = False
    fMilessConverter = False
    tMilessConverter = False
    if fromUnit == 'Celsius' or fromUnit == 'Kelvin' or fromUnit == 'Fahrenheit':
       ftempConverter = True
    if toUnit == 'Celsius' or toUnit == 'Kelvin' or toUnit == 'Fahrenheit':
        ttempConverter = True
    if fromUnit == 'Meters' or fromUnit == 'Yards' or fromUnit == 'Miles':
        fMilessConverter = True
    if toUnit == 'Meters' or toUnit == 'Yards' or toUnit == 'Miles':
        tMilessConverter = True

    if ftempConverter and ttempConverter or fMilessConverter and tMilessConverter:
        if fromUnit == 'Celsius':
            if toUnit == 'Fahrenheit':
                output = round(float((value * 9.0 / 5.0) + 32),2)
                return output
            elif toUnit == 'Kelvin':
                output = round(float(value + 273.15),2)
                return output
            elif toUnit == 'Celsius':
                output = float(value)
                return output
        elif fromUnit == 'Kelvin':
            if toUnit == 'Celsius':
                output = round(float(value - 273.15),2)
                return output
            elif toUnit == 'Fahrenheit':
                output = round(float((value * 9.0 / 5.0 ) - 459.67),2)
                return output
            elif toUnit == 'Kelvin':
                output = float(value)
                return output
        elif fromUnit == 'Fahrenheit':
            if toUnit == 'Celsius':
                output = round(float((value - 32) * 5.0 / 9.0),2)
                return output
            elif toUnit == 'Kelvin':
                output = round(float((value + 459.67) * 5.0 / 9.0 ),2)
                return  output
            elif toUnit == 'Fahrenheit':
                output = float(value)
                return output
        elif fromUnit == 'Miles':
            if toUnit == 'Yards':
                output = round(float(value * 1760.0),2)
                # print output
                return output
            elif toUnit == 'Meters':
                output = round(float(value / 0.00062137),2)
                # print output
                return output
            elif toUnit == 'Miles':
                output = round(float(value),2)
                # print output
                return output
        elif fromUnit == 'Yards':
            if toUnit == 'Miles':
                output = round(float(value * 0.00056818),2)
                # print output
                return output
            elif toUnit == 'Meters':
                output = round(float(value / 1.0936),2)
                # print output
                return output
            elif toUnit == 'Yards':
                output = round(float(value),2)
                # print output
                return output
        elif fromUnit == 'Meters':
            if toUnit == 'Yards':
                output = round(float(value * 1.0936),2)
                # print output
                return output
            elif toUnit == 'Miles':
                output = round(float(value / 1609.344),2)
                # print output
                return output
            elif toUnit == 'Meters':
                output = round(float(value),2)
                # print output
                return output
    else:
        raise ConversionNotPossible('Please check both units, conversion is not possible')

class ConvertTests(unittest.TestCase):

    def testTemperature(self):
        self.assertEqual(convert('Celsius','Fahrenheit',0),32.0)
        self.assertEqual(convert('Celsius','Kelvin',0),273.15)
        self.assertEqual(convert('Kelvin','Fahrenheit',0),-459.67)
        self.assertEqual(convert('Kelvin','Celsius',10),-263.15)
        self.assertEqual(convert('Fahrenheit','Celsius',32),0.0)
        self.assertEqual(convert('Fahrenheit','Kelvin',0),255.37)

    def testDistance(self):
        self.assertEqual(convert('Meters', 'Miles', 10000),6.21)
        self.assertEqual(convert('Meters','Yards',10),10.94)
        self.assertEqual(convert('Miles','Meters',10),16093.47)
        self.assertEqual(convert('Miles','Yards',10),17600.00)
        self.assertEqual(convert('Yards','Meters',3),2.74)
        self.assertEqual(convert('Yards','Miles',300),0.17)

    def testSanity(self):
        self.assertEqual(convert('Kelvin', 'Kelvin', 0), 0)
        self.assertEqual(convert('Celsius', 'Celsius', 0), 0)
        self.assertEqual(convert('Fahrenheit', 'Fahrenheit', 0), 0)
        self.assertEqual(convert('Meters', 'Meters', 0), 0)
        self.assertEqual(convert('Miles', 'Miles', 0), 0)
        self.assertEqual(convert('Yards', 'Yards', 0), 0)

    def testErrors(self):
        self.assertRaises(ConversionNotPossible,convert,'Yards','Kelvin',0)

if __name__ == '__main__':
    unittest.main()