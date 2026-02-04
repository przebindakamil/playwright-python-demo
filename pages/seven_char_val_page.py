from src.base_page import BasePage


class SevenCharValPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

    @property
    def url(self) -> str:
        return f"{self.ENDPOINT}/apps/7-char-val/"

    @property
    def input_field(self):
        return self.page.locator("input[name='characters']")

    @property
    def check_button(self):
        return self.page.locator("input[value='Check Input']")

    def navigate(self) -> None:
        self.page.goto(self.url)

    def enter_value(self, value: str) -> None:
        self.input_field.fill(value)

    def click_check(self) -> None:
        self.check_button.click()

    def get_result(self) -> str:
        return self.page.text_content("body")