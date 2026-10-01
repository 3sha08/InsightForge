import pandas as pd

from insightforge.summary import summarize_numeric


def test_summarize_numeric():
    df = pd.DataFrame(
        {
            "gdp": [100, 200, 300],
            "inflation": [4.0, 5.0, 6.0],
            "country": ["India", "USA", "UK"],
        }
    )

    result = summarize_numeric(df)

    assert "gdp" in result.index
    assert "inflation" in result.index
    assert "country" not in result.index
    assert result.loc["gdp", "mean"] == 200