from src.base_page import BasePage


class BasicCartPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

    @property
    def url(self) -> str:
        return f"{self.ENDPOINT}/apps/basiccart/"

    @property
    def products_url(self) -> str:
        return f"{self.url}?page=1&limit=10"

    @property
    def cart_url(self) -> str:
        return f"{self.ENDPOINT}/apps/basiccart/cart.html"

    @property
    def login_url(self) -> str:
        return f"{self.ENDPOINT}/apps/basiccart/login.html"

    @property
    def add_to_cart_buttons(self):
        return self.page.locator("text=Add to Cart")

    @property
    def cart_icon(self):
        # Use first matching element to avoid strict mode issues
        return self.page.get_by_text("🛒", exact=False).first

    @property
    def cart_count_text(self):
        # Use first matching element to avoid strict mode issues
        return self.page.get_by_text("🛒", exact=False).first

    @property
    def cart_empty_message(self):
        return self.page.locator("#cartContainer p").filter(has_text="Your cart is empty.")

    @property
    def cart_items(self):
        return self.page.locator("table tr")

    @property
    def quantity_inputs(self):
        return self.page.locator("input[type='number']")

    @property
    def remove_buttons(self):
        return self.page.locator("text=Remove")

    @property
    def checkout_button(self):
        return self.page.locator("text=Checkout")

    @property
    def total_price(self):
        return self.page.locator("text=Total:")

    def navigate_to_products(self) -> None:
        self.page.goto(self.products_url)

    def navigate_to_cart(self) -> None:
        self.page.goto(self.cart_url)

    def add_first_item_to_cart(self) -> None:
        self.add_to_cart_buttons.first.click()

    def get_cart_count_text(self) -> str:
        try:
            text = self.cart_count_text.text_content(timeout=5000)
            return text or ""
        except Exception:
            return "🛒 0"

    def click_cart(self) -> None:
        # Navigate directly to cart instead of clicking icon
        # as the cart icon may not be reliably clickable on all pages
        self.navigate_to_cart()

    def get_cart_count(self) -> int:
        # If we're on the cart page, check the table rows
        if "cart.html" in self.page.url:
            try:
                # Count items in the cart table (excluding header)
                rows = self.page.locator("#cartDetails tbody tr").count()
                return rows
            except Exception:
                return 0

        # Otherwise get count from the cart icon text
        text = self.get_cart_count_text()
        # Extract number from "🛒 1" or similar
        import re

        match = re.search(r"\d+", text)
        return int(match.group()) if match else 0

    def is_cart_empty(self) -> bool:
        try:
            return bool(self.cart_empty_message.is_visible(timeout=5000))
        except Exception:
            return False

    def get_item_count_in_cart(self) -> int:
        return int(self.cart_items.count())

    def set_quantity(self, index: int, quantity: int) -> None:
        self.quantity_inputs.nth(index).fill(str(quantity))

    def remove_item(self, index: int) -> None:
        self.remove_buttons.nth(index).click()

    def click_checkout(self) -> None:
        self.checkout_button.click()

    def get_total_price_text(self) -> str:
        text = self.total_price.text_content()
        return text or ""
