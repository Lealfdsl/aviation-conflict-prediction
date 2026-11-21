# Previsão de Conflitos Aéreos

Modelo preditivo de risco de conflitos aéreos (perda de separação) utilizando dados reais de ADS-B da OpenSky Network.

## Problema

A separação segura entre aeronaves é crítica para a segurança do tráfego aéreo. Este projeto explora o uso de dados abertos de ADS-B da OpenSky Network para detectar e prever situações de risco de perda de separação (Loss of Separation) entre pares de aeronaves. Combina análise geoespacial, engenharia de features e machine learning para identificar situações de alto risco.

Os mínimos de separação utilizados como referência são **5 milhas náuticas na horizontal** e **1.000 pés na vertical** (padrão ICAO).

## O que o projeto faz

- Coleta dados de posição de aeronaves (ao vivo ou históricos) via OpenSky Network
- Calcula features de pares de aeronaves (distância horizontal, separação vertical, velocidade relativa, diferença de rumo)
- Detecta potenciais conflitos com base em critérios de separação
- Calcula um score de risco para cada par de aeronaves
- (Em desenvolvimento) Treina um modelo preditivo para prever o risco de conflito
- Visualiza os pares de alto risco em mapa

## Tecnologias

- Python 3.10+
- pandas, numpy
- requests / pyopensky
- geopy
- scikit-learn / XGBoost
- Folium / Plotly
- Streamlit

## Instalação

```bash
git clone https://github.com/seuusuario/aviation-conflict-prediction.git
cd aviation-conflict-prediction
pip install -r requirements.txt
```

## Como usar

### Buscar dados ao vivo

```python
from src.data_loader import get_states

# Exemplo de bounding box (Sudeste do Brasil)
df = get_states(bbox=(-25.0, -48.0, -20.0, -40.0))
print(f"Aeronaves encontradas: {len(df)}")
```

### Calcular features de conflito

```python
from src.conflict import compute_pairwise_features

pairs = compute_pairwise_features(df, max_distance_nm=25)
high_risk = pairs.sort_values("risk_score", ascending=False)
print(high_risk.head(10))
```

## Estrutura do projeto

```
aviation-conflict-prediction/
├── README.md
├── requirements.txt
├── data/
├── notebooks/
│   └── 01_exploratory.ipynb
├── src/
│   ├── data_loader.py      # Coleta de dados OpenSky
│   ├── features.py         # Engenharia de features
│   └── conflict.py         # Detecção e scoring de conflitos
└── app/
    └── demo.py             # Demo Streamlit (planejado)
```

## Resultados

*Em breve — screenshots do mapa de risco e métricas do modelo serão adicionados conforme o projeto evoluir.*

## Roadmap

- [ ] Detecção básica de conflitos entre pares
- [ ] Tempo até o Ponto de Maior Aproximação (TCPA)
- [ ] Dados históricos via OpenSky Trino
- [ ] Modelo preditivo (Random Forest / XGBoost)
- [ ] Visualização interativa em mapa
- [ ] Demo em Streamlit

## Agradecimentos

Dados de aeronaves fornecidos pela [OpenSky Network](https://opensky-network.org).

> Schäfer, M., Strohmeier, M., Lenders, V., Martinovic, I., & Wilhelm, M. (2014). Bringing up OpenSky: A large-scale ADS-B sensor network for research. In *Proceedings of the 13th International Symposium on Information Processing in Sensor Networks* (pp. 83–94).

## Licença

MIT

---

# Aviation Conflict Prediction

Predictive model for air traffic conflict risk (loss of separation) using real-world ADS-B data from the OpenSky Network.

## Problem

Safe separation between aircraft is critical for air traffic safety. This project explores the use of open ADS-B data from the OpenSky Network to detect and predict loss of separation events between aircraft pairs. It combines geospatial analysis, feature engineering, and machine learning to identify high-risk situations.

The typical separation minima used as reference are **5 nautical miles horizontally** and **1,000 feet vertically** (ICAO standard).

## What it does

- Fetches live or historical aircraft state vectors from the OpenSky Network
- Computes pairwise features between aircraft (horizontal distance, vertical separation, relative speed, heading difference)
- Detects potential conflicts based on separation criteria
- Calculates a risk score for each aircraft pair
- (In progress) Trains a predictive model to forecast conflict risk
- Visualizes high-risk pairs on a map

## Technologies

- Python 3.10+
- pandas, numpy
- requests / pyopensky
- geopy
- scikit-learn / XGBoost
- Folium / Plotly
- Streamlit

## Installation

```bash
git clone https://github.com/yourusername/aviation-conflict-prediction.git
cd aviation-conflict-prediction
pip install -r requirements.txt
```

## Usage

### Fetch live aircraft data

```python
from src.data_loader import get_states

# Example bounding box (Southeast Brazil)
df = get_states(bbox=(-25.0, -48.0, -20.0, -40.0))
print(f"Aircraft found: {len(df)}")
```

### Compute conflict features

```python
from src.conflict import compute_pairwise_features

pairs = compute_pairwise_features(df, max_distance_nm=25)
high_risk = pairs.sort_values("risk_score", ascending=False)
print(high_risk.head(10))
```

## Project Structure

```
aviation-conflict-prediction/
├── README.md
├── requirements.txt
├── data/
├── notebooks/
│   └── 01_exploratory.ipynb
├── src/
│   ├── data_loader.py      # OpenSky data collection
│   ├── features.py         # Feature engineering
│   └── conflict.py         # Conflict detection and scoring
└── app/
    └── demo.py             # Streamlit demo (planned)
```

## Results

*Coming soon — screenshots of risk maps and model performance will be added as the project evolves.*

## Roadmap

- [ ] Basic pairwise conflict detection
- [ ] Time to Closest Point of Approach (TCPA)
- [ ] Historical data via OpenSky Trino
- [ ] Predictive model (Random Forest / XGBoost)
- [ ] Interactive map visualization
- [ ] Streamlit demo

## Acknowledgments

Aircraft data provided by the [OpenSky Network](https://opensky-network.org).

> Schäfer, M., Strohmeier, M., Lenders, V., Martinovic, I., & Wilhelm, M. (2014). Bringing up OpenSky: A large-scale ADS-B sensor network for research. In *Proceedings of the 13th International Symposium on Information Processing in Sensor Networks* (pp. 83–94).

## License

MIT
