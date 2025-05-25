import pytest
from src.transform import transform

sample_data = [{"address": {"city": "Paris"}}, {"address": {"city": "Tokyo"}}]

def test_transform():
    result = transform(sample_data)
    assert result == {"Paris": 1, "Tokyo": 1}