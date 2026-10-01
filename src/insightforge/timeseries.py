import pandas as pd


def moving_average(
    series: pd.Series,
    window: int = 3,
) -> pd.Series:
    return series.rolling(window=window).mean()