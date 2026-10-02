"""Tests for pricing logic."""

import pytest
from app.models.product import Product
from app.services.pricing import calculate_line_total


def test_unit_pricing():
    """Test per-unit pricing: 2 jars at $9.80 each = $19.60."""
    product = Product("Tahini 375g jar", 9.80, "unit")
    total = calculate_line_total(product, 2, 9.80)
    assert total == 19.60


def test_kg_pricing():
    """Test per-kg pricing: 1.5 kg at $3.40/kg = $5.10."""
    product = Product("Rolled oats", 3.40, "kg")
    total = calculate_line_total(product, 1.5, 3.40)
    assert total == 5.10


def test_kg_pricing_decimal():
    """Test per-kg pricing with decimal: 0.25 kg at $32.00/kg = $8.00."""
    product = Product("Coffee beans", 32.00, "kg")
    total = calculate_line_total(product, 0.25, 32.00)
    assert total == 8.00


def test_unit_pricing_rejects_decimal():
    """Unit-priced products cannot have decimal quantities."""
    product = Product("Eggs, dozen", 7.50, "unit")
    with pytest.raises(ValueError):
        calculate_line_total(product, 1.5, 7.50)
