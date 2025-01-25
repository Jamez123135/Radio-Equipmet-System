"""
Package - AS2

Represents a package, containing one or more radios, one or more antennas,
and a power supply.

25-MAY-2022 CRV UPEI SMCS
"""
from Radio import Radio
from Antenna import Antenna
from PowerSupply import PowerSupply
from RadioToolbox import RadioToolbox


class Package(object):
    package_count = 0  # static variable

    '''
    Constructor:    radios is a list of 1 or more Radio objects
                    antennas is a list of 1 or more Antenna objects
                    power_supply is a single PowerSupply object
    '''

    def __init__(self, radios, power_supply, antennas):
        self.__radios = radios
        self.__antennas = antennas
        self.__power_supply = power_supply
        Package.package_count += 1  # increment static variable
        self.__package_number = Package.package_count  # store my package number

    def add_radio(self, radio):
        self.__radios.append(radio)

    def drop_radio(self, index):
        self.__radios.pop(index)  # note, does not return popped value

    def add_antenna(self, antenna):
        self.__antennas.append(antenna)

    def drop_antenna(self, index):
        self.__antennas.pop(index)  # likewise, retured value dropped

    def num_radios(self):
        return len(self.__radios)

    def num_antennas(self):
        return len(self.__antennas)

    def get_package_number(self):
        return self.__package_number

    '''
    __base_package_valid: internal helper method (student can call it whatever)

    Returns a Boolean to show if the package contains at least 1 of each
    category of item; otherwise returns false
    '''

    def __base_package_valid(self):
        return len(self.__radios) > 0 and self.__power_supply \
            and len(self.__antennas) > 0

    '''
    validate_package:

    responsible for determining if a package is valid
    returns Boolean, and a description
    '''

    def validate_package(self):
        # do a preliminary count check
        if not self.__base_package_valid():
            return False, "Package initially incomplete: missing category."

        # check power supply against all radios in package
        power_supply_ok = True  # assume it's good, prove otherwise
        for radio in self.__radios:
            if not (RadioToolbox.radio_power_compatibility(radio, self.__power_supply)):
                power_supply_ok = False
        if not power_supply_ok:
            return False, "Power supply insufficient for all radios in package."

        # now check and be sure that every radio has an antenna that works with it;
        # if you find a radio without antennas, remove that radio
        #
        good_radios = []  # build a list of radios that have antennas
        for r in self.__radios:
            radio_has_antenna = False  # assume there is no valid antenna
            for a in self.__antennas:
                if RadioToolbox.transceiver_compatibility(r, a):
                    radio_has_antenna = True  # compatible with at least one antenna

            if radio_has_antenna:  # if antenna found for this radio
                good_radios.append(r)  # add it to 'good' list
        self.__radios = good_radios  # and keep good radios

        # now check and be sure that every antenna has a radio that works with it;
        # if you find an antenna without a radio, remove that antenna
        #
        good_antennas = []  # likewise, a list of good antennas
        for a in self.__antennas:
            antenna_has_radio = False  # assume there is no valid radio
            for r in self.__radios:
                if RadioToolbox.transceiver_compatibility(r, a):
                    antenna_has_radio = True  # compatible with at least one radio

            if antenna_has_radio:  # if radio found for this antenna
                good_antennas.append(a)  # add it to 'good' list
        self.__antennas = good_antennas  # keep good antennas

        # do a final count check
        if not self.__base_package_valid():
            return False, "Package incomplete after processing: missing category."

        # if we reach this point, the package is valid; return True and no explanation
        return True, ""

    # Stringifier dunder method
    #
    # Uses the stringifiers of the three objects to generate its own output

    def __str__(self):
        output = f"PACKAGE {self.__package_number}\n==========\n\n"

        for r in self.__radios:
            output += str(r) + "\n"

        output += str(self.__power_supply) + "\n"

        for a in self.__antennas:
            output += str(a) + "\n"

        return output
