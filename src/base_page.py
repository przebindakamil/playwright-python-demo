import logging

from playwright.sync_api import Page


class BasePage:
    ENDPOINT: str = "https://testpages.eviltester.com"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)
