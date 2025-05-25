import pytest
from src.extract import extract

def test_api_response():
    data = extract()
    assert isinstance(data, list)  # Ensure data is a list of users