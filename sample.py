# Load data
import pandas as pd
import numpy as np

path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)


# Simple Polynomial Regression
p = simple_polynomial_regression(df, 'highway-mpg', 'price', 13)
plt = get_spr_visualization(df, p, 'highway-mpg', 'price')


# Multiple Polynomial Regression
independent_names_1 = ['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']
independent_names_2 = ['normalized-losses', 'highway-mpg']

pipe1 = multiple_polynomia_regression(df, independent_names_1, 'price', 2)
pipe2 = multiple_polynomia_regression(df, independent_names_2, 'price', 2)

get_mlr_plot(df, 'price', [pipe1, pipe2], [independent_names_1, independent_names_2])



