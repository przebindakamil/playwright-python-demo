import pytest


@pytest.mark.parametrize(
    "side1,side2,side3,expected",
    [
        (5, 5, 5, "Equilateral"),
        (5, 5, 6, "Isosceles"),
        (3, 4, 5, "Scalene"),
        (1, 1, 10, "Error"),  # Invalid
        (0, 5, 5, "Error"),  # Zero
        (-1, 5, 5, "Error"),  # Negative
        ("abc", 5, 5, "Error"),  # Non-numeric
    ],
)
def test_validation(
    app_pages, side1: int | str, side2: int | str, side3: int | str, expected: str
) -> None:
    app_pages.triangle.navigate()
    app_pages.triangle.enter_sides(side1, side2, side3)
    app_pages.triangle.click_identify()
    result = app_pages.triangle.get_result()
    if expected == "Error":
        assert "Error" in result or "Not a valid" in result
    else:
        assert expected in result
