"""Pricing logic for Greenhill Food Co-op Ordering System.

This module handles the core domain logic:
- Per-unit pricing: quantity multiplied by unit price
- Per-kilogram pricing: actual weight multiplied by price per kg
"""


def calculate_line_total(product, quantity, unit_price):
    """Calculate the total for an order line.

    Args:
        product: The Product object being ordered
        quantity: The amount ordered (integer for units, float for kg)
        unit_price: The price at the time of order

    Returns:
        float: The line total, rounded to 2 decimal places

    Raises:
        ValueError: If quantity is invalid for the pricing type
    """
    if product.pricing_type == 'unit':
        # Unit-priced products require a whole number
        if not isinstance(quantity, int):
            raise ValueError("Unit-priced products require a whole number")
        return round(quantity * unit_price, 2)

    elif product.pricing_type == 'kg':
        # Kilogram-priced products can have decimal quantities
        return round(quantity * unit_price, 2)

    else:
        raise ValueError(f"Unknown pricing type: {product.pricing_type}")
