from collections.abc import Generator
from dataclasses import dataclass

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
import os

from pages.basic_cart_page import BasicCartPage
from pages.seven_char_val_page import SevenCharValPage
from pages.triangle_page import TrianglePage


def _headless() -> bool:
    # domyślnie headless, chyba że lokalnie ustawisz PW_HEADLESS=0
    return os.getenv("PW_HEADLESS", "1") not in {"0", "false", "False"}

@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=_headless())
        yield browser
        browser.close()


@pytest.fixture
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    ctx = browser.new_context()
    yield ctx
    ctx.close()


@pytest.fixture
def page(context: BrowserContext) -> Generator[Page, None, None]:
    p = context.new_page()
    yield p
    p.close()


@dataclass
class AppPages:
    triangle: TrianglePage
    seven_char_val: SevenCharValPage
    basic_cart: BasicCartPage


@pytest.fixture
def app_pages(page: Page) -> AppPages:
    return AppPages(
        triangle=TrianglePage(page),
        seven_char_val=SevenCharValPage(page),
        basic_cart=BasicCartPage(page),
    )
