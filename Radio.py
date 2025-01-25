"""
Radio - AS2

Represents a radio transceiver; contains accessors and mutators for all specified
parameters, as well as the dunder str method to render itself as text (per
the specification)

20-MAY-2022 CRV UPEI SMCS
"""


class Radio(object):
    # static dictionaries used for converting coded values into "chatty" text
    radio_type_dict = {"P": "Portable", "M": "Mobile", "F": "Fixed Station"}
    power_req_dict = {"B": "Battery", "D": "DC External Supply", "A": "AC Direct"}
    connector_type_dict = {"P": "SO-239", "N": "N-socket", "B": "Bayonet-socket", "S": "SMA-socket"}

    # constructor - all parameters are required (no defaults)
    def __init__(self, radio_type, bandset, power_output, power_requirement, current_requirement, connector,
                 manufacturer, model_id):
        self.__radio_type = radio_type
        self.__bandset = bandset
        self.__power_output = power_output
        self.__power_requirement = power_requirement
        self.__current_requirement = current_requirement
        self.__connector = connector
        self.__manufacturer = manufacturer
        self.model_id = model_id

    # mutators (setters) and accessors (getters) for each instance variable
    def set_radio_type(self, rt):
        self.__radio_type = radio_type

    def get_radio_type(self):
        return self.__radio_type

    def set_bandset(self, b):
        self.__bandset = b

    def get_bandset(self):
        return self.__bandset

    def set_power_output(self, po):
        self.__power_output = po

    def get_power_output(self):
        return self.__power_output

    def set_power_requirement(self, pr):
        self.__power_requirement = pr

    def get_power_requirement(self):
        return self.__power_requirement

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
        return self.model_id

    def get_current_requirement(self):
        return self.__current_requirement

    # dunder stringifier - must return a string
    def __str__(self):
        output = ""
        output += "RADIO\n"
        output += "\tType:           " + Radio.radio_type_dict[self.__radio_type] + "\n"
        output += "\tBandset:        " + self.__bandset + "\n"
        output += "\tPower Output:   " + self.__power_output + "W\n"
        output += "\tPower Reqs:     "
        for ch in self.__power_requirement:
            output += Radio.power_req_dict[ch] + "\n" + " " * 25
        output = output.strip()  # strip off final spaces
        output += "\n"  # put back the final newline
        output += "\tCurrent Req:    " + self.__current_requirement + "A\n"
        output += "\tConnector:      " + Radio.connector_type_dict[self.__connector] + "\n"
        output += "\tManufacturer:   " + self.__manufacturer + "\n"
        output += "\tModel ID:       " + self.model_id + "\n"

        return output
