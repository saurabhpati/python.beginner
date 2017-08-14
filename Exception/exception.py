outputTemp = 0;
def CtoFtoC_Conversion(inputTemp, outputTempType, isReturn):
    """This method converts to Celsius if given a Farhaniet and vice versa.
       inputTemp = The input temperature value.
       outputTempType = Type of output temperature required.
       isReturn = Whether output is required in return."""
    if outputTempType == 1:
        outputTemp = (inputTemp - 32) * 5 / 9;
    else:
        outputTemp = (9 * inputTemp / 5) + 32;
    if isReturn:
        return outputTemp;
    else:
        print(outputTemp, outputTempType);
        exit();

def CtoKtoC_Conversion(inputTemp, outputTempType, isReturn):
    """This method converts to Celsius if given a Kelvin and vice versa.
       inputTemp = The input temperature value.
       outputTempType = Type of output temperature required.
       isReturn = Whether output is required in return."""
    if outputTempType == 1:
        outputTemp = inputTemp + 273;
    else:
        outputTemp = inputTemp - 273;
    if isReturn:
        return outputTemp;
    else:
        print(outputTemp, outputTempType);
        exit();
    
def FtoKtoF_Conversion(inputTemp, outputTempType, isReturn):
    """This method converts to Farhaniet if given a Kelvin and vice versa.
       inputTemp = The input temperature value.
       outputTempType = Type of output temperature required.
       isReturn = Whether output is required in return."""
    if outputTempType == 3:
        intermediateTemp = CtoKtoC_Conversion(inputTemp, outputTempType, True);
        CtoFtoC_Conversion(intermediateTemp, outputTempType, False);
    else:
        intermediateTemp = CtoFtoC_Conversion(inputTemp, outputTempType, True);
        CtoFtoC_Conversion(inputTemp, outputTempType, False);

ioTemperatureDictionary = {
    'Celsius_Farhaniet': CtoFtoC_Conversion,
    'C_Farheniet': CtoFtoC_Conversion,
    'C_F': CtoFtoC_Conversion,
    'Celsius_F': CtoFtoC_Conversion,
    'Farhaniet_Celsius': CtoFtoC_Conversion,
    'F_Celsius': CtoFtoC_Conversion,
    'F_C': CtoFtoC_Conversion,
    'Farhaniet_C': CtoFtoC_Conversion,
    'Kelvin_Celsius': CtoKtoC_Conversion,
    'Kelvin_C': CtoKtoC_Conversion,
    'K_Celsius': CtoKtoC_Conversion,
    'K_C': CtoKtoC_Conversion,
    'Celsius_Kelvin': CtoKtoC_Conversion,
    'Celsius_K': CtoKtoC_Conversion,
    'C_Kelvin': CtoKtoC_Conversion,
    'C_K': CtoKtoC_Conversion,
    'Farhaniet_Kelvin': FtoKtoF_Conversion,
    'Farhaniet_K': FtoKtoF_Conversion,
    'F_Kelvin': FtoKtoF_Conversion,
    'F_K': FtoKtoF_Conversion,
    'Kelvin_Farhaniet': FtoKtoF_Conversion,
    'Kelvin_F': FtoKtoF_Conversion,
    'K_Farhaniet': FtoKtoF_Conversion,
    'K_F': FtoKtoF_Conversion,
};

outputTemperatureTypeDictionary = {
    'Celsius': 1,
    'C': 1,
    'Kelvin': 2,
    'K': 2,
    'Farhaniet': 3,
    'F': 3
}

inputTempType = input('Enter your input temperature type(Celsius/C, Kelvin/K, Farhaniet/F):');
outputTempType = input('Enter the output temperature type(Celsius, Kelvin, Farhaniet):');
inputTemp = int(input('Enter your input temperature:'));

if inputTempType == outputTempType:
    print('Duh! I am not a fool you know...');
    exit();

ioKey = inputTempType + '_' + outputTempType;
if ioKey not in ioTemperatureDictionary.keys() or outputTempType not in outputTemperatureTypeDictionary.keys():
    print('Cannot perform the conversion');
    exit();
print(ioTemperatureDictionary[ioKey]);
ioTemperatureDictionary[ioKey](inputTemp, outputTemperatureTypeDictionary[outputTempType], False);