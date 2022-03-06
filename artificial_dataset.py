import numpy as np
from numpy.lib import recfunctions as rfn
import pandas as pd

mean = [2.5, 78, -67, 457]
cov = [
    [1.000, 0.000, -75.0, -10.0],
    [0.000, 1.000, 42.00, 2345.],
    [-75.0, 42.00, 1.000, 689.0],
    [-10.0, 2345., 689.0, 1.000],
]
size = 300
correlated_lines = np.random.multivariate_normal(mean, cov, size=size)
correlated_columns = correlated_lines.T
int_column = np.random.randint(80, size=size)
normal_column = np.random.normal(56, 2.5, size=size)
dataset = rfn.merge_arrays(
    (
    correlated_columns[0],
    correlated_columns[1],
    correlated_columns[2],
    correlated_columns[3],
    int_column,
    normal_column,
    )
)

pd.DataFrame(dataset).to_csv('sample.csv')