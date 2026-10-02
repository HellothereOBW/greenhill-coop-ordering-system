"""Tests for member model."""

from app.models.member import Member


def test_member_creation():
    """Test that a member can be created with valid details."""
    member = Member("M-094", "Ky Tran", "0438 601 772")
    assert member.member_number == "M-094"
    assert member.name == "Ky Tran"
    assert member.active is True


def test_member_deactivation():
    """Test that a member can be deactivated."""
    member = Member("M-094", "Ky Tran", "0438 601 772")
    member.active = False
    assert member.active is False
