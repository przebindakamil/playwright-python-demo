from dataclasses import dataclass

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from pages.basic_cart_page import BasicCartPage
from pages.seven_char_val_page import SevenCharValPage
from pages.triangle_page import TrianglePage


@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def context(browser: Browser) -> BrowserContext:
    ctx = browser.new_context()
    yield ctx
    ctx.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:
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
