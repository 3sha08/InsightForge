import pandas as pd


def calculate_percentage_change(series: pd.Series) -> pd.Series:
    """Return percentage change between consecutive values."""
    return series.pct_change() * 100
def calculate_growth_rate(
    series: pd.Series,
    periods: int = 1,
) -> pd.Series:
    """Return percentage growth over the given number of periods."""
    return series.pct_change(periods=periods) * 100
def calculate_grouped_growth_rate(
    df: pd.DataFrame,
    group_by: str,
    value_column: str,
    periods: int = 1,
) -> pd.Series:
    return (
        df.groupby(group_by)[value_column]
        .pct_change(periods=periods)
        * 100
    )