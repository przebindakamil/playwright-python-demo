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
        return self.page.locator("text=🛒")

    @property
    def cart_count_text(self):
        return self.page.locator("text=🛒")

    @property
    def cart_empty_message(self):
        return self.page.locator("text=Your cart is empty.")

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
        return self.cart_count_text.text_content()

    def click_cart(self) -> None:
        self.cart_icon.click()

    def get_cart_count(self) -> int:
        text = self.get_cart_count_text()
        # Extract number from "🛒 1" or similar
        import re
        match = re.search(r'\d+', text)
        return int(match.group()) if match else 0

    def is_cart_empty(self) -> bool:
        return self.cart_empty_message.is_visible()

    def get_item_count_in_cart(self) -> int:
        return self.cart_items.count()

    def set_quantity(self, index: int, quantity: int) -> None:
        self.quantity_inputs.nth(index).fill(str(quantity))

    def remove_item(self, index: int) -> None:
        self.remove_buttons.nth(index).click()

    def click_checkout(self) -> None:
        self.checkout_button.click()

    def get_total_price_text(self) -> str:
        return self.total_price.text_content()