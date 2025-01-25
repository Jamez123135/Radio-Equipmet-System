"""
Antenna - AS2

Represents a radio antenna; contains accessors and mutators for all specified
parameters, as well as the dunder str method to render itself as text (per
the specification)

20-MAY-2022 CRV UPEI SMCS
"""


class Antenna(object):
    # static dictionaries used for converting coded values into "chatty" text
    antenna_type_dict = {"D": "Dipole", "E": "End-Fed", "W": "Whip", \
                         "V": "Vertical with Radials", "M": "Magnetic Loop", \
                         "Y": 'Yagi-Uda "Beam" Antenna'}
    connector_type_dict = {"P": "PL-259", "N": "N-plug", "B": "Bayonet-plug", "S": "SMA-plug"}

    # constructor - all parameters are required (no defaults)
    def __init__(self, design_bands, connector, antenna_type, manufacturer, model_id):
        self.__antenna_type = antenna_type
        self.__design_bands = design_bands
        self.__connector = connector
        self.__manufacturer = manufacturer
        self.__model_id = model_id

    # mutators (setters) and accessors (getters) for each instance variable
    def set_antenna_type(self, at):
        self.__antenna_type = at

    def get_antenna_type(self):
        return self.__antenna_type

    def set_design_bands(self, b):
        self.__design_bands = b

    def get_design_bands(self):
        return self.__design_bands

    def get_design_bands_list(self):
        extraction = self.__design_bands.split("/")
        data = []
        for item in extraction:
            if "." in item:  # if it has a decimal point
                data.append(float(item))  # it's a float
            else:
                data.append(int(item))  # otherwise, it's an int
        return data

    def set_connector(self, c):
        self.__connector = c

    def get_connector(self):
        return self.__connector

    def set_manufacturer(self, m):
        self.__manufacturer = m

    def get_manufacturer(self):
        return self.__manufacturer

    def set_model_id(self, m_id):
        self.__model_id = m_id

    def get_model_id(self):
        return self.__model_id

    # dunder stringifier - must return a string
    def __str__(self):
        output = ""
        output += "ANTENNA\n"
        output += "\tType:           " + Antenna.antenna_type_dict[self.__antenna_type] + "\n"
        output += "\tDesign Bands:   " + self.__design_bands + "\n"
        output += "\tConnector:      " + Antenna.connector_type_dict[self.__connector] + "\n"
        output += "\tManufacturer:   " + self.__manufacturer + "\n"
        output += "\tModel ID:       " + self.__model_id + "\n"

        return output
