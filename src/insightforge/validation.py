import pandas as pd


def check_missing_values(df: pd.DataFrame) -> pd.Series:
    """Return the number of missing values in each column."""
    return df.isna().sum()
def check_duplicates(df: pd.DataFrame) -> int:
    """Return the number of duplicate rows."""
    return int(df.duplicated().sum())
def check_required_columns(
    df: pd.DataFrame,
    required_columns: list[str],
) -> list[str]:
    """Return required columns that are missing from the DataFrame."""
    return [column for column in required_columns if column not in df.columns]