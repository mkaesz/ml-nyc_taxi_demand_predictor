import os

from dotenv import load_dotenv
import pandas as pd

from src.paths import PARENT_DIR

# load key-value pairs from .env file located in the parent directory
load_dotenv(PARENT_DIR / '.env')

HOPSWORKS_PROJECT_NAME = 'taxi_demand'
HOPSWORKS_API_KEY = os.environ['HOPSWORKS_API_KEY']

def get_historical_rides() -> pd.DataFrame:

    from datetime import datetime
    import pandas as pd
    from src.data import load_raw_data

    from_year = 2023
    to_year = datetime.now().year
    print(f'Downloading raw data from {from_year} to {to_year}')

    rides = pd.DataFrame()
    for year in range(from_year, to_year+1):
        
        # download data for the whole year
        rides_one_year = load_raw_data(year)
        
        # append rows
        rides = pd.concat([rides, rides_one_year])

    return rides

def run():

    rides = get_historical_rides()

    from src.data import transform_raw_data_into_ts_data
    ts_data = transform_raw_data_into_ts_data(rides)

    # make sure UTC timezone is set
    ts_data['pickup_hour'] = pd.to_datetime(ts_data['pickup_hour'], utc=True)

    from src.config import FEATURE_GROUP_METADATA
    from src.feature_store_api import get_or_create_feature_group
    feature_group = get_or_create_feature_group(FEATURE_GROUP_METADATA)

    feature_group.insert(ts_data, write_options={"wait_for_job": False})

if __name__ == '__main__':
    run()