import pytest
from playwright.sync_api import Page

from src.base_page import BasePage

APPS = [
    "triangle",
    "7-char-val",
    "basiccart",
    "button-calculator",
    "canvas-draw",
    "canvas-scribble",
    "client-server-form-validation",
    "html-table-generator",
    "countdown-timer",
    "server-side-calculator",
    "calculator-api",
    "text-transformer",
    "simulated-login",
    "numbers-to-text",
    "note-taker",
]


@pytest.mark.parametrize("app_name", APPS)
def test_iterate_through_apps(page: Page, app_name: str) -> None:
    base_page = BasePage(page)
    url = f"{base_page.ENDPOINT}/apps/{app_name}/"
    page.goto(url)
    assert page.title is not None, f"Page title should not be None for {app_name}"
