import pandas as pd
import pytest

from insightforge.timeseries import moving_average


def test_moving_average():
    series = pd.Series([10, 20, 30, 40])

    result = moving_average(series, window=3)

    assert pd.isna(result.iloc[0])
    assert pd.isna(result.iloc[1])
    assert result.iloc[2] == pytest.approx(20.0)
    assert result.iloc[3] == pytest.approx(30.0)