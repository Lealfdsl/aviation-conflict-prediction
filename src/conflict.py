from geopy.distance import geodesic
import pandas as pd

def compute_pairwise_features(df: pd.DataFrame, max_distance_nm: float = 30.0) -> pd.DataFrame:
    """
    Calcula pares de aeronaves e features de risco de conflito.
    """
    records = []
    n = len(df)
    
    for i in range(n):
        for j in range(i + 1, n):
            a = df.iloc[i]
            b = df.iloc[j]
            
            # Distância horizontal em milhas náuticas
            dist_nm = geodesic(
                (a.latitude, a.longitude),
                (b.latitude, b.longitude)
            ).nm
            
            if dist_nm > max_distance_nm:
                continue
                
            # Separação vertical em pés
            vert_ft = abs(a.baro_altitude - b.baro_altitude) * 3.28084
            
            # Diferença de rumo
            heading_diff = abs(a.true_track - b.true_track) % 360
            heading_diff = min(heading_diff, 360 - heading_diff)
            
            # Velocidade relativa
            rel_speed = abs(a.velocity - b.velocity)
            
            # Conflito simples (5 NM e 1000 ft)
            is_conflict = (dist_nm < 5.0) and (vert_ft < 1000)
            
            records.append({
                "icao_a": a.icao24,
                "icao_b": b.icao24,
                "dist_nm": round(dist_nm, 2),
                "vert_ft": round(vert_ft, 1),
                "heading_diff": round(heading_diff, 1),
                "rel_speed": round(rel_speed, 2),
                "is_conflict": is_conflict,
                "risk_score": round(1 / (dist_nm + 0.1) * (1000 / (vert_ft + 100)), 2)
            })
    
    return pd.DataFrame(records)
