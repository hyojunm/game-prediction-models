# Analyzing regression models for predicting the outcomes of Major League Baseball games

### Build project

Navigate to your desired directory on the terminal, then clone the project repository:

```bash
git clone https://github.com/hyojunm/game-prediction-models.git
```

Then, move into the repository directory:

```bash
cd game-prediction-models
```

Ensure that you have the following dependencies installed:

* [Python 3](https://www.python.org/)
* [Jupyter Lab/Notebook](https://jupyter.org/)

To run some visualizations, `graphviz` may need to be installed with:

```bash
sudo apt install graphviz
```

Create a virtual environment (replace `my_env` with a different name if you'd like):

```bash
python3 -m venv my_env
```

Activate the virtual environment:

```bash
source my_env/bin/activate
```

Install necessary Python packages:

```bash
python3 -m pip install pandas scikit-learn matplotlib numpy graphviz statsmodels pybaseball ipykernel
```

### Run project

To run programs, you need to be in the `models` directory:

```bash
cd models/
```

Double check that you are in the correct directory:

```bash
pwd
```

The output should end in `.../game-prediction-models/models`.

Convert Jupyter Notebook files to Python scripts (replace `random_forest_regression.ipynb` with the Notebook file you'd like to see):

```bash
jupyter nbconvert --to script random_forest_regression.ipynb
```

Run the converted Python script with (replace `random_forest_regression.py` with the appropriate file name, if different):

```bash
python3 random_forest_regression.py
```

***Note:** Necessary data files are already included within the repository.*

### Game data version log

* `v1` : no weights applied
* `v2` : stats weighted based on recency (60%-25%-15%)
* `v3` : stats weighted based on recency and sample size
* `v4` : using stats from past 2 seasons (instead of past 3)
* `v5` : using adjusted default rookie values
* `v6` : default rookie values are applied only for completely new players
* `v7` : using traditional stats (instead of expected stats)
* `v8` : using traditional stats from past 3 seasons (not including current)
* `v9` : using expected stats from past 3 seasons (not including current)

***Note:** When not explicitly mentioned, all data is compiled using stats from the past 3 seasons, including the current season. Additionally, game data from `v6` onwards will use default rookie values for completely new players and personal averages for all other players.*

### Open written outputs

To view the written outputs, you need to be in the `documents` directory:

```bash
cd documents
```

Double check that you are in the correct directory:

```bash
pwd
```

The output should end in `.../game-prediction-models/documents`.

Then, run the following commands in order:

```bash
pdflatex paper.tex
bibtex paper.aux
pdflatex paper.tex
pdflatex paper.tex
open paper.pdf
```

To open the presentation, run the following command:

```bash
open presentation.pdf
```