from Radio import Radio
from Antenna import Antenna

"""
RadioToolbox - AS2

This is a class filled with static functions, not methods - they are called
using the classname (i.e. RadioToolbox.compute_frequency(2) would be a possible call)

Like any class, it must be imported.  It also must import Radio and Antenna in order
to work with objects of those classes.

There are NO METHODS here.  There is no self reference used.

20-MAY-2022 CRV UPEI SMCS
"""


class RadioToolbox(object):

    # convert an antenna's design bands list into frequency ranges by referencing
    # the information provided in the assignment as a dictionary lookup
    def band_to_frequency(antenna):
        m_to_mhz = {"160": "1.8-2.0", "80": "3.5-4.0", "40": "7-7.3", "30": "10.1-10.15", \
                    "20": "14-14.35", "17": "18.068-18.168", "15": "21-21.45", \
                    "12": "24.89-24.99", "10": "28-29.7", "6": "50-54", "2": "144-148", \
                    "0.7": "430-450"}
        bands = antenna.get_design_bands().split("/")
        freqs = []
        for b in bands:
            freqs.append(m_to_mhz[b])
        return freqs

    # given a wavelength expressed in metres (lambda), return the corresponding
    # frequency, to 3 decimal places
    def compute_frequency(wavelength_lambda):
        c = 300  # speed of light in Mm/s (1000 km/s)
        # f = c/wavelength_lambda
        return round(c / wavelength_lambda, 3)  # rounded to 3 dp

    # given a transceiver (Radio), and an antenna (Antenna), determine if they can
    # be used together.  They can be used together if they have at least one band
    # in common.  This is returned as a Boolean value.
    def transceiver_compatibility(transceiver, antenna):
        # define values for band categories
        hf_bands = [160, 80, 40, 30, 20, 17, 15, 10]
        six = 6
        vhf = 2
        uhf = 0.7

        # process the bandset of the transceiver into numeric band values in a list
        # (note: there are more clever ways to do this, but they would be far less
        # readable to another programmer)
        transceiver_bands = []
        bandset = transceiver.get_bandset()
        if "H" in bandset:
            transceiver_bands.extend(hf_bands)
        if "6" in bandset:
            transceiver_bands.append(six)
        if "V" in bandset:
            transceiver_bands.append(vhf)
        if "U" in bandset:
            transceiver_bands.append(uhf)

        # get the numeric bands of the antenna
        antenna_bands = antenna.get_design_bands_list()

        # get the connector codes
        xcvr_conn = transceiver.get_connector()
        ant_conn = antenna.get_connector()

        # start with checking the connectors
        is_valid = xcvr_conn == ant_conn

        # use sets to determine if the antenna can service the transceiver
        xcvr_bands_set = set(transceiver_bands)
        ant_bands_set = set(antenna_bands)
        common_bands_set = xcvr_bands_set & ant_bands_set  # set intersection

        is_valid = is_valid and len(common_bands_set) > 0

        return is_valid

    """
    midpoint_frequency(freq_range)

    given a MHz frequency range in text form like "14-14.35" render the midpoint in MHz and
    also in wavelength
    """

    def midpoint_frequency(freq_range):
        data = freq_range.split("-")
        start = float(data[0])
        end = float(data[1])
        mid = (start + end) / 2
        m = 300 / mid
        return mid, m

    """
    radio_power_compatibility(radio, power_supply)

    given a radio object, and a power_supply object, determine if they are compatible:
    that is, the radio requires no more than 80% of the power supply's continuous power
    rating

    note that a battery powered radio (like a handheld) is 'compatible' with any power
    supply, since it won't be using it!
    """

    def radio_power_compatibility(radio, power_supply):
        if radio.get_power_requirement() == "B" or radio.get_power_requirement() == "A":
            return True  # only runs on battery or has integrated AC/DC supply
        elif "D" in radio.get_power_requirement():
            # current handling is stored as string:  surge / continuous
            # get the power supply continuous current from this
            ps_continuous_current = float((power_supply.get_current_handling().split("/"))[1])
            # radio current requirement is also stored as string; convert
            r_current_requirement = float(radio.get_current_requirement())
            return r_current_requirement <= 0.8 * ps_continuous_current

