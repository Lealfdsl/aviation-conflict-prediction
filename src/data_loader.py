import requests
import pandas as pd
from typing import Optional

def get_states(bbox: Optional[tuple] = None) -> pd.DataFrame:
    """
    Busca aeronaves ao vivo da OpenSky Network.
    
    bbox = (lamin, lomin, lamax, lomax)
    Exemplo Sudeste do Brasil: (-25, -50, -15, -35)
    """
    url = "https://opensky-network.org/api/states/all"
    params = {}
    if bbox:
        params = {
            "lamin": bbox[0], "lomin": bbox[1],
            "lamax": bbox[2], "lomax": bbox[3]
        }
    
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    
    cols = [
        "icao24", "callsign", "origin_country", "time_position",
        "last_contact", "longitude", "latitude", "baro_altitude",
        "on_ground", "velocity", "true_track", "vertical_rate",
        "sensors", "geo_altitude", "squawk", "spi", "position_source"
    ]
    
    df = pd.DataFrame(data["states"], columns=cols)
    df = df.dropna(subset=["latitude", "longitude", "baro_altitude"])
    df = df[~df["on_ground"]]  # apenas aeronaves em voo
    return df

if __name__ == "__main__":
    df = get_states(bbox=(-25.0, -48.0, -20.0, -40.0))
    print(f"Aeronaves encontradas: {len(df)}")
    print(df[["icao24", "callsign", "latitude", "longitude", "baro_altitude"]].head())
