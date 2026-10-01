import pandas as pd


def dataset_profile(df: pd.DataFrame) -> dict:
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "numeric_columns": int(df.select_dtypes(include="number").shape[1]),
        "non_numeric_columns": int(df.select_dtypes(exclude="number").shape[1]),
    }