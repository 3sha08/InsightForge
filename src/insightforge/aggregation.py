import pandas as pd


def aggregate_mean(
    df: pd.DataFrame,
    group_by: str,
    value_column: str,
) -> pd.DataFrame:
    return (
        df.groupby(group_by, as_index=False)[value_column]
        .mean()
    )
