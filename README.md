# Leaf Classifier

This project aims at building a classifier to identify Coniferous and Deciduous leaves with small data set.

The most important notebook is `01-leaf-classifier.ipynb` which is under `/exploration/notebooks/classify_leaf/`.

## Project Structure

```
.
├── README.md
├── docs
├── environment.yml            # conda environment file
├── exploration                # Exploratory analysis
│   ├── data
│   │   ├── processed
│   │   └── raw
│   └── notebooks
│       ├── classify_leaf      # leaf classifier
│       └── download_images    # download data
├── leaf_classifier            # package for modularized code
│   ├── __init__.py
│   └── util
│       ├── __init__.py
│       └── image.py
├── requirements.txt           # pip requirements file
└── setup.py                   # setup file for building python package
```

## Installation
### Install using conda
```
conda env create -f environment.yml
```

### Install using pip
```
pip install -r requirements.txt
```