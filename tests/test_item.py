"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_init(example):
    assert example.name == "Смартфон"
    assert example.price == 10000
    assert example.quantity == 20


def test_calculate_total_price(example):
    assert example.calculate_total_price() == 200_000


def test_apply_discount(example):
    example.apply_discount()
    assert example.price == 8000

