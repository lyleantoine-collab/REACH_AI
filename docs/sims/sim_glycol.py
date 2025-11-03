#!/usr/bin/env python3
"""
REACH_AI Glycol Heat Recovery Simulator
=======================================
Crunch heat from servers via glycol loop (ties to flowchart.md).
Baseline: 120C in → 80C out, 10GPM flow → ~6.7kW recoverable.

Run: python docs/sims/sim_glycol.py
Tweak vars for your P&ID sketches. Next: Tie to farm yield boost.

Inspired by oil/gas loops, made for AI sweat factories.
"""

def calculate_glycol_recovery(inlet_temp=120, outlet_temp=80, flow_rate=10, cp_glycol=2.4, hours_per_year=8760, kwh_rate=0.10):
    """
    Core heat recovery calc: Q = m * Cp * deltaT.
    - inlet_temp/outlet_temp: Glycol temps (C) from exchanger.
    - flow_rate: GPM (gal/min glycol).
    - cp_glycol: Specific heat (kJ/kg*C, ~2.4 for 50/50 mix).
    - Returns annual value of recovered heat.
    """
    delta_t = inlet_temp - outlet_temp
    # GPM to kg/s: 1 gal ≈ 3.78L, density ~1.1kg/L, /60 for sec
    mass_flow = flow_rate * 3.78 * 1.1 / 60  # kg/s
    # Heat in kW: (kJ/s) / 3.6 = kW
    heat_kw = mass_flow * cp_glycol * delta_t / 3.6
    annual_value = heat_kw * hours_per_year * kwh_rate
    
    print("REACH_AI Glycol Sim")
    print("===================")
    print(f"Delta T: {delta_t} C")
    print(f"Mass flow: {mass_flow:.2f} kg/s")
    print(f"Recoverable heat: {heat_kw:.1f} kW")
    print(f"Annual value (@ ${kwh_rate}/kWh): ${annual_value:.2f}")
    print("-" * 40)
    
    return annual_value

if __name__ == "__main__":
    # Baseline from flowchart: Servers hot → Exchanger cool-down
    savings = calculate_glycol_recovery(inlet_temp=120, outlet_temp=80, flow_rate=10)
    
    # What-if: Bigger loop for Colossus-scale (20GPM, hotter in)
    print("Scale-Up What-If: 20GPM + 130C In")
    savings_scale = calculate_glycol_recovery(inlet_temp=130, outlet_temp=80, flow_rate=20)
