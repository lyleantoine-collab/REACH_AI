#!/usr/bin/env python3
"""
REACH_AI Exhaust Scrubber Simulator
===================================
Crunch sulfur byproduct revenue from turbine exhaust (ties to p_and_id_final.md).
Baseline: 500 SCFM exhaust, 1000 ppm SO2, 95% capture → 1.2 tons/day sold.

Run: python docs/sims/sim_exhaust.py
Tweak vars for your exhaust specs. Next: Tie to carbon credits?

Inspired by oil/gas scrubbers, made for AI exhaust farms.
"""

def calculate_sulfur_sales(exhaust_flow=500, so2_conc=1000, scrub_eff=0.95, price_per_ton=200, days_per_year=365):
    """
    Core sulfur sales calc: Simplified tons/year from exhaust params.
    - exhaust_flow: SCFM (standard cubic ft/min).
    - so2_conc: PPM SO2 in exhaust.
    - scrub_eff: Capture efficiency (0-1).
    - price_per_ton: Market $/ton for sulfur.
    - Returns annual revenue.
    """
    # Rough tons/day: (flow * conc * eff * conversion factor); baseline tuned to 1.2 tons/day
    conversion_factor = 0.0000024  # Empirical (SCFM * PPM * days → tons; adjust for real chem)
    tons_per_day = exhaust_flow * so2_conc * scrub_eff * conversion_factor
    annual_tons = tons_per_day * days_per_year
    annual_revenue = annual_tons * price_per_ton
    
    print("REACH_AI Exhaust Sim")
    print("====================")
    print(f"Tons/day captured: {tons_per_day:.1f}")
    print(f"Annual tons: {annual_tons:.1f}")
    print(f"Revenue (@ ${price_per_ton}/ton): ${annual_revenue:.2f}")
    print("-" * 40)
    
    return annual_revenue

if __name__ == "__main__":
    # Baseline from P&ID: 500 SCFM exhaust, mid-SO2, high eff
    revenue = calculate_sulfur_sales(exhaust_flow=500, so2_conc=1000, scrub_eff=0.95)
    
    # What-if: Dirtier exhaust (higher SO2) or bigger turbine (1000 SCFM)
    print("Scale-Up What-If: 1000 SCFM + 1500 PPM SO2")
    revenue_scale = calculate_sulfur_sales(exhaust_flow=1000, so2_conc=1500, scrub_eff=0.95)
