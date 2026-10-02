"""Product model for Greenhill Food Co-op Ordering System."""


class Product:
    """Represents a product available for order.

    Products are sold either by unit (e.g., a jar of tahini)
    or by weight (e.g., oats, rice, lentils).
    """

    def __init__(self, name, price, pricing_type, bay=None):
        """Initialize a new product.

        Args:
            name: Product name
            price: Price per unit or per kilogram
            pricing_type: Either 'unit' or 'kg'
            bay: Optional storage bay location in the hall
        """
        self.name = name
        self.price = price
        self.pricing_type = pricing_type
        self.bay = bay
        self.available = True

    def __repr__(self):
        """Return a string representation of the product."""
        return f"<Product {self.name}: ${self.price}/{self.pricing_type}>"
