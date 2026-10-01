import pandas as pd


def summarize_numeric(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe(include="number").T