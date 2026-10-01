import pandas as pd
import pytest

from insightforge.aggregation import aggregate_mean


def test_aggregate_mean():
    df = pd.DataFrame(
        {
            "country": ["India", "India", "USA"],
            "inflation": [5.0, 7.0, 4.0],
        }
    )

    result = aggregate_mean(
        df,
        group_by="country",
        value_column="inflation",
    )

    india_value = result.loc[
        result["country"] == "India",
        "inflation",
    ].iloc[0]

    assert india_value == pytest.approx(6.0)