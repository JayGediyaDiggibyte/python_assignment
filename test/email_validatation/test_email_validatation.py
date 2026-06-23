from src.email_validatation.util import (
    is_valid_email,
    filter_valid_emails
)

def test_email_valid():
    assert is_valid_email("jay.g@diggibyte.com") is True

def test_invalid_email():
    assert is_valid_email("jay.g@diggibyte.comm") is False

def test_filter_valid_email():
    emails = [
        "jay@diggibyte.com",
        "saket-23@diggibyte.com",
        "nikita_54@diggibyte.com"
    ]
    result = filter_valid_emails(emails)
    assert result == [
        "jay@diggibyte.com",
        "nikita_54@diggibyte.com",
        "saket-23@diggibyte.com"
    ]