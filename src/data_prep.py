import pandas as pd
import numpy as np
from pathlib import Path

def generate_energy_data(out_path: str = "data/raw/historical_energy.csv") -> None:
    np.random.seed(42)

    out_file = Path(out_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    # 36 months of historical data
    dates = pd.date_range(start="2021-01-31", periods=36, freq="M")

    base_demand = 10000  # kWh baseline
    seasonal = 1500 * np.sin(2 * np.pi * (dates.month / 12.0))  # seasonality
    noise = np.random.normal(0, 500, len(dates))  # random variation

    energy_kwh = base_demand + seasonal + noise

    # Energy price & grid CO2 factor vary over time
    price_per_kwh = np.random.uniform(0.18, 0.28, len(dates))
    co2_factor = np.random.uniform(0.35, 0.45, len(dates))  # kg CO2 per kWh

    df = pd.DataFrame({
        "date": dates,
        "energy_kwh": np.round(energy_kwh, 0),
        "price_per_kwh": np.round(price_per_kwh, 3),
        "co2_factor": np.round(co2_factor, 3),
    })

    df.to_csv(out_file, index=False)
    print(f"✅ Saved dataset: {out_file.resolve()}")

if __name__ == "__main__":
    generate_energy_data()