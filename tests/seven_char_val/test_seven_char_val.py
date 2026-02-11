import pytest


@pytest.mark.parametrize(
    "input_value,expected_valid",
    [
        ("abc123*", True),  # Valid: 7 chars, allowed
        ("ABCDEFG", True),  # Valid: all letters
        ("1234567", True),  # Valid: all numbers
        ("abc123", False),  # Invalid: too short
        ("abc12345", False),  # Invalid: too long
        ("abc!@#$", False),  # Invalid: bad chars
        ("", False),  # Invalid: empty
        ("abc123!", False),  # Invalid: bad char
    ],
)
def test_validation(app_pages, input_value: str, expected_valid: bool) -> None:
    app_pages.seven_char_val.navigate()
    app_pages.seven_char_val.enter_value(input_value)
    app_pages.seven_char_val.click_check()
    result = app_pages.seven_char_val.get_result()
    if expected_valid:
        assert "Valid" in result or "valid" in result.lower()
    else:
        assert "Invalid" in result or "Error" in result or "invalid" in result.lower()
