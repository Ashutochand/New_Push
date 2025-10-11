import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test a list with multiple positive streaks, ensuring the longest is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    """Test that zeros and negative numbers correctly break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, -5, 6]) == 2

def test_all_positive_numbers():
    """Test a list composed entirely of positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_streak_at_the_end():
    """Test a list where the longest streak is at the end."""
    assert longest_positive_streak([1, 0, 3, 4, 5]) == 3

def test_single_element_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([42]) == 1

def test_single_element_non_positive():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-42]) == 0
    assert longest_positive_streak([0]) == 0

def test_mixed_positive_and_negative():
    """Test a more complex mixture of positive and negative numbers."""
    assert longest_positive_streak([-1, 2, 3, -4, 5, 6, 7, 8, 0, 9]) == 4