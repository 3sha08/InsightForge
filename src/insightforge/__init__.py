from insightforge.aggregation import aggregate_mean
from insightforge.cleaning import drop_missing_rows
from insightforge.indicators import (
    calculate_grouped_index,
    calculate_index,
)
from insightforge.loaders import load_csv
from insightforge.profiling import dataset_profile
from insightforge.statistics import correlation_matrix
from insightforge.timeseries import moving_average
from insightforge.transformations import (
    calculate_grouped_growth_rate,
    calculate_growth_rate,
    calculate_percentage_change,
)
from insightforge.validation import (
    check_duplicates,
    check_missing_values,
    check_required_columns,
)

__all__ = [
    "aggregate_mean",
    "calculate_grouped_growth_rate",
    "calculate_grouped_index",
    "calculate_growth_rate",
    "calculate_index",
    "calculate_percentage_change",
    "check_duplicates",
    "check_missing_values",
    "check_required_columns",
    "correlation_matrix",
    "dataset_profile",
    "drop_missing_rows",
    "load_csv",
    "moving_average",
]

__version__ = "0.1.0"