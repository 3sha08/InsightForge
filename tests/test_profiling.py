import pandas as pd

from insightforge.profiling import dataset_profile


def test_dataset_profile():
    df = pd.DataFrame(
        {
            "country": ["India", "USA", "USA"],
            "gdp": [100, 200, 200],
            "inflation": [5.0, None, None],
        }
    )

    result = dataset_profile(df)

    assert result["rows"] == 3
    assert result["columns"] == 3
    assert result["missing_values"] == 2
    assert result["duplicate_rows"] == 1
    assert result["numeric_columns"] == 2
    assert result["non_numeric_columns"] == 1