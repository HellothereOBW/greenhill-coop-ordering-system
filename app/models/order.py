"""Order model for Greenhill Food Co-op Ordering System."""


class OrderLine:
    """A single line in an order."""

    def __init__(self, product, quantity, unit_price):
        """Initialize a new order line.

        Args:
            product: The Product object being ordered
            quantity: Amount ordered (integer for units, float for kg)
            unit_price: Price at the time the order was placed
        """
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price

    def line_total(self):
        """Calculate the total for this order line."""
        return round(self.quantity * self.unit_price, 2)


class Order:
    """Represents a member's order for a round."""

    def __init__(self, member, round_id):
        """Initialize a new order.

        Args:
            member: The Member object placing the order
            round_id: The round identifier this order belongs to
        """
        self.member = member
        self.round_id = round_id
        self.lines = []
        self.status = 'open'

    def add_line(self, order_line):
        """Add an order line to this order."""
        self.lines.append(order_line)

    def order_total(self):
        """Calculate the total value of this order."""
        return round(sum(line.line_total() for line in self.lines), 2)
