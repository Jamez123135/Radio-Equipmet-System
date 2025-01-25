from Radio import Radio
# Importing the Radio class from the Radio module

class PortableRadio(Radio):
    # Subclass of Radio representing a Portable Radio

    def __init__(self, bandset, power_output, power_requirement, current_requirement, connector, manufacturer, model_id):
        super().__init__(bandset, power_output, power_requirement, current_requirement, connector, manufacturer, model_id)
        self._bandset = bandset

    def __str__(self):
        output = f"Portable Radio:\n"
        output += f"\tBandset:        {self.bandset}\n"
        output += f"\tPower Output:   {self.power_output}\n"
        output += f"\tPower Requirement: {self.power_requirement}\n"
        output += f"\tCurrent Requirement: {self.current_requirement}\n"
        output += f"\tConnector:      {self.connector}\n"
        output += f"\tManufacturer:   {self.manufacturer}\n"
        output += f"\tModel ID:       {self.model_id}\n"
        return output

class MobileRadio(Radio):
    # Subclass of Radio representing a Mobile Radio

    def __init__(self, bandset, power_output, power_requirement, current_requirement, connector, manufacturer, model_id):
        super().__init__(bandset, power_output, power_requirement, current_requirement, connector, manufacturer, model_id)
        self._bandset = bandset

    def __str__(self):
        output = f"Mobile Radio:\n"
        output += f"\tBandset:        {self.bandset}\n"
        output += f"\tPower Output:   {self.power_output}\n"
        output += f"\tPower Requirement: {self.power_requirement}\n"
        output += f"\tCurrent Requirement: {self.current_requirement}\n"
        output += f"\tConnector:      {self.connector}\n"
        output += f"\tManufacturer:   {self.manufacturer}\n"
        output += f"\tModel ID:       {self.model_id}\n"
        return output

class FixedStationRadio(Radio):
    # Subclass of Radio representing a Fixed Station Radio

    def __init__(self, bandset, power_output, power_requirement, current_requirement, connector, manufacturer, model_id):
        super().__init__(bandset, power_output, power_requirement, current_requirement, connector, manufacturer, model_id)
        self._bandset = bandset

    def __str__(self):
        output = f"Fixed Station Radio:\n"
        output += f"\tBandset:        {self.bandset}\n"
        output += f"\tPower Output:   {self.power_output}\n"
        output += f"\tPower Requirement: {self.power_requirement}\n"
        output += f"\tCurrent Requirement: {self.current_requirement}\n"
        output += f"\tConnector:      {self.connector}\n"
        output += f"\tManufacturer:   {self.manufacturer}\n"
        output += f"\tModel ID:       {self.model_id}\n"
        return output
