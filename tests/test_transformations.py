import pandas as pd
import pytest

from insightforge.transformations import (
    calculate_growth_rate,
    calculate_percentage_change,
)


def test_calculate_percentage_change():
    series = pd.Series([100, 110, 121])

    result = calculate_percentage_change(series)

    assert result.iloc[1] == pytest.approx(10)
    assert result.iloc[2] == pytest.approx(10)

def test_calculate_growth_rate():
    series = pd.Series([100, 120, 150])

    result = calculate_growth_rate(series)

    assert result.iloc[1] == pytest.approx(20)
    assert result.iloc[2] == pytest.approx(25)