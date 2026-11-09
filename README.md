# Laptop Price Prediction

Pipeline of 5 notebooks + a Streamlit app.

## Setup
```
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

## Run
```
python main.py                 # runs all notebooks in order
streamlit run app.py           # starts the web app
```

## Folder structure
```
data/
  raw/                Raw_laptop_data.csv          (original, untouched)
  processed/          01_ingested.csv, 02_preprocessed.csv, 03_features.csv
  artifacts/          model.joblib, scaler.joblib, label_encoder.joblib, metrics.json
    baseline/         baseline_pipeline.joblib, baseline_results.csv
common.py             shared paths, columns, helper functions
data_ingestion.ipynb
data_preprocessing.ipynb
data_feature_engineering.ipynb
model_training.ipynb
model_tuning.ipynb
main.py               runs the 5 notebooks in order
app.py                Streamlit app
```

## Saved artifacts
| File | What it is |
|------|------------|
| `model.joblib` | Final regressor (trained on log(Price)) |
| `scaler.joblib` | `StandardScaler` for numeric columns |
| `label_encoder.joblib` | `OrdinalEncoder` for categorical columns (unknown value -> -1) |
| `metrics.json` | Model name, CV / test scores, best parameters |

Prediction = `scaler` + `label_encoder` -> `model` -> `exp(output)` (see `predict_price` in `common.py`).
Open the notebooks with the project folder as working directory so `import common` works.
