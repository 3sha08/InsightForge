import pandas as pd
import pytest

from insightforge.statistics import correlation_matrix


def test_correlation_matrix():
    df = pd.DataFrame(
        {
            "gdp": [100, 200, 300],
            "consumption": [50, 100, 150],
        }
    )

    result = correlation_matrix(df)

    assert result.loc["gdp", "consumption"] == pytest.approx(1.0)