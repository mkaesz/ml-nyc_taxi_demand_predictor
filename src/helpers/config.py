import os
from src.helpers.feature_store_api import FeatureGroupConfig, FeatureViewConfig


HOPSWORKS_PROJECT_NAME = os.getenv('HOPSWORKS_PROJECT_NAME')
HOPSWORKS_API_KEY = os.getenv('HOPSWORKS_API_KEY')

FEATURE_GROUP_NAME = 'time_series_hourly_feature_group'
FEATURE_GROUP_VERSION = 1
FEATURE_GROUP_METADATA = FeatureGroupConfig(
    name='time_series_hourly_feature_group',
    version=1,
    description='Feature group with hourly time-series data of historical taxi rides',
    primary_key=['pickup_location_id', 'pickup_hour'],
    event_time='pickup_hour',
)

# TODO: remove FEATURE_VIEW_NAME and FEATURE_VIEW_VERSION, and use FEATURE_VIEW_METADATA instead
FEATURE_VIEW_NAME = 'time_series_hourly_feature_view'
FEATURE_VIEW_VERSION = 1
FEATURE_VIEW_METADATA = FeatureViewConfig(
    name='time_series_hourly_feature_view',
    version=1,
    feature_group=FEATURE_GROUP_METADATA,
)

MODEL_NAME = "taxi_demand_predictor_next_hour"
MODEL_FILE_NAME = "taxi_demand_predictor_next_hour.pkl"

# TODO: remove MODEL_VERSION as it is not used anywhere
MODEL_VERSION = 10

# added for monitoring purposes
# TODO remove FEATURE_GROUP_MODEL_PREDICTIONS and use FEATURE_GROUP_PREDICTIONS_METADATA instead
FEATURE_GROUP_MODEL_PREDICTIONS = 'model_predictions_feature_group'
FEATURE_GROUP_PREDICTIONS_METADATA = FeatureGroupConfig(
    name='model_predictions_feature_group',
    version=1,
    description="Predictions generate by our production model",
    primary_key = ['pickup_location_id', 'pickup_hour'],
    event_time='pickup_hour',
)

# TODO remove FEATURE_VIEW_MODEL_PREDICTIONS and use FEATURE_VIEW_PREDICTIONS_METADATA instead
FEATURE_VIEW_MODEL_PREDICTIONS = 'model_predictions_feature_view'
FEATURE_VIEW_PREDICTIONS_METADATA = FeatureViewConfig(
    name='model_predictions_feature_view',
    version=1,
    feature_group=FEATURE_GROUP_PREDICTIONS_METADATA,
)

FEATURE_VIEW_MONITORING = 'predictions_vs_actuals_for_monitoring_feature_view'

# number of historical values our model needs to generate predictions
N_FEATURES = 24 * 28

# maximum Mean Absolute Error we allow our production model to have
# MAX_MAE = 4.0
MAX_MAE = 10.0