import pandas as pd
from scipy.stats import f as stats_f, shapiro

_shapiro = shapiro  # backup
def shapiro(x):
    """
    Wrapper for the scipy.stats.shapiro function to allow for use the pandas.DataFrame.apply function
    """
    W, p = _shapiro(x)
    return pd.Series([W, p], index=['W', 'p'])




