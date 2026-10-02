"""Member model for Greenhill Food Co-op Ordering System."""


class Member:
    """Represents a member household in the co-op."""

    def __init__(self, member_number, name, phone, email=None):
        """Initialize a new member.

        Args:
            member_number: Unique member identifier (e.g., M-094)
            name: Full name of the member
            phone: Contact phone number
            email: Optional email address
        """
        self.member_number = member_number
        self.name = name
        self.phone = phone
        self.email = email
        self.active = True

    def __repr__(self):
        """Return a string representation of the member."""
        return f"<Member {self.member_number}: {self.name}>"
