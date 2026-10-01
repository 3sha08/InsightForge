import pandas as pd

from insightforge.loaders import load_csv


def test_load_csv(tmp_path):
    file_path = tmp_path / "sample.csv"

    expected = pd.DataFrame(
        {
            "country": ["India", "USA"],
            "gdp": [100, 200],
        }
    )

    expected.to_csv(file_path, index=False)

    result = load_csv(file_path)

    pd.testing.assert_frame_equal(result, expected)