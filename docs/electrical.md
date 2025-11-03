# REACH_AI Electrical Schematics

3-phase 480V backbone for glycol pumps, fans, scrubbers. PLC controls for auto-tune.

## Pseudo-Schematic
480V 3-Phase Bus
├── Glycol Pump VFD ──> Pump Motor (Temp Sensor Feedback)
├── Contra Fans ──> Fan Blades (PLC Speed Control)
├── Scrubbers ──> Turbine Gen (Modbus Link)
└── PLC Core ──> I/O (ESD Valves + Farm Alerts)
                 └── AI Predictor Hook (Future: Ethernet/IP)
## Components Table

## Components Table
| Component          | Spec                  | Est. Cost | Power Draw | Notes                          |
|--------------------|-----------------------|-----------|------------|--------------------------------|
| Glycol Pump VFD    | ABB ACS880, 0-60Hz    | $5k       | 10kW peak  | Temp-linked ramp-up            |
| Contra Fans        | ebm-papst, 2000 RPM   | $2k/ea.   | 2kW/ea.    | Skewed blades, 70% eff.        |
| PLC Core           | Allen-Bradley CompactLogix | $3k   | 0.5kW      | Modbus I/O for farm tie-in     |
| ESD Valves         | Solenoid, flex-joint safe | $1k/ea. | 0.1kW      | Auto-shut on leak              |
| **Total**          | -                     | **$11k+** | **~12.7kW**| **15% shave = $2k/yr savings** |
ROI: 15% fan power shave. Next: Arc-flash calcs.

KISS: Modular, NEC-compliant.
