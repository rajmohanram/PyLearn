# content of test_sample.py
def sum_of_numbers(x: int, y: int) -> int:
    return x + y


def test_sum_of_numbers():
    assert sum_of_numbers(3, 3) == 6


def product_of_numbers(x: int, y: int) -> int:
    return x * y


def test_product_of_numbers():
    assert product_of_numbers(3, 3) == 9
