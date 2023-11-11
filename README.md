# Taxi demand predictor service
==============================

Predict Taxi Demand in New York City

Frontend: https://ml-nyctaxidemandpredictor-benvmeyfusqdlquxsmvnak.streamlit.app/
Monitoring: https://ml-nyctaxidemandpredictor-ywu8raur4dgutsjodzcap9.streamlit.app/

Project Organization
------------

```
ml-nyc_taxi_demand_predictor/
├── .github/workflows            # Github Actions pipelines. Execute the pipelines in src/pipelines.
├── LICENSE     
├── README.md                  
├── Makefile                     
├── pyproject.toml               # Poetry config file                     
├── models                       # Serialized models
├── notebooks                    # Jupyter notebooks.
└── src                          # Source code for use in this project.
    ├── helpers                  # Helpers and utilities.
    ├── pipelines                # Pipelines for feature engineering, training and inference.
    └── ui                       # Streamlit web apps.
```
