def sum_activation(a):
  """Returns the sum of the values."""
  return sum(a)

def test_calculate_sum_activation():
  data = [1, 2, 3]
  result = sum_activation(data)
  assert result == 6

def test_calculate_sum_activation_fails():
  data = [1, 2, 3]
  result = sum_activation(data)
  assert result == 5
