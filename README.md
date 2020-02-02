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

<img src="exploration/data/raw/misc/Coniferous_45e7ed10a2154988a72ae959261b6083.jpg" width="300" height="300" />

`{'coniferous': 0.877267, 'deciduous': 0.122732975}`

<img src="exploration/data/raw/misc/Deciduous_59b21ec3ee184ef4809747ddd8254bc5.jpg" width="300" height="300" />

`{'coniferous': 0.054971006, 'deciduous': 0.94502896}`

<img src="exploration/data/raw/misc/Coniferous_1c9168a756474262869fd82093c583cb.jpg" width="300" height="300" />

`{'coniferous': 0.9271934, 'deciduous': 0.0728066}`

<img src="exploration/data/raw/misc/images.jpg" width="300" height="300" />

`{'coniferous': 0.47172523, 'deciduous': 0.52827483}`
