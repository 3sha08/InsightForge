import pandas as pd
import pytest

from insightforge.transformations import (
    calculate_cagr,
    calculate_grouped_growth_rate,
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

def test_calculate_grouped_growth_rate():
    df = pd.DataFrame(
        {
            "country": ["India", "India", "USA", "USA"],
            "gdp": [3500, 3800, 27000, 28500],
        }
    )

    result = calculate_grouped_growth_rate(
        df,
        group_by="country",
        value_column="gdp",
    )

    assert pd.isna(result.iloc[0])
    assert result.iloc[1] == pytest.approx(8.57142857)
    assert pd.isna(result.iloc[2])
    assert result.iloc[3] == pytest.approx(5.55555556)

def test_calculate_cagr():
    result = calculate_cagr(
        start_value=100,
        end_value=121,
        periods=2,
    )

    assert result == pytest.approx(10.0)

def test_calculate_cagr_invalid_periods():
    with pytest.raises(ValueError, match="periods must be greater than 0"):
        calculate_cagr(
            start_value=100,
            end_value=121,
            periods=0,
        )