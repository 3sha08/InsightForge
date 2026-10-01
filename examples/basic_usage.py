import pandas as pd

from insightforge.aggregation import aggregate_mean
from insightforge.indicators import calculate_grouped_index
from insightforge.transformations import calculate_grouped_growth_rate
from insightforge.validation import (
    check_duplicates,
    check_missing_values,
)


df = pd.DataFrame(
    {
        "country": ["India", "India", "USA", "USA"],
        "year": [2023, 2024, 2023, 2024],
        "gdp": [3500, 3800, 27000, 28500],
        "inflation": [5.7, 4.9, 4.1, 3.2],
    }
)

print("Missing values:")
print(check_missing_values(df))

print("\nDuplicate rows:")
print(check_duplicates(df))

print("\nAverage inflation by country:")
print(
    aggregate_mean(
        df,
        group_by="country",
        value_column="inflation",
    )
)

print("\nGDP growth rate by country:")
print(
    calculate_grouped_growth_rate(
        df,
        group_by="country",
        value_column="gdp",
    )
)

print("\nGDP index by country:")
print(
    calculate_grouped_index(
        df,
        group_by="country",
        value_column="gdp",
    )
)