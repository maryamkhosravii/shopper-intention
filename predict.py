import pandas as pd
import joblib
from scipy.stats.mstats import winsorize
from keras.models import load_model


model = load_model ("my_model.h5")
pipeline = joblib.load ("preprocessor.pkl")



def input_preprocessing (df: pd.DataFrame):
    df['ProductRelated_Duration'] = winsorize (df['ProductRelated_Duration'], limits=(0.05, 0.05))
    processed = pipeline.transform (df)
    return processed


def make_prediction (df: pd.DataFrame):
    processed = input_preprocessing (df)
    prob = model.predict (processed)[0][0]
    label = int (prob > 0.5)
    return float (prob), label