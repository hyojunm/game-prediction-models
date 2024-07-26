import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler, QuantileTransformer, Normalizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.linear_model import LinearRegression, LogisticRegression, PoissonRegressor
from sklearn.tree import DecisionTreeRegressor

import graphviz
from sklearn.tree import export_graphviz
from IPython.display import Image

import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

from analysis import get_feature_importances, visualize_decision_trees, get_vif, wl_accuracy, season_record, runs_per_game


# using game_data_v6.csv
season_indices = {
    2015: (0, 0),
    2016: (0, 0),
    2017: (0, 2430),
    2018: (2430, 4861),
    2019: (4861, 7290),
    2020: (7290, 8188),
    2021: (8188, 10617),
    2022: (10617, 13047),
    2023: (13047, 15477),
    2024: (0, 0)
}


def get_season_index(year):
    if year < 2015 or year > 2024:
        return (0, 0)
        
    return season_indices[year]


def separate_data(df, start, end):
    return pd.concat([df.iloc[0:start], df.iloc[end:]]), df.iloc[start:end]


# create the appropriate training and testing data based on home/away, dropping columns as needed
def create_data(df, drop_cols=['away_score', 'home_score', 'away_team', 'home_team'],
                y_col='away_score', split_by='random', season=2023):
    y = df[y_col]
    x = df.drop(drop_cols, axis=1)

    if split_by == 'season':
        season_start, season_end = get_season_index(season)
        x_train, x_test = separate_data(x, season_start, season_end)
        y_train, y_test = separate_data(y, season_start, season_end)
    else:
        x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True)
    
    return x_train, x_test, y_train, y_test