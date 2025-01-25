from SubRadio import PortableRadio, MobileRadio, FixedStationRadio
from SubAntenna import DipoleAntenna, VerticalAntenna
from SubPowerSupply import SwitchingPowerSupply, TransformerPowerSupply, Battery, PowerCable

def main():
    # Creating instances of radios
    portable_radio = PortableRadio("AM/FM", "10W", "12V", "1A", "BNC", "Sony", "PR-100")
    mobile_radio = MobileRadio("VHF/UHF", "50W", "24V", "5A", "SO-239", "Kenwood", "MR-2000")
    fixed_station_radio = FixedStationRadio("HF", "100W", "110V", "10A", "N-type", "Yaesu", "FSR-5000")

    # Creating instances of antennas
    dipole_antenna = DipoleAntenna("20m", "SO-239", "Comet", "DP-100")
    vertical_antenna = VerticalAntenna("40m", "N-type", "Diamond", "VA-200")

    # Creating instances of power supplies
    switching_power_supply = SwitchingPowerSupply("12V", "30A/25A", "Digital", "Mean Well", "SPS-1000")
    transformer_power_supply = TransformerPowerSupply("24V", "15A/10A", "Analog", "Samlex", "TPS-500")

    # Creating instances of battery and power cable
    battery = Battery("Duracell", "DUR-123", "12V", "Lead Acid")
    power_cable = PowerCable("Generic", "PC-456", "120V", "Heavy Duty")

    # Printing out information using __str__ methods
    print(portable_radio)
    print(mobile_radio)
    print(fixed_station_radio)
    print(dipole_antenna)
    print(vertical_antenna)
    print(switching_power_supply)
    print(transformer_power_supply)
    print(battery)
    print(power_cable)

if __name__ == "__main__":
    main()