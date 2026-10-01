import pandas as pd
import pytest

from insightforge.indicators import (
    calculate_grouped_index,
    calculate_index,
)

def test_calculate_index():
    series = pd.Series([200, 220, 250])

    result = calculate_index(series)

    assert result.iloc[0] == pytest.approx(100.0)
    assert result.iloc[1] == pytest.approx(110.0)
    assert result.iloc[2] == pytest.approx(125.0)

def test_calculate_grouped_index():
    df = pd.DataFrame(
        {
            "country": ["India", "India", "USA", "USA"],
            "gdp": [3500, 3800, 27000, 28500],
        }
    )

    result = calculate_grouped_index(
        df,
        group_by="country",
        value_column="gdp",
    )

    assert result.iloc[0] == pytest.approx(100.0)
    assert result.iloc[1] == pytest.approx(108.57142857)
    assert result.iloc[2] == pytest.approx(100.0)
    assert result.iloc[3] == pytest.approx(105.55555556)