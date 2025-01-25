from Antenna import Antenna
# Importing the Antenna class from the Antenna module

class DipoleAntenna(Antenna):
    # Subclass of Antenna representing a Dipole Antenna

    def __init__(self, design_bands, connector, manufacturer, model_id):
        super().__init__(design_bands, connector, "D", manufacturer, model_id)

    def __str__(self):
        output = "DIPOLE ANTENNA\n"
        output += "\tDesign Bands:   " + self.__design_bands + "\n"
        output += "\tConnector:      " + Antenna.connector_type_dict[self.__connector] + "\n"
        output += "\tManufacturer:   " + self.__manufacturer + "\n"
        output += "\tModel ID:       " + self.__model_id + "\n"
        return output
class VerticalAntenna(Antenna):
    # Subclass of Antenna representing a Vertical Antenna

    def __init__(self, design_bands, connector, manufacturer, model_id):
        super().__init__(design_bands, connector, "V", manufacturer, model_id)

    def __str__(self):
        output = "VERTICAL ANTENNA\n"
        output += "\tDesign Bands:   " + self.__design_bands + "\n"
        output += "\tConnector:      " + Antenna.connector_type_dict[self.__connector] + "\n"
        output += "\tManufacturer:   " + self.__manufacturer + "\n"
        output += "\tModel ID:       " + self.__model_id + "\n"
        return output