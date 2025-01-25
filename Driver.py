"""
AS2 Driver - the main entry point of the program

Responsible for loading contents from files, creating objects to be tested, and
housing any functionality not specifically assigned to any other object

20-MAY-2022 CRV UPEI SMCS
"""

from Radio import Radio
from Antenna import Antenna
from PowerSupply import PowerSupply
from Package import Package
from RadioToolbox import RadioToolbox

"""
read_file(filename)

reads data from the specified filename, and puts it into a list, which is
returned at the end of the method
"""


def read_file(filename):
    dataset = []
    file = open(filename, 'r')
    for line in file:
        line = line.strip()
        if line[0] != "#":
            data = line.split(",")
            dataset.append(data)
    file.close()  # be neat and tidy!
    return dataset


"""
main program
"""


def main():
    # read the radios.txt data and create radios from it
    radios = []
    radio_list = read_file("radios.txt")
    for radio in radio_list:
        radios.append(Radio(*radio))  # use a pointer to pass the list as elements

    antennas = []
    antenna_list = read_file("antennas.txt")
    for antenna in antenna_list:
        antennas.append(Antenna(*antenna))  # use a pointer to pass the list as elements

    power_supplies = []
    power_supply_list = read_file("powersupplies.txt")
    for power_supply in power_supply_list:
        power_supplies.append(PowerSupply(*power_supply))  # use a pointer to pass the list as elements

    # packages don't work like the rest of the stuff . . . we will have to do
    # some magic to process this
    packages = []
    with open("packages.txt") as f:
        for line in f:
            line = line.strip()
            if line == "" or line[0] == "#":
                continue  # stop processing, this is a comment, next!
            # set up lists to hold items from tuples and single value
            package_radios = []
            package_power_supply = 0
            package_antennas = []

            # get radio tuple, build list of radios
            # tuple of tuples, so we have (( at beginning
            # first value starts at position 2
            b = line.index(")")
            temp_indexes = line[2:b].split(",")  # get values as text
            for ti in temp_indexes:
                # intify and add radio to list - remember, off-by-one indexing!
                if ti != '':  # a tuple of 1 element has a blank second item!
                    package_radios.append(radios[int(ti) - 1])
            # remove the radio information from the line to make processing easier
            line = line[b + 1:]  # everything after the ) from the first tuple
            # get power supply index value - it has a comma before and after
            line = line[1:]  # get rid of leading comma
            c = line.index(",")  # find index of trailing comma
            package_power_supply_index = int(line[:c]) - 1  # get the index value
            package_power_supply = power_supplies[package_power_supply_index]  # add device
            # remove power supply from the line - what remains is antenna data
            line = line[c + 1:].strip()  # removes the trailing comma; strip any space
            # get antenna tuple, build list of antennas
            # first ( is now in position 0
            b = line.index(")")
            temp_indexes = line[1:b].split(",")  # get values as text
            for ti in temp_indexes:
                if ti != '':
                    package_antennas.append(antennas[int(ti) - 1])  # intify and add antenna
            # finally, add a package to the list with this information
            packages.append(Package(package_radios, package_power_supply, package_antennas))

    # validate packages; copy good packages to new list
    good_packages = []
    for p in packages:
        valid, reason = p.validate_package()
        if not valid:
            print(f"INVALID PACKAGE {p.get_package_number()}: {reason}")
        else:
            good_packages.append(p)

    print("\n\nPACKAGES\n========\n")
    for p in good_packages:
        print(p)


# if this is being called as the entry point of the program, then transfer
# control to the main function; if not, the main function would be ignored
#
# this is how you could put testing code into a class file, and have it not execute
# when the file is used solely as a class, and not as the entry point

if __name__ == "__main__":
    main()
