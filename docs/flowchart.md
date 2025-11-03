flowchart TD
    A[AI Servers/GPUs<br/>(14.7kW baseline draw)] --> B[Heat to Glycol Loop<br/>(99% Water Save)]
    B --> C[Glycol Exchanger<br/>(Temp: 80-120C In/Out)]
    C --> D[External Radiators w/ Contra Fans<br/>(2kW/ea., 15% Shave)]
    D --> B
    C --> E[Branch: Waste Heat/CO2<br/>(Alert if Temp >80C?)]
    E -->|Yes| F[PLC Alert → AI Predictor<br/>(Run sim_power.py)]
    E -->|No| G[Turbines + Exhaust Manifold<br/>(Flex Pipes, ESD Valves)]
    G --> H[Scrubber Tower: Amine Bubbler<br/>(Clean Exhaust)]
    H --> I[Sulfur Byproduct → Sell<br/>(ROI: $2k/yr est.)]
    H --> J[CO2/Heat to Vertical Farm<br/>(Trays + Diffusion, 2x Yields)]
    J --> K[Harvest: Greens + Cooling Feedback<br/>(ROI in 2 Yrs)]
    K --> L[ROI Loop: Scale to Colossus<br/>(Modular Build)]
    L --> A
    F --> L
    style A fill:#f9f,stroke:#333
    style L fill:#bbf,stroke:#333
