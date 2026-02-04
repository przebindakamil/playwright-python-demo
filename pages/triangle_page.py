from src.base_page import BasePage


class TrianglePage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

    @property
    def url(self) -> str:
        return f"{self.ENDPOINT}/apps/triangle/"

    @property
    def side1_input(self):
        return self.page.locator("input[name='side1']")

    @property
    def side2_input(self):
        return self.page.locator("input[name='side2']")

    @property
    def side3_input(self):
        return self.page.locator("input[name='side3']")

    @property
    def identify_button(self):
        return self.page.locator("text=Identify Triangle Type")

    def navigate(self) -> None:
        self.page.goto(self.url)

    def enter_sides(self, side1: int | str, side2: int | str, side3: int | str) -> None:
        self.side1_input.fill(str(side1))
        self.side2_input.fill(str(side2))
        self.side3_input.fill(str(side3))

    def click_identify(self) -> None:
        self.identify_button.click()

    def get_result(self) -> str:
        return self.page.text_content("body")