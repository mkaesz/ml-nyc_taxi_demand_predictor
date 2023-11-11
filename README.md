# Taxi demand predictor service
==============================
Predict Taxi Demand in New York City

## Quick setup

1. Create a free account at Hopsworks and export Hopsworks API key and project
    ```
    # Bash
   $ export HOPSWORKS_API_KEY="asd123"
   $ export HOPSWORKS_PROJECT_NAME="myproject"
    ```

2. Clone the project, cd into the project folder and run
    ```
    $ git clone https://github.com/mkaesz/ml-nyc_taxi_demand_predictor.git
    $ ch ml-nyc_taxi_demand_predictor
    $ make init
    ```

5. Backfill the feature group with historical data
    ```
    $ make backfill
    ```

6. Train an ML model
    ```
    $ make training
    ```

7. Run the feature pipeline for the last hour
    ```
    $ make features
    ```

8. Generate predictions for the last hour
    ```
    $ make inference
    ```

## Wanna see it in action?
### Hosted on Streamlit Cloud
- [Live Dashboard with model predictions](https://ml-nyctaxidemandpredictor-benvmeyfusqdlquxsmvnak.streamlit.app/)
- [Live Dashboard with model monitoring ](https://ml-nyctaxidemandpredictor-ywu8raur4dgutsjodzcap9.streamlit.app/)

### Run it locally
Model predictions

    $ make frontend
    
Model monitoring

    $ make monitoring

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
