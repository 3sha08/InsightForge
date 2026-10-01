import pandas as pd

from insightforge.cleaning import drop_missing_rows


def test_drop_missing_rows():
    df = pd.DataFrame(
        {
            "country": ["India", "USA", None],
            "gdp": [100, None, 300],
        }
    )

    result = drop_missing_rows(
        df,
        subset=["country", "gdp"],
    )

    assert len(result) == 1
    assert result.iloc[0]["country"] == "India"