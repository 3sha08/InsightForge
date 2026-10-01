import pandas as pd

from insightforge.visualization import plot_line


def test_plot_line():
    df = pd.DataFrame(
        {
            "year": [2022, 2023, 2024],
            "gdp": [100, 110, 120],
        }
    )

    fig, ax = plot_line(
        df,
        x="year",
        y="gdp",
    )

    assert ax.get_xlabel() == "year"
    assert ax.get_ylabel() == "gdp"
    assert ax.get_title() == "gdp by year"

    fig.clf()