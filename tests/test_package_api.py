import insightforge


def test_package_version():
    assert insightforge.__version__ == "0.1.0"


def test_public_api_exports():
    assert callable(insightforge.aggregate_mean)
    assert callable(insightforge.calculate_grouped_index)
    assert callable(insightforge.calculate_grouped_growth_rate)
    assert callable(insightforge.check_missing_values)