import pandas as pd


def calculate_index(
    series: pd.Series,
    base_value: float = 100.0,
) -> pd.Series:
    first_value = series.iloc[0]
    return (series / first_value) * base_value
def calculate_grouped_index(
    df: pd.DataFrame,
    group_by: str,
    value_column: str,
    base_value: float = 100.0,
) -> pd.Series:
    return df.groupby(group_by)[value_column].transform(
        lambda series: (series / series.iloc[0]) * base_value
    )