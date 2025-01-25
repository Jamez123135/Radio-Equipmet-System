from Radio import Radio

class FixedStationRadio(Radio):
    def __init__(self, bandset, power_output, power_requirement, current_requirement, connector, manufacturer, model_id):
        super().__init__("F", bandset, power_output, power_requirement, current_requirement, connector, manufacturer, model_id)

    def __str__(self):
        output = "FIXED STATION RADIO\n"
        output += "\tBandset:        " + self.__bandset + "\n"
        output += "\tPower Output:   " + self.__power_output + "W\n"
        output += "\tPower Req:      " + Radio.power_req_dict[self.__power_requirement] + "\n"
        output += "\tCurrent Req:    " + self.__current_requirement + "\n"
        output += "\tConnector:      " + Radio.connector_type_dict[self.__connector] + "\n"
        output += "\tManufacturer:   " + self.__manufacturer + "\n"
        output += "\tModel ID:       " + self.__model_id + "\n"
        return output
