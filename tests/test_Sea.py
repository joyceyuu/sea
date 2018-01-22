"""
Tests for `Sea` module.
"""

from Sea import Sea

def test_is_positive(integers):
    result = Sea.is_positive(integers)
    true_result = integers > 0
    assert (result == true_result)
