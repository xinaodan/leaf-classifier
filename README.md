# Leaf Classifier

This project aims at building a classifier to identify Coniferous and Deciduous leaves with small data set.

The most important notebook is `01-leaf-classifier.ipynb` which is under `/exploration/notebooks/classify_leaf/`.

The report in `/docs/` has more details about the project.

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

## Introduction

Transfer Learning technique is applied in the project. 

More specifically, the model is built on top of the MobileNet model with pre-trained ImageNet weights.

## Data

Only Coniferous and Deciduous leaf images are included in the training and validation data sets.

## Result

With image augmentation, the average validation accuracy is around 97% after 50 epochs.

The average validation accuracy is around 95% without image augmentation.

Here are some predictions on images not in the training data:

<img src="https://biomesbylenhardt.pbworks.com/f/DSCN0103.JPG" height="400" width="400"/>

{'coniferous': 0.877267, 'deciduous': 0.122732975}

<img src="https://us.123rf.com/450wm/alexeyzet/alexeyzet1103/alexeyzet110300007/8977117-vector-illustration-cartoon-tree-isolated-on-white-background.jpg?ver=6" height="400" width="400"/>

{'coniferous': 0.054971006, 'deciduous': 0.94502896}

<img src="https://c.wallhere.com/photos/84/91/canada_lake_coast_trees_coniferous_water_transparent_reflection-780184.jpg!d" height="400" width="600"/>

{'coniferous': 0.9271934, 'deciduous': 0.0728066}

<img src="https://www.postable.com/blog/wp-content/uploads/2018/06/puppy2.jpg" height="400" width="600"/>

{'coniferous': 0.47172523, 'deciduous': 0.52827483}