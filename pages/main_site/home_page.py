from pages.base_page import BasePage
from pages.main_site.components.header_component import MainHeader


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header = MainHeader(page)

    def open_homepage(self):
        self.open("https://www.trgint.com/")
