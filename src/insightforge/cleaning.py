import pandas as pd


def drop_missing_rows(
    df: pd.DataFrame,
    subset: list[str] | None = None,
) -> pd.DataFrame:
    return df.dropna(subset=subset).reset_index(drop=True)