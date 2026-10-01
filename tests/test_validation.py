import pandas as pd

from insightforge.validation import (
    check_duplicates,
    check_missing_values,
    check_required_columns,
)


def test_check_missing_values():
    df = pd.DataFrame(
        {
            "gdp": [100, None, 300],
            "inflation": [5.2, 6.1, None],
        }
    )

    result = check_missing_values(df)

    assert result["gdp"] == 1
    assert result["inflation"] == 1
def test_check_duplicates():
    df = pd.DataFrame(
        {
            "country": ["India", "USA", "India"],
            "gdp": [100, 200, 100],
        }
    )

    result = check_duplicates(df)

    assert result == 1
def test_check_required_columns():
    df = pd.DataFrame(
        {
            "country": ["India", "USA"],
            "gdp": [100, 200],
        }
    )

    result = check_required_columns(
        df,
        ["country", "gdp", "inflation"],
    )

    assert result == ["inflation"]