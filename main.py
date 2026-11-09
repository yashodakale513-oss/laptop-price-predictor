"""Run the whole pipeline: ingestion -> preprocessing -> features -> training -> tuning.

    python main.py

Each notebook is executed in order (outputs are saved back into the notebook).
The run stops at the first failure, because later notebooks depend on earlier outputs.
"""
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent

NOTEBOOKS = [
    "data_ingestion.ipynb",
    "data_preprocessing.ipynb",
    "data_feature_engineering.ipynb",
    "model_training.ipynb",
    "model_tuning.ipynb",
]


def run_notebook(nb: str) -> None:
    start = time.time()
    result = subprocess.run(
        [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--execute", "--to", "notebook", "--inplace", nb,
            "--ExecutePreprocessor.timeout=-1",
        ],
        cwd=ROOT,                      # notebooks import common.py and need this as cwd
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"[FAILED] {nb}\n{result.stderr}")
        sys.exit(1)
    print(f"[ OK ] {nb}  ({time.time() - start:.1f}s)")


if __name__ == "__main__":
    for notebook in NOTEBOOKS:
        run_notebook(notebook)
    print("\nPipeline finished. Start the app with:  streamlit run app.py")
