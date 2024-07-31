import pandas as pd
import matplotlib.pyplot as plt

import graphviz
from sklearn.tree import export_graphviz
from IPython.display import Image

import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

from data_format import get_season_index


# figure out which features (columns) are being considered most by the model
def get_feature_importances(cols, model):
    feature_importances = {
        'feature': [],
        'weight': []
    }
    
    for i in range(len(cols)):
        feature_importances['feature'].append(cols[i])
        feature_importances['weight'].append(round(model.feature_importances_[i] * 100, 2))
    
    return pd.DataFrame(feature_importances)


# visualizing decision trees
# https://www.datacamp.com/tutorial/random-forests-classifier-python
def visualize_decision_trees(model, cols, n_trees=1, max_depth=2):
    for i in range(n_trees):
        tree = model.estimators_[i]
        dot_data = export_graphviz(tree,
                                   feature_names=cols,  
                                   filled=True,  
                                   max_depth=max_depth, 
                                   impurity=False, 
                                   proportion=True)
        graph = graphviz.Source(dot_data)
        display(graph)


# get variance inflation factors for each feature - testing for multicollinearity
# https://www.datasklr.com/ols-least-squares-regression/multicollinearity
def get_vif(x):
    x_temp = sm.add_constant(x)

    vif = pd.DataFrame()
    vif['feature'] = x_temp.columns
    vif['variance_inflation_factor'] = [variance_inflation_factor(x_temp.values, i) for i in range(x_temp.values.shape[1])]
    
    return vif


# given a results dataframe, calculate the accuracy (in %) of the model in terms of predicting wins/losses
def wl_accuracy(results):
    num_correct = 0
    num_incorrect = 0
    
    for i in range(len(results)):
        game = results.iloc[i]
    
        pred_result = 1 if game['home_pred'] > game['away_pred'] else 0 # where 1 = home team wins
        actual_result = 1 if game['home_true'] > game['away_true'] else 0
        
        if pred_result == actual_result:
            num_correct += 1
        else:
            num_incorrect += 1

    return (num_correct / (num_correct + num_incorrect)) * 100


# calculate season records based on predictions
def season_record(df, results, season=2023):
    team_records = {}
    num_games = 60 if season == 2020 else 162
    season_start, season_end = get_season_index(season)

    for i in range(len(results)):
        away_team = df['away_team'].iloc[season_start + i]
        home_team = df['home_team'].iloc[season_start + i]
        
        home_team_won = results['away_pred'].iloc[i] <= results['home_pred'].iloc[i]
    
        if away_team not in team_records:
            team_records[away_team] = 0
    
        if home_team not in team_records:
            team_records[home_team] = 0
    
        team_records[away_team] += 1 if not home_team_won else 0
        team_records[home_team] += 1 if home_team_won else 0

    print('Season records:')
    count = 0
    
    for team in sorted(team_records, key=lambda x: team_records[x], reverse=True):
        count += 1
        print(f'{team}: {team_records[team]}-{num_games - team_records[team]}', end='\t')
        
        if count % 5 == 0:
            print()


# calculate each team's runs scored per game based on predictions
def runs_per_game(df, results, season=2023):
    runs_scored = {}
    num_games = 60 if season == 2020 else 162
    season_start, season_end = get_season_index(season)

    for i in range(len(results)):
        away_team = df['away_team'].iloc[season_start + i]
        home_team = df['home_team'].iloc[season_start + i]
        
        if away_team not in runs_scored:
            runs_scored[away_team] = 0
    
        if home_team not in runs_scored:
            runs_scored[home_team] = 0

        runs_scored[away_team] += results['away_pred'].iloc[i]
        runs_scored[home_team] += results['home_pred'].iloc[i]

    print('Runs scored per game:')
    count = 0
    
    for team in sorted(runs_scored, key=lambda x: runs_scored[x], reverse=True):
        count += 1
        print(f'{team}: {round(runs_scored[team] / num_games, 2)} ({round(runs_scored[team])})', end='\t')
        
        if count % 5 == 0:
            print()


# test models for n number of times and retrieve summary statistics
def test_n(model_away, model_home,
           x_train_away, y_train_away, x_train_home, y_train_home,
           x_test_away, y_test_away, x_test_home, y_test_home,
           n_iter=100):
    acc = []

    for i in range(n_iter):
        model_away.fit(x_train_away, y_train_away)
        model_home.fit(x_train_home, y_train_home)
        
        pred_away = model_away.predict(x_test_away)
        pred_home = model_home.predict(x_test_home)
        
        results = pd.DataFrame({'away_pred': pred_away, 'home_pred': pred_home, 'away_true': y_test_away, 'home_true': y_test_home})
        results.describe()
        
        acc.append(wl_accuracy(results))
    
    print(pd.DataFrame(acc).describe())
    
    plt.hist(acc, color='b')

    plt.xlabel('Accuracy (%)')
    plt.ylabel('Frequency')
    
    plt.show()