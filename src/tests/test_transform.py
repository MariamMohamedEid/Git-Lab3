import pytest
from ..transform import transform  # Relative import
sample_data = [{"address": {"city": "Paris"}}, {"address": {"city": "Tokyo"}}]

def test_transform():
    result = transform(sample_data)
    assert result == {"Paris": 1, "Tokyo": 1}