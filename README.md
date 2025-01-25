# Radio-Equipmet-System
Technical Highlights
Object-Oriented Design

Built a modular system with inheritance (PortableRadio, DipoleAntenna, SwitchingPowerSupply) and polymorphism for diverse radio equipment types.

Leveraged static dictionaries for human-readable data conversion (e.g., antenna_type_dict mapping "D" to "Dipole").

Data Processing & Validation

Engineered a file parser (read_file()) to ingest radios, antennas, and power supplies from TXT files.

Implemented package validation (Package.validate_package()) ensuring:

Power supply compatibility (80% continuous current rule).

Antenna-radio frequency/connector matching.

System Integration

Created a RadioToolbox with static methods for:

Frequency-wavelength conversion (compute_frequency()).

Bandset compatibility checks (transceiver_compatibility()).

Designed a Package class to bundle components, auto-incrementing package IDs.

