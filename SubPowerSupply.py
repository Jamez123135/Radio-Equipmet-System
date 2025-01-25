from PowerSupply import PowerSupply
# Importing the PowerSupply class from the PowerSupply module

class SwitchingPowerSupply(PowerSupply):
    def __init__(self, voltage_type, current_handling, meter_type, manufacturer, model_id):
        super().__init__("S", voltage_type, current_handling, meter_type, manufacturer, model_id)

    def __str__(self):
        output = "SWITCHING POWER SUPPLY\n"
        output += "\tVoltage Type:     " + PowerSupply.voltage_type_dict[self.__voltage_type] + "\n"
        data = self.__current_handling.split("/")
        output += "\tCurrent Handling: " + data[0] + "A surge / " + data[1] + "A continuous\n"
        output += "\tMeter Type:       " + PowerSupply.meter_type_dict[self.__meter_type] + "\n"
        output += "\tManufacturer:     " + self.__manufacturer + "\n"
        output += "\tModel ID:         " + self.__model_id + "\n"
        return output
class TransformerPowerSupply(PowerSupply):
    def __init__(self, voltage_type, current_handling, meter_type, manufacturer, model_id):
        super().__init__("T", voltage_type, current_handling, meter_type, manufacturer, model_id)

    def __str__(self):
        output = "TRANSFORMER POWER SUPPLY\n"
        output += "\tVoltage Type:     " + PowerSupply.voltage_type_dict[self.__voltage_type] + "\n"
        data = self.__current_handling.split("/")
        output += "\tCurrent Handling: " + data[0] + "A surge / " + data[1] + "A continuous\n"
        output += "\tMeter Type:       " + PowerSupply.meter_type_dict[self.__meter_type] + "\n"
        output += "\tManufacturer:     " + self.__manufacturer + "\n"
        output += "\tModel ID:         " + self.__model_id + "\n"
        return output
from PowerSupply import PowerSupply

class Battery(PowerSupply):
    def __init__(self, manufacturer, model_id, voltage, battery_type):
        super().__init__(manufacturer, model_id, voltage)
        self.battery_type = battery_type

    def __str__(self):
        return f"Battery:\n\tManufacturer: {self.manufacturer}\n\tModel ID: {self.model_id}\n\tVoltage: {self.voltage}\n\tBattery Type: {self.battery_type}\n"

class PowerCable(PowerSupply):
    def __init__(self, manufacturer, model_id, voltage, cable_type):
        super().__init__(manufacturer, model_id, voltage)
        self.cable_type = cable_type

    def __str__(self):
        return f"Power Cable:\n\tManufacturer: {self.manufacturer}\n\tModel ID: {self.model_id}\n\tVoltage: {self.voltage}\n\tCable Type: {self.cable_type}\n"
