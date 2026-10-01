import pandas as pd


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df.corr(numeric_only=True)