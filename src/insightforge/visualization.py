import pandas as pd
import matplotlib.pyplot as plt


def plot_line(
    df: pd.DataFrame,
    x: str,
    y: str,
):
    fig, ax = plt.subplots()
    ax.plot(df[x], df[y])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(f"{y} by {x}")
    return fig, ax