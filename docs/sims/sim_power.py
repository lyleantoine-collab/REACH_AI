#!/usr/bin/env python3
"""
REACH_AI Power Efficiency Simulator
====================================
Quick calc for electrical ROI from the Components Table (docs/electrical.md).
Baseline: 14.7kW (Glycol Pump 10kW + 2x Fans 4kW + PLC 0.5kW + 2x Valves 0.2kW).

Run: python docs/sims/sim_power.py
Tweak vars below for your colossus-scale what-ifs.

KISS: No deps, pure Python. Scale to farm/turbine ties next.
"""

def calculate_roi(baseline_power=14.7, efficiency_shave=0.15, kwh_rate=0.10, hours_per_year=8760):
    """
    Core ROI cruncher.
    - baseline_power: Total kW from electrical table.
    - efficiency_shave: % power reduction (e.g., 0.15 = 15%).
    - kwh_rate: Local industrial rate ($/kWh).
    - hours_per_year: 24/7 ops default.
    Returns annual savings.
    """
    after_shave = baseline_power * (1 - efficiency_shave)
    power_saved = baseline_power - after_shave
    hourly_savings = power_saved * kwh_rate
    annual_savings = hourly_savings * hours_per_year
    
    print("REACH_AI Power Sim")
    print("==================")
    print(f"Baseline draw: {baseline_power} kW")
    print(f"After {efficiency_shave*100:.1f}% shave: {after_shave:.1f} kW")
    print(f"Power saved: {power_saved:.1f} kW")
    print(f"Hourly savings (@ ${kwh_rate}/kWh): ${hourly_savings:.2f}")
    print(f"Annual savings ({hours_per_year} hrs): ${annual_savings:.2f}")
    print("-" * 40)
    
    return annual_savings

if __name__ == "__main__":
    # Your electrical table baseline—15% shave from contra fans + VFD tuning
    savings = calculate_roi(baseline_power=14.7, efficiency_shave=0.15)
    
    # Bonus: What-if for glycol loop tie-in (add 5kW heat recovery offset)
    print("Glycol What-If: +5kW recovery offset")
    effective_baseline = 14.7 - 5.0  # Heat-to-farm recoup
    savings_glycol = calculate_roi(baseline_power=effective_baseline, efficiency_shave=0.15)
