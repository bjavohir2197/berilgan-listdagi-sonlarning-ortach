import pytest
import numpy as np
from your_module import calculate_mean_and_std

def test_calculate_mean_and_std():
    numbers = [1, 2, 3, 4, 5]
    mean, std = calculate_mean_and_std(numbers)
    assert np.isclose(mean, 3.0)
    assert np.isclose(std, 1.4142135623730951)

def test_calculate_mean_and_std_empty_list():
    numbers = []
    with pytest.raises(ZeroDivisionError):
        calculate_mean_and_std(numbers)

def test_calculate_mean_and_std_single_element():
    numbers = [5]
    mean, std = calculate_mean_and_std(numbers)
    assert np.isclose(mean, 5.0)
    assert np.isclose(std, 0.0)

def test_calculate_mean_and_std_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    mean, std = calculate_mean_and_std(numbers)
    assert np.isclose(mean, -3.0)
    assert np.isclose(std, 1.4142135623730951)
