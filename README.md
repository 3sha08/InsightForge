# InsightForge

[![Tests](https://github.com/3sha08/InsightForge/actions/workflows/tests.yml/badge.svg)](https://github.com/3sha08/InsightForge/actions/workflows/tests.yml)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

InsightForge is a reusable Python analytics toolkit for economic and data analysis.

## Installation

Clone the repository and install InsightForge in editable mode:

```bash
git clone https://github.com/3sha08/InsightForge.git
cd InsightForge
python -m venv .venv
python -m pip install -e ".[dev]"
```

## Quick Start

```python
import pandas as pd

from insightforge import (
    calculate_grouped_growth_rate,
    calculate_grouped_index,
    dataset_profile,
)

df = pd.DataFrame(
    {
        "country": ["India", "India", "USA", "USA"],
        "year": [2023, 2024, 2023, 2024],
        "gdp": [3500, 3800, 27000, 28500],
    }
)

print(dataset_profile(df))

print(
    calculate_grouped_growth_rate(
        df,
        group_by="country",
        value_column="gdp",
    )
)

print(
    calculate_grouped_index(
        df,
        group_by="country",
        value_column="gdp",
    )
)
```

## Project Structure

```text
InsightForge/
├── .github/
│   └── workflows/
│       └── tests.yml
├── examples/
│   └── basic_usage.py
├── src/
│   └── insightforge/
│       ├── __init__.py
│       ├── aggregation.py
│       ├── cleaning.py
│       ├── indicators.py
│       ├── loaders.py
│       ├── profiling.py
│       ├── statistics.py
│       ├── summary.py
│       ├── timeseries.py
│       ├── transformations.py
│       ├── validation.py
│       └── visualization.py
├── tests/
├── LICENSE
├── README.md
└── pyproject.toml
```


## Current Features

- Data validation
- Missing-value checks
- Duplicate detection
- Required-column validation
- Data cleaning
- Percentage-change calculations
- Growth-rate calculations
- Grouped growth-rate calculations
- Aggregation
- Correlation analysis
- Economic index calculations
- Grouped economic index calculations
- Moving averages
- CSV loading
- Dataset profiling
- Numeric dataset summaries
- Basic line-chart visualization

## Development Status

Version: 0.1.0

InsightForge is currently under active development as the reusable analytics package supporting EconLens.