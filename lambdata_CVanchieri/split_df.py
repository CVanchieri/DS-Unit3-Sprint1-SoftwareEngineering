"""
Helpers - A bit of helper code for train/val/test split.
"""
# import the sklearn library.
import sklearn
# import train_test_split from sklearn.
from sklearn import train_test_split

# create a description title.
title = "A bit of helper code for train/val/test split"

# split into train and val (80/20 split, replace 'class/asd').
train, val = train_test_split(df, train_size=0.80, test_size=0.20,
                              stratify=df, random_state=42)

# split into train and test (80/20 split, replace 'class/asd').
train, test = train_test_split(train, train_size=0.80, test_size=0.20,
                               stratify=train, random_state=42)

# show the data frame shapes.
train.shape, val.shape, test.shape
