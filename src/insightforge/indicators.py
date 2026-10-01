import pandas as pd


def calculate_index(
    series: pd.Series,
    base_value: float = 100.0,
) -> pd.Series:
    first_value = series.iloc[0]
    return (series / first_value) * base_value