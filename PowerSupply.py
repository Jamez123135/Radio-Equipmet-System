"""
PowerSupply - AS2

Represents a power supply; contains accessors (but no mutators) for all specified
parameters, as well as the dunder str method to render itself as text (per
the specification)

20-MAY-2022 CRV UPEI SMCS
"""


class PowerSupply(object):
    # static dictionaries used for converting coded values into "chatty" text
    physical_type_dict = {"S": "Switching", "T": "Transformer"}
    voltage_type_dict = {"F": "Fixed 13.8vDC", "V": "Variable Voltage"}
    meter_type_dict = {"N": "No Meters", "V": "Voltage Meter Only", "C": "Current Meter Only",
                       "B": "Both Voltage and Current Meters"}

    # constructor - all parameters are required (no defaults)
    def __init__(self, physical_type, voltage_type, current_handling, meter_type, manufacturer, model_id):
        self.__physical_type = physical_type
        self.__voltage_type = voltage_type
        self.__current_handling = current_handling
        self.__meter_type = meter_type
        self.__manufacturer = manufacturer
        self.__model_id = model_id

    # accessors (getters) for each instance variable

    def get_physical_type(self):
        return self.__physical_type

    def get_voltage_type(self):
        return self.__voltage_type

    def get_current_handling(self):
        return self.__current_handling

    def get_meter_configuration(self):
        return self.__meter_configuration

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model_id(self):
        return self.__model_id

    # dunder stringifier - must return a string
    def __str__(self):
        output = ""
        output += "POWER SUPPLY\n"
        output += "\tPhysical Type:    " + PowerSupply.physical_type_dict[self.__physical_type] + "\n"
        output += "\tVoltage Type:     " + PowerSupply.voltage_type_dict[self.__voltage_type] + "\n"
        data = self.__current_handling.split("/")
        output += "\tCurrent Handling: " + data[0] + "A surge / " + data[1] + "A continuous\n"
        output += "\tMeter Type:       " + PowerSupply.meter_type_dict[self.__meter_type] + "\n"
        output += "\tManufacturer:     " + self.__manufacturer + "\n"
        output += "\tModel ID:         " + self.__model_id + "\n"

        return output
