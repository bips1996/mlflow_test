import os
import warnings
import sys

import pandas as pd

import mlflow

if __name__ == "__main__":
    filename = str(sys.argv[1])
    data = pd.read_csv(filename)
    with mlflow.start_run():
        print(data.head())

