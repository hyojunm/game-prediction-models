# game-prediction-models

A collection of statistical models to predict the outcomes of Major League Baseball games.


### Clone repository

Navigate to your desired directory on the terminal, then clone the project repository:

```bash
git clone https://github.com/hyojunm/game-prediction-models.git
```

Then, move into the repository directory:

```bash
cd game-prediction-models
```

### Install dependencies

Ensure that you have the following dependencies installed:

* [Python 3](https://www.python.org/)
* [Jupyter Lab/Notebook](https://jupyter.org/)

To run some visualizations, `graphviz` may need to be installed with:

```bash
sudo apt install graphviz
```

### Set up environment

1. Create a virtual environment (replace `my_env` with a different name if you'd like)

```bash
python3 -m venv my_env
```

2. Activate the virtual environment

```bash
source my_env/bin/activate
```

3. Install Python packages

```bash
python3 -m pip install pandas scikit-learn matplotlib numpy graphviz statsmodels pybaseball ipykernel
```

4. Convert Jupyter Notebook files to Python scripts (replace `random_forest_regression.ipynb` with the Notebook file you'd like to see)

```bash
jupyter nbconvert --to script random_forest_regression.ipynb
```

### Run the project

Run the converted Python script with (replace `random_forest_regression.py` with the appropriate file name, if different):

```bash
python3 random_forest_regression.py
```

**Note:** Necessary data files are already included within the repository, so there is no need to run the `baseball_data_collection.ipynb` file again (unless you would like to edit the data).