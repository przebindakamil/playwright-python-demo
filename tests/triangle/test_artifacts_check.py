def test_intentional_failure_to_check_artifacts(page):
    """Intentional failing test to verify artifacts (trace, video, screenshot) are created."""

    # Intentionally wrong expectation to trigger failure
    assert page.locator("text=This Text Does Not Exist").is_visible(), (
        "This is intentional failure to test artifact generation"
    )
