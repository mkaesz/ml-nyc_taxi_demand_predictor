.PHONY: init features training inference 

# downloads Poetry and installs all dependencies from pyproject.toml
init:
	curl -sSL https://install.python-poetry.org | python3 -
	poetry install

# generates new batch of features and stores them in the feature store
features:
	poetry run python src/pipelines/feature_pipeline.py

# trains a new model and stores it in the model registry
training:
	poetry run python src/pipelines/training_pipeline.py

# generates predictions and stores them in the feature store
inference:
	poetry run python src/pipelines/inference_pipeline.py

# backfills the feature store with historical data
backfill:
	poetry run python src/pipelines/backfill_feature_group.py

# starts the Streamlit app
frontend:
	poetry run streamlit run src/ui/frontend.py

monitoring:
	poetry run streamlit run src/ui/frontend_monitoring.py
