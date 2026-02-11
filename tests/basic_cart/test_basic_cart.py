import pytest
from playwright.sync_api import Page

from pages.basic_cart_page import BasicCartPage


@pytest.fixture
def cart_with_item(app_pages, page: Page) -> BasicCartPage:
    """Setup: navigate to products, add item, open cart."""
    cart_page = app_pages.basic_cart
    cart_page.navigate_to_products()
    cart_page.add_first_item_to_cart()
    page.wait_for_timeout(500)
    cart_page.click_cart()
    page.wait_for_load_state("networkidle")
    return cart_page


@pytest.fixture
def products_page(app_pages) -> BasicCartPage:
    """Setup: navigate to products page."""
    cart_page = app_pages.basic_cart
    cart_page.navigate_to_products()
    return cart_page


def test_load_products_page(products_page: BasicCartPage, page: Page) -> None:
    body_text = page.text_content("body")
    assert body_text is not None and "BasicStore Products" in body_text


def test_add_item_to_cart(products_page: BasicCartPage, page: Page) -> None:
    initial_count = products_page.get_cart_count()
    products_page.add_first_item_to_cart()
    updated_count = products_page.get_cart_count()
    assert updated_count == initial_count + 1


def test_view_cart_with_item(cart_with_item: BasicCartPage, page: Page) -> None:
    body_text = page.text_content("body")
    assert body_text is not None and "Shopping Cart" in body_text
    assert cart_with_item.quantity_inputs.count() > 0


def test_increase_quantity_in_cart(cart_with_item: BasicCartPage, page: Page) -> None:
    assert cart_with_item.quantity_inputs.count() > 0, "Quantity input should be visible"
    cart_with_item.set_quantity(0, 2)
    assert cart_with_item.quantity_inputs.nth(0).input_value() == "2"


def test_decrease_quantity_in_cart(cart_with_item: BasicCartPage, page: Page) -> None:
    assert cart_with_item.quantity_inputs.count() > 0, "Quantity input should be visible"
    cart_with_item.set_quantity(0, 3)
    cart_with_item.set_quantity(0, 1)
    assert cart_with_item.quantity_inputs.nth(0).input_value() == "1"


def test_add_multiple_items(products_page: BasicCartPage, page: Page) -> None:
    initial_count = products_page.get_cart_count()
    products_page.add_first_item_to_cart()
    products_page.add_to_cart_buttons.nth(1).click()
    updated_count = products_page.get_cart_count()
    assert updated_count == initial_count + 2


def test_checkout(cart_with_item: BasicCartPage, page: Page) -> None:
    cart_with_item.click_checkout()
    page.wait_for_timeout(1000)
    body_text = page.text_content("body") or ""
    assert "login" in page.url.lower() or "Thank you" in body_text or "confirm" in page.url.lower()


def test_empty_cart_checkout(app_pages, page: Page) -> None:
    cart_page = app_pages.basic_cart
    cart_page.navigate_to_cart()
    cart_page.click_checkout()
    assert "login" in page.url.lower()


def test_empty_cart_message(app_pages, page: Page) -> None:
    cart_page = app_pages.basic_cart
    cart_page.navigate_to_cart()
    page.wait_for_load_state("networkidle")
    cart_page.cart_empty_message.wait_for()
    assert cart_page.is_cart_empty()
    assert cart_page.get_cart_count() == 0


def test_remove_item_from_cart(cart_with_item: BasicCartPage, page: Page) -> None:
    initial_count = cart_with_item.get_cart_count()
    cart_with_item.remove_item(0)
    cart_with_item.cart_empty_message.wait_for()
    updated_count = cart_with_item.get_cart_count()
    assert updated_count == max(0, initial_count - 1)
    assert cart_with_item.is_cart_empty()


def test_pagination(app_pages, page: Page) -> None:
    cart_page = app_pages.basic_cart
    cart_page.navigate_to_products()
    page.goto(f"{cart_page.products_url.replace('page=1', 'page=2')}")
    page.wait_for_load_state("networkidle")
    assert "page=2" in page.url


def test_full_buying_flow(cart_with_item: BasicCartPage, page: Page) -> None:
    cart_with_item.click_checkout()
    page.wait_for_timeout(1000)
    page.locator("input").first.fill("xc95038807")
    page.locator("input").nth(1).fill("xc95038807_PASS")
    page.keyboard.press("Enter")
    page.wait_for_timeout(1000)
    assert page.url != cart_with_item.login_url
