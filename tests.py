def sum_activation(a):
    """Returns the sum of the values."""
    if not isinstance(a, list):
        raise TypeError("Input must be a list")
    return sum(a)


def test_calculate_sum_activation():
    data = [1, 2, 3]
    result = sum_activation(data)
    assert result == 6


def test_calculate_sum_activation_throws():
    import pytest

    with pytest.raises(TypeError):
        sum_activation("not a list")
