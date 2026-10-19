from validator import validate_email, validate_phone


def test_validate_email():
    assert validate_email("test@example.com") is True
    assert validate_email("invalid") is False


def test_validate_phone():
    assert validate_phone("+79991234567") is True
    assert validate_phone("89991234567") is False
    assert validate_phone("+7999123") is False


def test_phone_separators():
    assert validate_phone("+7 999 123-45-67") is True


def test_phone_without_plus():
    assert validate_phone("79991234567") is True


def test_phone_invalid_characters():
    assert validate_phone("+7999abc4567") is False
    assert validate_phone("") is False
